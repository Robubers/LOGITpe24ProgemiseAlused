# kirjuta programm mis
# küsib kasutajalt kas ta soovib osta boilerit
# (selle jaoks on vaja risttahuka valemit kasutada, ning küsida kasutajalt a ja b külg oõhjapindala jaoks sentimeetrites ja olevasoleva ala kõrguse h)
# olenevalt olemasolevast ruumalast
# - kui ruumala on liiga väike, öeldakse et meil ei ole pakkuda midagi sellises suuruses
# - kui ruumala on väike aga sobiv, pakutakse väikest boilerit väikese hinnaga
# - kui ruumala on paras, siis pakutakse väikest boilerit ja parajast boilerit
# - kui ruumala on suur, siis pakutakse väikest, parajast ja suurt boilerit.
# - kasutajalt küsitakse millist boilerit ta osta soovib NIMEPIDI, programm peab tuvastama õige nime kasutades .lower() või .upper() meetodeid
# väikese boileri maht arvutada a=35 b=35 h=70
# paraja boileri maht arvutada a=45 b=45 h=90
# suure boileri maht arvutada a=60 b=60 h=210
# hinnad mõtlete ise välja
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind

print("Tere, kas soovite osta boilerit?")
kasutaja_vastus = input()
vaike_boiler = 35 * 35 * 70
keskmine_boiler = 45 * 45 * 90
suur_boiler = 60 * 60 * 210
if(kasutaja_vastus == "ei"):
    print("head aega")  
 
 
 
 
 
vaike_boiler = 1000
keskmine_boiler = 2000
suur_boiler = 3000
 
 
 
 
 
 
#vaiksed
Vaillant_eloSTOR = 1000
 
Ariston_Velis = 1000
 
#keskimne
Bosch_Tronic_3000_T = 2000

#suured 
Termex_Compact = 3000

Ariston_Andris = 3000

Electrolux_EWH = 3000


 
 
    
else:
    print("meil on laos praegu need suurused: Väike boiler: a=35 b=35 h=70, Keskmine boiler: a=45 b=45 h=90, Suur boiler: a=60 b=60 h=210") 
    print("mis on teie a ja b külje põhjapindala, tahaks teada ka olevasoleva ala kõrguse (vastake cm-tes)")
    print("sisestage põhjapindala A")
    põhjapindala_a = int(input())
    print("põhjapindal_a on sisestatud")
    print("sisestage põhjapindala B")
    põhjapindala_b = int(input())
    print("sisestage olesoleva ala kõrguse H")
    ala_kõrgus_h = int(input()) 
     
     
     
    kasutaja_vastus_2 = põhjapindala_a * põhjapindala_b * ala_kõrgus_h
    if(kasutaja_vastus_2 < vaike_boiler):
        print("sinu sisestatud suurust praegu laos pole")           
    elif(kasutaja_vastus_2 > suur_boiler):
        print("teie sisustatud suurusega boilerit kahjuks pole laos")
    elif(kasutaja_vastus_2 == suur_boiler):
        print("teie siestatud boileri suurus ideaalselt sobib suure boileriga, võime teile pakkuda kaks boilerit: Vaillant eloSTOR, Ariston Velis")
    elif(kasutaja_vastus_2 == keskmine_boiler):
        print("teie sisestaud boileri suurus sobib ideaalselt keskmise boileriga, võime teile pakkuda ainult üks boilerit: Bosch Tronic 3000 T ")
    elif(kasutaja_vastus_2 == vaike_boiler):
        print("teie sisestaud boileri suurus sobib ideaalselt väikse boileriga, võime teile pakkuda kolm boilerit: Termex Compact, Ariston Andris, Electrolux EWH")
    
    elif(kasutaja_vastus_2 > vaike_boiler):
        print("teie sisestatud suurus on suurem kui antud väikse boileri suurus, aga selle suurusega boilereid on ka olemas: ")
    
    elif(kasutaja_vastus_2 > keskmine_boiler):
        print("teie sisestatud suurus on suurem kui antud keskmise boileri suurus, aga selle suurusega boilereid on ka olemas: ")
    
    
   
    print("kas valite suurt/keskmist/vaikset boileri? ")
    kasutaja_valik = input()
    if(kasutaja_valik == "väike boiler"):
        print("vaikse boileri hind "+vaike_boiler+""palun makske: "")
        kasutaja_sisestatud_summa1 = int(input())
        elif(kasutaja_sisestatud_summa1 == 1000):
            print("aitah maksmise eest")
            
    elif(kasutaja_valik == suur_boiler)
        print("suure boileri hind")
