def balance_list_length(list1, list2):
    if not isinstance(list1, list):
        raise TypeError(f"balance_list_length: parameter list1 '{list1}' is of type '{type(list1)}' instead of 'list'")
    if not isinstance(list2, list):
        raise TypeError(f"balance_list_length: parameter list2 '{list2}' is of type '{type(list2)}' instead of 'list'")
    
    length_list1 = len(list1)
    length_list2 = len(list2)
    element_difference = abs(length_list1 - length_list2)
    is_even_number_of_element = element_difference % 2 == 0
    
    list1_result = list1.copy()
    list2_result = list2.copy()

    if length_list1 > length_list2 and is_even_number_of_element:
        # Add half of the extra elements to the other list
        list2_result.extend(list1[int(-element_difference/2):])
        
        # Overwrite the list without the elements 
        # that was extended to the other list
        list1_result = list1[:int(-(element_difference/2))]
        
    elif length_list1 > length_list2 and not is_even_number_of_element:
        # Add half -1 of the extra elements to the other list
        list2_result.extend(list1[int(-(element_difference-1)/2):])
        
        # Overwrite the list without the elements 
        # that was extended to the other list
        list1_result = list1[:int(-(element_difference-1)/2)]

    elif length_list1 < length_list2 and is_even_number_of_element:
        # Add half of the extra elements to the other list
        list1_result.extend(list2[int(-element_difference/2):])
        
        # Overwrite the list without the elements 
        # that was extended to the other list
        list2_result = list2[:int(-(element_difference/2))]

    elif length_list1 < length_list2 and not is_even_number_of_element:
        # Add half -1 of the extra elements to the other list
        list1_result.extend(list2[int(-(element_difference-1)/2):])
        
        # Overwrite the list without the elements 
        # that was extended to the other list
        list2_result = list2[:int(-(element_difference-1)/2)]
    
    return list1_result, list2_result
