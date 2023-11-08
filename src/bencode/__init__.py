from .decode import Decoder
from .encode import Encoder
from .decode import BencodeDecodingError

def loads(s):
    """Deserialize ``s`` (``bytes`` or ``bytearray`` instance
    containing a Bencoded document) to a Python object.
    """
    return Decoder(s).decode()

def load(fp):
    """Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
    a Bencoded document) to a Python object.
    """
    return Decoder(fp.read()).decode()

def dumps(obj):
    """Serialize ``obj`` to a Bencode formatted ``str``."""
    return Encoder().encode(obj)

def dump(obj, fp):
    """Serialize ``obj`` as a Bencode formatted stream to ``fp`` (a
    ``.write()``-supporting file-like object).
    """
    fp.write(Encoder().encode(obj))



