import math
areaantenasprevias = 16600
tipoa = 50600
tipob = 19200
tipoc = 36900
tipod = 40500
tipoe = 34200
antenasnuevasa = 0
antenasnuevasb = 0
antenasnuevasc = 0
antenasnuevasd = 0
antenasnuevase = 0
can_antenas = 0
can_antenaa = 0
can_antenab = 0
can_antenac = 0
can_antenad = 0
can_antenae = 0

print("Ingrese el numero de zonas: ")
zonas = int(input())
if zonas == 0:
    print(zonas)
    print("a", "{0:.2f}%".format(0))
    print("b", "{0:.2f}%".format(0))
    print("c", "{0:.2f}%".format(0))
    print("d", "{0:.2f}%".format(0))
    print("e", "{0:.2f}%".format(0))
else:
    while zonas > 0:
        print("Ingrese el area:")
        area = float(input())
        print("Ingrese las antenas instaladas")
        antenasinstaladas = int(input())
        print("Ingrese el tipo de antena")
        tipoantenainst = str(input())
        zonas = zonas - 1
        area2 = round((area - (antenasinstaladas * areaantenasprevias)))
    
        if tipoantenainst == "a":
            antenasnuevasa = math.ceil(int(area2 / tipoa))
            if antenasnuevasa < 0:
               antenasnuevasa = 0
            can_antenaa = can_antenaa + antenasnuevasa
            can_antenas = can_antenas + antenasnuevasa
        else:
            if tipoantenainst == "b":
                antenasnuevasb = math.ceil(int(area2 / tipob))
                if antenasnuevasb < 0:
                   antenasnuevasb = 0
                can_antenab = can_antenab + antenasnuevasb
                can_antenas = can_antenas + antenasnuevasb
            else:
                if tipoantenainst == "c":
                    antenasnuevasc = math.ceil(int(area2 / tipoc))
                    if antenasnuevasc < 0:
                       antenasnuevasc = 0
                    can_antenac = can_antenac + antenasnuevasc
                    can_antenas = can_antenas + antenasnuevasc
                else:
                    if tipoantenainst == "d":
                        antenasnuevasd = math.ceil(int(area2 / tipod))
                        if antenasnuevasd < 0:
                            antenasnuevasd = 0
                        can_antenad = can_antenad + antenasnuevasd
                        can_antenas = can_antenas + antenasnuevasd
                    else:
                        if tipoantenainst == "e":
                            antenasnuevase = math.ceil(int(area2 / tipoe))
                            if antenasnuevase < 0:
                                antenasnuevase = 0
                            can_antenae = can_antenae + antenasnuevase
                            can_antenas = can_antenas + antenasnuevase
                        else:
                            if tipoantenainst > "e" and antenasinstaladas < 0:
                               can_antenas += 0
                                                                             
    print(can_antenas)
    print("a", "{0:.2f}%".format((can_antenaa / can_antenas) * 100))
    print("b", "{0:.2f}%".format((can_antenab / can_antenas) * 100))
    print("c", "{0:.2f}%".format((can_antenac / can_antenas) * 100))
    print("d", "{0:.2f}%".format((can_antenad / can_antenas) * 100))
    print("e", "{0:.2f}%".format((can_antenae / can_antenas) * 100))