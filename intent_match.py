from hash_table import DoubleHashMap

class CommandIntentMatcher:
    def __init__(self):
        self.vocab = DoubleHashMap(capacity=29)

    def train_phrase(self, list_of_words):
        for word in list_of_words:
            self.vocab.record_word(word)

    def assess_score(self, query_words):
        return sum(self.vocab.fetch_word_count(word) for word in query_words)
