from secret import token_bytes


def random_key(length: int) -> int:
    # Generate a random key of the specified length in bytes
    tb: bytes = token_bytes(length)
    # Convert the bytes to a bit string and return it
    return int.from_bytes(tb, "big")
