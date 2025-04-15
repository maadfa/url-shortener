import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def redirect_url(event, context):
    short_code = event['pathParameters']['shortCode']

    response = table.get_item(Key={'shortCode': short_code})

    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': 'URL not found'
        }

    long_url = response['Item']['longUrl']

    return {
        'statusCode': 302,
        'headers': {
            'Location': long_url
        }
    }
