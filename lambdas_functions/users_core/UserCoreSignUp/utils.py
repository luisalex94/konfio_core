import json
import random


def get_body(event):
    if 'body' in event:
        try:
            return json.loads(event['body'])
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON')
    return event


def account_number_generator():
    return random.randint(1, 99999999)


def pin_numer_generator():
    return random.randint(1, 9999)


def create_accout_data(user: str, name: str, address: str, password: str):
    return {
        'account': str(account_number_generator()),
        'user': user,
        'active_loan': '0',
        'active_user': '1',
        'address': address,
        'name': name,
        'password': password,
        'pin': str(pin_numer_generator())
    }


def create_bank_data(account: str):
    return {
        'account': account,
        'balance': '{"movements": []}'
    }


def response_200(body):
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }


def response_400(body):
    return {
        'statusCode': 400,
        'body': json.dumps(body)
    }


def response_500(body):
    return {
        'statusCode': 500,
        'body': json.dumps(body)
    }
