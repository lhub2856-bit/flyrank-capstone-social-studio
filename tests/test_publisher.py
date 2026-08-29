import sys
import os
import hmac
import hashlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.security_webhook import TokenSecurity, verify_webhook_signature

def test_token_encryption():
    security = TokenSecurity()
    token = "secret_oauth_token_123"
    encrypted = security.encrypt_token(token)
    
    decrypted = security.decrypt_token(encrypted["nonce"], encrypted["ciphertext"])
    assert decrypted == token

def test_webhook_signature():
    secret = "my_test_secret"
    payload = b'{"event": "published"}'
    
    valid_sig = hmac.new(secret.encode('utf-8'), payload, hashlib.sha256).hexdigest()
    
    assert verify_webhook_signature(payload, valid_sig, secret) is True
    assert verify_webhook_signature(payload, "invalid_signature", secret) is False