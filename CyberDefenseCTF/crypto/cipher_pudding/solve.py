#it's a wingdings font we decrypt it using dcode
#we get a b64 cipher we decrypt it twice to get integers
#we convert integers to ascii with dcode to get this cipher:
#6p 65 76 65 6p 65 66 66 65 63 74 7o 68 34 69 31 5s 37 30 5s 37 68 33 5s 63 68 33 66 7q
#we notice that it's again hex encoded bytes except the letters are shifted so we 
#correct it to:6c 65 76 65 6c 65 66 66 65 63 74 7b 68 34 69 31 5f 37 30 5f 37 68 33 5f 63 68 33 66 7d
#we convert it back to ascii :leveleffect{h4i1_70_7h3_ch3f}
