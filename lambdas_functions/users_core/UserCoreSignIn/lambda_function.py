import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user_core_ddbb')

def lambda_handler(event, context):

    if 'body' in event:
        try:
            body = json.loads(event['body'])
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON')
            }
    else:
        body = event

    account = body.get('account')
    password = body.get('password')

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

        if password == items[0].get('password'):
            return {
                'statusCode': 200,
                'body': json.dumps(items)
            }
        
        else:
            return {
                'statusCode': 401,
                'body': json.dumps('Incorrect password')
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error querying the database: {str(e)}")
        }