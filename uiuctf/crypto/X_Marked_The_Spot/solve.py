from itertools import cycle



with open("ct","r+") as file:
	cipher=file.read().encode()
print(cipher)
key=bytes(x ^ y for x,y in zip(b"uiuctf{",cipher[:7]))
key =key+chr((ord("}") ^ cipher[-1])).encode()
flag = bytes(x ^ y for x, y in zip(cipher, cycle(key)))
print(key)
print(flag)
#We will get the flag modified -- the second byte of 
#the key is modified after the second cycle the hint is X marked the spot
#so we need to xor X with _ to get the correct byte and then xor it with every
#second byte in each chunk of 8 bytes to get the real flag which is 
#uiuctf{n0t_ju5t_th3_st4rt_but_4l50_th3_3nd!!!!!}

