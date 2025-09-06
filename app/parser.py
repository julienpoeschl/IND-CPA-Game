
ENCODING = "utf-8"

def to_string(byte : bytes) -> str:
    return str(byte, ENCODING)

def to_bytes(string : str) -> bytes:
    return bytes(string, ENCODING)