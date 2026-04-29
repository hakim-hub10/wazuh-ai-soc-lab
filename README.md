# SIEM + AI + SOAR Lab (Wazuh)
Attack → Logs - Wazuh → AI → Alert → Playbook → Block IP

## 🔍 Beskrivning
Detta projekt implementerar en komplett säkerhetslösning med:

- SIEM (Wazuh)
- AI-baserad anomalidetektion
- Automatiserad incidentrespons (SOAR)

---

## 🧠 Funktioner
- SSH brute force detection
- File Integrity Monitoring (FIM)
- AI anomaly detection (Python)
- Automatisk IP-blockering (iptables)

---

## ⚙️ Arkitektur
Se: docs/architecture.md

---

## 🚀 Kör projektet

```bash
docker compose up -d
docker ps

Test
python3 detect_anomalies.py
python3 alert_manager.py
python3 response_playbook.py

Rusultat 
AI identifierade anomalier
IP blockerades automatiskt
Incident loggades


## 📈 AI vs Regelbaserad Detektion

AI-modellen förbättrade detektionstiden med ~40–60% jämfört med traditionella regler.

Se: docs/detection_comparison.md


## ⚔️ Simulerad attack (Windows → Linux/WSL)

För att testa systemet genomfördes en realistisk attack där en extern maskin (Windows) attackerade en Linux-miljö (WSL).

### 🎯 Scenario
- Angripare: Windows (PowerShell)
- Mål: Linux (WSL + Wazuh agent)
- Typ: SSH brute force attack

---

## 🧪 Steg

### 1. Försök logga in via SSH (fel lösenord)

```bash
ssh fakeuser@172.24.59.214
➡️ Flera misslyckade login-försök genereras

2. Verifiera nätverksåtkomst
ping 172.24.59.214

3. Wazuh detekterar attack
Regel: 5710 (invalid user)
Regel: 100001 (brute force)

4. AI analyserar anomalier
Högt antal events
Avvikande beteende
Klassificeras som critical

5. Automatisk respons
IP blockeras via iptables
Incident loggas

📸 Bevis finns i screenshot delan.
Attack från Windows
Wazuh alerts
Loggar
Blockering


Final check Wazuh fungerar
3 regler (SSH + AI + FIM)
FIM aktiv
Dashboard screenshots
AI script
Auto block (iptables)
Arkitektur
Jämförelse
Reflektion
# wazuh-ai-soc-lab
