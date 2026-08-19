from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# ---------------- ENCRYPT FILE ----------------
def encrypt_file(input_file, encrypted_file, key_file):

    # Generate AES Key
    aes_key = get_random_bytes(32)

    # AES Encryption
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)

    with open(input_file, "rb") as f:
        file_data = f.read()

    encrypted_data = cipher_aes.encrypt(
        pad(file_data, AES.block_size)
    )

    # Save encrypted file
    with open(encrypted_file, "wb") as f:
        f.write(cipher_aes.iv)
        f.write(encrypted_data)

    # Load RSA Public Key
    with open("keys/public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    # Encrypt AES Key using RSA
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    # Save encrypted AES key
    with open(key_file, "wb") as f:
        f.write(encrypted_aes_key)

    return True


# ---------------- DECRYPT FILE ----------------
def decrypt_file(encrypted_file, output_file, key_file):

    # Load RSA Private Key
    with open("keys/private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    # Read encrypted AES key
    with open(key_file, "rb") as f:
        encrypted_aes_key = f.read()

    # RSA decrypt AES key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    # Read encrypted file
    with open(encrypted_file, "rb") as f:
        iv = f.read(16)
        encrypted_data = f.read()

    # AES decrypt
    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)

    decrypted_data = unpad(
        cipher_aes.decrypt(encrypted_data),
        AES.block_size
    )

    # Save decrypted file
    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    return True