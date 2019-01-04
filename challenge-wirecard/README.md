# Test Ansible roles using Molecule
This is the how to guide for deploying devopschallenge.war in a Tomcat container with a self signed SSL Nginx reverse proxy.
## Introduction
There are three roles defined here and they are intended to install OpenJDK,Apache Tomcat, and Nginx. These roles are supposed to work on CenOS 7 as the testing Docker image is CentOs. Further, You may find the self signed certificates in **ansible-role-nginx/files** directory
This has been implemented in [Molecule] (https://molecule.readthedocs.io/en/latest/) .

# Directory hierarchy for Molecule roles

You can find below molecule roles in **molecule** directory (**challenge/challenge-wirecard/molecule**).

  - **ansible-role-tomcat:** This role installs OpenJDK 1.8 and Apache Tomcat 8. Furthermore, Tomcat  is 			configured to run default  port including systemd service.
  - **ansible-role-nginx:** This installs and configures reverse proxy with self signed SSL. At this moment Nginx version 1.12.2 is availble in the repos and installed.
  - **ansible-role-deployapp:** Deploys the **devopschallenge.war**	into newly build Apache Tomcat instance and restart the service.

## How to run and test Ansible roles
I assume you have installed below tools and applications in your local/desktop server.

**Pre-requisites:**

1. Docker in your localhost.
2. Molecule in your localhost. [https://molecule.readthedocs.io/en/latest/installation.html]
3. Install docker-py using pip.
    
       pip install docker-py
        
4. git in your localhost.
5. Firstly, you have to clone the repository and checkout the **Ansible** branch from BitBucket repo.

        git clone git@bitbucket.org:codefreaker/challenge.git
        git fetch && git checkout ansible
        git pull
 

6. Once you are done with all installations execute below commands sequentially assuming now you are here.

	   challenge/challenge-wirecard/molecule 

        
    You can see there are two commands are running for running role task and testing them.
   **molecule check:** Dry run the all actions in the role.
   **molecule converge:** Run the all tasks written in tasks/main.yml
   **molecule verify:** Run the testing scripts (molecule/default/ using **testinfra** 

    1. Execute below to install and config Tomcat.
       ```
         cd ansible-role-tomcat
         molecule check
         molecule converge
         molecule verify 
       ```
       You can see molecule executes all role tasks 

    2. Execute below to install and config Nginx with self signed SSL certificate.
        ``` 
         cd ansible-role-nginx
         molecule check
         molecule converge 
         molecule verify 
       ```
    3. This execution will install the application and restart the Tomcat.
        ``` 
         cd ansible-role-tomcat
         molecule check
         molecule converge 
         molecule verify 
       ```
                 
    4. Now you run below command in your host server. 
                ```
                curl -vk https://172.17.0.2 
                ```

    Expected output:
```
        
        * About to connect() to 172.17.0.2 port 443 (#0)
        *   Trying 172.17.0.2...
        * Connected to 172.17.0.2 (172.17.0.2) port 443 (#0)
        * Initializing NSS with certpath: sql:/etc/pki/nssdb
        * skipping SSL peer certificate verification
        * SSL connection using TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
        * Server certificate:
        *       subject: E=kaumina@gmail.com,CN=localhost,OU=DevOps,O=Default Company Ltd,L=Colombo,ST=Western,C=LK
        *       start date: Dec 31 01:59:12 2018 GMT
        *       expire date: Dec 31 01:59:12 2019 GMT
        *       common name: localhost
        *       issuer: E=kaumina@gmail.com,CN=localhost,OU=DevOps,O=Default Company Ltd,L=Colombo,ST=Western,C=LK
        > GET / HTTP/1.1
        > User-Agent: curl/7.29.0
        > Host: 172.17.0.2
        > Accept: */*
        > 
        < HTTP/1.1 200 
        < Server: nginx/1.12.2
        < Date: Fri, 04 Jan 2019 06:06:04 GMT
        < Content-Type: text/plain;charset=UTF-8
        < Content-Length: 38
        < Connection: keep-alive
        < 
        * Connection #0 to host 172.17.0.2 left intact
        Hello from Wirecard DevOps Challenge!!
 ```       
      





