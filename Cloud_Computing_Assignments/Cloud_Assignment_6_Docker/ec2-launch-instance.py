import boto3


access_id_key = 'ASIATNXW6TNDC77X5E5F'
secret_access_key = '4XzL9WB3yJb0QgEUyh10X2QV8nsj8Gj24HtkEcRp'
session_token_key = 'FwoGZXIvYXdzEPn//////////wEaDMYzLHq2r3lF6you4iLXAe18kLo+uyR9gzpHz1/99EljdmLGJWf4xJ9oDRZBpjMRxOqSmDu+KSeeIYwbwYLR9jgFck5Ta56ihqwiplwHeFh8LJ6IQKi4HFwj8t3BQvfP8fEDgJFfVWzDlm7coYulw9F6mxUaAvezsUMCoIBDeH16kdC/vKGQ5q/5KUFvpjMs4utCMy2cfxw+c60N4ZhzafiyccWRs8t5XkISXPqey2jqo7F84iGFGvR9rb0H2BPxdhND5tEoidwvXrFIr6yPPZJhoIS83ucA68apAs5cdPuHTf7VHg0vKL7d8YoGMi2A/akgvd6fwiNrIPg6n4WHGP7qhpQ6700RrsZJVxd6cKz9R6Ae48pq/ygpVKs='

ec2 = boto3.resource('ec2',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key,region_name='us-east-1')
instances = ec2.create_instances(ImageId='ami-0c2b8ca1dad447f8a', MinCount=1, MaxCount=1, InstanceType = 't2.micro',KeyName='cse351',
SecurityGroupIds=['sg-04210768c310e703f'],UserData = open('script.sh').read())

print(instances)
#printing instances.
for instance in instances:
        print(instance)


instance = instances[0]
#waiting until the lunched instance is running.import boto3

instance.wait_until_running()
instance.load()
print("dns name =",instance.public_dns_name)
