import re

def pp_unpunct():
    with open('unpunct_test.txt') as f:
        text = f.read()
    proc_text = re.sub("(\n| )\[.*?\](\n| )", " ", text)
    
    with open('unpunct_test_proc.txt', 'w') as f:
        f.write(proc_text)


pp_unpunct()