from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Fixed key K (must be 16, 24, or 32 bytes for AES)
KEY = b"this_is_16_bytes"

def encrypt(plaintext: bytes) -> bytes:
    """
    Encrypts given plaintext.

        Return:
            nonce + tag + ciphertext,
            so decryption can reconstruct.
    """
    
    nonce = get_random_bytes(12) # Generate a random nonce (never reuse with same key)
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(plaintext)
    
    return nonce + tag + ct

def decrypt(ciphertext: bytes) -> bytes:
    """Decrypts given ciphertext.
    
        Return:
            The prviously encrypted plaintext.    
    """
    nonce = ciphertext[:12]
    tag = ciphertext[12:28]
    ct = ciphertext[28:]
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ct, tag)