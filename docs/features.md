# Features

 It shorten any long URL using a unique short code  

 It automatically redirects users from the short URL to the long one 

 It is built using 100% serverless architecture (no servers to manage)  

 It is Scalable and cost-effective  
 
 Easily deployable using the Serverless Framework  

## Endpoints

### `POST /shorten`
- **Request Body**:
  ```json
  {
    "longUrl": "https://example.com"
  }
  ```

## Response:


```json

{
  "shortUrl": "https://yourdomain.com/abc123"
}
```



