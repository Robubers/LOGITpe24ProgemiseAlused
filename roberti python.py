# kirjuta programm mis
# küsib kasutajalt kui suur ta põrand on
# (selle jaoks on vaja ristküliku valemit kasutada, ning küsida kasutajalt a ja b külg sentimeetrites)
# küsib kasutajalt milliseid põrandaplaate ta tahab
# kasutajale antakse 6 ascii näidet, ja kasutaja sisestab numbri milline muster talle meeldib
#
# ██░░ ║┌─┐ ▀▄░░
# ░░██ ║└─┘ ░░▀▄ (muid mustreid saab välja mõelda kas tähtedest või start -> character map abiga)
# (ülejäänud kolm mustrit mõtle ise)
# väljasta kasutajale ekraan mustriga koos hinnaarvutusega.
# (esimene muster on odavaim, viimane kalleim, tehe on pindala*mustriväärtus)
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind

def ascii_patterns():
    """Väljasta kõik mustrid koos hindadega."""
    patterns = [
        ("██░░", 1.0),
        ("░░██", 1.5),
        ("║┌─┐", 2.0),
        ("▀▄░░", 2.5),
        ("░░▀▄", 3.0),
        ("▓▓▒▒", 3.5)
    ]
    
    print("Vali üks järgmistest mustritest:")
    for i, (pattern, price) in enumerate(patterns, start=1):
        print(f"{i}. {pattern} (hind: {price} EUR)")

    return patterns

def main():
   
    a = float(input("Sisesta oma põranda esimese külje pikkus (sentimeetrites): "))
    b = float(input("Sisesta oma põranda teise külje pikkus (sentimeetrites): "))
    
  
    pindala = a * b
    print(f"Teie põranda pindala on {pindala:.2f} cm².")
    
    
    patterns = ascii_patterns()
    
   
    muster_valik = int(input("Sisesta muster (1-6): "))
    
    
    muster, hind = patterns[muster_valik - 1]
    kogu_hind = pindala * hind
    
    
    print(f"\nValisid mustri: {muster}")
    print(f"Põranda katmiseks tuleb maksta: {kogu_hind:.2f} EUR.")
    
    
    maksab = input("Kas soovite maksta? (jah/ei): ").lower()
    
    if maksab == "ei":
        kogu_hind *= 0.9  
        print(f"Uus hind on: {kogu_hind:.2f} EUR.")
        
        maksab = input("Kas soovite maksta nüüd? (jah/ei): ").lower()
        if maksab == "ei":
            kogu_hind *= 0.9  
            print(f"Viimane hind on: {kogu_hind:.2f} EUR.")
    
    
    if maksab == "jah":
        print(f"Aitäh, makse sooritati! Kogu summa: {kogu_hind:.2f} EUR.")
    else:
        print("Ootame teid jälle, kui teil on raha!")


if __name__ == "__main__":
    main()









 



















































































































                                                           