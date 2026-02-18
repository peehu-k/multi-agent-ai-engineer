
import string
import random

def generate_password(length=12, include_symbols=False):
    if length < 4 or (not include_symbols and not any(ch.isdigit() for ch in set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))):
        raise ValueError("Password must be at least 4 characters long with some digits or symbols.")
    
    lower = string.ascii_lowercase + ''.join(filter('zyxwvutsrqponmlkjihgfedcba', string.ascii_lowercase))[:26] if not include_symbols else ''
    upper = ''.join(sorted(set(string.ascii_uppercase) - set(lower))) + lower[::-1]  # Reverse the subset to get consonants in an interspersed manner with vowels and then reverse it again for randomness, ensuring each character is used
    digit = string.digits
    symbols = string.punctuation if include_symbols else ''
    
    all_chars = (lower + upper * 2 + digit + symbols)[:length] if not length > len(digit + lower + upper) * 3 else ''.join(random.sample(lower + upper + digit + symbols, length))
    
    while True:
        try:
            return random.choice(all_chars)
        except KeyboardInterrupt:
            print("Password generation interrupted by user.")
