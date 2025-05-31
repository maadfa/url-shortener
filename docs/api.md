# API Guide (How it works)

This app has two main functions:

1. Make a short URL from a long one
2. Open the short URL and go to the original long one

---

## 1. POST /shorten

**What it does:**  
This lets you turn a long website link (URL) into a short one.

**How to use it:**
- You send a POST request to `/shorten`
- You must include your long URL like this:

```json
{
  "longUrl": "https://example.com"
}
```

2.  GET /shortCode


When someone opens the short link (for example: https://yourdomain.com/abc123), it will automatically open the original long link.

Users don’t have to send anything. Just click or type the short link in your browser and it will take you to the full website.


**What you get back**:

A new short link, like 

```json
{
  "shortUrl": "https://yourdomain.com/abc123"
}
```




