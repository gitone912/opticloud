import random
import csv
# Fetch all RDS database engines available in AWS
rds_database_engines = ['mysql', 'postgres', 'sqlserver', 'oracle']
# ... add more database engines as needed

# Fetch all RDS database instance classes available in AWS
rds_database_instance_classes = ['db.t2.micro', 'db.t3.small', 'db.t3.medium', 'db.t3.large', 'db.m5.large', 'db.m5.xlarge', 'db.m5.2xlarge']
# ... add more instance classes as needed

# Generate random RDS databases data
rds_databases_data = [
    {
        "DBInstanceIdentifier": f"mydbinstance{i}",
        "DBInstanceStatus": random.choice(["available", "stopped"]),
        "Engine": random.choice(rds_database_engines),
        "EngineVersion": "5.7.22",
        "DBInstanceClass": random.choice(rds_database_instance_classes),
        "AllocatedStorage": random.randint(10, 100),
    }
    for i in range(500)  # Generating data for 3 databases
]

# Save RDS databases data to CSV file
with open('rds_databases_data.csv', 'w', newline='') as csvfile:
    fieldnames = rds_databases_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rds_databases_data)
