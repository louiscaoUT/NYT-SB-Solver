"""Libraries"""

# used for word dictionary
import json


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


def dfs(
    letters: list,
    path: Stack,
    dictionary: dict,
    answers: list,
    required: str,
    stop: int,
) -> None:
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

    candidate = "".join(path)

    if len(candidate) > stop:
        return
    # check if candidate abides by rules of game
    if candidate in dictionary and required in path and len(candidate) >= 4:
        answers[len(candidate) - 4].add(candidate)

    for i in letters:
        path.push(i)
        dfs(letters, path, dictionary, answers, required, stop)
        # remove letter from path so we can reuse it later
        path.pop()


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
            print(f"\nAnswers of length {i}:", v, sep="\n", end="\n\n")
    else:
        print(
            f"\nAnswers of length {int(length)}:",
            answers[int(length) - 4],
            sep="\n",
            end="\n\n",
        )


def main():
    """Program takes in user input to solve the NYT spelling bee game"""
    # ask for letters for today
    letters = input(
        "Enter each letter in the spelling bee with no spaces. To exit press Enter: "
    ).strip()
    letters = [x for x in letters]

    while letters:
        # ask for the required letter in spelling bee
        required = input("Enter the required letter for today: ")

        # list below will store the family of strings by length
        answers = [set() for _ in range(4)]

        # open json file and make into dictionary using json library
        with open("words_dictionary.json") as json_file:
            # now we have a dictionary of possible words
            dictionary = preprocess_dictionary(json.load(json_file), letters, required)
            stack = Stack()
            stop = 7
            dfs(letters, stack, dictionary, answers, required, stop)

        # get their input to show answers
        length = input(
            "Enter the length of words you want to see, if you want to see all type 'all': "
        )
        while length:
            print_answers(answers, length)

            length = input(
                """\nEnter the length of words you want to see, if you want to see all type 'all'. If you want to exit press Enter: """
            )

        # break out early
        if not length:
            letters = ""
            continue

        # loop
        letters = (
            input(
                "Enter each letter in the spelling bee, each separated by a space. To exit press Enter: "
            )
            .strip()
            .split()
        )


if __name__ == "__main__":
    main()
