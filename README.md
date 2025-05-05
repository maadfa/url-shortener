# Serverless URL Shortener

A simple serverless URL shortener built with AWS Lambda, API Gateway, and DynamoDB using the Serverless Framework.This project shows a serverless URL  shortner that helps to shorten urls .It uses Lambda, API Gateway, and DynamoDB, and is managed through the Serverless Framework. The goal is to build a lightweight, scalable, and cost-effective solution without managing any servers.

## Technologies used:
1. AWS Lambda:
 
What it is:

A service that runs code in the cloud without needing to set up or manage servers.

What it does here:When someone wants to shorten a long URL, Lambda creates a short version of it.When someone opens the short URL, Lambda finds the original link and redirects to it.

Why it's important:It only runs when needed, saving costs. It’s fast and can scale automatically as more people use the app

2.API Gateways:

What it is: A service that lets people send HTTP requests (like POST or GET) to access cloud functions (like Lambda).

What it does here:Listens for incoming requests from users.Sends those requests to the correct Lambda function.

3.Dynamo DB:
What it is: A NoSQL database offered by AWS, built for fast and scalable storage.

What it does here:Stores the mapping between the short code (like abc123) and the original long URL.When someone uses the short code, it looks up the matching full URL.

Why it's important:It’s fast, always available, and doesn’t require managing any servers. Perfect for storing large numbers of short links.
   
 ## How the Architecture Works:
 
Flow Overview:

User sends a POST request to shorten a URL.

API Gateway receives the request and forwards it to a Lambda function.

Lambda generates a short code and stores it with the long URL in DynamoDB.

When someone visits the short URL (GET /{shortCode}), API Gateway routes it to Lambda.

Lambda looks up the code in DynamoDB and redirects to the long URL.



## Features

- Shorten any long URL with a unique short code
- Automatically redirects short URLs
- Built using AWS serverless services
- Infrastructure as Code via `serverless.yml`

## Endpoints

- `POST /shorten` → `{ "longUrl": "https://example.com" }`
- `GET /{shortCode}` → Redirects to original URL

## Deployment


npm install -g serverless
sls deploy
