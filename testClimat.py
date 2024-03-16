import numpy as np
# Insert the temperature and precipitation data for the 12 months of the year. Don't forget to change the hemisphere if necessary (Write "Nord" for North ans "Sud" for South).
# Insérer les données climatiques : température en °C et précipitation en mm, Noubliez pas d'indiquer l'hémisphère (Nord ou Sud).
Te = np.array([19.9,19.7,18.5,16.3,13.2,10.7,10.3,13.2,16.6,18.5,19.0,19.9])
Pr = np.array([136.4,109.8,86.7,41.0,27.6,16.3,7.4,19.6,16.5,85.4,72.9,117.8])
Hm = 'Sud'

# Array of summer month precipitation in mm
# Array of temperatures in summer in °C (Depending on the hemisphere winter and summer are reversed)
#Tableau des températures en été en °C (En fonction de l'hémisphère l'hiver et l'été sont inversés)
if Hm == 'Nord':
    STe = np.array([Te[3], Te[4], Te[5], Te[6], Te[7], Te[8]])
    WPr = np.array([Pr[0], Pr[1], Pr[2], Pr[9], Pr[10], Pr[11]]) #Tableau des précipitation des mois d'hiver en mm
    SPr = np.array([Pr[3], Pr[4], Pr[5], Pr[6], Pr[7], Pr[8]])
else:
    STe = np.array([Te[0], Te[1], Te[2], Te[9], Te[10], Te[11]])
    SPr = np.array([Pr[0], Pr[1], Pr[2], Pr[9], Pr[10], Pr[11]])#Tableau des précipitation des mois d'hiver en mm
    WPr = np.array([Pr[3], Pr[4], Pr[5], Pr[6], Pr[7], Pr[8]])

print('STe (temperature in °C)')
for i in range(6):
    print(f'STe[{i}] >>>: {STe[i]}')

print('SPr & WPr (precipitation in mm)')
for i in range(6):
    print(f'SPr[{i}]  >>>: {SPr[i]}')

for i in range(6):
    print(f'WPr[{i}]  >>>: {WPr[i]}')

# Calculate variables
NomClimat1Trouve = False
ClimatTrouve = False
PTHTrouve = False


b = 0
i = 0
Compte = 0

PTH = 0
Ia = 0

Tmax = max(Te)
Tmin = min(Te)
Tannuelle = sum(Te) / 12

Pmax = max(Pr)
Psmax = max(SPr)
Pwmax = max(WPr)
Pmin = min(Pr)
Psmin = min(SPr)
Pwmin = min(WPr)
Pannuelle = sum(Pr)

Phiver = sum(SPr)
Pete = sum(WPr)

# Calculate variables
NomClimat1Trouve = False
ClimatTrouve = False
PTHTrouve = False

b = 0
i = 0
Compte = 0

PTH = 0
Ia = 0

Tmax = max(Te)
Tmin = min(Te)
Tannuelle = sum(Te) / 12

Pmax = max(Pr)
Psmax = max(SPr)
Pwmax = max(WPr)
Pmin = min(Pr)
Psmin = min(SPr)
Pwmin = min(WPr)
Pannuelle = sum(Pr)

Phiver = sum(SPr)
Pete = sum(WPr) #Tableau des précipitation des mois d'été en mm*/

print('STe (température en °C)')
for i in range(6):
    print ('>>>', STe[i])
print(' SPr & WPr (précipitation en mm)')
for i in range(6):
    print ('>>>', SPr[i])
for i in range(6):
    print ('>>> ', WPr[i])
#Calcule des variables */
    
NomClimat1Trouvé = False
ClimatTrouvé = False
PTHTrouvé = False

b = 0
i = 0
Compte = 0

PTH = 0
Ia = 0

Tmax = max(Te)
Tmin = min(Te)

Tannuelle = Te.sum() / 12

Pmax = max(Pr)
Psmax = max(SPr)
Pwmax = max(WPr)
Pmin = min(Pr)
Psmin = min(SPr)
Pwmin = min(WPr)
Pannuelle = Pr.sum()

Phiver = SPr.sum()
Pété = WPr.sum()

#Calcule de l'indice de Gaussen */
#Tableau des mois arides */
Ar = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
for i in range(12):
    if Pr[i] < 2 * Te[i]:
        Ar[i] = 1
