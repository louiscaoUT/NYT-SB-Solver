from NYT_Spelling_Bee_Solver import *
import unittest
from unittest.mock import patch

def combine_sets(list_of_sets):
    """Converts a list of sets into a single set by merging values"""
    combined_set = set()
    for s in list_of_sets:
        combined_set.update(s)
    return combined_set

class Test_NYT(unittest.TestCase):
    def test_validate_letters(self):
        # less than 7 letters
        with self.assertRaises(Exception):
            validate_letters("a")

        # greater than 7 letters
        with self.assertRaises(Exception):
            validate_letters("aaaaaaa")

        # contains number
        with self.assertRaises(Exception):
            validate_letters("aaaa7")

        # correct input
        self.assertEqual(validate_letters("inkblot"), "inkblot")

    def test_validate_required_letter(self):
        # not a letter
        with self.assertRaises(Exception):
            validate_required_letter(letter="10", letters="i n k b l o t".split())

        # not in letters
        with self.assertRaises(Exception):
            validate_required_letter(letter="a", letters="i n k b l o t".split())

        # not in letters
        with self.assertRaises(Exception):
            validate_required_letter(letter="a", letters="i n k b l o t".split())

        # correct input
        self.assertEqual(
            validate_required_letter(letter="i", letters="i n k b l o t".split()), "i"
        )

    def test_validate_length(self):
        # length is less than 4
        with self.assertRaises(Exception):
            validate_length(3)

        # length is greater than 7
        with self.assertRaises(Exception):
            validate_length(8)

        # length is not a length and not "all"
        with self.assertRaises(Exception):
            validate_length("everything")

        # length is the exit command
        self.assertEqual(validate_length(length=""), "")

        # length is a correct input
        self.assertEqual(validate_length(length="7"), "7")

        # length is all the family of answers
        self.assertEqual(validate_length(length="all"), "all")

        # length is all the family of answers
        self.assertEqual(validate_length(length="exit"), "exit")

    def test_answers_1(self):
        """Checks if the generated answers matches a set of answers (1). Longest, for full test of capabilities"""
        answers1 = {'toil', 'blin', 'bino', 'bini', 'koil', 'bill', 'kilt', 'bitt', 'liin', 'loin', 'linn', 'intl', 'lint', 'koli', 'kiln', 'bilo', 'kobi', 'boni', 'kiki', 'lill', 'bibl', 'blit', 'olio', 'oink', 'liti', 'tilt', 'knit', 'bilk', 'oint', 'init', 'tino', 'tink', 'itll', 'ikon', 'bink', 'till', 'boii', 'titi', 'kino', 'kink', 'link', 'lion', 'nill', 'tiki', 'loki', 'obli', 'biti', 'into', 'lobi', 'bibb', 'noil', 'nito', 'bint', 'boti', 'ilot', 'lilt', 'lino', 'biol', 'kill', 'tint', 'bibi', 'bion', 'bito', 'toit', 'kilo', 'obit', 'boil', 'ioni', 'loli', 'kinoo', 'kikoi', 'oboli', 'linon', 'linin', 'binit', 'noint', 'nikko', 'iloko', 'niton', 'knoit', 'intil', 'ninon', 'oobit', 'tinni', 'boiko', 'biont', 'bilbi', 'onion', 'bilin', 'bibio', 'nikon', 'inion', 'kokio', 'kinot', 'bolti', 'ilion', 'nilot', 'obiit', 'bikol', 'likin', 'kioko', 'klino', 'bilio', 'kinin', 'kokil', 'intnl', 'bilbo', 'blini', 'blink', 'kikki', 'tibbit', 'initio', 'tonkin', 'ototoi', 'bookit', 'tiklin', 'libkin', 'koinon', 'inlook', 'lintol', 'biotin', 'liknon', 'bonito', 'billot', 'intill', 'inknot', 'inknit', 'notion', 'nonion', 'bobbin', 'lotion', 'boltin', 'billon', 'koilon', 'titbit', 'konini', 'bikini', 'kinbot', 'titoki', 'lbinit', 'koonti', 'tillot', 'toitoi', 'toolkit', 'bollito', 'kittool', 'kiloton', 'noonlit', 'nitinol', 'linolin', 'billion', 'littlin', 'libinit', 'inkblot', 'inition', 'kinboot', 'tittlin', 'bobooti', 'kilobit'}

        gen_answers = find_answers(["i", "n", "k", "b", "l", "o", "t"], "i")
        gen_answers = combine_sets(gen_answers)

        self.assertEqual(gen_answers, answers1)

    def test_answers_2(self):
        """Checks if the generated answers matches a set of answers (2). Shorter, so easier to manually verify"""
        answers2 = {'quot', 'quet', 'toque', 'queet', 'queue', 'quote', 'tuque', 'quott', 'toquet', 'quotee', 'totquot'}

        gen_answers = find_answers(["k", "e", "u", "j", "q", "o", "t"], "q")
        gen_answers = combine_sets(gen_answers)

        self.assertEqual(gen_answers, answers2)


    def test_answers_3(self):
        """Checks if the generated answers matches a set of answers (3)"""
        answers3 = {'externe', 'prex', 'export', 'exxon', 'exter', 'toxone', 'prorex', 'oxer', 'exor', 'expo', 'prox', 'expone', 'oxen', 'pnxt', 'exon', 'toxon', 'noex', 'expt', 'torpex', 'text', 'xerox', 'rexen', 'xenon', 'protext', 'exoner', 'oxter', 'oxetone', 'extern', 'exrx', 'expert', 'extent', 'next', 'extort', 'pretext', 'exert', 'exopt', 'oxeote'}

        gen_answers = find_answers(["x", "n", "e", "r", "o", "p", "t"], "x")
        gen_answers = combine_sets(gen_answers)

        self.assertEqual(gen_answers, answers3)

if __name__ == "__main__":
    unittest.main()
