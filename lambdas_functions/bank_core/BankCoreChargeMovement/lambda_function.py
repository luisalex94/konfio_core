# LambdaFunction to charge a movement in dynamodb, this call first check if the balance is enough to do the movement, if it is enough, the movement is added to the account movements.

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
        movement_type = 'charge'
    
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
    
            balance = 0
            for item in items.get('movements'):
                balance += item.get('amount')
    
            if balance - amount < 0:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Insufficient funds')
                }
    
            items['movements'].append({
                'id': id,
                'type': movement_type,
                'concept': concept,
                'amount': -amount,
                'date': date
            })
            table.update_item(
                Key={'account': account},
                UpdateExpression='SET movements = :movements',
                ExpressionAttributeValues={':movements': json.dumps(items)}
            )
    
            return {
                'statusCode': 200,
                'body': json.dumps('Movement charged')
            }
        
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f"Error querying the database: {str(e)}")
            }