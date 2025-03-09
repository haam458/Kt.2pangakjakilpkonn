def konto(algne_saldo):
    if algne_saldo == 100:
        print("Pangakontol on: " + str(algne_saldo) + " €")
konto(100)

def sisse(algne_saldo, summa):
    if toiming == "sisse":
        print(f"Kontojääk: {algne_saldo+summa}" + " €")    
#sisse(algne_saldo, summa)

def valja(algne_saldo, summa):
    if toiming == "valja":
        print(f"Kontojääk: {algne_saldo-summa}" + " €")
#valja(algne_saldo, summa)
algne_saldo = 100 

summa = int(input("Sisestage summa: "))


print("Kontojääk: ")   
            
    