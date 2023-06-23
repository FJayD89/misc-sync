import base64

prependstr = 'start-'
bytestart = bytes(prependstr, 'ascii')

plaintxt = 'textgoeshere'

bytestxt = bytes(plaintxt, "ascii")

encoded = base64.b64encode(bytestxt)

print(encoded)
print(bytestxt)

strdecoded = encoded.decode("ascii")

print(strdecoded)

conc = bytestart + bytestxt

decoded = conc.decode('ascii')

print(conc)
print(decoded)