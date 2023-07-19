import boto3

# Replace these values with your AWS credentials and region
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_REGION_NAME'  # e.g., 'us-east-1'

# Create a Boto3 RDS client
rds_client = boto3.client(
    'rds',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Specify the parameters for the new RDS instance
db_instance_params = {
    'DBInstanceIdentifier': 'YOUR_INSTANCE_IDENTIFIER',
    'DBInstanceClass': 'db.t2.micro',
    'Engine': 'mysql',  # Replace with the desired database engine (e.g., 'mysql', 'postgres', 'sqlserver')
    'MasterUsername': 'YOUR_MASTER_USERNAME',
    'MasterUserPassword': 'YOUR_MASTER_USER_PASSWORD',
    'AllocatedStorage': 20,
}

# Create the RDS instance
response = rds_client.create_db_instance(**db_instance_params)

# Get the endpoint and status of the new RDS instance
endpoint = response['DBInstance']['Endpoint']['Address']
status = response['DBInstance']['DBInstanceStatus']
print(f"RDS instance {response['DBInstance']['DBInstanceIdentifier']} created successfully.")
print(f"Endpoint: {endpoint}")
print(f"Status: {status}")
