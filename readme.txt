gifts for christmas
draw names

idea:
for every person generate txt file with key and encrypted name of other person
key is random alphabet, f.e. a=c, b=z, c=h
condition 0: a least 3 persons
condition 1: other person cannot be the same as current
condition 2: not person 1 to person 2 and person 2 to person 1

test:
generate txt files and check conditions for not random but every possible output


How to Use
Run the script by executing the following command in your terminal:

python3 secret_santa.py

Pass a file path (1)

Enter the names in the Vi editor and save the file.

The script will shuffle the names, assign Secret Santa pairs, and display the results.


Features
Create a Temporary File: The script provides an option to either pass a file path with names or create a temporary file for entering names.

Vi Editor Integration: If you choose to create a temporary file, the script opens it in the Vi editor for you to conveniently enter the list of names.

Countdown Timer: Displays a countdown timer when opening the temporary file in Vi editor, giving you time to prepare before entering names.