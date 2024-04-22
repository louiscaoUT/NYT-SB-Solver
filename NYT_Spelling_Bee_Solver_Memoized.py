"""Libraries"""

# used for word dictionary
import json
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Stack:
    """Just a basic stack implementation"""

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def __iter__(self):
        # Create a reverse iterator over the stack for LIFO behavior
        return reversed(self.stack)

    def __str__(self):
        return str(self.stack)


def preprocess_dictionary(dictionary: dict, letters: list, required: str):
    """Returns a dictionary consisting of only possible words given letters
    - Input:
        - dictionary of words: dict
        - letters for spelling bee that day: list
        - required letter: str
    - Output: dictionary consisting of possible words given letters"""

    letters_set = set(letters)
    # Keep words that have the required letter and consist only of the provided letters
    return {
        word
        for word in dictionary
        if required in word and set(word).issubset(letters_set) and len(word) >= 4
    }


def print_error() -> None:
    print("***Misinput detected, please try again***", end="\n\n")


def get_letters():
    """Function gets the 7 unique letters of the game"""

    # get letters
    while True:
        letters = input(
            "Enter the 7 unique letters of the day with no spaces in between: "
        ).strip()

        try:
            # turn into list
            letters = [x.lower() for x in letters]
            return validate_letters(letters=letters)

        except ValueError:
            # if error, reprompt
            print_error()


def validate_letters(letters):
    try:
        if len(set(letters)) != 7 or not (all(x.isalpha() for x in set(letters))):
            raise ValueError()
        return letters

    except ValueError:
        raise ValueError("Letters must be 7 unique letters!")


def get_required_letter(letters):
    """Function gets the required letter"""

    while True:
        letter = input("Enter the required letter for today: ").strip().lower()
        try:
            return validate_required_letter(letter=letter, letters=letters)
        except ValueError:
            print_error()


def validate_required_letter(letter, letters):
    try:
        if letter not in set(letters) or not (letter.isalpha()):
            raise ValueError()
        else:
            return letter
    except ValueError:
        raise ValueError("Letter must be one of the 7 provided!")


def get_length():
    """Function gets family of answers the user wants to see"""

    while True:
        length = (
            input(
                "Enter the length of word you want to see from 4-7 inclusive. To exit press Enter: "
            )
            .strip()
            .lower()
        )
        try:
            return validate_length(length=length)
        except ValueError:
            print_error()


def validate_length(length):
    try:
        if not length or 4 <= int(length) <= 7 or length == "all":
            return length
        else:
            raise ValueError()
    except ValueError:
        raise ValueError("Length has to be 4-7 inclusive or 'all'!")


def dfs(
    letters: list,
    path: Stack,
    dictionary: dict,
    answers: list,
    required: str,
    stop: int,
    cache: dict
) -> None:
    candidate = "".join(path)
    """Function recursively creates words (candidates) given a list of letters,
    if candidate abides by rules of the game, and is considered a word, function will
    add that candidate to a 2-D list where each element is a list containing family of
    words by length, i.e. one list will contain all words of length four, another of length five etc.

    - Input:
        - letters: list of chars
        - path: A stack containing all the letters in our candidate word
        - dictionary: dictionary of valid words
        - answers: 2-D list comprised of lists grouped by length of word
        - required: char, the required letter that has to be in the word
        - stop: the max length of word we want to search for
    - Output: None, function dynamically changes an array"""

    # Check if the candidate is in the cache
    if candidate in cache:
        return cache[candidate]

    if len(candidate) > stop:
        return
    # check if candidate abides by rules of game
    if candidate in dictionary and required in path and len(candidate) >= 4:
        answers[len(candidate) - 4].add(candidate)

    for i in letters:
        path.push(i)
        dfs(letters, path, dictionary, answers, required, stop, cache)
        # remove letter from path so we can reuse it later
        path.pop()

    # Store the result in the cache
    cache[candidate] = None


def print_answers(answers: list, length: str) -> None:
    """Function nicely prints the family of answers given by the user,
    if the user inputs 'all' for length, the function will output
    all the families of answers

    - Input:
        - answers: 2-D list comprised of lists grouped by length of word
        - length: str that denotes what families of answers the user wants to see
    - Output:
        - returns nothing, only prints the family of answers the user wants to see"""

    # all the answers
    if length == "all":
        for i, v in reversed(list(enumerate(answers, start=4))):
            if not v:
                v = "No valid answers"
            print(f"\nAnswers of length {i}:", v, sep="\n", end="\n\n")
    else:
        print(
            f"\nAnswers of length {int(length)}:",
            answers[int(length) - 4],
            sep="\n",
            end="\n\n",
        )

def find_answers(letters, required):
    """
    Solves for the set of answers using the set of letters and the required letter
    """
    # list below will store the family of strings by length
    answers = [set() for _ in range(4)]

    # open json file and make into dictionary using json library
    with open(os.path.join(__location__, "words_dictionary.json"), encoding = "utf-8") as json_file:
        # now we have a dictionary of possible words
        dictionary = preprocess_dictionary(json.load(json_file), letters, required)
        stack = Stack()
        stop = 7
        cache = {}
        dfs(letters, stack, dictionary, answers, required, stop, cache)  
    return answers

def main():
    """Program takes in user input to solve the NYT spelling bee game"""
    # ask for letters for today
    letters = get_letters()

    while letters:
        # ask for the required letter in spelling bee
        required = get_required_letter(letters=letters)

        # calculate set of answers
        answers = find_answers(letters, required)

        # get their input to show answers
        length = get_length()

        while length:
            print_answers(answers, length)
            length = get_length()

        # break out early
        if not length:
            letters = ""
            continue

        # loop
        letters = get_letters()


if __name__ == "__main__":
    main()
