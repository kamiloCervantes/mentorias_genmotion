entradas = input().split(' ')

n = int(entradas[0])
m = int(entradas[1])

i = 0

meds_suc = []
meds_suc2 = []

list_suc = []

prints_finales = []

if n >= 1:
    for x in range(1, n + 1):
        list_suc.append(x)

    while i <= n:
        med = int(input())

        if med >= 1:

            i += 1

            meds_suc.append(med)
            meds_suc2.append(med)

            if i == n:

                for j in range(0, m):
                    num_med = input().split(' ')
                    sucursal = int(num_med[0])
                    estado = num_med[1]
                    glucosa = float(num_med[2])

                    if estado == 'ayunas':

                        if glucosa < 4.4:
                            meds_suc[sucursal - 1] -= 1

                        elif glucosa >= 4.4 and glucosa < 6.1:
                            pass

                        elif glucosa >= 6.1 and glucosa < 7:
                            meds_suc[sucursal - 1] -= 4

                        elif glucosa >= 7:
                            meds_suc[sucursal - 1] -= 10

                    elif estado == 'posprandial':

                        if glucosa < 7.8:
                            pass

                        elif glucosa >= 7.8 and glucosa < 11:
                            meds_suc[sucursal - 1] -= 7

                        elif glucosa >= 11:
                            meds_suc[sucursal - 1] -= 13

                    else:
                        pass
                break

prints_finales.append(
    f'{meds_suc.index(min(meds_suc)) + 1} {min(meds_suc)}')
prints_finales.append(
    f'{meds_suc.index(max(meds_suc)) + 1} {max(meds_suc)}')

for e in range(1, len(meds_suc) + 1):
    prints_finales.append(
        f'{e} {(meds_suc2[e - 1] - meds_suc[e - 1]) * 100/meds_suc2[e -1]:.2f}%')

for z in range(len(prints_finales)):
    print(prints_finales[z])
"""

    while n >= 1:
        for i in range(n):
                med = input()#i+1
                med = int (med)
                meds_suc.append(med)
                meds_suc2.append(med)
"""