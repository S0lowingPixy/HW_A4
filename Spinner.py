import random
class Spinner:
    def __init__(self, synonym_file):
        self.synonyms = self.load_synonyms(synonym_file)

    def load_synonyms(self, synonym_file):
        synonyms = {}
        with open(synonym_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    word, synonym_str = line.split(':')
                    synonym_list = synonym_str.split(',')
                    synonyms[word] = synonym_list
        return synonyms

    def spin_text(self, text):
        words = text.split()
        spun_words = []
        for word in words:
            if word in self.synonyms:
                if random.randint(1, 100) > 50:
                    replacement = random.choice(self.synonyms[word])
                    spun_words.append(replacement)
                else:
                    spun_words.append(word)
            else:
                spun_words.append(word)
        return ' '.join(spun_words)