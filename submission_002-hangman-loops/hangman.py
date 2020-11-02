import random
import sys


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    random_index = random.randint(0, len(word)-1)
    word_list = list(word)
    split = ''
    for i in range (0,len(word)):
        if (word_list[i] !=  word_list[random_index]):
            word_list[i] = "_"
    return (split.join(word_list))



# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    index = 0

    for i in range(len(answer_word)):
        if (char == original_word[index] and char != answer_word[i]):
            return True
        index += 1
    else:
        return False
        


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
   # if (char in original_word and char not in answer_word):
       # index = original_word.index(char)
    index = 0
    word_list = list(answer_word)
    for i in word_list:
        if (char == original_word[index] and char != i):
            word_list[index] = char

        index += 1
        
    new_word = ''.join(word_list)
    return(new_word)




def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("/----\n|\n|\n|\n|\n_______")
    elif number_guesses == 3:
        print('/----\n|   0\n|  \n|   \n|  \n_______')
    elif number_guesses == 2:
        print('/----\n|   0\n|   |\n|   |\n|  \n_______')
    elif number_guesses == 1:
        print("/----\n|   0\n|  /|\\\n|   |\n|   \n_______")
    else:
        print('/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______')

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    guesses = 5
    while (guesses > 0):
        if answer == word:
            break
        else:
            guess = get_user_input()
            if guess == "exit" or guess == "quit":
                print("Bye!")
                break
            elif is_missing_char(word, answer, guess):
                answer = do_correct_answer(word, answer, guess)
            else:
                guesses -= 1
                do_wrong_answer(answer, guesses)
    if (guesses == 0):
        print("Sorry, you are out of guesses. The word was:",word)
        


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    if len(sys.argv)== 2:
        words_file = sys.argv[1]
    else:
        words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

