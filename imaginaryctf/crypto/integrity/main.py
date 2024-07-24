from Crypto.Util.number import *
from binascii import crc_hqx

# Given values
n = <value_of_n>
ct = <value_of_ct>
signature = <value_of_signature>

# Brute force the CRC value
for crc_value in range(2**16):
    try:
        # Verify the signature
        verified_flag = pow(signature, crc_value, n)
        
        # Decrypt the ciphertext
        decrypted_flag = pow(ct, crc_value, n)
        
        # Compare the results
        if verified_flag == decrypted_flag:
            flag = long_to_bytes(decrypted_flag)
            print(f"Flag: {flag.decode()}")
            break
    except Exception as e:
        continue
