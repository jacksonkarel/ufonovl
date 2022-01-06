import re


class Clean_text:
    def __init__(self, input_file, output_file, sub_pattern, substitute):
        self.input_file = input_file
        self.output_file = output_file
        self.sub_pattern = sub_pattern
        self.substitute = substitute

    def txt_write(self):
        with open(self.input_file) as f:
            text = f.read()
        proc_text = re.sub(self.sub_pattern, self.substitute, text)
        
        with open(self.output_file, 'w') as f:
            f.write(proc_text)

clean_youtube_auto = Clean_text("unpunct.txt", "unpunct_clean.txt", "(\n| )\[.*?\](\n| )", " ")
clean_toe = Clean_text("unpunct_toe.txt", "unpunct_toe_clean.txt", "(CJ|LE)( |-|:)*", "")

# clean_toe.txt_write()

