import pandas

data = pandas.read_csv('nato.csv')

#Creates a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#Creates a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)