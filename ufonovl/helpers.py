def list_diff(list_a, list_b):
    text_set = set(list_a)
    stop_set = set(list_b)
    diff_list = list(text_set - stop_set)
    return diff_list

def punct_list():
    with open('data/punct.txt') as f:
        punct = f.readlines()
    
    return punct