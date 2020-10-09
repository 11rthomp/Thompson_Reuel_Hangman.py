#Hangman
import random
life_total = 7
guess_truth = False

with open("word_list.txt") as f:
    word_list = f.read().splitlines()
    
random_num = random.randint(0, len(word_list)-1)
word = word_list[random_num]


asterix_word= word.replace(word, "*" * len(word))

while life_total > 0 and not guess_truth:
    print(asterix_word)
    guess = input("Please enter your next guess:")
    if guess not in word:
        life_total -= 1  
    else:
        word_list = list(asterix_word)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
            word_list[index] = guess
            asterix_word = "".join(word_list)
            if "*" not in asterix_word:
                guess_truth = True

if life_total == 0:
    print("You lose")
else:
    print("congratulations you win")
