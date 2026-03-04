uang = 0
rate=0
time=0

while True :
    uang = float(input("masukan berapa banyak uang yang telah kamu investasikan :"))
    if uang < 0 :
        print(F"hasil mu invalid")
    else:
     break

while True :
    rate = float(input("masukan berapa presentase tahunan uang yang telah kamu investasikan :"))
    if  rate < 0 :
        print(F"hasil mu invalid")
    else:
        break
while True:
    time= float(input("masukan berapa lama uang yang telah kamu investasikan :"))
    if time <0 :
        print(F"hasil mu invalid")
    else:
        break
dolaR = float(uang * pow((1 + rate/100), time))
dolar = f"{dolaR:,.2f}"

rupiaH =dolaR *16.700
rupiah = f"{rupiaH:,.0f}"



hasil_dolar = dolar.replace(",", "x" ).replace(".",",").replace ("x", ".")
hasil_rupiah = rupiah.replace(",",".")

print(f"hasil investment mu adalah {hasil_dolar} $ ")
print(f"total investment adalah{hasil_rupiah } rupiah ")