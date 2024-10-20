# Lambda function to add to the dynamodb table bank_core_ddbb a new movement of an account. This movement is a deposit and it is saved in the json format in the dynamodb table.

import json
import boto3                                # type: ignore
from boto3.dynamodb.conditions import Key   # type: ignore
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bank_core_ddbb')

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
    
        '''
        In this section is where the code ask to user_core_valid_user_info lambda function if the user is valid
        '''
    
        # Get the movements from the dynamodb database with the account number as the key
    
        account = body.get('account')
        concept = body.get('concept')
        amount = body.get('amount')
        date = body.get('date')

        # genrate a random id de 10 digits
        id = random.randint(0000000000, 9999999999)

        # type of movement: deposit
        movement_type = 'deposit'
    
        try:
            response = table.query(
                KeyConditionExpression=Key('account').eq(account)
            )
            items = response.get('Items', [])
    
            if not items:
                return {
                    'statusCode': 404,
                    'body': json.dumps('Account not found')
                }
    
            items = json.loads(items[0].get('movements'))
    
            items['movements'].append({
                'id': id,
                'type': movement_type,
                'concept': concept,
                'amount': amount,
                'date': date
            })
    
            table.update_item(
                Key={
                    'account': account
                },
                UpdateExpression='SET movements = :val1',
                ExpressionAttributeValues={
                    ':val1': json.dumps(items)
                }
            )
    
            return {
                'statusCode': 200,
                'body': json.dumps('Deposit movement successfully added')
            }
        
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f"Error querying the database: {str(e)}")
            }