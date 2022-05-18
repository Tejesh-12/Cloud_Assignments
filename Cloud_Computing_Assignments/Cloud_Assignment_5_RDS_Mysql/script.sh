!/usr/bin/python



import os


os.system('yum install -y python python-dev python-pip')
os.system('pip install boto3')


os.system('sudo yum update -y')
os.system('sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2')
os.system('sudo yum install -y httpd')
os.system('sudo systemctl start httpd')
os.system('sudo usermod -a -G apache ec2-user')
os.system('sudo chown -R ec2-user:apache /var/www')
os.system('sudo chmod 2775 /var/www')
os.system('find /var/www -type d -exec sudo chmod 2775 {} \;')
os.system('find /var/www -type f -exec sudo chmod 0664 {} \;')

os.system('mkdir var/www/inc')
os.system("""echo " <?php define('DB_SERVER', 'tejesh.coztso5flgrl.us-east-1.rds.amazonaws.com');define('DB_USERNAME', 'Tejesh');define('DB_PASSWORD', 'chandu07@');
define('DB_DATABASE', 'Tejesh');?>" >> var/www/inc/dbinfo.inc""")

import boto3

access_id_key = "ASIAWTQ2NIW57NQOSBUM"
secret_access_key = "rcmiIg/nBKI/P574YF/tjz2P2b2j4AP5DDmpp4BO"
session_token_key = "FwoGZXIvYXdzEKr//////////wEaDM8dXbrKwomP5FS0hyLLAc18S0oQIsUS7OBmS9TzV281pcKaOYf1kEc2J+G6ICmZLuQj4IhcI1p9NyQngSF2CFq+JIQjqdhZ6X9m2mvIE9ZhQriDIwx1R7SmPwq22IeBF7+tBKGuP7Nden2IrwSVYK8PCIcxwgw4xt2whP63jCISbQ0QgF6apt6Zlr2rW5dbg0CEiQKrJGl8SnewtIU2lcpK9seiPnYTCE2Yl0BMev94JDy8M8nDUmgy3C4Tk0G7r7tPWQTdAbPT7J8P0CgIlOh6QZvOsmEOx1QSKO+LqIoGMi0VtX3Bi6nhDSZoDZmTgC6HTAXznYNV+t07TXfFQSCL8ID/s6hLRUCNZuMXCmA="


s3client = boto3.client('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key)
s3client.download_file('cse-351-q1','index.html','var/www/html/index.html')
s3client.download_file('cse-351-q1','authentication.php','var/www/html/authentication.php')
s3client.download_file('cse-351-q1','connection.php','var/www/html/connection.php')
s3client.download_file('cse-351-q1','customer.html','var/www/html/customer.html')
s3client.download_file('cse-351-q1','customer.php','var/www/html/customer.php')
s3client.download_file('cse-351-q1','feeedback.php','var/www/html/feeedback.php')
s3client.download_file('cse-351-q1','style.css','var/www/html/style.css')