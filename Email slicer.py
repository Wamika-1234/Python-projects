a=str(input("Enter your email address"))
email=a.strip()
print(email)
symbol_index=email.index("@")
print(symbol_index)
username=email[0:symbol_index]
print(username)
domain_name=email[symbol_index+1:]
print(domain_name)

print("Your username is ",username, "and your domain name is ",domain_name)
