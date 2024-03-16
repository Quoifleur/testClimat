# testClimat
## Readme
A small program in python to determine a climate according Köppen–Geiger climate classification of a place with their climatological normal of temperature, precipitation and their hemisphere.
> [!WARNING]
> **testCLimat _need_ the package NumPy to run**.

> [!NOTE]
> A web version of this program with more functionality exists here : https://testclimat.ovh/

### How use testClimat ?
All the instructions to use testClimat are written commentary directly in code.
Just keep in mind that you only need to enter your data properly into two tables (one for temperatures and the other for precipitation) and say whether these data were collected in the northern or southern hemisphere.
> [!IMPORTANT]
> Please use metric system of scale, with temperatures in degree Celsius (°C) et precipitations in millimeters (mm).
>
> Otherwise testclimat will do wrong values.

Example of values and overviews of the area to modify to use testClimat:
```python
# Array of temperatures in °C (12 months, first month is January)
Te = np.array([19.9,19.7,18.5,16.3,13.2,10.7,10.3,13.2,16.6,18.5,19.0,19.9]) 
# Array of precipitation in mm (12 months, first month is January)
Pr = np.array([136.4,109.8,86.7,41.0,27.6,16.3,7.4,19.6,16.5,85.4,72.9,117.8])
# True if North Hemisphere, False if South Hemisphere
North = False
# After the data is entered, run the program.
```

## Lisez-moi
Un petit programme en python pour déterminer le climat d'un lieu selon la classification de Köppen–Geiger avec les normales climatiques du lieu composé des normales de température, de précipitation et son hémisphère.
> [!WARNING]
> **testClimat _a besoin_ du package NumPy pour fonctionner**.

> [!NOTE]
> Il existe une version web de ce programm avec des fonctionnalités en plus ici : https://testclimat.ovh/

### Comment utiliser testClimat ?
Toutes les instructions d'utilisation de testClimat sont des écrits sous forme de commentaires directement dans le code. 
Garder juste à l'esprit qu'il ne vous faut que rentrer vos données convenablement dans deux tableaux (un pour les températures et l'autre pour les précipitations) et dire si ces données ont été récoltées dans l'hémisphère nord ou sud.
> [!IMPORTANT]
> Veuillez utiliser le système d'échelle métrique, avec les températures en degrés Celsius (°C) et les précipitations en millimètres (mm).
>
> Sinon, testclimat donnera des valeurs erronées.

Exemple de valeurs et aperçus de la zone à modifier pour utiliser testClimat :
```python
# Tableau des températures en °C (12 mois, le premier mois est celui de janvier)
Te = np.array([19.9,19.7,18.5,16.3,13.2,10.7,10.3,13.2,16.6,18.5,19.0,19.9]) 
# Tableau des précipitation en mm (12 mois, le premier mois est celui de janvier)
Pr = np.array([136.4,109.8,86.7,41.0,27.6,16.3,7.4,19.6,16.5,85.4,72.9,117.8])
# True si hémisphère Nord, False si hémisphère Sud
North = False
# Après avoir entré les données, exécutez le programme.
```
