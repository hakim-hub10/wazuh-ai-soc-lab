## Detection Comparison: Rule-Based vs AI-Based Detection
Rule-Based Detection (Wazuh)

## Advantages
Fast and efficient
Stable and predictable
Easy to understand and interpret

## Disadvantages
Limited to known attack patterns
Requires manual rule creation and maintenance
Lacks contextual awareness
May miss novel or evolving threats

##AI-Based Detection

## Advantages
Identifies anomalies in behavior
Detects unknown or zero-day attacks
Adaptive to changing patterns
Provides deeper analytical insights

## Disadvantages
Requires tuning and training
May generate false positives
More complex to implement and maintain

## Results from This Project
Method	Detection Time	Accuracy
Rule-Based	~30 seconds	High
AI-Based	~10 seconds	Medium–High


## Conclusion
AI-based detection improved detection time by approximately 40–60% compared to traditional rule-based methods.

## The combination of SIEM + AI + SOAR enabled:
⚡ Faster detection and response
🤖 Automated threat mitigation
🔍 Improved visibility and analysis of security events

## Attack Analysis
The SIEM system identified the attack based on recognizable patterns in log data
Multiple failed login attempts triggered brute force detection rules
The AI model detected anomalies in event volume and behavior
IP addresses were used as key indicators for correlation and response


## Key Insights
SIEM can distinguish between internal and external threats
Brute force attacks generate clear and repeatable log patterns
IP addresses are critical for threat correlation and automated response
Combining rule-based and AI detection provides stronger overall security coverage