import re
mydic = {  'A':'.-',     'B':'-...',
                'C':'-.-.',   'D':'-..',     'E':'.',
                'F':'..-.',   'G':'--.',     'H':'....',
                'I':'..',     'J':'.---',    'K':'-.-',
                'L':'.-..',   'M':'--',      'N':'-.',
                'O':'---',    'P':'.--.',    'Q':'--.-',
                'R':'.-.',    'S':'...',     'T':'-',
                'U':'..-',    'V':'...-',    'W':'.--',
                'X':'-..-',   'Y':'-.--',    'Z':'--..',
                '1':'.----',  '2':'..---',   '3':'...--',
                '4':'....-',  '5':'.....',   '6':'-....',
                '7':'--...',  '8':'---..',   '9':'----.',
                '0':'-----',  ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.',   '-':'-....-',
                '(':'-.--.',  ')':'-.--.-' }

temp=input("enter morse code: ")
pattern = re.match(".|-",temp)

#for single character
# if pattern:
#     for key, value in mydic.items():
#         if value == temp:
#             print(key)   
# else: 
#     print("Please enter morse code")

# for multiple charcters
letters = temp.split(" ")

result = ""
for letter in letters:
    for key, value in mydic.items():
        if value == letter:
            result += key
print(result)


