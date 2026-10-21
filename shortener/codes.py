import hashlib

def generate_code(long_url):
    hash=hashlib.sha256(long_url.encode("utf-8")).hexdigest()
    return hash[:6]
