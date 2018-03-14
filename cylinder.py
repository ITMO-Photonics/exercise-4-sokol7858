### ---------------------------------------------------------------------
### Exercise-4: Write a Python script which calculates volume
###       and surface area of a cylinder of radius R and length L.
### ---------------------------------------------------------------------
import math # use math.pi from this module

# Function for calculation of volume of a cylinder
def cylinder_volume(R, L):
    return math.pi*(R**2)*L

# Function for calculation of surface area of a cylinder
def cylinder_area(R, L):
    return 2*math.pi*(R**2)*2*math.pi*R*L

