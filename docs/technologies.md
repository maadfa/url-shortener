# Technologies Used

# Technologies Used

This project uses several Amazon Web Services (AWS) and developer tools to build a **serverless** and **scalable** URL shortener. Here's a breakdown of each technology used, what it does, and why it's important.

---

## ⚙️ AWS Lambda

**What is it?**  
AWS Lambda is a serverless computing service from Amazon. It runs your code **only when needed**, without requiring you to manage or provision any servers.

**What it does in this project:**  
- When a user submits a long URL, a Lambda function is triggered to generate a short code and save it in the database.
- When a user clicks a short URL, another Lambda function is triggered to fetch the original URL and redirect the user.

**Why it's useful:**  
- **No server management:** You only write your code; AWS handles the rest.
- **Cost-efficient:** You pay only for the time your function runs.
- **Scalable:** Automatically handles more traffic when needed.

---

## 🌐 Amazon API Gateway

**What is it?**  
API Gateway is a fully managed service that makes it easy to create, publish, maintain, and monitor APIs (Application Programming Interfaces).

**What it does in this project:**  
- Acts as the **entry point** to the application.
- Receives HTTP requests (`POST` to shorten URLs and `GET` to retrieve them) and passes them to the correct Lambda function.

**Why it's useful:**  
- **Security & control:** You can manage who accesses your APIs.
- **Scalable:** Automatically handles many incoming requests at once.
- **Flexible routing:** You can map different routes like `/shorten` or `/{shortCode}` to different Lambda functions.

---

## 🗃️ Amazon DynamoDB

**What is it?**  
DynamoDB is Amazon’s fast and flexible **NoSQL database** service, designed for high-performance applications.

**What it does in this project:**  
- Stores the mapping between short codes and long URLs.
- When someone enters a short code, the app looks it up in DynamoDB to find the matching original URL.

**Why it's useful:**  
- **High performance:** Quickly reads/writes data even at scale.
- **Serverless:** No need to manage database servers.
- **Highly available:** Your data is always accessible.

---

## 🛠️ Serverless Framework

**What is it?**  
The Serverless Framework is an open-source tool that helps you build and deploy serverless applications easily using Infrastructure as Code (IaC).

**What it does in this project:**  
- Manages the deployment of Lambda, API Gateway, and DynamoDB using one simple configuration file (`serverless.yml`).
- Automates the creation of AWS resources with a single command (`sls deploy`).

**Why it's useful:**  
- **Simple deployments:** Deploy everything with one command.
- **Reusable code:** Write configuration once and use it across environments.
- **Faster development:** Focus on your application, not the infrastructure.

---

## 🌐 HTTP Methods: GET & POST

**What are they?**  
They are types of requests sent from a client (like your browser or an app) to the server.

- `POST`: Used when you **send data** to the app (e.g., a long URL to be shortened).
- `GET`: Used when you **request data** (e.g., accessing a short URL to be redirected).

**Why they're important:**  
These methods are how users interact with your API. In this project:
- A `POST` request is used to create a short link.
- A `GET` request is used to open the short link and redirect the user.

---

## 🧾 YAML (`serverless.yml`)

**What is it?**  
YAML (Yet Another Markup Language) is a format used to write configuration files in a human-readable way.

**What it does in this project:**  
The `serverless.yml` file defines:
- What functions to deploy
- Which routes to expose (like `/shorten`)
- What permissions and resources (like DynamoDB tables) your app needs

**Why it's useful:**  
- Makes deployments predictable
- Easy to understand and edit
- Keeps all setup in one place

---

## 📦 Python

**What is it?**  
Python is a popular programming language known for its simplicity and readability.

**What it does in this project:**  
- The logic to shorten and expand URLs is written in Python (`handler.py` and `redirect.py`).

**Why it's useful:**  
- Easy to learn and write
- Lots of libraries and support
- Supported by AWS Lambda

---



