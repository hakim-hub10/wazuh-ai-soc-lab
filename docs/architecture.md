## Architecture — SIEM + AI + SOAR
📌 Overview

This system implements a complete security pipeline combining:

SIEM (Wazuh) – log collection and rule-based detection
AI Detection (Python) – anomaly detection using statistical and ML methods
SOAR (Automation) – automated incident response

## Architecture Layers

The system is divided into three main layers:

Data Collection (Wazuh Agent)
Analysis (Wazuh + AI Model)
Response (SOAR / Active Response)

## Data Flow
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
[iptables Block]

## Process Flow (Simplified)
Attack
  ↓
Logs Generated
  ↓
Wazuh Detection
  ↓
AI Analysis
  ↓
Alert Creation
  ↓
Response Playbook
  ↓
IP Blocked

## Components
Wazuh (SIEM)
Log collection from system and applications
Rule-based detection (e.g. SSH brute force)
File Integrity Monitoring (FIM)

AI Detection
Z-score analysis for anomaly detection
Isolation Forest for behavioral anomalies
Identifies deviations from normal activity

SOAR (Automated Response)
Automatic IP blocking using iptables
Incident logging and tracking
Alert generation and handling

Network
Docker-based environment (172.x.x.x network)
Communication flow:
[Agent] → [Manager] → [Indexer] → [Dashboard]
External attacker simulated from Windows → Linux (WSL)

## Response Flow
Attack occurs (e.g. SSH brute force)
Wazuh generates events based on logs
AI analyzes anomalies in behavior
Alert is generated
Response playbook is executed
Malicious IP is blocked via iptables


## Security Objectives
⚡ Fast detection of threats
🤖 Automated incident response
🔒 Reduced attack surface
📊 Improved visibility into security events