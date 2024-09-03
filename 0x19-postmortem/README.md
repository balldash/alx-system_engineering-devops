### Postmortem: HandyHub Service Outage

#### Issue Summary
**Duration**: August 25, 2024, 14:00 - 16:30 GMT+2  
**Impact**: HandyHub's search and browse functionality was down, affecting 60% of users. Users experienced slow response times and were unable to search for tradesmen.  
**Root Cause**: A misconfigured API Gateway routing rule caused requests to loop indefinitely, leading to high server load and eventual service downtime.

#### Timeline
- **14:00** - Issue detected via monitoring alert indicating high server load.
- **14:05** - Initial investigation by on-call engineer; assumption was a DDoS attack.
- **14:15** - Misleading path: Network team investigated potential external threats.
- **14:30** - Customer complaints confirmed the issue was affecting search functionality.
- **14:45** - Escalated to backend engineering team.
- **15:00** - Identified misconfigured API Gateway routing rule.
- **15:15** - Applied temporary fix by disabling the problematic rule.
- **15:45** - Full resolution by correcting the routing configuration.
- **16:30** - Services fully restored and monitored for stability.

#### Root Cause and Resolution
**Root Cause**: The API Gateway had a misconfigured routing rule that caused requests to loop back to the gateway instead of being routed to the appropriate backend service. This misconfiguration led to an exponential increase in server load, causing the search and browse functionality to become unresponsive.

**Resolution**: The issue was resolved by first disabling the problematic routing rule to stop the looping requests. Then, the routing configuration was corrected to ensure that requests were properly directed to the backend services. A thorough review of all routing rules was conducted to prevent similar issues in the future.

#### Corrective and Preventative Measures
**Improvements**:
- Implement stricter validation and testing of API Gateway configurations before deployment.
- Enhance monitoring to detect unusual traffic patterns indicative of routing issues.
- Conduct regular audits of routing rules and configurations.

**Tasks**:
1. **Patch API Gateway**: Update the API Gateway to the latest version to include any bug fixes and improvements.
2. **Add Monitoring**: Implement detailed monitoring on API Gateway traffic to detect anomalies.
3. **Automate Testing**: Develop automated tests for API Gateway configurations to catch misconfigurations early.
4. **Review and Document**: Conduct a comprehensive review of current routing rules and document them thoroughly.
5. **Training**: Provide training for engineers on best practices for configuring and managing API Gateways.

By addressing these measures, we aim to improve the reliability and stability of HandyHub's services, ensuring a better user experience and reducing the likelihood of similar outages in the future.
