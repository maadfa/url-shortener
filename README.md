# Serverless URL Shortener

A simple serverless URL shortener built with AWS Lambda, API Gateway, and DynamoDB using the Serverless Framework.

## Features

- Shorten any long URL with a unique short code
- Automatically redirects short URLs
- Built using AWS serverless services
- Infrastructure as Code via `serverless.yml`

## Endpoints

- `POST /shorten` → `{ "longUrl": "https://example.com" }`
- `GET /{shortCode}` → Redirects to original URL

## Deployment

```bash
npm install -g serverless
sls deploy
