image = Image.open('Star-map.jpg')

# The goal of this project was to add the solar traverse to the Star-map.jpg file

# I used paint.net to get a good understanding of where the pixels I would like to edit are located
# The star chart itself begins at pixel 62 and ends at pixel 3455 (left to right)
#
# This is fundamentally a sin function around the zero degree line, located at approximately pixel 901 (vertical)
#
# My derived equation to morph from hour angle to pixel angle is:
# a = (3393 - (i - 62)) / 3393
#
# The value of a is then inserted in the usual declination sin equation:
# d = 23.4 * sin(2*pi*a)
#
# My derived equation to morph from declination into vertical pixel coordinate:
# z = 901 - (d*9.34)
#
# I then iterate these calculations across every horixontal from 62 to 3455 thrice to add three pixel lines to ensure visibility
# 

for i in range(62, 3455):
  a = (3393 - (i - 62)) / 3393
  d = 23.4 * math.sin(2*math.pi*a)
  z = int(901 - (d * 9.34))
  image.putpixel((i,z), (255, 164, 0))
  image.putpixel((i,z-1), (255, 164, 0))
  image.putpixel((i,z-2), (255, 164, 0))
  
image.save('star-map-with-sun-traverse.jpg')
