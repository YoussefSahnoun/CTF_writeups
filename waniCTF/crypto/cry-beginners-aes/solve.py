from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

enc = b'\x16\x97,\xa7\xfb_\xf3\x15.\x87jKRaF&"\xb6\xc4x\xf4.K\xd77j\xe5MLI_y\xd96\xf1$\xc5\xa3\x03\x990Q^\xc0\x17M2\x18'
flag_hash = "6a96111d69e015a07e96dcd141d31e7fc81c4420dbbef75aef5201809093210e"
key_base = b'the_enc_key_is_'
iv_base = b'my_great_iv_is_'
for i in range(256):
    for j in range(256):
        key = key_base + bytes([i])
        iv = iv_base + bytes([j])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        try:
            decrypted_message = unpad(cipher.decrypt(enc), 16)
            # Check if it matches the flag format
            if decrypted_message.startswith(b'FLAG{'):
                print(f"Decrypted message: {decrypted_message}")
                print(f"Key: {key}")
                print(f"IV: {iv}")
        except:
            continue
