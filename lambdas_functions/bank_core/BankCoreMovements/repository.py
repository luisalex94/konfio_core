import boto3                                # type: ignore
from boto3.dynamodb.conditions import Key   # type: ignore
import json

dynamodb = boto3.resource('dynamodb')

class DynamoDBRepository:
    def __init__(self, table_name: str):
        self.table = dynamodb.Table(table_name)

    def get_movements(self, account: str):
        response = self.table.query(
            KeyConditionExpression=Key('account').eq(account)
        )
        items = response.get('Items', [])
        if items:
            return json.loads(items[0].get('movements'))
        return None