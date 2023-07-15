import simplekml

# Create a new KML object
kml = simplekml.Kml()

# List of places with their coordinates
places = [
    ('Nassau, Bahamas', 25.0343, -77.3963),
    ('Atlantis Paradise Island, Bahamas', 25.0849, -77.3241),
    ('Exuma Cays Land and Sea Park, Bahamas', 24.1833, -76.6000),
    ('Harbour Island, Bahamas', 25.4983, -76.6361),
    ('Grand Bahama Island', 26.6583, -78.2686),
    ('Andros Island, Bahamas', 24.3963, -77.8000),
    ('Windward Islands, Lesser Antilles', 15.3725, -61.3333),
    ('Leeward Islands, Lesser Antilles', 17.9000, -62.8333),
    ('Leeward Antilles', 12.1784, -68.2385),
    ('St. Kitts and Nevis', 17.3578, -62.782998),
    ('Lima, Peru', -12.0464, -77.0428),
    ('Cusco, Peru', -13.53195, -71.967463),
    ('La Paz, Bolivia', -16.5000, -68.1500),
    ('Sucre, Bolivia', -19.0333, -65.2627),
    ('Asuncion, Paraguay', -25.2637, -57.5759),
    ('Brasilia, Brazil', -15.7942, -47.8825),
    ('Manaus, Brazil', -3.4653, -62.2159),
    ('Caracas, Venezuela', 10.4806, -66.9036),
    ('Maracaibo, Venezuela', 10.6317, -71.6406),
    ('Cartagena, Colombia', 10.4000, -75.5000),
    ('Bogota, Colombia', 4.7110, -74.0721),
    ('Quito, Ecuador', -0.1807, -78.4678),
    ('Guayaquil, Ecuador', -0.2295, -78.5248)
]

# Create points for each place
for index, place in enumerate(places):
    point = kml.newpoint(name=f"{index+1}. {place[0]}", coords=[(place[2], place[1])])

# Create a linestring object with all coordinates to connect the points
linestring = kml.newlinestring()
linestring.coords = [(place[2], place[1]) for place in places]

# Save the KML
kml.save("itinerary.kml")
