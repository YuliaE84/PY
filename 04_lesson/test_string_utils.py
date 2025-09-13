import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("123", "123"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   hello", "hello"),               
        ("world", "world"),                  
        ("   test   ", "test   "),                        
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),                            
        ("   ", ""),                                                                      
    ],
)
def test_trim_negative(input_str, expected):
   assert string_utils.trim(input_str) == expected 


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [                    
        ("Test", "t", True),                                          
        ("привет", "п", True),                     
        ("Привет", "z", False),                    
        ("test", "T", False),                                          
    ],
)
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol",
    [  
        ("test", 123),                           
        (None, "A"),
     ],
)
def test_contains_negative(input_str, symbol):
    with pytest.raises(Exception):
        string_utils.contains(input_str, symbol)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),               
        ("123abc", "2", "13abc"),              
        ("Привет", "и", "Првет"),
         ("", "", ""),
],
)
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, exception_class",
    [
        ("test", 123, TypeError),                
        ("test", [], TypeError),
     ],
)
def test_delete_symbol_negative(input_str, symbol, exception_class):
    with pytest.raises(exception_class):
        string_utils.delete_symbol(input_str, symbol)