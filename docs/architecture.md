# Architecture

## Flow Overview

 **User sends a POST request** to shorten a long URL.
 
 **API Gateway** receives the request and sends it to a **Lambda function**.
 
 **Lambda** generates a short code and stores it in **DynamoDB** with the original URL.
 
 **GET request** to the short URL triggers another Lambda function.
 
 **Lambda** looks up the code in **DynamoDB** and **redirects** the user to the original long URL.


