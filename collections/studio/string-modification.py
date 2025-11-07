my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
modified_string = (my_string[3:] + my_string[:3])


# Use a template literal to print the original and modified string in a descriptive phrase.
print(f"The original string is {my_string} and the modified string is {modified_string}.")


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
number_of_letters = int(input("Enter the number of letters that will be relocated:"))
updated_string = (my_string[number_of_letters:] + my_string[:number_of_letters])

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
number_of_letters = int(input("Enter the number of letters that will be relocated:"))
if number_of_letters > len(my_string):
    print(f"Invalid input: {number_of_letters} is larger than word. Default to 3 characters.")
    updated_string = (my_string[3:] + my_string[:3])
else:
    updated_string = (my_string[number_of_letters:] + my_string[:number_of_letters])

print(f"The original string is {my_string} and the updated string is {updated_string}")