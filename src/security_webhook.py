import os
import hmac
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# 1. Token Encryption & Decryption (AES-GCM)
class TokenSecurity:
    def __init__(self, key: bytes = None):
        # Generate or use a 32-byte key for AES-256-GCM
        self.key = key or AESGCM.generate_key(bit_length=256)
        self.aesgcm = AESGCM(self.key)

    def encrypt_token(self, token: str) -> dict:
        nonce = os.urandom(12)  # Random IV / Nonce
        encrypted_data = self.aesgcm.encrypt(nonce, token.encode('utf-8'), None)
        return {"nonce": nonce.hex(), "ciphertext": encrypted_data.hex()}

    def decrypt_token(self, nonce_hex: str, ciphertext_hex: str) -> str:
        nonce = bytes.fromhex(nonce_hex)
        ciphertext = bytes.fromhex(ciphertext_hex)
        decrypted_data = self.aesgcm.decrypt(nonce, ciphertext, None)
        return decrypted_data.decode('utf-8')

# 2. Webhook Signature Verification (HMAC-SHA256)
def verify_webhook_signature(payload_body: bytes, received_signature: str, secret_key: str) -> bool:
    """
    Verifies the HMAC signature of incoming webhooks from the platform.
    """
    computed_signature = hmac.new(
        secret_key.encode('utf-8'),
        payload_body,
        hashlib.sha256
    ).hexdigest()
    
    # Secure comparison to prevent timing attacks
    return hmac.compare_digest(computed_signature, received_signature)