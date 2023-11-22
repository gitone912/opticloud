import boto3
import csv
import random
from datetime import datetime

# Generate random EC2 instances data
ec2_instances_data = [
    {
        "InstanceId": f"i-{random.randint(1000000000, 9999999999)}",
        "InstanceType": random.choice(['t2.micro', 't3.small', 't3.medium', 't3.large', 'm5.large', 'm5.xlarge', 'm5.2xlarge' ]),
        "State": {"Name": random.choice(["running", "stopped"])},
        "LaunchTime": datetime.utcnow().isoformat(),
        "Tags": [{"Key": "Name", "Value": f"Instance_{i}"}],
    }
    for i in range(500)  # Generating data for 5 instances
]

# Save EC2 instances data to CSV file
with open('ec2_instances_data.csv', 'w', newline='') as csvfile:
    fieldnames = ec2_instances_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(ec2_instances_data)
