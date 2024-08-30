# fetches data for the planets to include,name,mass,orbit period
# fetches which planet has the longest orbit



import requests
#fetches data for the planets
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            names = planet.get("englishName")
            mass = planet.get("mass")
            massValue=(mass['massValue'])
            orbit_period = planet.get("sideralOrbit")
            print(f"Planet: {names}, Mass: {massValue}, Orbit Period: {orbit_period} days")
            
            
fetch_planet_data()


#finds which planet has the longest orbit

longest_planet_orbit={}
def fetch_planet_orbit():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            names = planet.get("englishName")
            orbit_period = planet.get("sideralOrbit")
            longest_planet_orbit[names] =orbit_period
            #print(longest_planet_orbit)
    orbits = max(longest_planet_orbit.values())
    planet_name =max(longest_planet_orbit, key =longest_planet_orbit.get)
    print(f"\n{planet_name} has the longest orbit period of  {orbits} days")
fetch_planet_orbit()