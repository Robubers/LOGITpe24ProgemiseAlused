# kirjuta programm mis
#
# küsib kasutajalt tema nime | tegevus on tsüklis | nimi mida kontrollima peab on Siim
# küsib kasutajalt tema perekonnanime | tegevus on tsüklis | nimi mida kontrollima peab on Kallas
# nii kasutaja ees, kui ka perekonnanimi peab olema õige. Selle jaoks saab kasutada loogilist tehet,
# ning kasutajasisestus tuleb töödelda läbi funktsiooniga .capitalize()
# küsib kasutajalt esimest pin koodi | tegevus on tsüklis (ei tohi olla 0000 ega 1234)
# küsib kasutajalt ühte kolmest tegevusest mida ta teha soovib: | tegevus on tsüklis
# tegevused on: konto jäägi vaatamine, seifis oleva kulla koguse vaatamine, ja tehingu tegemin
# kui kasutaja valib konto jäägi vaatamise, siis tagastatakse kasutajale sõnum, tema konto jäägiga
# kui kasutaja valib eifis oleva kulla koguse vaatamise, siis küsitakse kasutajalt teist pin koodi
# - kui pin kood on õige, näidatakse kasutajale tema kulla kogust, programm väljastab tsüklis
# - ascii artina igale reale kullakangi niipalju kui neid on. | tegevus on tsüklis, väljastatakse vajalik kogus ridu
# kui kasutaja valib konto jäägi vaatamitehingu tegemise, siis küsitakse kasutajalt mõlemat pin koodi kahe küsimusega | tegevus on tsüklis
# ning kui mõlemad on õiged, alles siis lastakse kasutaja tehingumenüü juurde | tegevus on tsüklis
# - tehingumenüüs on 2 valikut:
# - välju (mis lõpetab programmi sõnumiga "headaega <eesnimi><perekonnanimi>, järgmise korrani, teie kuld on ohutult hoiul meie juures"
# - ülekanne
# - kui kasutaja valib ülekanne siis:
# - - küsitakse temalt saaja ees ja perekonnanime, teist pin koodi, kui palju raha ja kui palju kulda ta üle kanda soovib: | tegevus on tsüklis

olemasolevNimi = "Siim"
kasutajaNimi = ""
olemasolevPNimi = "Kallas"
kasutajaPNimi = ""
kontojaak = 10000000
kullajaak = 420



while (kasutajaNimi != olemasolevNimi):
    kasutajaNimi = input("Tere tulemast kullaautomaati, palun sisesta oma nimi: ").capitalize()

while (kasutajaPNimi != olemasolevPNimi):
    kasutajaPNimi = input("Palun sisesta oma perekonnanimi ka: ").capitalize()

if (kasutajaNimi == olemasolevNimi and kasutajaPNimi == olemasolevPNimi):
    correctPin1 = 4545
    correctPin2 = 6767
    kasutajaPin1 = int(input("Palun sisesta pin-kood #1"))
    if (kasutajaPin1 == 0000 or kasutajaPin1 == 1234):
        print("masin ei votta vastua lihtaid pin koode nau, 0000 voi 1234")
    elif (kasutajaPin1 == 0000 or kasutajaPin1):
        kasutajaTegevus == ""
        while (kasutajaTegevus == ""):
            kasutajaTegevus = input("palun valige tegevus: /n== vaata konto jääki == `konto`/n== vaata seifi kulda == `kuld`/n== tee tehing       == `tehing`")
            if(kasutajaTegevus.lower() == "konto" or kasutajaTegevus.lower() == "kuld" or kasutajaTegevus.lower() == "tehing"):
                if(kasutajaTegevus.lower() == "konto"):
                    print("palun"+kasutajaNimi+"" +kasutajaPNimi+"", "teie konto jaak on: " +str(kontojaak)+"  krooni.")
                elif(kasutajaTegevus.lower() == "kuld"):
                    kasutajaPin2 = int(input("palun sisesta pin kood #2 edasinemiseks."))
                    if(kasutajaPin2 == 0000 or kasutajaPin2 == 1234):
                        print("masin ei votta vastua lihtaid pin koode, nagu 0000 voi 1234")
                    elif (kasutajaPin2 == correctPin2):
                        increment = 0
                        while (increment != kullajaak):
                            print("/_//_/_24k_1kg___//")
                            increment += 1 
                        print("palun"+kasutajaNimi+" "+kasutajaPnimi+", seifis teil on kulda: "+str(kullajaak)+" kilo.")
                elif(kasutajaTegevus.lower() == "tehing"):
                    kasutajaPin1 = 0 
                    kasutajaPin2 = 0
                    while (kasutajaPin1 == 0 or kasutajaPin2 == 0):
                        if (kasutajaPin1 == 0):
                            kasutajaPin1 = int(input("palun sisestage pin-kood #1 uuesti"))
                        if (kasutajaPin1 == 0):
                            kasutajaPin2 = int(input("palun sisestage pin-kood #2 uuesti"))
                    if (kasutajapin1 == correctPin1 and kasutajaPin2 == correctPin2):
                        menuuValik = ""
                        while (menuuValik == ""):
                            print("tehingumenuu: vali tegevus/n== ulekanne == `ük`/n== valju   == `xt`")
                            menuuValik = input()
                            if (menuuvalik == "Ük"):
                            
                            else:
                                print("head aega "+kasutajaNimi+" "+kasutajaPNimi+" ,järgmise korrani, teie kuld on ohutult hoiul meie juures!")
                            
                                                    
                        
                        
            else:
                print ("palun sisesta õigesti kirjutatud valik")
                kasutajaTegevus = ""
                
        
    else:
        print("pin-kood on vale")
        
        
        
        
        
        
        
        
        
