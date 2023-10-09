ranking = ['John', 'Sen', 'Lisa']

# Prompt the user to input a rank number and assign it to the variable 'rank'.
rank = int(input("Enter rank number: ")) - 1

# Access the element in the ranking list based on the given rank and assign it to the variable 'name'.
name = ranking[rank]

# Print the name of the person who has the given rank.
print(name)