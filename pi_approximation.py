import math
import random

#global functions used later
radius = 1.0
area_square = 4.0

#this generates a random dart position
def dart_thrown(radius):
    return (random.uniform(-radius, radius),
            random.uniform(-radius, radius))

#checks if dart is/isn't in circle
def inside_circle(x, y, radius):
    return math.sqrt(x**2 + y**2) < radius

num_of_throws = int(input("Throw some darts! \nHigher values yeild more accurate results: "))

#loop shows how darts are thrown
throw_count = 0
hit_count = 0

while throw_count < num_of_throws:      #creates and throws specified number of darts
    x, y = dart_thrown(radius)          #
    throw_count += 1                    #

    in_circle = inside_circle(x, y, radius)         #checks if dart is in circle
    hit_count += in_circle                          #

pi = (hit_count / throw_count) * area_square        #calculations for pi estimate

#lets user pick the amount of darts thrown and prints...
#... different results depending on the integer entered
if 100 <= num_of_throws <= 100000:
    print(f'Throws: {num_of_throws}, PI: {pi:.4f}')

elif 0 < num_of_throws < 100:
    print("You can throw more than that! \nTry throwing more (between 100 & 100000).")
    
elif num_of_throws > 100000:
    print("That's a lot of darts! \nTry throwing less (between 100 & 100000).")

print("Invalid integer. You can throw negative darts. \nTry throwing between 100 & 100000 darts.")

else:
    print("Something went wrong, try again")
    