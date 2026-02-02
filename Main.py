print("Welcome to Email Slicer developed by Monty")

email = input("Enter your email address:").strip()

if "@" in email and "." in email:
    username, domain = email.split("@")
    print("Username:", username)
    print("Domain:", domain)
else:
    print("Invalid email address . Please try again.")    

