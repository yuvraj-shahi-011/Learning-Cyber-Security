import re
password = input("Enter a test password: ")
print("\nPassword Strength Check:")
#Minimumlength
if len(password) >= 8:
    print(" Minimum length: PASS")
else:
    print(" Minimum length: FAIL")
#Uppercase
if re.search(r"[A-Z]", password):
    print(" Uppercase letter: PASS")
else:
    print(" Uppercase letter: FAIL")
#Lowercase
if re.search(r"[a-z]", password):
    print(" Lowercase letter: PASS")
else:
    print(" Lowercase letter: FAIL")
#Number
if re.search(r"[0-9]", password):
    print(" Number: PASS")
else:
    print(" Number: FAIL")
#Special character
if re.search(r"[^A-Za-z0-9]", password):
    print(" Special character: PASS")
else:
    print("Special character: FAIL")