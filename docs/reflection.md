# 🧾 Reflektion

I detta projekt har jag implementerat en komplett säkerhetslösning med SIEM (Wazuh), AI-baserad anomalidetektion och automatiserad incidentrespons (SOAR).

En av de viktigaste lärdomarna var hur olika komponenter samverkar i en modern säkerhetsarkitektur. Wazuh hanterade logginsamling och regelbaserad detektion, medan Python-skript användes för att analysera anomalier baserat på statistik och machine learning.

En utmaning var att få dataflödet att fungera korrekt mellan AI-detektion och Wazuh. Specifikt krävdes korrekt JSON-struktur för att Wazuh skulle kunna tolka AI-genererade larm. Ett annat problem var att konfigurera automatiserad respons, där jag först använde sudo och senare gick över till att exekvera iptables direkt i Docker-containern.

Jag lärde mig även vikten av loggstruktur, datavalidering och felsökning i distribuerade system. Att debugga Wazuh-regler och förstå hur events processas var centralt.

Resultatet blev en fungerande pipeline där:
- attacker detekteras
- anomalier identifieras
- IP-adresser blockeras automatiskt

Projektet visar tydligt hur AI kan komplettera traditionella säkerhetslösningar och bidra till snabbare och mer dynamisk hotdetektion.

Framöver skulle systemet kunna förbättras genom:
- fler datakällor
- bättre ML-modeller
- integration med externa alert-system (Slack, email)

Sammanfattningsvis har projektet gett en djup förståelse för både SIEM, cybersäkerhet och automatisering.
