import os.path
import requests

cities = [
    'Aachen',
    'Aarhus',
    'Adelaide',
    'Albuquerque',
    'Alexandria',
    'Amsterdam',
    'Antwerpen',
    'Arnhem',
    'Auckland',
    'Augsburg',
    'Austin',
    'Baghdad',
    'Baku',
    'Balaton',
    'Bamberg',
    'Bangkok',
    'Barcelona',
    'Basel',
    'Beijing',
    'Beirut',
    'Berkeley',
    'Berlin',
    'Bern',
    'Bielefeld',
    'Birmingham',
    'Bochum',
    'Bogota',
    'Bombay',
    'Bonn',
    'Bordeaux',
    'Boulder',
    'BrandenburgHavel',
    'Braunschweig',
    'Bremen',
    'Bremerhaven',
    'Brisbane',
    'Bristol',
    'Brno',
    'Bruegge',
    'Bruessel',
    'Budapest',
    'BuenosAires',
    'Cairo',
    'Calgary',
    'Cambridge',
    'CambridgeMa',
    'Canberra',
    'CapeTown',
    'Chemnitz',
    'Chicago',
    'ClermontFerrand',
    'Colmar',
    'Copenhagen',
    'Cork',
    'Corsica',
    'Corvallis',
    'Cottbus',
    'Cracow',
    'CraterLake',
    'Curitiba',
    'Cusco',
    'Dallas',
    'Darmstadt',
    'Davis',
    'DenHaag',
    'Denver',
    'Dessau',
    'Dortmund',
    'Dresden',
    'Dublin',
    'Duesseldorf',
    'Duisburg',
    'Edinburgh',
    'Eindhoven',
    'Emden',
    'Erfurt',
    'Erlangen',
    'Eugene',
    'Flensburg',
    'FortCollins',
    'Frankfurt',
    'FrankfurtOder',
    'Freiburg',
    'Gdansk',
    'Genf',
    'Gent',
    'Gera',
    'Glasgow',
    'Gliwice',
    'Goerlitz',
    'Goeteborg',
    'Goettingen',
    'Graz',
    'Groningen',
    'Halifax',
    'Halle',
    'Hamburg',
    'Hamm',
    'Hannover',
    'Heilbronn',
    'Helsinki',
    'Hertogenbosch',
    'Huntsville',
    'Innsbruck',
    'Istanbul',
    'Jena',
    'Jerusalem',
    'Johannesburg',
    'Kaiserslautern',
    'Karlsruhe',
    'Kassel',
    'Katowice',
    'Kaunas',
    'Kiel',
    'Kiew',
    'Koblenz',
    'Koeln',
    'Konstanz',
    'LaPaz',
    'LaPlata',
    'LakeGarda',
    'Lausanne',
    'Leeds',
    'Leipzig',
    'Lima',
    'Linz',
    'Lisbon',
    'Liverpool',
    'Ljubljana',
    'Lodz',
    'London',
    'Luebeck',
    'Luxemburg',
    'Lyon',
    'Maastricht',
    'Madison',
    'Madrid',
    'Magdeburg',
    'Mainz',
    'Malmoe',
    'Manchester',
    'Mannheim',
    'Marseille',
    'Melbourne',
    'Memphis',
    'MexicoCity',
    'Miami',
    'Moenchengladbach',
    'Montevideo',
    'Montpellier',
    'Montreal',
    'Moscow',
    'Muenchen',
    'Muenster',
    'NewDelhi',
    'NewOrleans',
    'NewYork',
    'Nuernberg',
    'Oldenburg',
    'Oranienburg',
    'Orlando',
    'Oslo',
    'Osnabrueck',
    'Ostrava',
    'Ottawa',
    'Paderborn',
    'Palma',
    'PaloAlto',
    'Paris',
    'Perth',
    'Philadelphia',
    'PhnomPenh',
    'Portland',
    'PortlandME',
    'Porto',
    'PortoAlegre',
    'Potsdam',
    'Poznan',
    'Prag',
    'Providence',
    'Regensburg',
    'Riga',
    'RiodeJaneiro',
    'Rostock',
    'Rotterdam',
    'Ruegen',
    'Saarbruecken',
    'Sacramento',
    'Saigon',
    'Salzburg',
    'SanFrancisco',
    'SanJose',
    'SanktPetersburg',
    'SantaBarbara',
    'SantaCruz',
    'Santiago',
    'Sarajewo',
    'Schwerin',
    'Seattle',
    'Seoul',
    'Sheffield',
    'Singapore',
    'Sofia',
    'Stockholm',
    'Stockton',
    'Strassburg',
    'Stuttgart',
    'Sucre',
    'Sydney',
    'Szczecin',
    'Tallinn',
    'Tehran',
    'Tilburg',
    'Tokyo',
    'Toronto',
    'Toulouse',
    'Trondheim',
    'Tucson',
    'Turin',
    'UlanBator',
    'Ulm',
    'Usedom',
    'Utrecht',
    'Vancouver',
    'Victoria',
    'WarenMueritz',
    'Warsaw',
    'WashingtonDC',
    'Waterloo',
    'Wien',
    'Wroclaw',
    'Wuerzburg',
    'Wuppertal',
    'Zagreb',
    'Zuerich'
]

total_size = 0
for city in cities:
    dest_path = 'D:/GIS Data/download.bbbike.org/{0}.osm.shp.zip'.format(city)
    if not os.path.exists(dest_path):
        url = 'https://download.bbbike.org/osm/bbbike/{0}/{0}.osm.shp.zip'.format(city)
        print(url)
        r = requests.get(url)
        with open(dest_path, 'wb') as f:
            f.write(r.content)
print("Cities: %d" % len(cities))
print("Total size: {0}".format(total_size))
