# Bencode

## Usage

Reading bencoded data:
```python3
with open("bencoded_file.torrent", "rb") as fp:
    decoded_dic = bencode.load(fp)

# or if you have encoded data in a variable
decoded_dic = bencode.loads(encoded_data)

```

Encoding data:
```python3
peers_dic = {b'peers': [
                {b'127.0.0.1': b'29123'}, 
                {b'127.0.0.1': b'6432'}
            ]}

# this will result in b"d5:peersl9:127.0.0.15:29123 ...etc""
bencoded_peers = bencode.dumps(peers_dic)

```