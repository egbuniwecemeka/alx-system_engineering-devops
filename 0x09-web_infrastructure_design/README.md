# WEB INFRASTRUCTURE DESIGN

## Resource 1

What is a database?
A database is a collection of organized structure of information, or data stored electronically on a computer system. A database is managed by a database management system (DBMS). The data, DBMS, and related applications is known as a database system or database.

Data of most programming languages are stored in rows and colums in tables so as to enable efficiient data querying and processing. The data can then be easily accessed, managed, modified, updated, controlled and organized
Most DB uses SQL for writing and querying data

* What is SQL?
SQL is a programming language used by almost all relational databases to query, manage and define data, and also grant access to it.

## Difference between a database and a spreadsheet?

Both are convienent is storing data, but the following are the key differences

* How data is stored and manipulated

* Who can access the data

* How much data can be stored

Spreadsheets were designed for single users, or small numbers of users who do not need to carry out complex data manipulation. Databases on the other hand allows for complex data manipulations by  both single and multiple users. They hold much larger collection of organized collection of information. Users can securely access and manipulate data using high complex logic and language

## Types of DBs

They are **Relational DB, Object-oriented DBs, Distributed DBs, Data warehouses, No SQL DBs, Graph DBs, OLTP DBs, Open source DBs, Cloud DBs, Multimodel DB, Document/JSON DB, Self-driving DB**

## What is a DB Software?

DB software is used to create, edit and maintain data files and records.
The software also handles data storage, backup and reporting, multi-access control, and security. Database software is also referred to as DBMS

## What is a DBMS?

Databases require a database software program(DBMS). The DBMS serves as an interface between the database and the end-user or application that allows users to access, retrieve, update, manage how infomation/data is organized and optimized. DBMS facilitates other administrative functions such as tuning,monitoring,recovery, performance and backup. Example of DBMSs include: MySQL, Microsoft Access, Microsoft SQL Server, Oracle Database.

## What is a MySQL

MySQL is an open-source relational database management system based on SQL. It was originally designed for web applications but can be used on any platform. MySQL is generally accepted by web developers and web-based applications because of its ability to process millions of queries and thousands of transactions. **On-demand flexibility is the primary feature of MySQL**. MySQL is the major DBMS behing most of the worlds leading websites eg. Uber, LinkedIn, Youtube, Airbnb, Twitter etc

## Using databases to improve business performance and decision-making

Using database and other computing and business intelligence tools, organizations can now leverage the data they collect to run more efficiently, enable better decision-making, and become more agile and scalable.

## Database challenges

Present large enterprise databases support very comlex queries while giving nearly instant responses. Due to this administrators are usually need to provide methods that help improve performances. Some challenges faced are:

* Absorbing significant increases in data volume
* Ensuring data security
* Keeping up with demand
* Managing and maintaining the databases and infrastructure
* Removing limits on scalability
* Ensuring data sovereignty, data residency and latency requirements

## How autonomous technology is improving database management

Self-driving databases offers the intruiging possibility of organizations using advanced and latest technology database services without the headache of running or operating that technology.. Self-driving DBs uses cloud-based technology and machine learning to automate routine tasks required to manages DBs, tuning, security, ackups, updates and other routine managements tasks. The first autonomous database was announced in late 2017.

## RESOURCE 2

Q. What is the difference between application server and a Web server?

A web server exclusively handles HTTP requests while application server serves business logic to application programs through any numbers of protocols

* The Web Server
The web server handles HTTP protocols. When the web server receives a HTTP request, it provides an HTTP response eg HTML page.
Web server's delegation model: Request -> Web server -> Program(to handle request) -> (server side program provides for itself functions for transaction, processing, database connectivity and messaging.)

* Application server
An application server exposes business protocols to client applications through various protocols possibly including HTTP.  While a web server basically provides HTML responses for display in a web browser, an application server provides business logic for use by client application programs. The application can use these logic as it would call a method or object or function.

## An Example

An online vendor that offers a home delivery service on various products will most likely have a form to fill. On submission of query, site performs a lookup and gives a HTML response. This can be implemented in different scenarios. Lets look at a a scenario that involves an application server and another that doesnt

