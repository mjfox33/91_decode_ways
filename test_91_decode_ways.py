import code_91_decode_ways as c

def test_example_1():
    s = c.Solution()
    assert s.numDecodings('12') == 2

def test_example_2():
    s = c.Solution()
    assert s.numDecodings('226') == 3

def test_example_3():
    s = c.Solution()
    assert s.numDecodings('06') == 0