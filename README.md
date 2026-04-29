🛡️ SIEM + AI + SOAR Lab (Wazuh)

Attack → Logs → Wazuh → AI → Alert → Playbook → Block IP

🔍 Beskrivning

Detta projekt implementerar en komplett säkerhetslösning som kombinerar:

SIEM – logginsamling och regelbaserad detektion (Wazuh)
AI – anomalidetektion med Python (Z-score + Isolation Forest)
SOAR – automatiserad incidentrespons (iptables)

Systemet detekterar attacker, analyserar beteenden och agerar automatiskt genom att blockera hot.

🧠 Funktioner
🔐 SSH brute force-detektion
📁 File Integrity Monitoring (FIM)
🤖 AI-baserad anomalidetektion
🚨 Automatisk larmgenerering
🔥 Automatisk IP-blockering (iptables)
🧾 Incidentloggning

🏗️ Arkitektur
🔹 Översikt

Systemet består av:
Wazuh SIEM (Docker)
AI anomalidetektion (Python)
Alert manager
Automatiserad respons (SOAR)

🔄 Dataflöde
[Attack]
   ↓
[Logs]
   ↓
[Wazuh Agent]
   ↓
[Wazuh Manager]
   ↓
[OpenSearch]
   ↓
[Dashboard]

[AI Detection]
   ↓
[Alert Manager]
   ↓
[Response Playbook]
   ↓
[Block IP (iptables)]

🔐 Komponenter

Wazuh
Logginsamling
Regelbaserad detektion
FIM

AI Detection
Z-score analys
Isolation Forest

SOAR (Response)
Automatisk IP-blockering
Incident logging
Alert generering

⚡ Responsflöde
Attack sker (t.ex. SSH brute force)
Wazuh genererar events
AI analyserar anomalier
Alert skapas
Playbook körs
IP blockeras automatiskt

🚀 Kör projektet
docker compose up -d
docker ps

🧪 Testa pipeline
python3 detect_anomalies.py
python3 alert_manager.py
python3 response_playbook.py

📊 Resultat
AI identifierade anomalier i realtid
Attacker detekterades via Wazuh
IP-adresser blockerades automatiskt
Incidenter loggades

📈 AI vs Regelbaserad Detektion
Metod	Tid till detektion	Precision
Regelbaserad	~30 sek	Hög
AI	~10 sek	Medium–Hög

👉 AI förbättrade detektionstiden med ~40–60%


🧠 Slutsats

Kombinationen av:
SIEM
AI
SOAR

gav:

⚡ Snabbare detektion
🤖 Automatiserad respons
🔍 Bättre hotanalys
⚔️ Simulerad attack (Windows → Linux/WSL)

En realistisk attack simulerades från en extern Windows-maskin mot en Linux-miljö.


### 🎯 Scenario
- Angripare: Windows (PowerShell)
- Mål: Linux (WSL + Wazuh agent)
- Typ: SSH brute force attack

---

## 🧪 Steg

### 1. Försök logga in via SSH (fel lösenord)

Attack
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


🧠 Analys av attack
SIEM identifierade attack via loggmönster
Flera failed logins → brute force
AI identifierade avvikelse i event-volym
IP-adresser användes som nyckelindikator
🔍 Insikter
SIEM kan särskilja interna vs externa hot
Brute force skapar tydliga loggmönster
IP-adresser är kritiska för korrelation
🧾 Reflektion

I detta projekt implementerades en komplett säkerhetslösning med SIEM, AI och automatiserad respons.

En viktig lärdom var hur olika komponenter samverkar i en modern säkerhetsarkitektur. Wazuh hanterade logginsamling och regelbaserad detektion, medan Python användes för att analysera anomalier.

Utmaningar inkluderade:

korrekt JSON-format mellan AI och Wazuh
konfigurering av automatiserad respons
felsökning av loggflöden

Lösningen utvecklades från att använda sudo till att köra iptables direkt i Docker-containern.

✅ Resultat
Attacker detekteras automatiskt
Anomalier identifieras med AI
IP-adresser blockeras i realtid

🚀 Framtida förbättringar
Fler datakällor
Mer avancerade ML-modeller
Integration med Slack / Email alerts
🎯 Sammanfattning

Projektet visar hur:

SIEM + AI + SOAR = modern, automatiserad cybersäkerhet


👨‍💻 Författare
Abdihakim
DevOps & Cybersecurity