* Scenario 1: Web server without application server
In this scenario, a web server alone provides the online vendors functionality.
Web server -> Request -> Server-side program ->Program(lookup )information on database -> HTML response -> Webserver -> Web browser.
Summary: A web server processes HTTP requests and responds with HTML pages.

* Scenario 2: Similarities to scenario 1 in that web server delegaetaes rsponse generation to a script. However, the business logic can be included for the lookup info onto an application server. With this, instead of the script looking up data and formulating responses, the script can simply call the application server lookup service. The script can then use the server's responses when the script generates a response.
By separating the pricing logic from the HTML response-generating code, the pricing logic becomes far more reusable between applications.
In contrast, in Scenario 1 the pricing lookup service is not reusable because the information is embedded within the HTML page. In Scenario, the web server handles HTTP requests and provides HTML responses while the application server serves application logic by processing related requests

## Caveats

Recently, XML Web services have blurred the line between application servers and Web servers. By passing an XML payload to a Web server, the Web server can now process the data and respond much as application servers have in the past

## RESOURCE 3

* DNS Record Types: Defined and Explained
Domain name system is a global system for mapping human readable hostnames to their corresponding Internet protocol(IP) addresses.
Note: The human readble hostnames are strings of words that are easy to remember and the IP addresses(IPV4) a set of numbers seperated by dots and harder to remember. Also note that tha IP address mapped to a domain name may change depending on the server hosting the website
* A DNS resolver is respnsible for finding the correct IP address for a hostname.

## What are DNS record types?

Theses a records that provide information about a hostname or domain. Eg Current IP for domain

* DNS records are stored in text files(Zone files) on d authoritative DNS server
Content of DNS record file: strirng and special commands(understood by DNS server)

## DNS record types

A record
AAAA record
CNAME record
Nameserver(NS) record
Mail(MX) exchange

* A record
This is the most important DNS record type. The A stands for "address" as it shows the IP address of a specific hostname or domain
Uses: IP address lookup. Eg using A recorsd, a web browser is able to access a website using their domain names. A pratical example is accessing websites on the internet without knowing their IP addresses.
Another use in domain name system-based blackhole list. It can be used to block mails from known spam sources.

* AAAA record
Just lika A record, this is used to look for IP addresses of domain names. The only difference being that it point to IPV6 addresses.

IPV6 is an upgrade of IPV4. As it has an increased IP address value. With IPV6 you cannot run out of unique IP addresses.
Eg: **3001:0db7:3c5d:0024:0000:0000:1a2f:3c1b**Note: A colon seperates each field in an IP address
Uses:
DNS resolution(It has IPV6 address)
As the Internet is growing, we are running out of IPV4 addresses, the potential of IPV6 is increasing
AAAA record i
s used to resolve a domain name to IPV6 protocol

* CNAME record(canonical record)
This is a DNS record that is used to point a domain name(an alias) to another domain name. In CNAME the alias does not point to an IP address and the domain name the alias points to is the canonical name. FOr example: **the subdomain ng.ejh.com can point to ejh.com, which points to an IP address using an A record.
Usage:
Running multiple subdomains for different purposes on the same server.
For example: we can use ftp.example.com for File Transfer Protocol and serve webpages via <www.example.com>. We can then use CNAME records to point both subdomains to example.com. The main domain example.com then points to the IP address using A record
A CNAME can point to another CNAME. (Inefficient and slows load speed, poor user experience)

* NS record
The nameserver(NS) record specifies the authoritative DNS server for the domain. In other words, NS records points to where an application eg web server can find an IP address for a domain name.
Usage:
Creating a simple web site or purchasing a web hosting service, the user will have received an email with nameserver details. The nameserver connects the domain name to the server your site is hosted on.

* MS record
Nail service(MX) record speccifies where emails for a domain should be routed to. In simple words it makes it possible to direct emails to a mail server
Note: The can be multiple MX records for a single domain name. **The lower the priority value, the higher the actual priority.**
Usage:
With MX record it is possible to hand off email to a dedicated server.

## Conclusion

DNS makes it possibel for us to use human-readable domain names to access resources on the internet.