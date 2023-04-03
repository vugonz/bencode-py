# Bencode

A module that mimics the `json` standard lib module interface for
Bencode

## Installation
Simply clone the repository and then run the following on the root dir of the repo.
```sh
python3 -m build && python3 -m pip install dist/bencode-0.0.1-py3-none-any.whl
```

## Usage

### Reading bencoded data
Both `load` and `loads` functions will decode bencoded data.
```python3
with open("bencoded_file.torrent", "rb") as fp:
    decoded_dic = bencode.load(fp)

# or if you have encoded data in a variable
decoded_dic = bencode.loads(encoded_data)


```

### Encoding data
Pragmatically, only dictionaries are encoded in real life applications of this encoding format, but any other supported types can be singularly encoded. 
```python3
peers_dic = {b'peers': [
                {b'127.0.0.1': b'29123'}, 
                {b'127.0.0.1': b'6432'}
            ]}

bencoded_peers = bencode.dumps(peers_dic)
# b'd5:peersld9:127.0.0.15:29123ed9:127.0.0.14:6432eee'


```
Serialize an object as a bencoded stream to a file:
```python3
with open("my_bencoded_file.torrent", "rb") as fp:
    bencode.dump(my_dict, fp)

```