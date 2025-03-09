algne_saldo = 100 

def konto(algne_saldo):
    print("Pangakontol on: " + str(algne_saldo) + " €")

def sisse(algne_saldo, summa):
    return algne_saldo + summa
    
def valja(algne_saldo, summa):
    return algne_saldo - summa

konto(algne_saldo)  

toiming = input("Kas soovite toiminguga raha (sisse) või (valja): ")
summa = int(input("Sisestage summa: "))

while True:
    if toiming == "sisse":
        print(f"Kontojääk: {algne_saldo+summa}" + " €") 
    elif toiming == "valja":
        print(f"Kontojääk: {algne_saldo-summa}" + " €")      
        break    
    