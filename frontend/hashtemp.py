from streamlit_authenticator.utilities  import Hasher

# List of plain text passwords
passwords = ['IbMpAsSwOrD', 'NeStLePaSsWoRd', 'MiCrOsOfTpAsSwOrD']

# Hash the passwords
hashed_passwords = Hasher(passwords).generate()

# Print the hashed passwords
for plain, hashed in zip(passwords, hashed_passwords):
    print(f"Plain: {plain} -> Hashed: {hashed}")
