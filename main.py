m = int(input("Adja meg a henger magasságát méterben: "))
r = int(input("Adja meg a henger sugarának hosszúságát méterben: "))
terfogat = 3.14*r*r*m
felszin = 2*3.14*r*(r+m)
print("A Háromszög térfogat:", terfogat, ("m3"))
print("A Háromszög felszin:", felszin, ("m2"))
