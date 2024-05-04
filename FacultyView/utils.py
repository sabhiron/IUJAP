from django.utils.crypto import get_random_string
unique_id = get_random_string(length=32)

def set_unique_id():
    global unique_id
    unique_id = get_random_string(length=32)
