import module
import pytest

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
    "Marie Gustafsson"
]

def test_autocomplete_compare_master_list_with_whole_words():
    assert module.autocomplete_list("Maria", master_list) == ["Maria Andersson"]
    assert module.autocomplete_list("Andersson", master_list) == ["Karl Andersson", "Maria Andersson"]
    

def test_autocomplete_compare_master_list_with_part_of_words():
    assert module.autocomplete_list("Ma", master_list) == ["Maria Andersson", "Margareta Eriksson", "Marie Gustafsson"]
    assert module.autocomplete_list("Per", master_list) == ["Per Eriksson", "Olof Persson", "Karin Persson"]


def test_autocomplete_input_should_be_a_string():
    assert module.autocomplete_list("Karl Andersson", master_list) == [master_list[0]]
    with pytest.raises(TypeError):
        module.autocomplete_list(1, master_list)
    with pytest.raises(TypeError):
        module.autocomplete_list(True, master_list)
    with pytest.raises(TypeError):
        module.autocomplete_list(["Karl", "Andersson"], master_list)
    

def test_autocomplete_is_not_case_sensitive():
    assert module.autocomplete_list("karl andersson", master_list) == [master_list[0]]
    assert module.autocomplete_list("KARL ANDERSSON", master_list) == [master_list[0]]

def test_autocomplete_empty_input_string():
    assert module.autocomplete_list("", master_list) == None