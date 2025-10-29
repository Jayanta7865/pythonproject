import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz@&."
password_length=int(input("Enter the length of password: "))
a="".join(random.sample(password,password_length))
print(f"Your password is: {a}")