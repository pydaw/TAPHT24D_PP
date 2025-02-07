import module
import pytest

def test_autocomplete_compare_master_list_with_whole_words():
    master_list = [
        "Vad är mpox?",
        "Vad betyder sigma?",
        "Vad ska jag rösta i EU-valet?",
        "Vad är en shaman?",
        "Vad är mykoplasma?"
    ]
    assert module.autocomplete_list("mpox", master_list) == [master_list[0]]
    assert module.autocomplete_list("Vad", master_list) == master_list
    

def test_autocomplete_compare_master_list_with_part_of_words():
    master_list = [
        "Vad är mpox?",
        "Vad betyder sigma?",
        "Vad ska jag rösta i EU-valet?",
        "Vad är en shaman?",
        "Vad är mykoplasma?"
    ]
    assert module.autocomplete_list("mp", master_list) == [master_list[0]]
    assert module.autocomplete_list("Va", master_list) == master_list


def test_autocomplete_input_should_be_a_string():
    master_list = [
        "Vad är mpox?",
        "Vad betyder sigma?",
        "Vad ska jag rösta i EU-valet?",
        "Vad är en shaman?",
        "Vad är mykoplasma?"
    ]
    assert module.autocomplete_list("mp", master_list) == [master_list[0]]
    with pytest.raises(TypeError):
        module.autocomplete_list(1, master_list)
    with pytest.raises(TypeError):
        module.autocomplete_list(True, master_list)
    with pytest.raises(TypeError):
        module.autocomplete_list(["Vad", "är", "mpox?"], master_list)
    

def test_autocomplete_is_not_case_sensitive():
    master_list = [
        "Vad är mpox?",
        "Vad betyder sigma?",
        "Vad ska jag rösta i EU-valet?",
        "Vad är en shaman?",
        "Vad är mykoplasma?"
    ]
    assert module.autocomplete_list("MP", master_list) == [master_list[0]]
    assert module.autocomplete_list("va", master_list) == master_list

def test_autocomplete_empty_input_string():
    master_list = [
        "Vad är mpox?",
        "Vad betyder sigma?",
        "Vad ska jag rösta i EU-valet?",
        "Vad är en shaman?",
        "Vad är mykoplasma?"
    ]
    assert module.autocomplete_list("", master_list) == None