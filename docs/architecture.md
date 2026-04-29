# Architecture

## Overview

This system consists of:

- Wazuh SIEM (Docker)
- AI anomaly detection (Python)
- Alert manager
- Automated response (iptables)

## Flow

Attack → Logs → Wazuh → AI Detection → Alert → Playbook → Block IP

## Components

- Wazuh Manager (log analysis)
- OpenSearch (indexing)
- Dashboard (visualization)
- Python scripts (AI + automation)

## Network

- Docker network (172.x.x.x)
- Agent → Manager communication


# 🏗️ Arkitektur — SIEM + AI + SOAR

## Översikt

Systemet består av tre huvuddelar:

1. **Datainsamling (Wazuh Agent)**
2. **Analys (Wazuh + AI-modell)**
3. **Respons (SOAR / Active Response)**

---

## 🔄 Dataflöde
[Linux System / Logs]
↓
[Wazuh Agent]
↓
[Wazuh Manager]
↓
[OpenSearch Indexer]
↓
[Dashboard]

[AI Detection Script (Python)]
↓
[Alert Manager]
↓
[Response Playbook (SOAR)]
↓
[iptables block]




---

## 🔐 Komponenter

### Wazuh
- Logginsamling
- Regelbaserad detektion
- FIM (File Integrity Monitoring)

### AI Detection
- Z-score analys
- Isolation Forest (anomaly_score)

### SOAR (Response)
- Automatisk IP-blockering
- Incident logging
- Alert generering

---

## ⚡ Responsflöde

1. Attack sker (t.ex SSH brute force)
2. Wazuh genererar events
3. AI analyserar anomalier
4. Alert genereras
5. Response playbook körs
6. IP blockeras via iptables

---

## 🎯 Säkerhetsmål

- Snabb detektion
- Automatiserad respons
- Minskad attackyta
