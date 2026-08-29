# flyrank-capstone-social-studio
this is my capstone project assignment.
# FlyRank Social Studio (Capstone Project)

FlyRank Social Studio is an automated social campaign publishing and content management utility designed with enterprise-grade adapter layers, secure token encryption, and robust webhook verification safeguards.

## 🚀 Key Features

### 1. Content Generation Pipeline
* **Image Variants**: Automatically generates tailored image dimensions (e.g., 1080x1080 for Instagram and 1600x900 for X/Twitter).
* **Caption Composer**: Combines shared brand voice fragments with platform-specific requirements.

### 2. Adapter Layer & Reliability
* **SocialPublisher Interface**: Implements an abstract base class pattern utilizing `FakeInstagramPublisher` and `FakeXPublisher` adapters for reliable cross-platform publishing.
* **Idempotency & Rate Limit Handling**: Built-in `Idempotency-Key` header support and robust exponential backoff logic for handling HTTP 429 Retry-After responses safely.

### 3. Security & Webhook Verification
* **Encrypted Tokens**: Employs AES-GCM encryption with random IV/nonce generation for secure OAuth token storage and handling via `security_webhook.py`.
* **Webhook Trust**: Configured with HMAC-SHA256 signature verification to securely authenticate incoming payloads and reject unauthorized or forged requests with a `400` status code.

---

## 🛠️ Tech Stack & Testing
* **Language**: Python
* **Cryptography**: `cryptography` (AES-GCM)
* **Security & Hashing**: `hmac`, `hashlib` (SHA-256)
* **Testing Suite**: `pytest` (covering unit tests for token encryption, image pipeline, and webhook signatures)

## 🧪 Running Tests
To verify the test suite locally in your virtual environment, run:
```bash
pytest -v
