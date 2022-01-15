class Corpus:
    def __init__(self, filename):
        self.filename = filename

    def file_to_corpus(self):
        with open(self.filename) as f:
            punct_text = f.read()
        corpus = punct_text.split("\n")
        return corpus

def punct_file_corpus():
    punct_corpus = Corpus("data/punct.txt")
    pcftc = punct_corpus.file_to_corpus()
    return pcftc