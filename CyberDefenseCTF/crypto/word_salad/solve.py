import base64
import codecs
ct="TnprS056SUtOamtLTnpJS056a0tOeklLTnpNS056TUtOeklLTnpBS05qY0tOMklLTnpBS016QUtOMkVLTmpNS056a0tNekVLTjJFS016TUtOakVLTXpjS016VUtOV1lLTXpjS016QUtOV1lLTXpjS056VUtNek1LTldZS056QUtOelVLTXpNS056TUtOMlE9"
ct=base64.b64decode(base64.b64decode(ct))
l=ct.split(b'\n')
s=''.join([chr(int(i,16)) for i in l])
print(codecs.encode(s,'rot-13'))