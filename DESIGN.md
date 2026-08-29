# Design Document: Multi-Platform Social Campaign Publisher

## 1. Problem Statement
Converting a single published blog post into a multi-platform social media campaign manually is time-consuming, prone to duplicate publishing during network timeouts, vulnerable to rate limits (429), and lacks secure token handling and verifiable webhook tracking.

## 2. Architecture & Layers
- **Content Generation Layer:** Generates platform-specific image variants (Instagram 1080x1080, X 1600x900) and composable captions.
- **Publisher Adapter Layer:** Implements a generic `SocialPublisher` interface with platform-specific adapters (`FakeInstagramPublisher`, `FakeXPublisher`).
- **Reliability & Queue Layer:** Handles idempotency keys, exponential backoff for rate limits, and durable scheduling.
- **Trust & Webhook Layer:** Verifies HMAC signatures on delivery webhooks before updating campaign status.

## 3. Data Model
- **Campaigns:** id, title, source_content_url, created_at
- **Posts:** id, campaign_id, platform, status (queued, publishing, published, failed), image_url, caption, idempotency_key
- **Tokens:** encrypted oauth tokens with random IV.

## 4. Non-Goals
- Connecting to live, production social media APIs (core build relies strictly on the provided fake platform server).