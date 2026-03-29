# core/security.py
import hashlib
import hmac
import os

class SecurityCore:
    def __init__(self):
        # In production, this secret would be in your .env file
        self.secret_key = os.getenv("APP_SECRET", "IMMORTAL_PROTOCOL_77").encode()

    def generate_token(self, message):
        """Creates a secure HMAC token for a message."""
        return hmac.new(self.secret_key, message.encode(), hashlib.sha256).hexdigest()

    def verify_integrity(self, message, token):
        """Checks if the message matches the secure token."""
        expected_token = self.generate_token(message)
        return hmac.compare_digest(expected_token, token)

    def hash_ip(self, ip_address):
        """Anonymizes IP addresses in logs for privacy/security."""
        return hashlib.md5(ip_address.encode()).hexdigest()

# Global security instance
security_provider = SecurityCore()