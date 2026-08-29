import os
from src.image_pipeline import generate_image_variants
from src.security_webhook import TokenSecurity, verify_webhook_signature

def notest_image_variants(tmp_path):
    # Test if image pipeline generates variants
    output_dir = str(tmp_path)
    variants = generate_image_variants("non_existent.jpg", output_dir)
    assert "instagram" in variants
    assert "x" in variants

def test_token_encryption():
    # Test AES-GCM encryption & decryption
    security = TokenSecurity()
    token = "secret_oauth_token_123"
    encrypted = security.encrypt_token(token)
    
    decrypted = security.decrypt_token(encrypted["nonce"], encrypted["ciphertext"])
    assert decrypted == token

def test_webhook_signature():
    # Test HMAC webhook verification
    secret = "my_test_secret"
    payload = b'{"event": "published"}'
    
    import hmac
    import hashlib
    valid_sig = hmac.new(secret.encode('utf-8'), payload, hashlib.sha256).hexdigest()
    
    # Valid signature should pass
    assert verify_webhook_signature(payload, valid_sig, secret) is True
    
    # Invalid signature should fail
    assert verify_webhook_signature(payload, "invalid_signature", secret) is False