import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user_core_ddbb')

def lambda_handler(event, context):

    account = event.get('account')
    password = event.get('password')

    if not account:
        return {
            'statusCode': 400,
            'body': json.dumps('user_id is required')
        }
    
    try:
        response = table.query(
            KeyConditionExpression=Key('account').eq(account)
        )
        items = response.get('Items', [])
        
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error querying the database: {str(e)}")
        }