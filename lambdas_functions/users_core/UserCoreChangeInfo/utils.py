import json


def get_body(event):
    if 'body' in event:
        try:
            return json.loads(event['body'])
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON')
    return event

def update_user_info(user, name, address):
    user['name'] = name,
    user['address'] = address
    return user


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
