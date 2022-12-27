import random
import string

def random_string(length:int) -> str:
    str_result = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return str_result