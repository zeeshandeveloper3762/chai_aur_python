# password = input("Please Enter your Password !")


# if len(password) < 6:
#     streangth = "Weak"
# elif len(password) <= 10:
#     streangth = "Medium"
# else: 
#     streangth = "Strong"

# print("your password is ", streangth)

# more optimize code

password = input("Please Enter your Password !")
password_length = len(password)

if password_length < 6:
     streangth = "Weak"
elif password_length <= 10:
     streangth = "Medium"
else:
    streangth = "Strong"

print("your password is ", streangth)

