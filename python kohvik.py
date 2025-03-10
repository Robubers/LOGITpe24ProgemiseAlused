# kirjuta programm mis
#
# küsib kasutajalt kas tal on kõht tühi.
# kui kasutaja vastab ei:
#---siis programm ütleb talle vastu tagasi "ootame teid jälle kui teil isu on"
# kui kasutaja vastab ja:
#---küsib programm kas ta tahab ise võileiva kokku panna, või lasta arvutil selle genereerida
#---kui kasutaja tahab ise kokku panna, siis:
#-------küsib programm temalt kas ta tahab ühepoolset võileiba või kahepoolset võileiba:
#-------küsib programm temalt kas ta tahab võileivale võid või majoneesi
#-------küsib programm temalt kas ta tahab kurki võileivale
#-------küsib programm temalt kas ta tahab tomatit võileivale
#-------küsib programm temalt kas ta tahab peekonit võileivale
#---kui kasutaja tahab suvaliselt kokku panna, siis genereeritakse talle 5 korda erinev võileiva osa järjest
#---programm koostab kasutajale ascii pildi erinevatest kihtidest mida kasutaja lisanud on või arvuti genereerinud on
#---, ja küsib temalt raha 1.50 + 0.75 iga lisatud kihi eest
#---kui kasutaja ei maksa, siis öeldakse talle "ootame teid jälle kui teil isu on ja raha ka"
#---kui kasutaja maksab, siis tagastatakse ascii võileib teatega "aitäh tellimuse eest, tulge jälle"
# sai - [ , ,, '' ']
# või ja majoneesi jaoks ei kuvata kihti, aga ta annab hinnas lihtsalt juurde
# kurk - ▄▄▄▄ ▄▄▄
#tomat - ( | ▌|██)
#bacon - "~-,._.,-~"~-,.






from random import randint 



algsumma = 1.50
lisand = 0.75 



kasutaja_vastus = input("tere kasutaja kas teil on koht tuhi")
if(kasutaja_vastus.lower == "ei"):
    print("ootame teid jalle kui teil isu on")
else:
    print("kas te tahate ise voileiva teha voi akki tahate et arvuti teeks seda teie eest")
    kasutaja_vastus2 = input()
if(kasutaja_vastus2.lower() == "ise"):
    kasutaja_valik_sai  = input("tahad uhepoolset voileiva voi kahepoolset voileiva (uks/kaks)")
    kasutaja_valik_kaste = input("tahad void voi majoneesi?")
    kasutaja_valik_kurk  = input("tahad kurki? (ja/ei)")
    kasutaja_valik_tomat = input("tahad tomatit? (ja/ei") 
    kasutaja_valik_peekon = input("tahad peekoni? (ja/ei)")
    
    arvuti_valik_sai = randint(0,1)
    arvuti_valik_kaste = randint(0,1)
    arvuti_valik_kurk = randint(0,1)
    arvuti_valik_tomat = randint(0,1)
    arvuti_valik_peekon = randint(0,1) 
    
     if(arvuti_valik_sai == 1):
            sandwich_layers.append("Kahepoolne sai")
            algsumma += lisand
        else:
            sandwich_layers.append("Ühepoolne sai")
        
        if(arvuti_valik_kaste == 1):
            sandwich_layers.append("Või kastmega")
            algsumma += lisand
        
        if(arvuti_valik_kurk == 1):
            sandwich_layers.append("Kurk")
            algsumma += lisand
        
        if(arvuti_valik_tomat == 1):
            sandwich_layers.append("Tomat")
            algsumma += lisand
        
        if(arvuti_valik_peekon == 1):
            sandwich_layers.append("Peekon")
            algsumma += lisand
        
        
    
    
    
    
    

    if(kasutaja_valik_sai == "uks"):
        print("valisiduhepoolse leiva") 
    else:   
         algsumma += lisand
        print("valisid kahepoolset voileiva") 
        
        
    
    if(kasutaja_valik_kaste == "void"):
        algsumma = algsumma + lisand
        print("valisid"+kasutaja_valik_kaste+"")
    else:   
         algsumma += lisand
        print("valisid majoneesi") 
        
        
        

    if(kasutaja_valik_kurk == "ei"):
        print("kui ei taha siis ei taha")
    else:
         algsumma += lisand
        print("valisid kurki") 
        
        
    
    if(kasutaja_valik_tomat == "ei"):
        print("kui ei taha siis ei taha")
    else:   
        algsumma += lisand
        print("valisid tomati") 
    
    
    if(kasutaja_valik_peekon == "ei"):
        print("kui ei taha siis ei taha")
    else:   
        algsumma += lisand
        print("valisid peekoni") 
        
        
        print("siin on sinu võileib mis sisaldab: " +kasutaja_valik_sai+"" +kasutaja_valik_kaste+"" +kasutaja_valik_kurk+"" +kasutaja_valik_tomat+"" +kasutaja_valik_peekon+"" "teie lõppsumma tuleb: " +str(algsumma)+"")
        
        
        
        
        
e
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    