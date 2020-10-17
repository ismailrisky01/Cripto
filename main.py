import binascii
import base64
if __name__ == '__main__':
    text = "Road to Security Engineer"
    text_utf8 = text.encode("utf-8")
    text_b64 = base64.b64encode(text_utf8)
    text_hex = binascii.hexlify(text_utf8)
    print("text = " + text)
    print("utf8 encode = " + str(text_utf8))
    print("base64 encode = " + str(text_b64))
    print("hexadec encode = " + str(text_hex))

   #mendecode hasil diatas
    base64_decode_bytes = base64.decodebytes(text_b64)
    text_hex_decode_bytes = binascii.unhexlify(text_hex).decode('utf-8')
    print("Hasil base Decode = " + base64_decode_bytes.decode())
    print("Hasil Hex Decode = " + str(text_hex_decode_bytes))


