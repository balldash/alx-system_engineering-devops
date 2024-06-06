Explanation of this architecture:
1. Load balancer:
- Reason for adding: To distribute incoming traffic across multiple servers, ensuring no single server becomes a bottleneck.
- Distribution Algorithm: Round Robin, where incoming requests are distributed evenly across the available servers. It works by sending each new request to the next server in line, looping back to the first server after the last one.

2 Active-Active Vs. Active-Passive:
- Active-Active: All servers are actively handling requests. This setup maximized resource utilization and provides higher availability and load distribution.
- Active-Passive: Only one server is active and handling requests at any time, while the other one is on standby and only becomes active if the first server fails. This setup provides failover capability but does not utilize all resources optimally.

Primary-Replica Database cluster:
- How it works: The primary database handles all write operations. The replica receives updates from the primary database and is used for read operations. This setup helps distribute the load and ensures data redundancy.
- Difference between primary and replica:
-- Primary Node: Handles all write operations and propagates changes to replicas.
-- Replica Node: Handles read operations and receives updates from the primary node.

Issues with This Infrastructure:
- Single Points of Failure (SPOF): Load Balancer: If the load balancer goes down, the entire website becomes inaccessible.
- Database: If the primary database goes down and there's no failover mechanism in place, the application won't be able to process write operations.
- Security Issues: No Firewall: Without a firewall, the server is vulnerable to unauthorized access and attacks.
- No HTTPS: Without HTTPS, data transmitted between the user and the server is not encrypted, making it susceptible to interception and man-in-the-middle attacks.
- No Monitoring: Lack of Monitoring: Without monitoring, it's difficult to detect and respond to issues like server downtime, high load, or security breaches in real-time.
