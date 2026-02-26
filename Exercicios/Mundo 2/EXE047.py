print('{:=^50}'.format(' EXE 047 '), end='\n\n')
for c in range(1,51):
    if c % 2 == 0:
        print((c),' ' ,end='')
        if c % 10 == 0:
            print()
print(('\nFIM!'), end='\n')
print('=' * 50)