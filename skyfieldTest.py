# https://rhodesmill.org/skyfield/positions.html

from skyfield.api import EarthSatellite, Topos, load

ts = load.timescale()
t = ts.now()

# line1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
# line2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'
starlink_url = "https://celestrak.com/NORAD/elements/starlink.txt"
starlinks = load.tle_file(starlink_url)
print ("Loaded", len(starlinks), "satellites")

results = []

for satellite in starlinks:

    # Geocentric
    geometry = satellite.at(t)

    # Geographic point beneath satellite
    subpoint = geometry.subpoint()
    latitude = subpoint.latitude
    longitude = subpoint.longitude
    elevation = subpoint.elevation

    # print latitude.degrees, ',', longitude.degrees

    satCoord = []
    satCoord.append(latitude.degrees)
    satCoord.append(longitude.degrees)

    results.append(satCoord)

print results
