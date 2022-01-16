import re

from ufonovl.punctuation import segment_sents


class Clean_text:
    def __init__(self, input_file, output_file, sub_pattern, substitute, seg_sents):
        self.input_file = input_file
        self.output_file = output_file
        self.sub_pattern = sub_pattern
        self.substitute = substitute
        self.seg_sents = seg_sents

    def txt_write(self):
        with open(self.input_file) as f:
            text = f.read()
        if self.seg_sents is True:
            text_sents = segment_sents(text, newlines='')
            proc_text = '\n'.join(text_sents)
        else:
            proc_text = re.sub(self.sub_pattern, self.substitute, text)
        
        with open(self.output_file, 'w') as f:
            f.write(proc_text)

clean_youtube_auto = Clean_text("unpunct.txt", "unpunct_clean.txt", "(\n| )\[.*?\](\n| )", " ", False)
clean_toe = Clean_text("unpunct_toe.txt", "unpunct_toe_clean.txt", "(CJ|LE)( |-|:)*", "", False)
seg_toe = Clean_text("unpunct_toe_clean.txt", "punct_test.txt", None, None, True)