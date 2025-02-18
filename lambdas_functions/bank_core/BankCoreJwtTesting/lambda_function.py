import jwt
import logging

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    logger.info("lambda_handler:private_key")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    logger.info("lambda_handler:formatted_private_key")
    formatted_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    logger.info("lambda_handler:payload")
    payload = {
        'user_id': '123456789',
        'role': 'admin',
    }
    
    logger.info("lambda_handler:headers")
    headers = {
        'alg': 'RS256',
        'typ': 'JWT',
    }
    
    logger.info("lambda_handler:jwt_token")
    jwt_token = jwt.encode(
        payload,
        formatted_private_key,
        algorithm='RS256',
        headers=headers
    )
    
    logger.info("lambda_handler:public_key")
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
    
    logger.info("lambda_handler:decode_payload")
    decode_payload = jwt.decode(
        jwt_token,
        public_key,
        algorithms=['RS256']
    )
    
    logger.info("lambda_handler:done")
    logger.info("lambda_handler:decode_payload: %s", decode_payload)
    
    return "Done"