print('Mois aride')
for i in range(12):
    print ('>>>', Ar[i])

#Calcule de l'indice de Martonne */
Ia = Pannuelle / (Tannuelle + 10) # Pour l'année*/
Im = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(12):
    Im[i] = 12 * Pr[i] / (Te[i] + 1)
print('Martonne')
for i in range(12):
    print('Im[' + str(i) + '] >>> ' + str(Im[i]))
#Détermination de la variable b (il s'agit d'un régime thermique possible pour les climats tempérées) */
for i in range(12):
    if Te[i] > 10:
        Compte += 1
if Compte >= 4:
    b = 1
else:
    b = 0
#Détermination du PTH
if Tmax < 10:
    PTH = Tannuelle * 2
    PTHTrouvé = True
if not PTHTrouvé and (Pannuelle * (2 / 3)) >= Pété:
    PTH = (Tannuelle * 2) + 28
    PTHTrouvé = True

if not PTHTrouvé:
    PTH = (Tannuelle * 2) + 14
    PTHTrouvé = True
#Détermination du climat (testClimat)*/
if Tmax < 10:
    LettreClimat1 = "E"
    NomClimat1 = "polaire "
    if Tmax >= 0 and Tmax < 10:
        LettreClimat2 = "t"
        NomClimat2 = " de toundra "
        ClimatTrouvé = True
    if Tmax <= 0 and not  ClimatTrouvé:
        LettreClimat2 = "f"
        NomClimat2 = "glacier "
        ClimatTrouvé = True

if Pannuelle < 10 * PTH and not  ClimatTrouvé:
    LettreClimat1 = "B"
    NomClimat1 = " aride "

    if (Pannuelle > 5 * PTH):
        LettreClimat2 = "s"
        NomClimat2 = "de steppe "

        if (Tannuelle >= 18 and not  ClimatTrouvé):
            LettreClimat3 = "h"
            NomClimat3 = "chaud "
            ClimatTrouvé = True
        
        if (not ClimatTrouvé):
            LettreClimat3 = "k"
            NomClimat3 = "froid "
            ClimatTrouvé = True
        
    
    if (Pannuelle <= 5 * PTH and not ClimatTrouvé):
        LettreClimat2 = "w"
        NomClimat2 = "de désert "

        if (Tannuelle >= 18):
            LettreClimat3 = "h"
            NomClimat3 = "chaud "
            ClimatTrouvé = True
        
        if (Tannuelle < 18 and not ClimatTrouvé):
            LettreClimat3 = "k"
            NomClimat3 = "froid "
            ClimatTrouvé = True
        
    

if (Tmin >= 18 and not ClimatTrouvé):
    LettreClimat1 = "A"
    NomClimat1 = "équatorial "

    if (Pmin >= 60):
        LettreClimat2 = "f"
        LettreClimat3 = ""
        NomClimat2 = "avec forêt humide équatoriale "
        NomClimat3 = ""
        ClimatTrouvé = True
    
    if (Pannuelle >= 25 * (100 - Pmin) and not ClimatTrouvé):
        LettreClimat2 = "m"
        LettreClimat3 = ""
        NomClimat2 = "avec mousson équatoriale "
        NomClimat3 = ""
        ClimatTrouvé = True
    
    if (Psmin < 60 and not ClimatTrouvé):
        LettreClimat2 = "s"
        LettreClimat3 = ""
        NomClimat2 = "avec savane équatoriale avec été sec "
        NomClimat3 = ""
        ClimatTrouvé = True
    
    if (Pwmin < 60 and not ClimatTrouvé):
        LettreClimat2 = "w"
        LettreClimat3 = ""
        NomClimat2 = "avec savane équatoriale avec hiver sec "
        NomClimat3 = ""
        ClimatTrouvé = True
    

if (Tmin > -3 and Tmin < 18 and not ClimatTrouvé):
    LettreClimat1 = "C"
    NomClimat1 = " tempéré "
    NomClimat1Trouvé = True


if (Tmin <= -3 and not ClimatTrouvé and not NomClimat1Trouvé):
    LettreClimat1 = "D"
    NomClimat1 = " continental neigeux "

