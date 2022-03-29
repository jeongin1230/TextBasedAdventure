print("""
WELCOME! LET'S START THE ADVENTURE

You are standing outside of your house and you see a man running towards you and asking for urgent shelter.

Will you provide shelter to him. (Yes / No)
""")

answer1 = input(">>").upper()

if answer1 == 'YES' or answer1 == 'Y':
    print(
        "\nAfter 2 minutes, the Police came to your house, and ask you that whether the thief is "
        "in your house or not. Will you say (Yes / No)\n")

    answer2 = input(">>").upper()
    if answer2 == 'YES' or answer2 == 'Y':
        print("\nYou are an honest person. He was a thief & You won the Game")
    elif answer2 == 'NO' or answer2 == 'N':
        print("\nYou helped a thief. Now, go to Jail. GAME OVER")
    else:
        print("\nYou typed the wrong input. GOODBYE!")

elif answer1 == 'NO' or answer1 == 'N':
    print("\nNow, he is trying to kill you. Will, you knock him down? (Yes / No)\n")

    answer3 = input(">>").upper()

    if answer3 == 'YES' or answer3 == 'Y':
        print("\nCongrats! He was a thief & You helped the police to catch him with your bravery.")

    elif answer3 == 'NO' or answer3 == 'N':
        print("\nSorry! You are dead. He was a thief & He killed you. GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

else:
    print("\nYou typed the wrong input. GOODBYE!")
