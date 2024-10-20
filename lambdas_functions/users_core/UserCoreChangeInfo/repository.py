import json
import boto3                                # type: ignore
from boto3.dynamodb.conditions import Key   # type: ignore

dynamodb = boto3.resource('dynamodb')


class DynamoDBRepository:
    def __init__(self, table_name: str):
        self.table = dynamodb.Table(table_name)

    def get_user(self, account: str):
        response = self.table.query(
            KeyConditionExpression=Key('account').eq(account)
        )
        items = response.get('Items', [])
        if items:
            return items[0]
        return None

    def update_user(self, account: str, user: dict):
        self.table.update_item(
            Key={'account': account},
            UpdateExpression='SET account = :account',
            ExpressionAttributeValues={':account': json.dumps(user)}
        )
