guess = input("Guess a letter: ")
alpha_flag = guess.isalpha()
guess_len = len(guess)
if (alpha_flag) and (guess_len != 1):
    print('E1')
elif not(alpha_flag) and (guess_len == 1):
    print('E2')
elif not(alpha_flag) and (guess_len != 1):
    print('E3')
elif (alpha_flag) and (guess_len == 1):
    print(guess.lower())

