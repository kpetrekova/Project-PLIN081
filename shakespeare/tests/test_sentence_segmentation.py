import pytest


from shakespeare.preprocessing.regex_sentence_segmentation import sentence_segmentation

@pytest.mark.parametrize("text, expected", [
    ("Hello, world! Hello.", ["Hello, world!", "Hello."]),
    ("", []),
    ])
def test_sentence_segmentation(text, expected):
    print(sentence_segmentation(text))
    assert sentence_segmentation(text) == expected