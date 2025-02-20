# download pandas if you didn't install it yet
# IN TERMINAL ENTER ( pip install pandas )
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}
while True:
    try:
        user_input = input("Enter the name: ").upper()
        result = [nato_dict[letter] for letter in user_input]
        break
    except KeyError:
        print("Sorry, only letters in the English alphabet please.")

print(result)