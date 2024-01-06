# Nutikapp_Lapikutega
Nutikapi kood koostöös Lapikutega.
Selleks, et meie tehtud tööd omal käel järgi teha on sul vaja 12V toiteblokki, solenoid lukke, magnet lüliteid(ukse asendi kotrollimiseks), transistori, mis avaneb vähemalt 3.3V peale, mõned takistid, Raspberry PI 3 ja Arduinot(laias laastus ei ole oluline, millise sa valid). Meie kasutasime lisaks puutetundliku ekraani Raspberry jaoks, kuid see ei ole sul vajalik.
Lae vastavad koodid oma mikrokontrolleritele, ühenda need omvahel I2C jaoks(Kontrolli oma boardi pinnid üle, et need õieti ühendada).
Lõpuks ühenda ka elektriskeemil kõik ära, nii et pinge Arduino pinilt avaks transistori, mis juhib solenoidi ning pull down või pull up lüliti magnet lüliti jaoks.
