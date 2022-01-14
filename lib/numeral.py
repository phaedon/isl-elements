from islenska import Bin

# import grammar_enums
# import difflib

icebin = Bin()


class Numeral:
    """Docstring."""

    def __init__(self, word):
        """Docstring."""
        self.word = word

    def get_form(self, case, gender):
        """Docstring."""
        variants = icebin.lookup_variants(
            self.word, "to", to_inflection=(gender.value, case.value)
        )
        # print(variants)
        if len(variants) < 1:
            return None
        # Required for disambiguation:
        for match in variants:
            if match.ord == self.word:
                return match.bmynd
        return None


def is_numeral(bin_lookup_entry):
    return bin_lookup_entry.ofl == "to"


def create_numeral(word):
    _, matches = icebin.lookup(word)
    for match in matches:
        if is_numeral(match):
            return Numeral(match.ord)
    return None


first_four = {
    1: create_numeral("einn"),
    2: create_numeral("tveir"),
    3: create_numeral("þrír"),
    4: create_numeral("fjórir"),
}
