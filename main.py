with open('pm10.txt', 'r', encoding="utf8") as pm:
    z = pm.readlines()

with open('stacje.txt', 'r', encoding="utf8") as s:
    g = s.readlines()

for it in g:
    tab = it.split(';')
    if "Katowice" in tab[5]:
        print(tab[3])
    if "Kraków" in tab[5]:
        print(tab[3])

sumKrak = 0
sumKat = 0
dzielKrak = 0
dzielKat = 0
for it in z:
    tab = it.split(';')
    if tab[4] in "MpKrakAlKras" + "MpKrakBujaka" + "MpKrakBulwar":
        sumKrak += float(tab[8].replace(',', '.')) * int(tab[15])
        dzielKrak += int(tab[15])
    if tab[4] in "SlKatoKossut" + "SlKatoPlebA4":
        sumKat += float(tab[8].replace(',', '.')) * int(tab[15])
        dzielKat += int(tab[15])

print("PM10 w Krakowie " + str(sumKrak / dzielKrak))
print("PM10 w Katowicach " + str(sumKat / dzielKat))
