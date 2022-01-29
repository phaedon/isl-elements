from adjective import *
from reader import *
import random


entries = load_word_entries("../data/2022-vor.txt")
adj_entries = [e for e in entries if e.grammarcat == "lo"]
adjectives = [create_adj(w) for w in adj_entries]

for a in adjectives:
    print(
        a.word,
        "{mst} *",
        a.get_form(
            Gender.MASCULINE, Case.NOMINATIVE, Number.SINGULAR, InflClass.COMPARATIVE
        ),
    )
    print(
        a.word,
        "{est} *",
        a.get_form(
            Gender.MASCULINE,
            Case.NOMINATIVE,
            Number.SINGULAR,
            InflClass.SUPERLATIVE_STRONG,
        ),
    )
