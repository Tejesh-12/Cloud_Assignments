import boto3
 
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(ImageId='ami-0c2b8ca1dad447f8a', MinCount=1, MaxCount=1, InstanceType = 't2.micro',KeyName='CS351-CG31',
SecurityGroupIds=['sg-05b7a0133edf7c2c5'], UserData = open('assign2.sh').read())
 
print(instances)
#printing instances.
for instance in instances:
        print(instance)
 
 
instance = instances[0]
#waiting until the lunched instance is running.import boto3
 
instance.wait_until_running()
instance.load()
print("dns name =",instance.public_dns_name)