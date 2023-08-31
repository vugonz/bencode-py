class BencodeEncodingError(ValueError):
    ...

class Encoder:
    """Simple Bencode encoder <https://en.wikipedia.org/wiki/Bencode>
    
    Performs the following translations in encoding by default:
    +---------------+-------------------+
    | Python        | Bencode           |
    +===============+===================+
    | int           | integer           |
    +---------------+-------------------+
    | str           | string            |
    +---------------+-------------------+
    | bytes         | string            |
    +---------------+-------------------+
    | list          | list              |
    +---------------+-------------------+
    | dict          | dictionary        |
    +---------------+-------------------+
    """
    @classmethod
    def encode(cls, item) -> bytes:
        """ Encode passed item into corresponding Bencode type """
        if isinstance(item, dict):
            ret = cls.encode_dict(item)
        elif isinstance(item, list):
            ret = cls.encode_list(item)
        elif isinstance(item, int):
            ret = cls.encode_int(item)
        elif isinstance(item, bytes):
            ret = cls.encode_byte_str(item)
        elif isinstance(item, str):
            ret = cls.encode_str(item)
        else:
            raise BencodeEncodingError(f'Unsupported type {type(item)}')

        return ret

    @classmethod
    def encode_int(cls, num: int) -> bytes:
        res = bytearray(b'i') 
        res += bytes(str(num), 'utf-8')
        res += b'e'

        return bytes(res)

    @classmethod
    def encode_byte_str(cls, string: bytes) -> bytes:
        length = bytes(str(len(string)), 'utf-8')

        return length + b":" + string 

    @classmethod
    def encode_str(cls, string: str) -> bytes:
        length = bytes(str(len(string)), 'utf-8')

        return length + b":" + bytes(string, 'utf-8') 

    @classmethod
    def encode_list(cls, lst: list) -> bytes:
        res = bytearray(b'l')
        for item in lst:
            res += cls.encode(item)
        res += b'e'

        return bytes(res)

    @classmethod
    def encode_dict(cls, dic: dict) -> bytes:
        res = bytearray(b'd')
        for k, v in dic.items():
            res += cls.encode(k)
            res += cls.encode(v)
        res += b'e'

        return bytes(res)


