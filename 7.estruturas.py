#estruturas de decisão
"""
temp = int(input('entre com a temperatua atual:'))

if temp<0:
    print('congelando')
elif temp<20:
    print('frio')
elif temp <25:
    print('normal')
elif temp<35:
    print('calor')
else:
    print('muito quente')
"""
print ('exemplo loop while')
num = 1
while (num < 10):
    num +=1
    if (num==4):
            continue
    print(num)
    num +=1
    if (num ==7):
        break
print('\n loop for')
for x in range (10):
    if (num==4):
         continue
    print(x)
    if (x==7):
        break
print('alfabeto')
for c in range(65,91):
    print(chr(c)+ chr(c+32),end='')
