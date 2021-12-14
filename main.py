# vstupni promenne
SEPARATOR = "=" * 40
USERS = {
    "bob": {"123"},
    "ann": {"pass123"},
    "mike": {"password123"},
    "liz": {"pass123"}
}
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

#prihlaseni, kontrola uzivatelskeho vstupu a registrace, uvitani
user = input("USER:")
password = input("PASSWORD:")

if not user in USERS.keys():
    print("Unregistered user! Ending program...")
    quit()

elif not password in USERS.get(user):
    print ("Incorrect password! Ending program...")
    quit()
else:
    print("OK", SEPARATOR, sep="\n")
    print(f'{"Welcome to text analyzer".upper()} {user.upper()}!'.center(len(SEPARATOR)))
    print(SEPARATOR)
    print("We have " + str(len(TEXTS)) + " texts to be analyzed.")

#vyber textu, overeni vstupu
text_choice = (input("Enter a number between 1 and 3 to choose your text: "))

if text_choice.isnumeric():
    if int(text_choice) >=1 and int(text_choice) <= 3:
        text_index = TEXTS[int(text_choice) - 1]
        print(f"Choosen text no.: {int(text_choice)}")
        print(SEPARATOR)
    else:
        print(f"Choosen text no. {text_choice} dosen't exist! Ending program...")
        quit()
else:
    print("Next time enter a number! Ending program")
    quit()

#rozdělení na slova, odstranění teček a mezer
cleaned_words = []
chars_to_clean = ",.:;[]?!"

for word in text_index.split():
    if word in chars_to_clean:
        text_index.strip(word)
    else:
        cleaned_words.append(word.strip(",.:;[]?!"))

#pocet slov v textu
words_count = 0

for word in cleaned_words:
    words_count +=1
print (f"There are {words_count} words in the selected text.")

#pocet slov zacinajicich velkym pismenem
words_titlecase = 0

for word in cleaned_words:
    if word.istitle():
        words_titlecase +=1
print(f"There are {words_titlecase} titlecase words.")

#pocet slov psanych velkymi pismeny
words_uppercase = 0

for word in cleaned_words:
    if word.isupper():
        words_uppercase +=1

if words_uppercase == 1:
    print(f"There is {words_uppercase} uppercase word.")

else:
    print(f"There are {words_uppercase} uppercase words.")

#pocet slov psanych malymi pismeny
words_lowercase = 0

for word in cleaned_words:
    if word.islower():
        words_lowercase +=1
print(f"There are {words_lowercase} lowercase words.")

#pocet ciselnych retezcu v textu
nums=0

for word in cleaned_words:
    if word.isnumeric():
        nums +=1

#mnozne cislo ve vypisu
if nums == 1:
    print(f"There is {nums} numeric string.")
else:
    print(f"There are {nums} numeric strings.")

#suma cisel obsazenych v textu
nums_list = []

for word in cleaned_words:
    if word.isnumeric():
        nums_list.append(int(word))

print(f"The sum of all the numbers is {sum(nums_list)}.")

#cetnost jednotlivych delek slov
len_occur = {}

for word in cleaned_words:
    word_len = len(word)
    len_occur[word_len] = len_occur.setdefault(word_len, 0) + 1

#ziskani a serazeni delek slov
words_len = list(len_occur.keys())
sorted_lens = [words_len.pop(0)]

for l in words_len:
    for index, sorted_len in enumerate(sorted_lens):
        if l < sorted_len:
            sorted_lens.insert(index, l)
            break

    else:
            sorted_lens.append(l)

#vypis sloupcoveho grafu
print(SEPARATOR)
print(f'LEN | {"OCCURENCES":<17} | NR.'.ljust(len(SEPARATOR)))

for index in sorted_lens:
    num_stars = len_occur.get(index) * "*"
    occur = len_occur.get(index)
    print(f"{index:<3} | {num_stars:<17} | {occur:<3}".ljust(len(SEPARATOR)))

