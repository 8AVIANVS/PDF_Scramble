import binascii, textwrap

def hexdump(bs, width=16):
    for i in range(0, len(bs), width):
        chunk = bs[i:i+width]
        hex_part = " ".join(f"{b:02x}" for b in chunk)
        ascii_part = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        print(f"{i:08x}  {hex_part:<{width*3}}  {ascii_part}")

with open("sample.pdf", "rb") as fh:
    data = fh.read()

hexdump(data[:512])     # dump first 512 bytes
