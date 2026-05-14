from sorter import sort_numbers

def test_empty():
    assert sort_numbers([]) == []

def test_single():
    assert sort_numbers([1]) == [1]

def test_sorted():
    assert sort_numbers([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert sort_numbers([3, 2, 1]) == [1, 2, 3]

def test_duplicates():
    assert sort_numbers([3, 1, 2, 1]) == [1, 1, 2, 3]
