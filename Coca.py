import base64
string_b="this is my".encode("utf-8")
base64_bytes = base64.b64encode(string_b)
print(base64_bytes)
print(base64_bytes.decode("utf-8"))
base64_decode_bytes = base64.decodebytes(base64_bytes)
print(base64_decode_bytes.decode())
