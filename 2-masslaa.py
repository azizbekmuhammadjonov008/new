import os
os.system("cls")

a = int(input("uch xonali son kiriting => "))
birlar_xonasi = a%10
onlar_xonasi = a%100//10
yuzlar_xonasi = a%1000//100
teskar_son = birlar_xonasi*100+onlar_xonasi*10 + yuzlar_xonasi
print(f"birlar xonasi => {birlar_xonasi}\no'nlar xonasi => {onlar_xonasi}\nyuzlar xonasi => {yuzlar_xonasi}\nberilgan songa tekari son => {teskar_son}")

