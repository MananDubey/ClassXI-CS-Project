# TODO: add formulae
# TODO: add more shapes and remove weird shapes
# TODO: GUI popups

def square(side, choice_2d):
    def area():
        return side * side

    def perimeter():
        return side * 4

    if choice_2d == "area" or choice_2d == "a":
        return area()

    if choice_2d == "perimeter" or choice_2d == "p":
        return perimeter()

    if choice_2d == "both" or choice_2d == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def circle(radius, choice_2d):
    def area():
        return 3.14 * (radius ** 2)

    def perimeter():
        return 2 * 3.14 * radius

    if choice_2d == "area" or choice_2d == "a":
        return area()

    if choice_2d == "perimeter" or choice_2d == "p":
        return perimeter()

    if choice_2d == "both" or choice_2d == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def triangle(side, choice_2d):
    def area():
        pass

    def perimeter():
        pass

    if choice_2d == "area" or choice_2d == "a":
        return area()

    if choice_2d == "perimeter" or choice_2d == "p":
        return perimeter()

    if choice_2d == "both" or choice_2d == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def rectangle(length, breadth, choice_2d):
    def area():
        pass

    def perimeter():
        pass

    if choice_2d == "area" or choice_2d == "a":
        return area()

    if choice_2d == "perimeter" or choice_2d == "p":
        return perimeter()

    if choice_2d == "both" or choice_2d == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def trapezium(choice_2d):
    def volume():
        pass

    def surface_area():
        pass

    if choice_2d == "volume" or choice_2d == "v":
        return volume()

    if choice_2d == "surface_area" or choice_2d == "sa":
        return surface_area()

    if choice_2d == "both" or choice_2d == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def quadrilateral(side1, side2, side3, side4, choice_2d):
    def area():
        pass

    def perimeter():
        pass

    if choice_2d == "area" or choice_2d == "a":
        return area()

    if choice_2d == "perimeter" or choice_2d == "p":
        return perimeter()

    if choice_2d == "both" or choice_2d == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def n_sided(*sides, choice_2d):
    def area():
        pass

    def perimeter():
        pass

    if choice_2d == "area" or choice_2d == "a":
        return area()

    if choice_2d == "perimeter" or choice_2d == "p":
        return perimeter()

    if choice_2d == "both" or choice_2d == "b":
        return "area: " + str(area()) + " Perimeter: " + str(perimeter())


def cube(choice_3d):
    def volume():
        pass

    def surface_area():
        pass

    if choice_3d == "volume" or choice_3d == "v":
        return volume()

    if choice_3d == "surface_area" or choice_3d == "sa":
        return surface_area()

    if choice_3d == "both" or choice_3d == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def cuboid(choice_3d):
    def volume():
        pass

    def surface_area():
        pass

    if choice_3d == "volume" or choice_3d == "v":
        return volume()

    if choice_3d == "surface_area" or choice_3d == "sa":
        return surface_area()

    if choice_3d == "both" or choice_3d == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def sphere(choice_3d):
    def volume():
        pass

    def surface_area():
        pass

    if choice_3d == "volume" or choice_3d == "v":
        return volume()

    if choice_3d == "surface_area" or choice_3d == "sa":
        return surface_area()

    if choice_3d == "both" or choice_3d == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def hemisphere(choice_3d):
    def volume():
        pass

    def surface_area():
        pass

    if choice_3d == "volume" or choice_3d == "v":
        return volume()

    if choice_3d == "surface_area" or choice_3d == "sa":
        return surface_area()

    if choice_3d == "both" or choice_3d == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def pyramid(choice_3d):
    def volume():
        pass

    def surface_area():
        pass

    if choice_3d == "volume" or choice_3d == "v":
        return volume()

    if choice_3d == "surface_area" or choice_3d == "sa":
        return surface_area()

    if choice_3d == "both" or choice_3d == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


def cone(choice_3d):
    def volume():
        pass

    def surface_area():
        pass

    if choice_3d == "volume" or choice_3d == "v":
        return volume()

    if choice_3d == "surface_area" or choice_3d == "sa":
        return surface_area()

    if choice_3d == "both" or choice_3d == "b":
        return "area: " + str(volume()) + " Perimeter: " + str(surface_area())


