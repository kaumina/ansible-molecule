# Test Ansible roles using Molecule
This is the how to guide for deploying devopschallenge.war in a Tomcat container with a self signed SSL Nginx reverse proxy.
# Introduction
There are three roles defined here and they are intended to install OpenJDK,Apache Tomcat, and Nginx. These roles are supposed to work on CenOS 7 as the testing Docker image is CentOs. Further, You may find the self signed certificates in **ansible-role-nginx/files** directory
This has been implemented in [Molecule] (https://molecule.readthedocs.io/en/latest/).

# Directory hierarchy for Molecule roles

You can find below molecule roles in **molecule** directory (**challenge/challenge-wirecard/molecule**).

  - **ansible-role-tomcat:** This role installs OpenJDK 1.8 and Apache Tomcat 8. Furthermore, Tomcat is configured to run default  port including systemd service.
  - **ansible-role-nginx:** This installs and configures reverse proxy with self signed SSL. At this moment Nginx version 1.12.2 is availble in the repos and installed.
  - **ansible-role-deployapp:** Deploys the **sample.war**	into newly build Apache Tomcat instance and restart the service.

# How to run and test Ansible roles

I assume you have installed below tools and applications in your local/desktop server.

## Pre-requisites:

1. Docker in your localhost.
2. Molecule in your localhost. [https://molecule.readthedocs.io/en/latest/installation.html]
3. Install docker-py using pip.

    ```
     pip install docker-py
    ```    
    
4. git in your localhost.
5. Once you are done with all installations execute below commands sequentially assuming now you are here.
    ``` 
    ansible-molecule/molecule 
    ```
    
## Steps:  

1.Firstly, you have to clone the repository from BitBucket repo.
   
```

  git clone git@bitbucket.org:codefreaker/ansible-molecule.git
  
```
   
You can see there are two commands are running for running role task and testing them.
    
   * **molecule check:** Dry run the all actions in the role.
   * **molecule converge:** Run the all tasks written in tasks/main.yml
   * **molecule verify:** Run the testing scripts (molecule/default/ using **testinfra**     
   

2.Execute below to install and config Tomcat.  
    
```

  cd ansible-role-tomcat
  molecule check
  molecule converge
  molecule verify 
  
```

You can see molecule executes all role tasks 

3.Execute below to install and config Nginx with self signed SSL certificate.

``` 
  cd ansible-role-nginx
  molecule check
  molecule converge 
  molecule verify          
```
4.This execution will install the application and restart the Tomcat.
   
``` 
  cd ansible-role-tomcat
  molecule check
  molecule converge 
  molecule verify       
```

5.Now you run below command in your host server. 

```
curl -vk https://172.17.0.2 
```

Expected output:

	<html>
	<head>
	<title>Sample "Hello, World" Application</title>
	</head>
	<body bgcolor=white>
	<table border="0">
	<tr>
	<td>
	<img src="images/tomcat.gif">
	</td>
	<td>
	<h1>Sample "Hello, World" Application</h1>
	<p>This is the home page for a sample application used to illustrate the
	source directory organization of a web application utilizing the principles
	outlined in the Application Developer's Guide.
	</td>
	</tr>
	</table>
	<p>To prove that they work, you can execute either of the following links:
	<ul>
	<li>To a <a href="hello.jsp">JSP page</a>.
	<li>To a <a href="hello">servlet</a>.
	</ul>
	</body>
	</html>
     
      