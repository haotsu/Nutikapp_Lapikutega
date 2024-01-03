# Nutikapp_Lapikutega
Nutikapi kood koostöös Lapikutega.

Kasutajaliidese kood:
I2C ühenduse loomiseks kasutasime SMBus teeki (https://raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2) ning kasutajaliidese visuaalseks kuvamiseks kasutasime guizero (https://lawsie.github.io/guizero/) teeki. 

Programmi alguses luuakse App objekt, mis sisaldab kõigi teisi vidinaid, mida programm kasutab. Et vidinad oleksid rohkem organiseeritud ja nende asukoht oleks ka visuaalselt ilus, siis oleme kasutanud kahte Box objekti konteineritena, kuhu oleme paigutanud kuvatavad nupud, pildi jne. Koodi sisestuseks oleme kasutanud TextBox objekti. Lisaks visuaalsetele objektidele, luuakse ka ühendus mikrokontrolleriga läbi I2C ühenduse.

Kasutajaliidesel on numbri nupud 0-st 9-ni, millega saab sisestada 6-kohalist koodi. Samuti on kasutajaliidesel kustutamise nupp “DEL”, millega saab kõik numbrid tekstiväljas ära kustutada ja uuesti proovida numbreid sisestada. Viimaseks on koodi sisestamise nupp “ENT”, mida vajutades tehakse kapp lahti, kui on õige kood või kuvatakse administraatori paneeli, kui on sisestatud spetsiaalne administraatori kood (1337). Vale koodi korral kuvatakse veateade.

Loodud App objekti full_screen omadus on sätitud tõeseks, kuna siis ei ole võimalik tavakasutajal ligi pääseda operatsioonisüsteemi keskkonnale kasutades puutetundlikku ekraani. Tehnikutel on võimalus väljuda kasutajaliidese programmist kasutades VNC rakendust või sisestades nutikapi juures spetsiaalset väljumiskoodi (0000).

Vajutades nuppe, kus on peal number, kutsutakse välja input_to_textbox funktsioon, mis lisab numbri tekstiväljale kasutades TextBox-i append meetodit. Seda meetodit kasutades säilivad kõik väärtused, mis on eelnevalt sisestatud. 

Kustutamise nuppu “DEL” vajutades, kutsutakse välja clear_textbox funktsioon, mis kustutab kõik väärtused tekstiväljalt kasutades TextBox-i clear meetodit. 

Koodi sisestamise nuppu “ENT” vajutades, kutsutakse välja funktsioon nimega send_data, mis laeb kõik genereeritud koodid salvestatud failist used_codes hulka. Samuti kontrollitakse, kas sisestatud kood on administraatori kood või väljumiskood. Kui on sisestatud väljumiskood, siis programm läheb kinni ja kui on administraatori kood, siis kuvatakse administraatori paneel.

Administraatori paneel kuvatakse Window vidinaga ja paneel näitab olemasolevaid kappe. Kappe saab avada valides soovitud kapi radio nupu ning lisaks on võimalik kapile kood genereerida. Koode genereeritakse juhuslikult ja koodid on 6-kohalised. 

Koodi sisestamisel kontrollitakse, kas sisestatud kood on used_codes hulgas. Kui ei ole, siis annab kasutajaliides veateate kasutades App objekti error omadust. Kui kood on leitud hulgast, siis luuakse sellele koodile ajatempel, et oleks võimalik 15 minuti jooksul veel kasutada sama koodi kapi jaoks, ning avatakse kapp. Kasutajale antakse 8 sekundit aega ja siis küsib Raspberry Pi läbi I2C liidese mikrokontrollerilt kapi ukse seisundit. Kui uks on avanud ja kinni pandud, siis on kõik korras, aga kui uks ei ole avanud või kui uks ei ole kinni pandud, siis annab kasutajaliides sellest teada kasutades App objekti info omadust.

Installeerimine:

1) Python/Pip - sudo apt install python3 python3-pip
2) I2C - sudo raspi-config -> Interfacing Options -> Enable I2C
3) I2C Tools - sudo apt install -y i2c-tools
4) SMBus - sudo apt install -y python3-smbus
5) guizero - pip3 install guizero

I2C seadmete tuvastamiseks: sudo i2cdetect -y 1

Käivitamine:

1) Ava terminal
2) Navigeeri skripti asukohta (ls - näha faile ja kaustasi, cd <kausta_nimi> - liikuta valitud kausta)
3) python3 <faili_nimi> (nt: python3 nutikapp.py)
