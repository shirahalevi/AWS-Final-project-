import json
import boto3
import random

dynamodb = boto3.resource('dynamodb')
VEHICLES_TABLE = 'Vehicles'

# Example data sources
NAMES = ["John", "Sara", "David", "Kuku", "Maya", "Ali", "Nina"]
ROLES = ["DevOps", "Engineer", "Security", "Cleaner", "Manager", "Intern"]

def lambda_handler(event, context):
    try:
        table = dynamodb.Table(VEHICLES_TABLE
        for i in range(50):
            plate = str(1000000 + i)
            name = random.choice(NAMES)
            role = random.choice(ROLES)
            item = {
                'license_plate': plate,
                'driver_name': f"{name} {random.randint(1, 99)}",
                'employee_id': f"E{i:03d}",
                'phone_number': f"050-{random.randint(1000000, 9999999)}",
                'email': f"{name.lower()}{i}@example.com",
                'role': role,
                'fouls': 0
            }
            table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': '50 cars added with fouls=0'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


