import time
from stellar_sdk import Keypair

def find_vanity_keypair(suffix):
    """
    Find a Stellar Keypair whose public key ends with a specific suffix.

    :param suffix: The desired ending string for the public key.
    :return: The keypair with the matching public key.
    """
    print(f"Searching for a Stellar public key ending with '{suffix}'...")
    attempts = 0
    start_time = time.time()

    while True:
        attempts += 1
        keypair = Keypair.random()
        public_key = keypair.public_key

        if public_key.endswith(suffix):
            elapsed_time = time.time() - start_time
            print(f"Found matching keypair after {attempts} attempts in {elapsed_time:.2f} seconds!")
            print(f"Public Key: {public_key}")
            print(f"Secret Key: {keypair.secret}")
            return keypair

# Set the desired suffix for the vanity public key
desired_suffix = "KNEX"
find_vanity_keypair(desired_suffix)
