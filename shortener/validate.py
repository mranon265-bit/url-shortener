def validate(url):
    if not url:
        return False
    if not url.startswith(('http://', 'https://' , 'www.')) :
        return False
    return True