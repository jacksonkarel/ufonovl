import re

from tqdm import tqdm

from ufonovl.helpers import punct_list

def remove_blank_lines():
    punct = punct_list()
    for line in tqdm(punct):
        if line != "\n":
            with open('data/punct_b.txt', 'a') as f:
                f.write(line)

def remove_beg_spaces():
    punct = punct_list()
    for line in tqdm(punct):
        clean_line = re.sub("^\s*", "", line)
        with open('data/punct_b.txt', 'a') as f:
            f.write(clean_line)

def remove_space_lns():
    punct = punct_list()
    for line in tqdm(punct):
        space_line = re.search("^\s*$", line)
        if space_line is None:
            with open('data/punct_b.txt', 'a') as f:
                f.write(line)