"""
Representation of nouns in Icelandic.
"""

import difflib
from islenska import Bin
import grammar_enums

icebin = Bin()


def _get_variant_tuple(case, number, article):
    """Helper function which packages grammar info to send to Bin lookup_variants."""
    return (case.value, number.value, article.value)


class Noun:
    """Docstring."""

    def __init__(self, word, gender):
        """Docstring."""
        self.word = word
        self.gender = gender
        self._infl_class = None

    def get_form(self, case, number, article=grammar_enums.Article.INDEFINITE):
        """Docstring."""
        variants = icebin.lookup_variants(
            self.word, self.gender.value, _get_variant_tuple(case, number, article)
        )
        if len(variants) < 1:
            return None
        # Required for disambiguation:
        for match in variants:
            if match.ord == self.word:
                return match.bmynd
        return None

    def get_inflection_summary(self):
        """
        TODO(sinis): This is currently broken for any nouns with vowel shifts.
        Examples: "dvöl", "firði"
        """
        gen_sing = self.get_form(
            grammar_enums.Case.GENITIVE,
            grammar_enums.Number.SINGULAR,
            grammar_enums.Article.INDEFINITE,
        )
        nom_pl = self.get_form(
            grammar_enums.Case.NOMINATIVE,
            grammar_enums.Number.PLURAL,
            grammar_enums.Article.INDEFINITE,
        )
        s = difflib.SequenceMatcher(None, self.word, gen_sing)
        match = s.find_longest_match(0, len(self.word), 0, len(gen_sing))
        return self.word[0 : match.size]

    @property
    def infl_class(self):
        """Docstring."""
        return self._infl_class

    @infl_class.setter
    def infl_class(self, infl_class):
        """Docstring."""
        self._infl_class = infl_class


def is_noun(bin_lookup_entry):
    try:
        grammar_enums.Gender(bin_lookup_entry.ofl)
        return True
    except ValueError:
        return False


def create_nouns(word):
    """
    Returns a list of Nouns corresponding to the input word.
    If the input is unambiguous ("bílinn") only one instance is returned.
    In the case of ambiguous matches ("á") all instances are returned.
    """
    nouns = []
    _, matches = icebin.lookup(word)
    seen = []
    for match in matches:
        if is_noun(match):
            noun = Noun(match.ord, grammar_enums.Gender(match.ofl))
            if (noun.word, noun.gender) not in set(seen):
                nouns.append(noun)
                seen.append((noun.word, noun.gender))
    # print(seen)
    return nouns


def get_gender(w):
    """Converts a string like 'no kk' to a Gender enum"""
    if w.startswith("no "):
        return grammar_enums.Gender(w.removeprefix("no "))
    return None


def create_noun_from(word, gender):
    _, matches = icebin.lookup(word)
    for match in matches:
        if is_noun(match) and match.ofl == gender.value:
            return Noun(match.ord, grammar_enums.Gender(match.ofl))
    return None


def create_noun(w):
    maybe_noun = create_noun_from(w.word, get_gender(w.grammarcat.strip()))
    if maybe_noun is None:
        return None
    maybe_noun.wordentry = w
    return maybe_noun


def generate_nouns(word_list):
    """Temporary helper to get nouns."""
    nouns = []
    for word in word_list:
        nouns += create_nouns(word)
    return nouns


def generate_noun_decl_models():
    nouns = []
    for line in open("noun_decl_patterns.txt"):
        n, _, _, g = line.split(",")
        noun = create_noun(n, grammar_enums.Gender(g.strip()))
        if noun:
            nouns.append(noun)
    return nouns


# gn = generate_nouns(["bílinn", "á", "hestur", "dvöl", "firði"])
# print(gn)
# for g in gn:
#    print(g.word, g.gender)
