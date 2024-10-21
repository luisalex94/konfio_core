import boto3    # type: ignore

client = boto3.client("ses")


def send_email(source: str, destination, message):
    response = client.send_email(
        Source=source, Destination=destination, Message=message)
    return response
