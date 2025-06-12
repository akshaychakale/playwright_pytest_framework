import random
import string

def random_email(domain="example.com"):
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{name}@{domain}"

def random_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def random_string(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_number_string(length=6):
    return ''.join(random.choices(string.digits, k=length))