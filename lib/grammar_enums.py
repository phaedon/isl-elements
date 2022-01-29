"""Enums representing grammatical concepts in Icelandic."""

import enum
import random


class Article(enum.Enum):
    """Docstring"""

    DEFINITE = "gr"
    INDEFINITE = "nogr"


class Gender(enum.Enum):
    """
    The grammatical gender of a lemma (such as a noun) or a particular form
    (such as the feminine form of an adjective).
    """

    MASCULINE = "kk"
    FEMININE = "kvk"
    NEUTER = "hk"


class Case(enum.Enum):
    """
    The case of a noun, adjective, or other declinable word.
    """

    NOMINATIVE = "NF"
    ACCUSATIVE = "ÞF"
    DATIVE = "ÞGF"
    GENITIVE = "EF"


class Number(enum.Enum):
    """
    The number of a word.
    """

    SINGULAR = "ET"
    PLURAL = "FT"


class InflClass(enum.Enum):
    """
    The inflectional class (weak or strong) of a word.
    """

    STRONG = "FSB"
    WEAK = "FVB"
    SUPERLATIVE_STRONG = "ESB"
    SUPERLATIVE_WEAK = "EVB"
    COMPARATIVE = "MST"


class Voice(enum.Enum):
    INDICATIVE = "FH"
    SUBJUNCTIVE = "VH"


class Tense(enum.Enum):
    PRESENT = "NT"
    PRETERITE = "ÞT"


class Person(enum.Enum):
    FIRST = "1P"
    SECOND = "2P"
    THIRD = "3P"


def get_personal_pronoun(person, number):
    if number == Number.SINGULAR:
        if person == Person.FIRST:
            return "ég"
        if person == Person.SECOND:
            return "þú"
        if person == Person.THIRD:
            return random.choice(["hann", "hún", "það"])
    if number == Number.PLURAL:
        if person == Person.FIRST:
            return "við"
        if person == Person.SECOND:
            return "þið"
        if person == Person.THIRD:
            return random.choice(["þeir", "þær", "þau"])
