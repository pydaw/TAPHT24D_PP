
def pretty_print(input_list):
    if len(input_list) > 0:
        print(f"Listan har {len(input_list)} element:")
        for element in input_list:
            i = input_list.index(element) + 1
            print(f"{i}: {element}")
    else:
        print("Listan är tom")
        