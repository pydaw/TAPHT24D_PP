
def cut_edges(input_list):
    if len(input_list)>=2:
        return input_list[1:-1]
    else:
        raise Exception("List need two elements or more")
