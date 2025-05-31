# Serverless URL Shortener Guide

This is a step by step guide to build serverless URL shortner using  AWS free tier . It uses:

- **AWS Lambda** for handling the logic
- **API Gateway** for routing HTTP requests
- **DynamoDB** for storing URL mappings
- **Serverless Framework** for deployment purpose
  
  The overview of interconnection of each  service works is given below.
  
1. **User sends a POST request** with a long URL.
2. **API Gateway** receives the request and sends it to a **Lambda function**.
3. The Lambda function:
   - Generates a unique short code.
   - Saves the short code and original URL to **DynamoDB**.
4. When someone accesses the short link (`GET /{shortCode}`), another Lambda function:
   - Looks up the code in DynamoDB.
   - Redirects the user to the original long URL.

The goal is to shorten URLs efficiently without the need to manage servers.

Explore the documentation using the navigation on the left.
