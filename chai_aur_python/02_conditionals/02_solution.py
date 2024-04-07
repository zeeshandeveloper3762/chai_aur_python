# algorithem: 
# 1. user ki age malom karo =>  (userage = int(input("Please provide your age ")))
# 2. malom karo wednesday he ya nhi => ()
# 3. 18 se niche walon ke lye ticket price 8 aur 18 ya oper walon ki ticket price 12 => (price = $12 if userage >= 18 else $8  )  

# problem solving by myself
# userage = int(input("Please provide your age "))

# if userage < 18:
#     print("your ticket price is $8")
# else:
    # print("your ticket price is $12")

day = "Wednesday"
user_age = int(input("Please Enter your age "))
price = 12 if user_age >= 18 else 8
if day == "Wednesday":
    price = price -2
    # price -= 2

print("Ticket Price for you is ", price, "\n $2 discount")