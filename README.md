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

# will result in the following bencoded bytes
# b'd5:peersld9:127.0.0.15:29123ed9:127.0.0.14:6432eee'
bencoded_peers = bencode.dumps(peers_dic)


```