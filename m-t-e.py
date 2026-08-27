import re
mydic = {'A' : '.-', 'H' : '....','I':'..'}

temp=input("enter morse code: ")
pattern = re.findall(".|-",temp)
if pattern==True:
    for key, value in mydic.items():
        if value == temp:
            print(key)   
else: 
    print("Please enter morse code")


