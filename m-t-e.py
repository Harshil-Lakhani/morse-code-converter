import re
from encrypt_dict import encrypt_dict

temp=input("enter morse code: ")
pattern = re.fullmatch(r"[.\- ]+", temp)

# for multiple charcters
letters = temp.split(" ")

result = ""
if pattern:
    for letter in letters:
        for key, value in encrypt_dict.items():
            if value == letter:
                result += key  
    print(result)
else: 
    print("Please enter morse code")
