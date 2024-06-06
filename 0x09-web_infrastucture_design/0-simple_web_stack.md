Explanation of the infrastucture:
1. What is a server?
- A server is a computer that serves other computers called clients on a network. It handles requests from clients, processes these requests and returns the apporiate response.

2. What is the role of the domain name?
- The domain name is a human-readable address that a user can type into their browswer to access the website. It helps simplfy the process of reaching websites as compared to remembering IP addresses.

3. What type of DNS record www is in www.foobar.com?
- The 'www' record in 'www.foobar.com' is an A (Address) record, that maps the domain name ot the IP address 8.8.8.8. This allows the user to reach the server by typing 'www.foobar.com'.

4. What is the role of the web server?
- The web server handles incoming http requests from the user over the internet. It serves static content like HTML pages and forwards dynamic requests to the application server.

5. What is the role of the application server?
- The application server processes the dynamic requests received from the web server. It executes the application code to generate the appropriate responses.

6. What is the role of the database?
- The database stores the data that is required by the application, such as user information, sales information.

Issues with this infrastucture:
1. SPOF (Single Point of Failure) - Since all components are hosted on a single server, if the server goes down, the entire website becomes unavailable.

2. Downtime when maintenance needed - Performing maintenance tasks will cause downtime, making the website inaccessible during these periods.

3. Cannot scale if too much incoming traffic - A single server has limited resources. If the website receives too much traffice, the server might become slow or crash.
