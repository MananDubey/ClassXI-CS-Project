def square(side, choice):
    def area():
        return side * side

    def perimeter():
        return side * 4

    if choice == "area" or choice == "a":
        return area()

    if choice == "perimeter" or choice == "p":
        return perimeter()

    if choice == "both" or choice == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def circle(radius, choice):
    def area():
        return 3.14 * (radius ** 2)

    def perimeter():
        return 2 * 3.14 * radius

    if choice == "area" or choice == "a":
        return area()

    if choice == "perimeter" or choice == "p":
        return perimeter()

    if choice == "both" or choice == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def triangle(side, choice):
    def area():
        pass

    def perimeter():
        pass

    if choice == "area" or choice == "a":
        return area()

    if choice == "perimeter" or choice == "p":
        return perimeter()

    if choice == "both" or choice == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def rectangle(length, breadth, choice):
    def area():
        pass

    def perimeter():
        pass

    if choice == "area" or choice == "a":
        return area()

    if choice == "perimeter" or choice == "p":
        return perimeter()

    if choice == "both" or choice == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())

    
def trapezieum(choice):
    def volume():
        pass

    def surface_area():
        pass

    if choice == "volume" or choice == "v":
        return volume()

    if choice == "surface_area" or choice == "sa":
        return surface_area()

    if choice == "both" or choice == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def quadrilateral(side1, side2, side3, side4, choice):
    def area():
        pass

    def perimeter():
        pass

    if choice == "area" or choice == "a":
        return area()

    if choice == "perimeter" or choice == "p":
        return perimeter()

    if choice == "both" or choice == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def n_sided(*sides, choice):
    def area():
        pass

    def perimeter():
        pass

    if choice == "area" or choice == "a":
        return area()

    if choice == "perimeter" or choice == "p":
        return perimeter()

    if choice == "both" or choice == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def cube(choice):
    def volume():
        pass

    def surface_area():
        pass

    if choice == "volume" or choice == "v":
        return volume()

    if choice == "surface_area" or choice == "sa":
        return surface_area()

    if choice == "both" or choice == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def cuboid(choice):
    def volume():
        pass

    def surface_area():
        pass

    if choice == "volume" or choice == "v":
        return volume()

    if choice == "surface_area" or choice == "sa":
        return surface_area()

    if choice == "both" or choice == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def sphere(choice):
    def volume():
        pass

    def surface_area():
        pass

    if choice == "volume" or choice == "v":
        return volume()

    if choice == "surface_area" or choice == "sa":
        return surface_area()

    if choice == "both" or choice == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def hemisphere(choice):
    def volume():
        pass

    def surface_area():
        pass

    if choice == "volume" or choice == "v":
        return volume()

    if choice == "surface_area" or choice == "sa":
        return surface_area()

    if choice == "both" or choice == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def pyramid(choice):
    def volume():
        pass

    def surface_area():
        pass

    if choice == "volume" or choice == "v":
        return volume()

    if choice == "surface_area" or choice == "sa":
        return surface_area()

    if choice == "both" or choice == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())



def cone(choice):
    def volume():
        pass

    def surface_area():
        pass

    if choice == "volume" or choice == "v":
        return volume()

    if choice == "surface_area" or choice == "sa":
        return surface_area()

    if choice == "both" or choice == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())
