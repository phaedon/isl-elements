import collections


class WordEntry:
    def __init__(self, word, grammarcat):
        self.word = word
        self.grammarcat = grammarcat
        self.examples = []


def lines_to_word_entries(lines):
    entries = []
    curr_entry = None
    i = 0
    while i < len(lines):
        curr_line = lines[i].strip()
        if curr_line == "orð:":
            curr_entry = WordEntry(
                word=lines[i + 1].strip(), grammarcat=lines[i + 2].strip()
            )
            i += 2
            # continue
        elif len(curr_line) == 0 and curr_entry != None:
            entries.append(curr_entry)
        elif len(curr_line) == 0:
            pass
            # continue
        elif len(curr_line) > 0 and curr_line[0] == "#":
            pass
        elif curr_line == "EOF":
            pass
        else:
            key, value = curr_line.split(":")
            value = value.strip()
            if key == "tm":
                curr_entry.timestamp = value
            elif key == "src":
                curr_entry.source = value
            elif key == "defn":
                curr_entry.definition = value
            elif key == "note":
                curr_entry.note = value
            elif key == "dæmi":
                curr_entry.examples.append(value)
            elif key == "fallst":
                curr_entry.steers_case = value

        i += 1
    return entries


def load_word_entries(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines_to_word_entries(lines)


entries = load_word_entries("../data/2021-haust.txt")

print("now printing the final...")
for entry in entries:
    print(entry.word, entry.grammarcat, entry.timestamp, entry.source, entry.definition)
    print(entry.examples)
