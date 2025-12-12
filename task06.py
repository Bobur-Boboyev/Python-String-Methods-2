email = input("Email: ")

ind = email.find("@")

if ind == -1:
    print("@ belgisi yo'q.")
    
print(ind)