import boto3
import csv
import random
from datetime import datetime, timedelta
import pandas as pd

# Generate random AWS Cost Explorer data with additional parameters
cost_explorer_data = [
    {
        "TimePeriod": {
            "Start": (datetime.utcnow() - timedelta(days=i)).isoformat(),
            "End": datetime.utcnow().isoformat(),
        },
        "Service": random.choice(["EC2", "RDS", "S3"]),
        "UsageType": random.choice(["DataTransfer-Out-Bytes", "EBS:VolumeUsage.gp2", "RDS:GP2-Storage"]),
        "Operation": random.choice(["RunInstances", "CreateDBInstance", "GetObject"]),
        "Resource": f"arn:aws:{random.choice(['ec2', 'rds', 's3'])}:us-west-2:123456789012:{random.choice(['instance-id', 'db-instance-id', 'bucket-name'])}/resource-id",
        "BlendedCost": {
            "Amount": round(random.uniform(10.0, 100.0), 2),
            "Unit": "USD",
        },
    }
    for i in range(500)  # Generating data for 5 time periods
]

# Convert AWS Cost Explorer data to DataFrame
cost_explorer_df = pd.DataFrame(cost_explorer_data)

# Extract useful features from the "Resource" column
cost_explorer_df['AWS Service'] = cost_explorer_df['Resource'].apply(lambda x: x.split(":")[2] if ":" in x else None)
cost_explorer_df['Region'] = cost_explorer_df['Resource'].apply(lambda x: x.split(":")[3] if ":" in x else None)
cost_explorer_df['Resource Type'] = cost_explorer_df['Resource'].apply(lambda x: x.split(":")[4] if ":" in x else None)
cost_explorer_df['Resource ID'] = cost_explorer_df['Resource'].apply(lambda x: x.split(":")[5] if ":" in x else None)

# Drop the original "Resource" column
cost_explorer_df = cost_explorer_df.drop(columns=['Resource'])

# Save AWS Cost Explorer data to CSV file
cost_explorer_df.to_csv('cost_explorer_data.csv', index=False)
