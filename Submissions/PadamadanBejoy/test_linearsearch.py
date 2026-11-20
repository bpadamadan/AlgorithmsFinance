from search_v1 import linear_search


def test_linear_search_example():
    ids = [8,10,9,9]
    queries = [7,8,10,6,9]

    result = linear_search(ids, queries)

    assert result == [False, True, True, False, True]
