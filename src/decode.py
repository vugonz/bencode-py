class BencodeDecodingError(ValueError):
    ...

class Decoder:
    """Simple Bencode decoder <https://en.wikipedia.org/wiki/Bencode>
    
    Performs the following translations in decoding by default:
    +---------------+-------------------+
    | Bencode       | Python            |
    +===============+===================+
    | object        | dict              |
    +---------------+-------------------+
    | integer       | int               |
    +---------------+-------------------+
    | string        | bytes             |
    +---------------+-------------------+
    | list          | list              |
    +---------------+-------------------+
    | dictionary    | dict              |
    +---------------+-------------------+
    """

    _TOKENS = {
        "int": b"i",
        "str": b"0123456789",
        "list": b"l",
        "dict": b"d",
        "sep": b":",
        "end": b"e"
    }

    def __init__(self, data):
        self._data = data 
        self._index = 0

    def _current_byte(self):
        """ Peek current byte """
        return self._data[self._index:self._index + 1]
    
    def _increment_index(self):
        self._index += 1

    def _consume_byte(self):
        """ Read byte """
        ret = self._current_byte()
        self._increment_index()

        return ret

    def decode_int(self) -> bytes:
        # discard 'i' begin token
        self._increment_index()

        res = bytearray()

        while self._current_byte() != self._TOKENS["end"]:
            res += self._consume_byte()
        
        # no leading zeros
        if res[0:1] == b'0' and len(res) > 1:
            raise BencodeDecodingError(f"Invalid integer encoding {bytes(res)}")

        # discard 'e' end token
        self._increment_index()

        return int(res) 


    def decode_str(self) -> bytes:
        length = 0
        while self._current_byte() != self._TOKENS["sep"]:
            # unclosed str length 
            if self._current_byte() not in self._TOKENS["str"]:
                raise BencodeDecodingError(f"Invalid token {self._current_byte()} at index {self._index}, missing ':'?")

            length = length*10 + ord(self._consume_byte()) - ord('0')

        # discard ':' separator token
        self._increment_index()

        res = bytearray()

        while length > 0:
            res += self._consume_byte()
            length -= 1

        return bytes(res)
        

    def decode_list(self) -> list:
        # discard 'l' begin token
        self._increment_index()

        lst = []
        while self._current_byte() != self._TOKENS["end"]:
            new_item = self.decode()
            lst.append(new_item)
        
        # discard 'e' end token
        self._increment_index()
        return lst


    def decode_dict(self) -> dict:
        # discard 'd' begin token
        self._increment_index()

        dic = {}
        while self._current_byte() != self._TOKENS["end"]:
            key = self.decode()
            value = self.decode()
            dic[key] = value
            
        # discard 'e' end token
        self._increment_index()
        return dic


    def decode(self):
        if self._current_byte() == b"":
            raise BencodeDecodingError(f"Out of bounds read, missing 'e'?")

        if self._current_byte() == self._TOKENS["int"]:
            item = self.decode_int()
        elif self._current_byte() == self._TOKENS["list"]:
            item = self.decode_list()
        elif self._current_byte() == self._TOKENS["dict"]:
            item = self.decode_dict()
        elif self._current_byte() in self._TOKENS["str"]:
            item = self.decode_str()
        else:
            raise BencodeDecodingError(f"Unexpected token {self._current_byte()} at position {self._index}")

        return item