# Bencode

A module that mimics the `json` standard lib module interface for
Bencode

## Usage

#### Reading bencoded data
Both `load` and `loads` functions will decode bencoded data.
```python3
with open("bencoded_file.torrent", "rb") as fp:
    decoded_dic = bencode.load(fp)

# or if you have encoded data in a variable
decoded_dic = bencode.loads(encoded_data)


```

#### Encoding data
Encoding an item with `dumps` method. Pragmatically, only dictionaries are encoded in real life applications of this encoding format, but any other supported types can be singularly encoded. 
```python3
peers_dic = {b'peers': [
                {b'127.0.0.1': b'29123'}, 
                {b'127.0.0.1': b'6432'}
            ]}

# will result in the following bencoded bytes
# b'd5:peersld9:127.0.0.15:29123ed9:127.0.0.14:6432eee'
bencoded_peers = bencode.dumps(peers_dic)


```
Serialize an object as a bencoded stream:
```python3
with open("my_bencoded_file.torrent", "rb") as fp:
    bencode.dump(my_dict, fp)

```