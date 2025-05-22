#Palindrome
#Word backwords

while True:
    word = input('Choose a word: ')
    check = word[::-1]
    if word == check:
        print(word + " is a palindrome")
        choice1 = input("Would you like to test another word? Type Y/N: ")
        print(choice1)
        while choice1.lower() != 'n' and choice1.lower() != 'y':
            choice1 = input("Try again, choose Y or N: ")
        if choice1.lower() == 'n':
            break
        elif choice1.lower() == 'y':
            continue
    if word != check:
        print(word + " is not a palindrome")
        choice2 = input("Would you like to test another word? Type Y/N: ")
        print(choice2)
        while choice2.lower() != 'n' and choice2.lower!= 'y':
            choice2 = input("Try again, choose Y or N: ")
        if choice2.lower() == 'n':
            break
        elif choice2.lower() == 'y':
            continue