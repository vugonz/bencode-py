from .decode import Decoder

def loads(bencoded_str: bytes) -> dict:
    return Decoder(bencoded_str).decode()

def load(fp) -> dict:
    return Decoder(fp.read()).decode()

def dumps():
    ...

def dump():
    ...