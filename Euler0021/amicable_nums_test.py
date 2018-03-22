from .amicable_nums import sum_of_fs


def test_examples():
    assert sum_of_fs(284) == 220
    assert sum_of_fs(220) == 284
