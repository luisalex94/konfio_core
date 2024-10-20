import boto3                                # type: ignore
from boto3.dynamodb.conditions import Key   # type: ignore

database = boto3.resource('dynamodb')


class DynamoDBRepository:
    def __init__(self, table_name: str):
        self.table = database.Table(table_name)
        
    # create_user method in dynamodb repository
    def create_user(self, data: dict):
        self.table.put_item(Item=data)