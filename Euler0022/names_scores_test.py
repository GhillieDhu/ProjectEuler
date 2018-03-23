from .names_scores import read_names, numerate


def test_example():
    assert read_names()[937] == 'COLIN'
    assert numerate('COLIN') == 53
