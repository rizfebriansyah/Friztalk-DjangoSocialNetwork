import uuid

def generate_random_character():
    randomcode = str(uuid.uuid4())[:9].replace('-','').lower()
    return randomcode 
