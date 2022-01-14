from adjective import *
from noun import *
from numeral import *
from reader import *
import random


entries = load_word_entries("../data/2022-vor.txt")
nouns = [create_noun(w) for w in entries]

for n in nouns:
    print(n.word)


def aefing_1_2_1(noun):
    prompt = "Hér er bara... Já, en þarna eru... [1, {root}, margur]".format(
        root=noun.word
    )
    einn = create_numeral("einn")
    einn_form = einn.get_form(Case.NOMINATIVE, noun.gender)
    margur = Adjective("margur")
    many = margur.get_form(
        noun.gender, Case.NOMINATIVE, Number.PLURAL, Article.INDEFINITE
    )
    noun_plural = noun.get_form(Case.NOMINATIVE, Number.PLURAL)
    answer_1 = "{einn} {noun}".format(einn=einn_form, noun=noun.word)
    answer_2 = "{margir} {nouns}".format(margir=many, nouns=noun_plural)
    return prompt, "{answer_1}, {answer_2}".format(answer_1=answer_1, answer_2=answer_2)


def play():
    while True:
        # subj = random.choice(nouns)
        # verb = random.choice(verbs)
        # adj = random.choice(adjectives)
        noun = random.choice(nouns)
        prompt, answer = aefing_1_2_1(noun)
        # prompt, answer = aefing_1_3_3(subj, verb, adj, noun)
        print(noun.wordentry.definition)
        print(prompt)
        attempt = input()
        if attempt == answer:
            print(":-)\n")
        else:
            print(answer, "\n")


play()
