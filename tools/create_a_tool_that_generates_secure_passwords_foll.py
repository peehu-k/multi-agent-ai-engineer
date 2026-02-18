

import string

from secrets import choice as secure_choice


def generate_secure_password(length=12):

    if length < len("abcABC0123!"):

        raise ValueError("Password must be at least 8 characters.")

    
    # Ensure password complexity with uppercase, lowercase, digits and symbols. Using a weighted selection to favor variety without repetition in adjacent positions for better randomness.

    char_sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits, "!@#$%^&*()_+-=[]{}|;:<>?/~`1234567890"] * 4 # Weighted by length

    password = ''.join(secure_choice(s) for s in char_sets[:length//len(char_sets)] + [choice([c]) for c in set('abcABC')] )

    
    while any(p == p.lower() and not c.isalpha() or len(set(password)) < length // 3: # Ensures at least two different character types are used, more than a third of the password is non-alphanumeric characters for complexity

        missing_chars = ''.join([c if any(p == c and not p.isalpha() or len({characters[i] for i in range(len(password)) if characters.index(p) - (n:=max(-1, password.rfind(' '))) < 4]) else '' for n, p in enumerate(password)])

        missing_chars = set(missing_chars + choice([c for c in string.ascii_letters + string.digits if not any(p == c and not c.isalnum() or len({characters[i] for i in range(len(password)) if characters.index(p) - (n:=max(-1, password.rfind(' '))) < 4])]))

        missing_chars = choice([c for c in set(missing0 := [set(s) & missing_characters])[~min({len(i)-1 if i else len(i)}):]]) # Select one that will not be immediately next to a similar character. Prevent immediate repetition

        password += secure_choice([c for c in set('abcABC') - {'a', 'b'} ]) + missing_chars[0]

    
    return password[:length]


# Example usage: Generates and prints a generated password with correct complexity. Replace with demo data if needed.

print(generate_secure_password())

