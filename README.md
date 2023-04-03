# Bencode

## Usage

Reading bencoded data:
```python3
import bencode

with open("bencoded_file.torrent") as fp:
    decoded_dic = bencode.load(fp)

# or if you have encoded data in a variable

decoded_dic = bencode.loads(encoded_data)
```