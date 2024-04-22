# NYT *Spelling Bee* Solver

The *New York Times*' *Spelling Bee* game is a simple online game in which the goal is to construct the maximum number of words with a given set of letters, with the condition that there is a particular letter that must be used. The words can be any length greater than 4. We implement a Python script that automatically generates the set of all possible words for the given *Spelling Bee* letter set.

On the implementation end, we thought we could improve upon our solution by a dynamic programming approach and memoizing subproblems. However, after implementing it, it actually took significantly more time for the solver to generate a solution! If there are any other potential improvements, we would like to hear them! We also acknowledge that we can add more descriptive comments and docstrings to improve the reading experience.

We downloaded a dictionary detailing the possible words that were extracted from the NYT website, and then posted on GitHub by someone else. The only libraries used is the built-in `json` module.

As for test cases, we manually define them by inputting historical *Spelling-Bee* problems and solutions. `NYT_unittests.py` automates this process.

While the program is functional now, it is relatively slow (on the order of a few seconds in the upper limit). Our current implementation does not check for redundant subproblems, and that clearly has performance concerns.

Please note that in this implementation, the required letter is typed with the entire family of letters, and then by itself. E.g., when asked to input the letters in the spelling bee, one would type `nchikmu` and then `n` on the next line.

Credits to this github repository for the dictionary https://github.com/dwyl/english-words?tab=readme-ov-file
