import pytest
import module


def test_balance_list_length_parameters_is_lists():
    with pytest.raises(TypeError):
        module.balance_list_length(None, [1, 2, 3, 4])
    
    with pytest.raises(TypeError):
        module.balance_list_length(1, [1, 2, 3, 4])
    
    with pytest.raises(TypeError):
        module.balance_list_length(1.0, [1, 2, 3, 4])
    
    with pytest.raises(TypeError):
        module.balance_list_length("str", [1, 2, 3, 4])

    
    with pytest.raises(TypeError):
        module.balance_list_length([1, 2, 3, 4], None)
    
    with pytest.raises(TypeError):
        module.balance_list_length([1, 2, 3, 4], 1)
    
    with pytest.raises(TypeError):
        module.balance_list_length([1, 2, 3, 4], 1.0)
    
    with pytest.raises(TypeError):
        module.balance_list_length([1, 2, 3, 4], "str")

def test_balance_list_length_return_two_lists():
    list1, list2 = module.balance_list_length([1, 2, 3, 4], [1, 2, 3, 4])
    assert isinstance(list1, list) and isinstance(list2, list)

def test_balance_list_length_when_total_sum_of_elements_is_even():
    list_large = [1, 2, 3, 4, 5, 6]
    list_small = [7, 8]
    list1_result, list2_result = module.balance_list_length(list_large, list_small)
    assert list1_result == [1, 2, 3, 4]
    assert list2_result == [7, 8, 5, 6]
    
    list1_result2, list2_result2 = module.balance_list_length(list_small, list_large)
    assert list1_result2 == [7, 8, 5, 6]
    assert list2_result2 == [1, 2, 3, 4]
    
def test_balance_list_length_when_total_sum_of_elements_is_odd():
    list_large = [1, 2, 3, 4, 5, 6, 7]
    list_small = [8, 9]
    
    list1_result, list2_result = module.balance_list_length(list_large, list_small)
    assert list1_result == [1, 2, 3, 4, 5]
    assert list2_result == [8, 9, 6, 7]
    
    list1_result, list2_result = module.balance_list_length(list_small, list_large)
    assert list1_result == [8, 9, 6, 7]
    assert list2_result == [1, 2, 3, 4, 5]

def test_balance_list_length_total_sum_of_element_should_be_same_after_balancing():
    list_large = [1, 2, 3, 4, 5, 6, 7]
    list_small = [8, 9]
    list1_result, list2_result = module.balance_list_length(list_large, list_small)
    
    excepted1 = len(list_large) + len(list_small)
    actual1 = len(list1_result) + len(list2_result)
    assert excepted1 == actual1
    
    list_large = [1, 2, 3, 4, 5, 6]
    list_small = [7, 8]
    list1_result, list2_result = module.balance_list_length(list_large, list_small)
    
    excepted1 = len(list_large) + len(list_small)
    actual1 = len(list1_result) + len(list2_result)
    assert excepted1 == actual1


def test_balance_list_empty_list():
    list_large = [1, 2]
    list_small = []
    list1_result, list2_result = module.balance_list_length(list_large, list_small)
    assert list1_result == [1]
    assert list2_result == [2]

    list1 = []
    list2 = []
    list1_result, list2_result = module.balance_list_length(list1, list2)
    assert list1_result == []
    assert list2_result == []

def test_balance_list_same_length():
    list_large = [1, 2]
    list_small = [3, 4]
    list1_result, list2_result = module.balance_list_length(list_large, list_small)
    assert list1_result == [1, 2]
    assert list2_result == [3, 4]

