from islenska import Bin
from grammar_enums import *

icebin = Bin()


class Adjective:
    def __init__(self, word):
        self.word = word

    def get_form(self, gender, case, number, article):
        """Docstring."""
        infl_class = (
            InflClass.STRONG if article == Article.INDEFINITE else InflClass.WEAK
        )
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
