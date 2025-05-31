# Architecture

## Flow Overview

1. **User sends a POST request** to shorten a long URL.
2. **API Gateway** receives the request and sends it to a **Lambda function**.
3. **Lambda** generates a short code and stores it in **DynamoDB** with the original URL.
4. **GET request** to the short URL triggers another Lambda function.
5. **Lambda** looks up the code in **DynamoDB** and **redirects** the user to the original long URL.


