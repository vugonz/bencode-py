import unittest
import bencode
import pickle

class DecodeTest(unittest.TestCase):
    def test_simple_int(self):
        self.assertEqual(bencode.loads(b"i23e"), 23, "Expected integer: 23")
    
    def test_simple_str(self):
        self.assertEqual(bencode.loads(b"2:hi"), b"hi", "Expected string: hi")

    def test_simple_dict(self):
        self.assertEqual(bencode.loads(b"d2:hii0ee"), {b"hi": 0}, "Expected dict with 'hi' string as key and 0 integer as value")
    
    def test_recursive_dict(self):
        self.assertEqual(bencode.loads(b"di1ed4:eggs3:fooee"), {1: {b"eggs": b"foo"}}, "Should have a dict with one key '1' and another dict as value")
    
    def test_debian_iso(self):
        with open("tests/pickles/debian.iso.torrent.dat", "rb") as fp:
            debian_dic = pickle.load(fp)
        
        with open("tests/torrents/debian.iso.torrent", "rb") as fp:
            self.assertEqual(bencode.load(fp), debian_dic)

if __name__ == '__main__':
    unittest.main()