square(5, "b")
if __name__ == "__main__":
    shapes = list(str(i).split()[1].capitalize() for i in globals().values() if type(i) == type(square))

    import inspect
    import tkinter
    from tkinter import *
    from tkinter import ttk

    entries = []
    labels = []
    checkboxes = []


    def window_manager(event):
        for entry in entries:
            entry.destroy()
        entries.clear()
        for label in labels:
            label.destroy()
        labels.clear()
        for checkbox in checkboxes:
            checkbox.destroy()
        checkboxes.clear()
        area_value.set(0)
        perimeter_value.set(0)
        volume_value.set(0)
        surface_area_value.set(0)
        pos_y = 45
        params = "".join(i for i in str(inspect.signature(globals()[event.widget.get().lower()]))
                         if i.isalnum() or i == " " or i == "_").split()
        for i in params:
            if i == "choice_2d":
                area_checkbox = Checkbutton(window, text="area", onvalue=1, offvalue=0, variable=area_value)
                area_checkbox.place(x=250, y=45)
                checkboxes.append(area_checkbox)
                perimeter_checkbox = Checkbutton(window, text="perimeter", variable=perimeter_value, onvalue=1,
                                                 offvalue=0)
                perimeter_checkbox.place(x=250, y=80)
                checkboxes.append(perimeter_checkbox)
                continue
            if i == "choice_3d":
                volume_checkbox = Checkbutton(window, text="volume", variable=volume_value, onvalue=1, offvalue=0)
                volume_checkbox.place(x=250, y=45)
                checkboxes.append(volume_checkbox)
                surface_area_checkbox = Checkbutton(window, text="surface area", variable=surface_area_value,
                                                    onvalue=1, offvalue=0)
                surface_area_checkbox.place(x=250, y=80)
                checkboxes.append(surface_area_checkbox)
                continue
            if i == "sides":
                continue
            entry = tkinter.Entry(window, relief="groove")
            label = Label(window, text="Enter {}:".format(i))
            label.place(x=10, y=pos_y, height=25)
            entry.place(x=100, y=pos_y, width=60, height=25)
            pos_y += 35
            entries.append(entry)
            labels.append(label)


    def calculate():
        if shape_combo is not None and (i.get for i in entries) is not None \
                and (area_value.get() or perimeter_value.get() or surface_area_value.get() or volume_value.get()):
            parameters = []
            for entry in entries:
                if entry.get is not None:
                    parameters.append(entry.get())
                else:
                    # TODO: make a error popup
                    return

            if "".join(i for i in str(inspect.signature(globals()[shape_combo.get().lower()]))
                       if i.isalnum() or i == " " or i == "_").split()[-1] == "choice_2d":
                if area_value.get() and perimeter_value.get():
                    parameters.append("b")
                elif area_value.get():
                    parameters.append("a")
                elif perimeter_value.get():
                    parameters.append("p")
                else:
                    parameters.append("b")

            else:
                if volume_value.get() and surface_area_value.get():
                    parameters.append("b")
                elif volume_value.get():
                    parameters.append("v")
                elif surface_area_value.get():
                    parameters.append("sa")
                else:
                    parameters.append("b")

            # TODO : add a results popup
            globals()[shape_combo.get().lower()](*parameters)


    # Init
    window = Tk()
    window.title = "calc"
    window.geometry("400x300+50+50")
    window.resizable(False, True)
    area_value = IntVar()
    perimeter_value = IntVar()
    volume_value = IntVar()
    surface_area_value = IntVar()

    # ComboBox
    shape_combo = ttk.Combobox(window, values=shapes)
    shape_combo.set("Select a shape")
    shape_combo['state'] = "readonly"
    shape_combo.place(x=10, y=10, width=200, height=25)
    shape_combo.bind('<<ComboboxSelected>>', window_manager)

    # Calculate Button
    calculate_button = Button(window, text='Calculate', height=1, command=calculate, relief="groove")
    calculate_button.place(x=330, y=260, width=60, height=30)

    # MainLoop
    window.mainloop()
