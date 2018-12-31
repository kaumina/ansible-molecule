# Ansible Deployments
This is the how to guide for deploying devopschallenge.war in a Tomcat container with a Nginx reverse proxy with self signed SSL.
## Introduction
They are 3 roles define here and they are intended to install OpenJDK,Apache Tomcat, and Nginx. These roles are supposed to work on Ubuntu >16.04 and CenOS 7.
Further, this playbook uses selfsigned certificates for nginx reverse proxy.

  - **install_tomcat:** This role installs OpenJDK 1.8 and Apache Tomcat 8. Tomcat cat is configured to run default port including systemd service.
  - **install_nginx:** This installs and configures reverse proxy with self signed SSL. At this moment Nginx version 1.12.2 is availble in the repoes.
  - **deploy_app:** Deploys the devopschallenge.war	in to newly build Apache Tomcat instance and restart the service.

# Directory hierarchy

```sh
challenge/challenge-wirecard
```
# How to run
**Prerequisites:**
- It's better to have a BitBucket accound and fork this repository.
- Install git and make it available for your system user.
- Use the ansible branch.

1. Clone the repository. I have given using ssh.
```sh
git clone git@bitbucket.org:codefreaker/challenge.git 
cd challenge-wirecard
ansible-playbook -i staging deploy.yml

```

2. Move to the directory challenge-wirecard and there you see below files and directories.
 
- **ansible.cfg:** Local ansible configuration you may have to edit this file as per your system requirments.
- **roles:** This is directory where above mentioned roles are defined.
- **prod:** The investory file for prod servers.
- **staging:** The investory file for staging servers.
- **deploy.yml:** This is playbook defining all roles and variables.

3. Change below files according to your deployment.
```sh
Add you domain name or IP as required in the server block in roles/install_nginx/files/proxy.conf
server_name <your domain name/IP>;
```
```sh
Change your list of servers in your invenstory files(prod/staging).
```



