# Nutikapp_Lapikutega
Nutikapi kood koostöös Lapikutega.

Kuidas kasutada
See kood on kirjutatud Arduinole. Ise kasutamiseks, kopeeri kood, pane oma Arduino IDE'sse, lae kood oma mikrokontrollerile ja ühenda selle pinnid vastavalt vajadusele.

## Füüsiline
Raspi ja Arduino GND, SCL ja SDA on ühendatud.

## Virtuaalne

kood töötab nii

pin struct sisaltab iga kapi sensorite ja solenoidi füüsiliste pinnide numbreid
kappi struct sisaldab pinni structi, magnet sensori olekut, ir sensori olekut(mida hetkel veel ei ole), magnet sensori olekut(int uks, 0 - kinni, 1 lahti) ja error koodi.

