import colorsys
import math
import random
import time

try:
    import unicornhathd as unicorn
    print("16x16 unicorn detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd

print("""Unicorn HAT HD: Stars
This example simulates a wooshing star field.
Press Ctrl+C to exit!
""")

star_count = 25
star_speed = 0.05
stars = []

for i in range(0, star_count):
  stars.append((random.uniform(4, 11), random.uniform(4, 11), 0))

try:
    while True:
      unicornhathd.clear()

      for i in range(0, star_count):
        stars[i] = (
            stars[i][0] + ((stars[i][0] - 8.1) * star_speed),
            stars[i][1] + ((stars[i][1] - 8.1) * star_speed),
            stars[i][2] + star_speed * 50)

        if stars[i][0] < 0 or stars[i][1] < 0 or stars[i][0] > 16 or stars[i][1] > 16:
          stars[i] = (random.uniform(4, 11), random.uniform(4, 11), 0)

        v = stars[i][2]

        unicornhathd.set_pixel(stars[i][0], stars[i][1], v, v, v)

      unicornhathd.show()

except KeyboardInterrupt:
    unicornhathd.off()  
