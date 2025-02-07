
def autocomplete_list(input, master_list):
    if not len(input) > 0:
        return None
    
    # Check type of parameters
    if not isinstance(input, str):
        raise TypeError(f"autocomplete: input '{input}' is of type '{type(input)}' instead of 'str'")
    if not isinstance(master_list, list):
        raise TypeError(f"autocomplete: master_list '{master_list}' is of type '{type(master_list)}' instead of 'list'")

    # Make input not case sensitive
    input = str(input).casefold()

    filtered_list = []
    for element in master_list:
        # Check type of element
        if not isinstance(element, str):
            raise TypeError(f"autocomplete: master_list element '{element}' is of type '{type(element)}' instead of 'str'")

        # Check if input is part of element (compare in lower case)    
        if str(element).casefold().find(input) != -1:
            filtered_list.append(element)
        else:
            continue
    return filtered_list


if __name__ == "__main__":
    master_list = [
        "Karl Andersson",
        "Erik Johansson",
        "Lars Karlsson",
        "Anders Nilsson",
        "Per Eriksson",
        "Mikael Larsson",
        "Johan Olsson",
        "Olof Persson",
        "Nils Svensson",
        "Jan Gustafsson",
        "Maria Andersson",
        "Elisabeth Johansson",
        "Anna Karlsson",
        "Kristina Nilsson",
        "Margareta Eriksson",
        "Eva Larsson",
        "Linnéa Olsson",
        "Karin Persson",
        "Birgitta Svensson",
        "Marie Gustafsson",
        1234
    ]
    print(autocomplete_list("mpox", master_list) == [master_list[0]])
    print(autocomplete_list(True, master_list) == [master_list[0]])
    

