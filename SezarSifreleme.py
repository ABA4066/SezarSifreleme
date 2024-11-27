x=int(input("Mesajı Gizlimek için 1, Gizli Mesaji Açmak için 2 ye basın\n"))
w=list()
if x==1:
    mesaj=input("Mesajı girin\n")
    for i in mesaj :
        w.append(chr(ord(i)+4))
    w = ''.join(w)
    print(w)
elif x==2:
    mesaj = input("Mesajı girin\n")
    for i in mesaj:
        w.append(chr(ord(i) - 4))
    w=''.join(w)
    print(w)
else:
    print("Yanlış girdiniz!!!")