if (LettreClimat1 == "C" or LettreClimat1 == "D"):
    if (Psmin < Pwmin):
        if (Pwmax > (3 * Psmin) and Psmin < 40):
            LettreClimat2 = "s"
            NomClimat2 = "avec été sec et hiver pluvieux "

            if (LettreClimat1 == "D"):
                if (Tmin <= -38 and not ClimatTrouvé):
                    LettreClimat3 = "d"
                    NomClimat3 = "avec un été et hiver très froid"
                    ClimatTrouvé = True
                
            
            if (LettreClimat1 == "C" or LettreClimat1 == "D"):
                if (Tmax >= 22 and not ClimatTrouvé):
                    LettreClimat3 = "a"
                    NomClimat3 = "avec un été chaud "
                    ClimatTrouvé = True
                
                if (b == 1 and not ClimatTrouvé):
                    LettreClimat3 = "b"
                    NomClimat3 = "avec un été tempéré "
                    ClimatTrouvé = True
                
                if (Tmin > -38 and not ClimatTrouvé):
                    LettreClimat3 = "c"
                    NomClimat3 = "avec un été frais et hiver froid "
                    ClimatTrouvé = True
                
            
        
    
    if (not ClimatTrouvé):
        if (Pwmin < Psmin and Psmax > 10 * Pwmin):
            LettreClimat2 = "w"
            NomClimat2 = "avec hiver sec et été pluvieux "

            if (LettreClimat1 == "D"):
                if (Tmin <= -38 and not ClimatTrouvé):
                    LettreClimat3 = "d"
                    NomClimat3 = "avec un été et hiver très froid "
                    ClimatTrouvé = True
                
            
            if (LettreClimat1 == "C" or LettreClimat1 == "D"):
                if (Tmax >= 22 and not ClimatTrouvé):
                    LettreClimat3 = "a"
                    NomClimat3 = "avec un été chaud "
                    ClimatTrouvé = True
                
                if (b == 1 and not ClimatTrouvé):
                    LettreClimat3 = "b"
                    NomClimat3 = "avec un été tempéré "
                    ClimatTrouvé = True
                
                if (Tmin > -38 and not ClimatTrouvé):
                    LettreClimat3 = "c"
                    NomClimat3 = "avec un été frais et hiver froid "
                    ClimatTrouvé = True
                
            
        
    
    if (ClimatTrouvé == False):
        LettreClimat2 = "f"
        NomClimat2 = "humide "
        if (LettreClimat1 == "D" and not ClimatTrouvé):
            if (Tmin <= -38):
                LettreClimat3 = "d"
                NomClimat3 = "été et hivers très froid "
                ClimatTrouvé = True
            
        
        if (LettreClimat1 == "C" or LettreClimat1 == "D"):
            if (Tmax >= 22):
                LettreClimat3 = "a"
                NomClimat3 = "été chaud "
                ClimatTrouvé = True
            
            if (b == 1 and not ClimatTrouvé):
                LettreClimat3 = "b"
                NomClimat3 = "été tempéré "
                ClimatTrouvé = True
            
            if (Tmin > -38 and not ClimatTrouvé):
                LettreClimat3 = "c"
                NomClimat3 = "été frais et hivers froid "
                ClimatTrouvé = True
            
        
    

#Débug */
NomClimat = NomClimat1 + NomClimat2 + NomClimat3
LettreClimat = LettreClimat1 + LettreClimat2 + LettreClimat3

print ('ClimatTrouvé >>> ', ClimatTrouvé)
print ('PHTrouvé >>> ', PTHTrouvé)
print ('.')
print ('b >>> ', b)
print ('i >>> ',i)
print ('Compte >>> ', Compte)
print ('')
print ('PTH >>> ', PTH)
print ('Ia >>> ', Ia)
print ('')
print ('Tmax >>> ', Tmax)
print ('Tmin >>> ', Tmin)
print ('Tannuelle >>> ', Tannuelle)
print ('.')
print ('Pmax >>> ', Pmax)
print ('Psmax >>> ', Psmax)
print ('Pwmax >>> ', Pwmax)
print ('Pmin >>> ', Pmin)
print ('Psmin >>> ', Psmin)
print ('Pwmin >>> ', Pwmin)
print ('Pannuelle >>> ', Pannuelle)
print ('.')
print ('Phiver >>> ', Phiver)
print ('Pété >>> ', Pété)
print ('.')
print (NomClimat)
print (LettreClimat)
