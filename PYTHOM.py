# kirjuta programm mis
# küsib kasutajalt tsükli sees kui vana ta on (tühja sisestuse puhul küsitakse uuesti niikaua kuni kasutaja on midagi kirjutanud)
# - kui kasutaja on noorem kui 3 aastat, ütle kasutajale et on liiga noor, ning kujundit ei joonistata
# küsib kasutajalt tsükli sees mis on ta lemmikvärv
# - Valikusse pange(punane oranz kollane roheline helesinine tumesinine lilla roosa must valge pruun tumerohline ja teal)
# - kasutajasisend tuleb standardiseerida sõnetöötlusmeetoditega
# - kui kasutaja ei sisesta midagi mis on valikus, töötab tsükkel niikaua kuni kasutaja sisestab midagi mis on
# - kasutajasisend tõlgitakse turtle jaoks inglise keelde ifide abil
# küsib kasutajalt tsükli sees mis on ta lemmikkujund
# - Valikusse pange(ring, ruut, võrdhaarne kolmnurk, kuusnurk)
# - kasutajasisend tuleb standardiseerida sõnetöötlusmeetoditega
# - kui kasutaja ei sisesta midagi mis on valikus, töötab tsükkel niikaua kuni kasutaja sisestab midagi mis on
# Põhinedes kasutajalt saadud andmetele, joonista kasutaja lemmikvärviga tema lemmikkujund.
# Siis tagasta konsooli sõnum "Palun <nimi>, siin on sinu <värv> <kujund>!"

import turtle 



tsykel = True
while tsykel:
    print("sisesta enda vanus palun")
    vanus = int(input())
    print("nüüd nimi")
    nimi = input()
    tsykel = False
    if(vanus < 3):
        print("oled liiga noor")
    

    else:
        print("mis on su lemmikvärv vali nendest: punane oranz kollane roheline helesinine tumesinine lilla roosa must valge pruun tumerohline ja teal")
        värv = input().lower()
        

varv_tsykel = True
while varv_tsykel:
    
        if(värv == "punane"):
           print("saaab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk ")
       
        elif(värv == "oranz"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
       
        elif(värv == "kollane"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
       
        elif(värv == "roheline"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
       
        elif(värv == "helesinine"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
       
        elif(värv == "tumesinine"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
       
        elif(värv == "lilla"):
           print("saaab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
       
        elif(värv == "roosa"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
       
        elif(värv == "must"):
           print("saaab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
       
        elif(värv == "valge"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
      
        elif(värv == "pruun"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
       
        elif(värv == "tumeroheline"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
         
        elif(värv == "teal"):
           print("saab valida need kujundit: ring, ruut, võrdhaarne kolmnurk, kuusnurk")
        varv_tsykel = False
        
        kujund = input().lower()
        
      
        if kujund == "ring":
            t.circle(50)
            
        elif kujund == "ruut":
            
           
           
            
    
        elif kujund == "võrdhaarne kolmnurk":
            
            
        
        elif kujund == "kuusnurk":
      


    


  