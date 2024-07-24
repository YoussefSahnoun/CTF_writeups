import randcrack

inputs = [
    "aaaabbbbccccdddd",
    "abcdabcdabcdabcd",
]

outputs = [
    "ccaccdabdbdbbada",
    "bcaadbdcdbcdacab",
]
c="owuwspdgrtejiiud"
PERM=[9,10,0,8,11,13,3,6,15,5,14,7,4,2,12,1]
result=""
for i in range(16):
    result+=c[PERM.index(i)]
print("DUCTF{"+result+"}")


