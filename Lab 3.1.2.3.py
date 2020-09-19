secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
answer = 0
while answer !=777:
    answer =int(input('Please Enter the Guess Number : '))
    if answer == secret_number:
        print('You guessed :' , answer, 'Correct! :)')
        print("Well done, muggle! You are free now.")
    else:
        print("Ha ha! You're stuck in my loop!")