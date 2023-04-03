from .decode import Decoder
from .encode import Encoder

def loads(s: bytes) -> dict:
    """Deserialize ``s`` (``bytes`` or ``bytearray`` instance
    containing a Bencoded document) to a Python object.
    """
    return Decoder(s).decode()

def load(fp) -> dict:
    """Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
    a Bencoded document) to a Python object.
    """
    return Decoder(fp.read()).decode()

def dumps(obj):
    """Serialize ``obj`` to a JSON formatted ``str``."""
    return Encoder().encode(obj)

def dump(obj, fp):
    """Serialize ``obj`` as a Bencoded formatted stream to ``fp`` (a
    ``.write()``-supporting file-like object).
    """

    fp.write(Encoder().encode(obj))

