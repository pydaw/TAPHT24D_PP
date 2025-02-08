import pytest
import module

def test_multiplcation_table():
    assert module.muliplication_table(n=3,limit=4) == [3, 6, 9, 12]
    assert module.muliplication_table(n=5,limit=10) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

def test_multiplcation_table_parameter_limit_should_be_positive():
    assert module.muliplication_table(n=3,limit=1) == [3]
    assert module.muliplication_table(n=3,limit=0) is None
    
def test_multiplcation_table_parameter_n_is_of_type_int():
    assert module.muliplication_table(n=3,limit=4) == [3, 6, 9, 12]
    with pytest.raises(TypeError):
        module.muliplication_table(n=3.0, limit=4)
    with pytest.raises(TypeError):
        module.muliplication_table(n="3", limit=4)
    with pytest.raises(TypeError):
        module.muliplication_table(n=[3], limit=4)

def test_multiplcation_table_parameter_limit_is_of_type_int():
    assert module.muliplication_table(n=3,limit=4) == [3, 6, 9, 12]
    with pytest.raises(TypeError):
        module.muliplication_table(n=3, limit=4.0)
    with pytest.raises(TypeError):
        module.muliplication_table(n=3, limit="4")
    with pytest.raises(TypeError):
        module.muliplication_table(n=3, limit=[4])

def test_multiplcation_table_len_of_result():
    length = 6
    assert len(module.muliplication_table(n=5,limit=length)) == length
    
def test_multiplcation_table_start_with_product_of_1():
    multiplcation_table = 5
    excpeted = 5*1
    actual = module.muliplication_table(n=multiplcation_table, limit=4)
    assert actual[0] == excpeted

def test_multiplcation_table_result_is_of_type_list():
    result = module.muliplication_table(n=3,limit=4)
    assert isinstance(result, list)