# dynamic value from user
userage = int(input("please Enter your Age "))

if userage < 13:
    print("Child")
elif userage < 20: 
    print("Teenager")
elif userage < 60:
    print("Adult")
else:
    print("Senior")