import secrets

print("New secret key generated.")
print(f"Secret key : {secrets.token_hex()}")

print("\nWrite down at your .env file with key SECRET_KEY")