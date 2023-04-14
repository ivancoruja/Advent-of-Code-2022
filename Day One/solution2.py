# Clears terminal before each run

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Sets correct path to input data file 

this_folder = os.path.dirname(os.path.abspath(__file__))
input_data = os.path.join(this_folder, 'input.in')

X = [l.strip() for l in open(input_data)]
# print(X)

X2 = (('\n').join(X)).split('\n\n')
# print(X2)

Q = []
for elf in ('\n'.join(X)).split('\n\n'):
    print(elf)
    q = 0
    for x in elf.split('\n'):
        print(q)
        q += int(x)
    Q.append(q)
    # print(q)
    # print(Q)

print(Q)
# Q = sorted(Q)

# print(max(Q))
# print(Q[-1],Q[-2],Q[-3])
# print(Q[-1]+Q[-2]+Q[-3])