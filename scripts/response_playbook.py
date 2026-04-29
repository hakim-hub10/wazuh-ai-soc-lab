#!/usr/bin/env python3
"""
Automatiserad incidentrespons-playbook.
"""

import json
import subprocess
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('incident_response.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class IncidentResponder:
    def __init__(self):
        self.incidents = []
        self.blocked_ips = set()

    def block_ip(self, ip: str, reason: str, duration: int = 3600):
        if not ip:
            logger.warning("Ingen IP att blockera")
            return

        if ip in self.blocked_ips:
            logger.info(f"IP {ip} redan blockerad")
            return

        try:
            subprocess.run(
                [
                    'docker', 'exec', 'single-node-wazuh.manager-1',
                    'iptables', '-I', 'INPUT', '-s', ip, '-j', 'DROP'
                ],
                check=True
            )

            self.blocked_ips.add(ip)

            logger.warning(f"BLOCKERAD: {ip} — {reason}")

            self.log_incident('block_ip', {
                'ip': ip,
                'reason': reason,
                'duration': duration
            })

        except subprocess.CalledProcessError as e:
            logger.error(f"Kunde inte blockera {ip}: {e}")

    def send_alert(self, severity: str, message: str):
        alert = {
            'severity': severity,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }

        logger.warning(f"LARM [{severity.upper()}]: {message}")

        alerts_file = Path('response_alerts.json')
        existing = json.loads(alerts_file.read_text()) if alerts_file.exists() else []
        existing.append(alert)
        alerts_file.write_text(json.dumps(existing, indent=2))

    def log_incident(self, action: str, details: dict):
        incident = {
            'action': action,
            'details': details,
            'timestamp': datetime.now().isoformat()
        }

        self.incidents.append(incident)

        with open('incident_log.json', 'w') as f:
            json.dump(self.incidents, f, indent=2)

    def process_alert(self, alert: dict):
        severity = alert.get('severity', 'medium')
        details = alert.get('details', {})

        # 🔥 RÄTT fält
        src_ip = details.get('srcip', '')

        logger.info(f"Behandlar larm: {severity} — {json.dumps(details)}")

        if severity == 'critical':
            if src_ip:
                self.block_ip(src_ip, 'Kritisk anomali')
            self.send_alert('critical', f'Kritisk incident: {details}')

        elif severity == 'high':
            if src_ip:
                self.block_ip(src_ip, 'Hög anomali', duration=1800)
            self.send_alert('high', f'Hög incident: {details}')

        elif severity == 'medium':
            self.send_alert('medium', f'Medium incident: {details}')


if __name__ == '__main__':
    responder = IncidentResponder()

    try:
        with open('active_alerts.json') as f:
            alerts = json.load(f)
    except FileNotFoundError:
        print("Kör detect_anomalies.py och alert_manager.py först")
        exit(1)

    print(f"Behandlar {len(alerts)} larm...")

    for alert in alerts:
        responder.process_alert(alert)

    print(f"\nFärdigt. {len(responder.incidents)} åtgärder vidtagna.")
    print(f"Blockerade IP:n: {responder.blocked_ips}")
