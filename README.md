# Bencode

A module that mimics the `json` standard lib module interface for
Bencode

## Installation
Install it using `pip`.
```sh
pip install bencode-vug
```

## Usage

### Reading bencoded data
Both `load` and `loads` functions will decode bencoded data.
```python3
import bencode

decoded_dic = bencode.loads(encoded_data)

# deserializing bencoded data from a file
with open("bencoded_file.torrent", "rb") as fp:
    decoded_dic = bencode.load(fp)


```

### Encoding data
Pragmatically, only dictionaries are encoded in real life applications of this encoding format, but any other supported types can be singularly encoded. 
```python3
import bencode

peers_dic = {b'peers': [
                {b'127.0.0.1': b'29123'}, 
                {b'127.0.0.1': b'6432'}
            ]}

# b'd5:peersld9:127.0.0.15:29123ed9:127.0.0.14:6432eee'
bencoded_peers = bencode.dumps(peers_dic)

# serialize an object as a bencoded stream to a file:
with open("my_bencoded_file.torrent", "rb") as fp:
    bencode.dump(peers_dic, fp)


```
