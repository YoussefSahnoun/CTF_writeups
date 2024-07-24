
from Crypto.Cipher import AES
import base64
Flag='577ca2e5adb9dc46b44f668923055b238243f9b398c670584430e1e327141949ed345afce50fa4c9de130d3c331936cebd5104206a959daf74b9f15b68cfb193'

Key='00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff'

IV='0102030405060708090a0b0c0d0e0f10'
cipher = AES.new(bytes.fromhex(Key),AES.MODE_CBC,bytes.fromhex(IV))
print(base64.b64decode(cipher.decrypt(bytes.fromhex(Flag))))
