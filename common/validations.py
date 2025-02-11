import hashlib
import uuid
from rest_framework.exceptions import ParseError
from config.settings import MAX_UPLOAD_SIZE

def generate_filename(instance, filename):
    return f"{hashlib.sha256(uuid.uuid4().hex.encode('utf-8')).hexdigest()}.{filename.split('.')[-1]}"


def validate_file_size(value):
    if value.size > MAX_UPLOAD_SIZE:
        raise ParseError("File size is too large")
    return value
