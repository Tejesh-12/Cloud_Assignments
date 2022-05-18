#!/usr/bin/python

import os

os.system('yum install -y python python-dev python-pip')
os.system('pip install boto3')

os.system('yum -y update')
os.system('yum install -y httpd')
os.system('service httpd start')
os.system('cd ~')

import boto3


access_id_key = 'ASIATNXW6TNDC77X5E5F'
secret_access_key = '4XzL9WB3yJb0QgEUyh10X2QV8nsj8Gj24HtkEcRp'
session_token_key = 'FwoGZXIvYXdzEPn//////////wEaDMYzLHq2r3lF6you4iLXAe18kLo+uyR9gzpHz1/99EljdmLGJWf4xJ9oDRZBpjMRxOqSmDu+KSeeIYwbwYLR9jgFck5Ta56ihqwiplwHeFh8LJ6IQKi4HFwj8t3BQvfP8fEDgJFfVWzDlm7coYulw9F6mxUaAvezsUMCoIBDeH16kdC/vKGQ5q/5KUFvpjMs4utCMy2cfxw+c60N4ZhzafiyccWRs8t5XkISXPqey2jqo7F84iGFGvR9rb0H2BPxdhND5tEoidwvXrFIr6yPPZJhoIS83ucA68apAs5cdPuHTf7VHg0vKL7d8YoGMi2A/akgvd6fwiNrIPg6n4WHGP7qhpQ6700RrsZJVxd6cKz9R6Ae48pq/ygpVKs='



client = boto3.client('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key)


client.download_file('assignment6website','index.html','/var/www/html/'+'index.html')
client.download_file('assignment6website','carrom.png','/var/www/html/'+'carrom.png')
client.download_file('assignment6website','cloud.png','/var/www/html/'+'cloud.png')
client.download_file('assignment6website','computer.png','/var/www/html/'+'computer.png')
client.download_file('assignment6website','favicon.ico','/var/www/html/'+'favicon.ico')
client.download_file('assignment6website','mountain.png','/var/www/html/'+'mountain.png')
client.download_file('assignment6website','profile.jpg','/var/www/html/'+'profile.jpg')
client.download_file('assignment6website','styles.css','/var/www/html/'+'styles.css')

os.system('sudo yum update -y')
#Installing the most recent Docker Engine package
os.system('sudo amazon-linux-extras install docker')
#Starting the Docker service.
os.system('sudo service docker start')
#Adding  the ec2-user to the docker group so you can execute Docker commands without using sudo.
os.system('sudo usermod -a -G docker ec2-user')

#creating the dockerfile
os.system('sudo touch Dockerfile')
