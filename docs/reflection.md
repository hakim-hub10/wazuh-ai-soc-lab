## Reflection

In this project, I implemented a complete security solution combining SIEM (Wazuh), AI-based anomaly detection, and automated incident response (SOAR).

One of the most important learnings was understanding how different components interact within a modern security architecture. Wazuh handled log collection and rule-based detection, while Python scripts were used to analyze anomalies using statistical methods and machine learning techniques.

One of the main challenges was ensuring a correct data flow between the AI detection module and Wazuh. Specifically, it was necessary to structure the JSON output properly so that Wazuh could interpret AI-generated alerts. Another challenge was configuring automated response, where I initially used sudo, but later improved the solution by executing iptables directly inside the Docker container.

I also learned the importance of log structure, data validation, and troubleshooting in distributed systems. Debugging Wazuh rules and understanding how events are processed was a key part of the development process.

## Outcome

The final result was a fully functional pipeline where:

Attacks are detected
Anomalies are identified using AI
Malicious IP addresses are automatically blocked

This project clearly demonstrates how AI can complement traditional security solutions and contribute to faster and more dynamic threat detection.

## Future Improvements
Integrate additional data sources
Improve machine learning models
Add integrations with external alerting systems (e.g., Slack, email)

## Summary

Overall, this project provided a deep understanding of SIEM systems, cybersecurity workflows, and automation, and how these components can be combined to build a modern and effective security solution.