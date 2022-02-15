def list_diff(list_a, list_b):
    stop_set = set(list_a)
    text_set = set(list_b)
    diff_list = list(text_set - stop_set)
    return diff_list