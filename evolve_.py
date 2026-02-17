

def perform_mutation(candidate, population):

    if random.random() < mutation_rate:

        # Flip a bit (character) with the current candidate to create a new one for this generation

        flipped = ''.join([char if random.random() > 0.5 else chr(ord(char) + 32) for char in candidate])  # shifts from A-Z/a-z, wraps around after Z to ensure a valid character remains within the range

        return flipped

    else:

        return candidate

