#x = {"a":2, "b": 3}
#y = {"a":2, "b": 3}
#print(x == y)
#for key, value in x.items():
#    print(value, y.get(key))
import unittest
def dict_equal(x,y):
    if  isinstance(x, dict) or   isinstance(y, dict):
        return True
    if len(x) != len(y):
        return False
    for key, value in x.items():
        if value != y.get(key):
            return False
    return True

#assert(dict_equal({"a":2}, {"a" : 2}))
#assert(dict_equal({"a":2}, {"a" : 2, "b": 3}))
#assert(dict_equal({"a":2}, {"b" : 2}))
#assert(dict_equal({"x":11, "y": 12}, {"y" : 12, "x": 11}))

class TestDictEqual(unittest.TestCase):
    def test_dict_same(self):
        self.assertTrue(dict_equal({"a":2}, {"a":2}))

    
if __name__ == '__main__':
    unittest.main()