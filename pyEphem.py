# https://space.stackexchange.com/a/20629

import ephem
import datetime

name = "STARLINK-31";
line1 = "1 44235U 19029A   20119.25001157  .00015812  00000-0  92215-3 0  9992";
line2 = "2 44235  53.0008  78.4903 0001148  58.3107 248.5044 15.12129102 52621";

tle_rec = ephem.readtle(name, line1, line2);
tle_rec.compute();

print tle_rec.sublong, tle_rec.sublat;
