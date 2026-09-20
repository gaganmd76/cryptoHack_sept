
import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Decode the hex string into bytes
decoded_bytes = bytes.fromhex(hex_string)

# Encode the bytes into Base64
base64_bytes = base64.b64encode(decoded_bytes)

# Convert bytes to a string and print
print(base64_bytes.decode())