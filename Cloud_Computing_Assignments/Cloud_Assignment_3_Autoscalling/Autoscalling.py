import boto3
import time

auto_s = boto3.client('autoscaling', region_name='us-east-1',
                     aws_access_key_id='ASIAXJKLR5ZW34ZSM4VQ', aws_secret_access_key='nqBqaOSQqeVVaEZxJ89bHnbb4r9JnTUVKxGCTUve', aws_session_token='FwoGZXIvYXdzEHIaDKDVnGnmnWv+rhTv9iLLAZp0gr5EwlyQV79y8GqWBmwTK4I77qlg7FEDHOdiGqxkO6ZkUrc38uhzwWSK6idX0HOBIPLpQr8I7DlWTI1upwVq0Zx10yyRSaIWpUi8MJJZlGQ1uPpdtW9uA1nlJu3/b0Xx176uDfN7jATLlXzV1lH4oDLWxdorVWo0K7iIwQSNsHhtkLDanvnbqd2ajaoUoI83eXpShwHDJ1ppmw6kS4Fyv9OA3IDhj6c5NmQYwj/dKjWeCbC7D5dbZkzG39NOF87zPvQkpEoWkkyQKJS+44kGMi3g6QcfjPTj0RsYFHcoddvaEThM7hkvo8nDxJCBtRWb00l1ks3aHiMlLEARbzc=')

lc=auto_s.create_launch_configuration(LaunchConfigurationName='my-launch-config',InstanceType='t2.micro',KeyName='CS351-CG31',ImageId = 'ami-0c2b8ca1dad447f8a',SecurityGroups=['sg-05b7a0133edf7c2c5'],
UserData=script)

auto_s.create_auto_scaling_group(
 AutoScalingGroupName='my-auto-scaling-group',
 LaunchConfigurationName='my-launch-config',
 AvailabilityZones=['us-east-1c'],
 MaxSize=3,
 MinSize=1
 ) 

scale_up_policy=auto_s.put_scaling_policy(
AdjustmentType='ChangeInCapacity',
AutoScalingGroupName='my-auto-scaling-group',
PolicyName='scale_up',
ScalingAdjustment=1
)
scale_down_policy=auto_s.put_scaling_policy(
AdjustmentType='ChangeInCapacity',
AutoScalingGroupName='my-auto-scaling-group',
PolicyName='scale_down',
ScalingAdjustment=-1
)

cloud_w = boto3.client('cloudwatch',aws_access_key_id='ASIAXJKLR5ZW34ZSM4VQ',aws_secret_access_key='nqBqaOSQqeVVaEZxJ89bHnbb4r9JnTUVKxGCTUve', aws_session_token='FwoGZXIvYXdzEHIaDKDVnGnmnWv+rhTv9iLLAZp0gr5EwlyQV79y8GqWBmwTK4I77qlg7FEDHOdiGqxkO6ZkUrc38uhzwWSK6idX0HOBIPLpQr8I7DlWTI1upwVq0Zx10yyRSaIWpUi8MJJZlGQ1uPpdtW9uA1nlJu3/b0Xx176uDfN7jATLlXzV1lH4oDLWxdorVWo0K7iIwQSNsHhtkLDanvnbqd2ajaoUoI83eXpShwHDJ1ppmw6kS4Fyv9OA3IDhj6c5NmQYwj/dKjWeCbC7D5dbZkzG39NOF87zPvQkpEoWkkyQKJS+44kGMi3g6QcfjPTj0RsYFHcoddvaEThM7hkvo8nDxJCBtRWb00l1ks3aHiMlLEARbzc=',region_name='us-east-1')
cloud_w.put_metric_alarm(
AlarmName='up_alarm',
Namespace='AWS/EC2',
MetricName='CPUUtilization',
Statistic='Average',
ComparisonOperator='GreaterThanThreshold',
Threshold=70,
Period=60,
EvaluationPeriods=2,
AlarmActions=[scale_up_policy['PolicyARN']]
)
cloud_w.put_metric_alarm(
AlarmName='down_alarm',
Namespace='AWS/EC2',
MetricName='CPUUtilization',
Statistic='Average',
ComparisonOperator='LessThanThreshold',
Threshold=40,
Period=60,
EvaluationPeriods=2,
AlarmActions=[scale_down_policy['PolicyARN']]
)

time.sleep(1)
response = auto_s.describe_auto_scaling_groups(
AutoScalingGroupNames=['my-auto-scaling-group'],
)
list_auto = response['AutoScalingGroups']
req_instance_id = (((list_auto[0])['Instances'])[0])['InstanceId']
print(req_instance_id)
ec2 = boto3.resource('ec2',aws_access_key_id='ASIAXJKLR5ZW34ZSM4VQ',aws_secret_access_key='nqBqaOSQqeVVaEZxJ89bHnbb4r9JnTUVKxGCTUve', aws_session_token='FwoGZXIvYXdzEHIaDKDVnGnmnWv+rhTv9iLLAZp0gr5EwlyQV79y8GqWBmwTK4I77qlg7FEDHOdiGqxkO6ZkUrc38uhzwWSK6idX0HOBIPLpQr8I7DlWTI1upwVq0Zx10yyRSaIWpUi8MJJZlGQ1uPpdtW9uA1nlJu3/b0Xx176uDfN7jATLlXzV1lH4oDLWxdorVWo0K7iIwQSNsHhtkLDanvnbqd2ajaoUoI83eXpShwHDJ1ppmw6kS4Fyv9OA3IDhj6c5NmQYwj/dKjWeCbC7D5dbZkzG39NOF87zPvQkpEoWkkyQKJS+44kGMi3g6QcfjPTj0RsYFHcoddvaEThM7hkvo8nDxJCBtRWb00l1ks3aHiMlLEARbzc=',region_name='us-east-1')
instance = ec2.Instance(id=req_instance_id)
instance.wait_until_running()
instance.load()
print("dns name=",instance.public_dns_name)

