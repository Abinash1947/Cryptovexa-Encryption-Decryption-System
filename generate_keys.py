from Crypto.PublicKey import RSA
import os

def generate_rsa_keys():
    if not os.path.exists("keys"):
        os.makedirs("keys")

    key = RSA.generate(2048)

    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("keys/private.pem", "wb") as f:
        f.write(private_key)

    with open("keys/public.pem", "wb") as f:
        f.write(public_key)
    print("RSA key generated   successfully!")

if __name__ == "__main__":
    generate_rsa_keys()
