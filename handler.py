import json
import string
import random
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def shorten_url(event, context):
    body = json.loads(event['body'])
    long_url = body['longUrl']

    short_code = generate_short_code()

    table.put_item(Item={
        'shortCode': short_code,
        'longUrl': long_url
    })

    return {
        'statusCode': 200,
        'body': json.dumps({
            'shortUrl': f"https://your-api-domain.com/{short_code}"
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
