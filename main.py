# TODO: add more shapes
from math import sqrt


def square(side, choice_2d):
    def area():
        return side * side

    def perimeter():
        return side * 4

    if choice_2d == "area" or choice_2d == "a":
        return "Area: " + str(area())

    if choice_2d == "perimeter" or choice_2d == "p":
        return "Perimeter: " + str(perimeter())

    if choice_2d == "both" or choice_2d == "b":
        return "Area: " + str(area()) + "\nPerimeter: " + str(perimeter())


def circle(radius, choice_2d):
    def area():
        return 3.14 * (radius ** 2)

    def perimeter():
        return 2 * 3.14 * radius

    if choice_2d == "area" or choice_2d == "a":
        return "Area: " + str(area())

    if choice_2d == "perimeter" or choice_2d == "p":
        return "Perimeter: " + str(perimeter())

    if choice_2d == "both" or choice_2d == "b":
        return "Area: " + str(area()) + "\nPerimeter: " + str(perimeter())


def triangle(side1, side2, side3, choice_2d):
    def area():
        semi_perimeter = (side1 + side2 + side3) / 2
        return sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))

    def perimeter():
        return side1 + side2 + side3

    if choice_2d == "area" or choice_2d == "a":
        return "Area: " + str(area())

    if choice_2d == "perimeter" or choice_2d == "p":
        return "Perimeter: " + str(perimeter())

    if choice_2d == "both" or choice_2d == "b":
        return "Area: " + str(area()) + "\nPerimeter: " + str(perimeter())


def rectangle(length, breadth, choice_2d):
    def area():
        return length * breadth

    def perimeter():
        return 2 * (length + breadth)

    if choice_2d == "area" or choice_2d == "a":
        return "Area: " + str(area())

    if choice_2d == "perimeter" or choice_2d == "p":
        return "Perimeter: " + str(perimeter())

    if choice_2d == "both" or choice_2d == "b":
        return "Area: " + str(area()) + "\nPerimeter: " + str(perimeter())


def trapezium(side1, side2, side3, side4, height, choice_2d):
    def area():
        return ((side1 + side3) * height) / 2

    def perimeter():
        return side1 + side2 + side3 + side4

    if choice_2d == "area" or choice_2d == "a":
        return "Area: " + str(area())

    if choice_2d == "perimeter" or choice_2d == "p":
        return "Perimeter: " + str(perimeter())

    if choice_2d == "both" or choice_2d == "b":
        return "Area: " + str(area()) + "\nPerimeter: " + str(perimeter())


def cube(side, choice_3d):
    def volume():
        return side ** 3

    def surface_area():
        return 6 * (side ** 2)

    if choice_3d == "volume" or choice_3d == "v":
        return "Volume: " + str(volume())

    if choice_3d == "surface_area" or choice_3d == "sa":
        return "Surface Area: " + str(surface_area())

    if choice_3d == "both" or choice_3d == "b":
        return "Volume: " + str(volume()) + "\nSurface Area: " + str(surface_area())


def cuboid(length, breadth, height, choice_3d):
    def volume():
        return length * breadth * height

    def surface_area():
        return 2 * (length * breadth + breadth * height + length * height)

    if choice_3d == "volume" or choice_3d == "v":
        return "Volume :" + str(volume())

    if choice_3d == "surface_area" or choice_3d == "sa":
        return "Surface Area: " + str(surface_area())

    if choice_3d == "both" or choice_3d == "b":
        return "Volume: " + str(volume()) + "\nSurface Area: " + str(surface_area())


def sphere(radius, choice_3d):
    def volume():
        return 4 / 3 * 3.14 * radius ** 3

    def surface_area():
        return 4 * 3.14 * radius ** 2

    if choice_3d == "volume" or choice_3d == "v":
        return "Volume :" + str(volume())

    if choice_3d == "surface_area" or choice_3d == "sa":
        return "Surface Area: " + str(surface_area())

    if choice_3d == "both" or choice_3d == "b":
        return "Volume: " + str(volume()) + "\nSurface Area: " + str(surface_area())


def hemisphere(radius, choice_3d):
    def volume():
        return 2 / 3 * 3.14 * radius ** 3

    def surface_area():
        return 3 * 3.14 * radius ** 2

    if choice_3d == "volume" or choice_3d == "v":
        return "Volume :" + str(volume())

    if choice_3d == "surface_area" or choice_3d == "sa":
        return "Surface Area: " + str(surface_area())

    if choice_3d == "both" or choice_3d == "b":
        return "Volume: " + str(volume()) + "\nSurface Area: " + str(surface_area())


def pyramid(base_length, base_width, pyramid_height, choice_3d):
    def volume():
        return (base_length * base_width * pyramid_height) / 3

    def surface_area():
        return base_length * sqrt(((base_width / 2) ** 2) + pyramid_height ** 2 + base_width) + base_width * sqrt(
            ((base_length / 2) ** 2) + pyramid_height ** 2)

    if choice_3d == "volume" or choice_3d == "v":
        return "Volume :" + str(volume())

    if choice_3d == "surface_area" or choice_3d == "sa":
        return "Surface Area: " + str(surface_area())

    if choice_3d == "both" or choice_3d == "b":
        return "Volume: " + str(volume()) + "\nSurface Area: " + str(surface_area())


def cone(radius, height, choice_3d):
    def volume():
        return (3.14 * height * (radius ** 2)) / 3

    def surface_area():
        return 3.14 * radius * (radius + sqrt((height ** 2) + (radius ** 2)))

    if choice_3d == "volume" or choice_3d == "v":
        return "Volume :" + str(volume())

    if choice_3d == "surface_area" or choice_3d == "sa":
        return "Surface Area: " + str(surface_area())

    if choice_3d == "both" or choice_3d == "b":
        return "Volume: " + str(volume()) + "\nSurface Area: " + str(surface_area())


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

            entry = tkinter.Entry(window, relief="groove")
            label = Label(window, text="Enter {}:".format(i))
            label.place(x=10, y=pos_y, height=25)
            entry.place(x=100, y=pos_y, width=60, height=25)
            pos_y += 35
            entries.append(entry)
            labels.append(label)


    def calculate():
        if shape_combo is not None and (area_value.get() or perimeter_value.get() or surface_area_value.get() or
                                        volume_value.get()):
            parameters = []
            for entry in entries:
                try:
                    parameters.append(int(entry.get()))
                except ValueError:
                    empty_value_error_popup = Toplevel(window)
                    empty_value_error_popup.title("Error")
                    Label(empty_value_error_popup, text="All values have not been filled").pack(padx=20, pady=20)

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

            result_popup = Toplevel(window)
            result_popup.title("Result")
            Label(result_popup, text=globals()[shape_combo.get().lower()](*parameters)).pack(padx=20, pady=20)
        else:
            option_error_popup = Toplevel(window)
            option_error_popup.title("Error")
            Label(option_error_popup, text="You need to select at least one option to calculate").pack(padx=20, pady=20)


    # Init
    window = Tk()
    window.title("Calculator")
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
