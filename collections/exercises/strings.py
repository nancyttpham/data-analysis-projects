# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.

print(text[:12])

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!

print(text[-12:])

# 3. Print a slice of the middle 12 characters from 'text'.
print(text[12:24])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
full_index = len(word)
for index in range(full_index):
    print(word[index])

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
full_index = len(word)-1
for index in range(full_index, -1, -1):
    print(word[index])

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').

full_index = len(word)-1
combo_word = ""
for index in range(full_index, -1, -1):
    combo_word += word[index]
print(word, "|", combo_word)