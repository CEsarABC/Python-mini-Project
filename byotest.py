def number_of_evens(numbers):
    return 0


def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got  {1}".format(actual, expected)


def test_not_equal(a, b):
    assert a!= b, "did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)


def test_not_in(collection, item):
    assert item not in collection, "{0} contains {1}".format(collection, item)


def test_is_between(lower , item , upper):
    assert lower < item < upper, "{0} is not between {1} and {2}".format(item, lower, upper)
    #print(str(item) + ' is between ' + str(lower) + ' and ' + str(upper))


# test_are_equal(number_of_evens([1, 2, 3, 4, 5]), 2)

#test_not_equal(1234, 1234)

#test_is_in([1, 2, 3, 4, 5], 6)

#test_not_in([1, 2, 3, 4, 5], 3)

test_is_between(20, 57, 100)
