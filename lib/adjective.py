from islenska import Bin
from grammar_enums import *

icebin = Bin()


class Adjective:
    def __init__(self, word):
        self.word = word

    def get_form(self, gender, case, number, infl_class):
        """Docstring."""
        variants = icebin.lookup_variants(
            self.word, "lo", (gender.value, case.value, number.value, infl_class.value)
        )
        if len(variants) < 1:
            return None
        # Required for disambiguation:
        for match in variants:
            if match.ord == self.word:
                return match.bmynd
        return None


def create_adj(w):
    maybe_adj = Adjective(w.word)
    if maybe_adj is None:
        return None
    maybe_adj.wordentry = w
    return maybe_adj
