vrsta=float(input("koliko strano prizmo imate? (3/4/6)"))
if vrsta < 4:
    Kateri_3_kotnik=float(input("kakšen trikotnik je spodaj (pravokoten=1/enakostranièen=2/enakokraki=3/raznostranièen=4)"))
    if Kateri_3_kotnik < 2:
        pkaq=float(input("Ali imate stranico a?(ja=1/ne=2)"))
        if pkaq < 2:
            pka=float(input("in koliko je a?"))
            pkbq=float(input("aliimate stranico b? (ja=1/ne=2)"))
            if pkbq < 2:
                pkb = float(input("in kolimo je?"))
                pkO=(pka*pkb)/2
                print("osnovna ploskev je:" , pkO , ".")
