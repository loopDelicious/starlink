from skyfield.api import EarthSatellite, Topos, load

ts = load.timescale()
t = ts.now()

line1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
line2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'

boston = Topos('42.3583 N', '71.0603 W')
satellite = EarthSatellite(line1, line2, name='ISS (ZARYA)')

# Geocentric

geometry = satellite.at(t)

# Geographic point beneath satellite

subpoint = geometry.subpoint()
latitude = subpoint.latitude
longitude = subpoint.longitude
elevation = subpoint.elevation

# Topocentric

difference = satellite - boston
geometry = difference.at(t)

print latitude, longitude;