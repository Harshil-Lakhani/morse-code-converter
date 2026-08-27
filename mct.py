from encrypt_dict import encrypt_dict

word=str(input("Enter word : ")).upper()
loc=list(word)
for chars in loc:
    print(encrypt_dict[chars])

    