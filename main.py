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
    import ctypes

    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)  # Hide python console window
    import inspect
    import tkinter
    from base64 import b64decode
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
            entry.place(x=150, y=pos_y, width=60, height=25)
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
    try:
        photo = PhotoImage(file="icon.png")
        window.iconphoto(False, photo)
    except:
        image_bytes = b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAAD0eNT6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0"
            "RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAACAASURBVHic7d15lN11ff/x1zCTDQgkhLAlbAGSkAQCCGEJELaiIaCt"
            "C6C4lKrYuvRXi21/tke00t/PatX21OUn7gqiqFiXEBYlICYqhgoJCZCwGyAhQNgSIMlM5vfHYFWEEDLfO9977+fxOCcnOcC8v2/u"
            "5Nzvc7536wh1GZVkQpKJScY/+2vXJNs8+2vks78PrmtBgH5an2Rtkkef/X1tkhVJliVZmuS2Z//8SF0Llqyj7gUKsnOSY5OclORP"
            "kuxd7zoATWNFknlJfpLkiiS/qXedMgiAxpqQ5E1JXvvsnwF4cbcmuTTJhem7QkADCIDq7ZDk9ek78R9e8y4Are6X6QuBbyVZXfMu"
            "bUUAVGfnJO9N8p4kW9e8C0C7WZfka0nOT3Jfzbu0BQHQf3ul78R/TpKh9a4C0PbWJ7kkfSFwe827tDQBsOWGJ/lQkr9O0lXvKgDF"
            "2ZDkP5J8OMmamndpSZ11L9CiTksyO8krkmxV8y4AJepMMj3Jnyd5OMnCWrdpQa4AvDS7J/likpPrXgSAP3BFkrfH8wM2mwDYfCcl"
            "uSh9T/YDoPk8nOQtSebUvUgr8BDAi+tKcl6SL6TvcX8AmtPWSd6QvpdjX51kY73rNDdXADZtdJLvJzmq7kUAeEnmJfmz9F0V4HkI"
            "gBe2Z5Ir4x38AFrVbUleHm8t/Lw8g/35TUpfPTr5A7Suiel7J8GpdS/SjATAHzsifSf/sXUvAkC/7Zpkbrw1+x/xEMAfmpzkuvQ9"
            "gQSA9vF4khnxfgH/QwD8zu5J5j/7OwDt54H0vXnQPTXv0RQ8BNBnxyRXxckfoJ3tluTHSXaqe5FmIACSQUl+kL4niwDQ3vZN8t34"
            "DBdvBJTko0nOqHsJAAbMnun74e/quhepU+nPATg1yQ9T4+0weMjQ7DXxgIzZe7/stOvuGT1m92y73YgM22bbDB4yLJ1dxUcq0KJ6"
            "uruzft3TeXrtmqx5/NE89MB9WbViee6/a1nuXnpzNqxbV+d6G5PMSt9nCBSp5ADYPcmNSUYN9IG33X5kDp5+Yg6Ydkx2329iOjud"
            "5IGy9HR35zd33Jqbr78uN82fmzVPPFbHGg8lOTjJ/XUcvG4lB8CVGeBP9Ru3/4E59tTTM/Ggadmq06MvAEnS09OdpTf9Ktf+6JLc"
            "c9vigT78nPRdCShOqQHwuiTfHqiD7TNpak4+/ezsPfGAgTokQEu665aFueo7X81dty4ayMO+Osl/DeQBm0GJATA8ya1JxjT8QCN2"
            "yClveHsOOeZP0tFR4k0NsGUW/fKn+f5XPpU1jz86EIdbnr63gF8zEAdrFiVeh/5I+j4coqEOOPzYvO0fP5o99tvfyR/gJdp57F6Z"
            "dsLMPLzivqx6oOGf5bN9+s6HP2n0gZpJaWemcUmWpoGv/+waNCinvemvcuTJr2rUIQCK0dvbm/lX/lcuu+iC9HR3N/JQ65OMT3Jv"
            "Iw/STEq7AvDRJIc1avjgocPylvd9OAcddUKjDgFQlI6Ojuyx7/7Za8KULFkwL93dGxp1qM70vTfAnEYdoNmUdAVgTJI7kwxpxPBt"
            "thuRt/7vj2TsuPGNGA9QvOV3Ls2X//X9Wfvk4406xDPpu1K8olEHaCYlXQE4P30fAlG5IcO2ztv/6WNO/gANtP0OO2bfKQflpp9f"
            "k57GXAn47cPDVzVieLMpJQBGJbkofZd3KtU1aFDO/vv/k70mTKl6NADPsd3IHTN23Pgs/MW16d24sRGHmJrk/6XvakBbKyUA/iJJ"
            "Q56V96o/f3emHnlcI0YD8DxG7bxbhgzdOssWLmjE+MHp+7jgGxoxvJmU8mmAb2rE0AMOP9az/QFqcPTMV2fKYUc3anxDzhnNpoQA"
            "mJDk8KqHbjdiVF57zrlVjwVgM3R0dOR1f/m+bLvdiEaMPzLJfo0Y3ExKCICGlNysN70jw7bZthGjAdgMw7YZnllnvaMRozuSvLER"
            "g5tJCQHw2qoH7jNpag6efmLVYwF4iQ459k8a9TkrlZ87mk27B8Bu6XsIoFInn3521SMB2AIdHR05+XV/3ojR+yfZtRGDm0W7B0Dl"
            "P6aP2/9An+oH0ET2mXxQ9ppY+UuxO5IcX/XQZtLuAVD5N+/YU0+veiQA/TSjMffNbf2+7u0eAJV+87bdfmQmHjStypEAVGDiwYdn"
            "m+pfESAAWtQOSfascuAhR5+YrTpLee8kgNbR2dmVg46q/KLv3uk7l7Sldg6AiVUPnHLYMVWPBKAiU6Y15D66bT/kRQBspkFDhmT3"
            "fStvCgAqstf4yRk0pPIPfK38lWTNop0DoNJq23vigens6nrx/xCAWnR2dWWv8ZOrHisAWlCl37Sxe7f9u0ICtLyx4yo/XwuAFrRL"
            "lcNG77Z7leMAaIDRu46teuTOVQ9sFu0cAJW+UX8D/lIBULEG/LA2vOqBzaKdA6DSb9rwkaOqHAdAAwwfUfmr9gRAC6r0mzZk6NZV"
            "jgOgAYYMq/y+WgC0oEofAhgydFiV4wBogAb8sCYAWtDgKod5CSBA8+saNKjqkZW/sUCzaOcAAABegAAAgAIJAAAokAAAgAIJAAAo"
            "kKe2t5Ge7u4sXjAvS26Yn/vvvj2PP/JQ1q97pu61gBY1eMjQbD9qdMbsvV8mHzo9Uw472iui2ojvZJu4+frrctk3Pp/Vq1bUvQrQ"
            "JtaveyYPPbA8Dz2wPDfNn5tRO++WWWedkynTjql7NSrgIYAWt3Hjxsy+6HO58N//2ckfaKhHHnwgX//kh3LZRRekt7e37nXoJwHQ"
            "4uZc/PlcN/s7da8BFOSns7+dy7/5hbrXoJ8EQAu7+frrnPyBWlz7w0uyZMH8utegHwRAi+rp7s6cixU4UJ8fXfjZ9HR3170GW0gA"
            "tKjFC+blkQcfqHsNoGCrV63MkhtcBWhVAqBFLVkwr+4VAARACxMALeq+u5bVvQKA+6IWJgBa1BOPra57BYA8vvrhuldgCwmAFrX+"
            "mafrXgHAfVELEwAAUCABAAAFEgAAUCABAAAFEgAAUCABAAAFEgAAUCABAAAFEgAAUKCuuhegOSxZ9f66VwAGyOSdPlL3CjQBVwAA"
            "oEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEAC"
            "AAAKJAAAoEBddS8A0I42rO/JT+Ysy9wrluXWRQ9m5QNPJEl22W277H/gzjlx5vicOHN8Bg3urHlTSiUAACr249lL8/F/npv77n3s"
            "j/7d3Xc8krvveCRzvndLdt9rZN73weNz0qwJNWxJ6TwEAFCRnp7e/NuH5uZv/uJ7z3vyf67l9zya/3X29/LxD83Nxo29A7Ah/I4A"
            "AKjIJ8+/Jl/97PUv+eu+8tnr8x//cm31C8EmCACACvx49tItOvn/1pc+/ctcffmyCjeCTRMAAP20YX1PPvHha/o952MfuDob1vdU"
            "sBG8OAEA0E8/mbMsy+95tN9z7vvNY5l7xe0VbAQvTgAA9NPcCi/dz73CwwAMDAEA0E9LFq6sbtZN1c2CTREAAP300INrKpv14Ion"
            "K5sFmyIAAPrpqbXrm3IWbIoAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIAC"
            "CQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQCAftp6m8GVzdp2+JDKZsGmCACAftppl20rmzW6"
            "wlmwKQIAoJ8mTd2lsllTpu5a2SzYFAEA0E8nzhxf2awTZu5X2SzYFAEA0E8nnTIhe+w9st9zxu45Ise/XAAwMAQAQD91Ddoq5553"
            "fL/n/MP5J2XQ4M4KNoIXJwAAKnDSrAk5+52Hb/HXv/U9R+SEV/jpn4EjAAAq8rfnHZ+/eNcRL/nr3vruI/I3/3Rc9QvBJggAgIps"
            "tVVHzv3g8fnPr71ms54TsMfeI/Opr782f3ve8dlqq44B2BB+p6vuBQDazYkzx2fGSfvm6suXZe4Vy7Jk4co8+MCTSZKddxueyVN3"
            "yYkzx+eEV4xP1yA/h1EPAQDQAF2DtsrLXzkxL3/lxLpXgeclPQGgQAIAAAokAACgQAIAAAokAACgQAIAAAokAACgQAIAAAokAACg"
            "QAIAAAokAACgQAIAAAokAACgQAIAAAokAACgQAIAAAokAACgQAIAAAokAACgQF11L0BzmLzTR+peAYAB5AoAABRIAABAgQQAABRI"
            "AABAgQQAABRIAABAgQQAABRIAABAgQQAABRIALSowUOH1b0CQIYO27ruFdhCAqBFbT9yVN0rAGS7kTvWvQJbSAC0qDHjxte9AkDG"
            "7uO+qFUJgBY1+dDpda8A4L6ohQmAFjVl2tEZtcuYutcACrbDTrtm0suOqnsNtpAAaFGdnV2Z9Ya3170GULDT3vxX6ezyqfKtSgC0"
            "sCnTjsmMU0+vew2gQMe98kyX/1ucAGhxp5x1TmacdkbdawAFOe6VZ2Tm699W9xr0k2s3La6joyOzzjone42fnNnfuCCPrLy/7pWA"
            "NjVqlzE59Y3v8JN/mxAAbWLyYdMz8ZDDs2TB/Cy5YX7uv+v2PLb6oax/5um6VwNa1OChwzJih9EZM26/TDns6Ew69Kh0djpttAvf"
            "yTbS2dmVA4+YkQOPmFH3KgA0Oc8BAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAA"
            "AIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIACCQAAKJAAAIAC"
            "CQAAKFA7B8BTVQ0aNGRIVaMAoCm0cwCsqGrQ9iN3rGoUADSFdg6Am6satMse46oaBQBNoZ0D4IdVDZp86FFVjQKAptDOAfCdJCv7"
            "O2S7EaNywOHHVrAOADSPrroXaKA1ST6Y5IL+DDn5jLMzeMjQajZqsJ7u7ixeMC9Lbpif++++PY8/8lDWr3um7rWAFjV4yNBsP2p0"
            "xuy9XyYfOj1TDjs6nV3tfNooS0fdCzRYR5ILk5y1JV98yDEn5cx3vb/ajRrk5uuvy2Xf+HxWr6rsuY8Af2DUzrtl1lnnZMq0Y+pe"
            "ZZP+/swTqx7ZlufKtvyfeo6hSb6W5PSX8kVTjzwuZ7zzH9I1aHBjtqrIxo0bM+fiz+e62d+pexWgEDNOPT2nnHVOOjqa8xQiADZP"
            "CddynklyZpJfJjkvyYhN/cfDthmek17zphw989VN+5f79zn5AwPtp7O/nY6tOnLKG86pexX6oYQASJLeJP+e5OtJ3prkVUlelmRI"
            "knQNGpSx4yZk8qFH5bDjT8nW2w6vb9OX4Obrr3PyB2px7Q8vyZ77Tc7kw6bXvQpbqJQA+K1Hknzs2V9JMvqDn7901TbbbfKiQFPq"
            "6e7OnIu/UPcaQMF+dOFnM/Hgwz0xsEW188sAN8dDrXjyT5LFC+blkQcfqHsNoGCrV63Mkhvm170GW6j0AGhZSxbMq3sFAAHQwgRA"
            "i7rvrmV1rwDgvqiFCYAW9cRjq+teASCPr3647hXYQgKgRa1/5um6VwBwX9TCBAAAFEgAAECBBAAAFEgAAECBBAAAFEgAAECBBAAA"
            "FEgAAECBBAAAFMhnOJIkmX/zXXWv0JTmXjUnHzj33ZXNO+HkU3L+Jz5d2bx28oH3vSdzr7yssnnnf/xTOeHlsyqb106mHzCu7hVo"
            "Aq4AAECBBAAAFEgAAECBBAAAFEgAAECBBAAAFEgAAECBBAAAFEgAAECBSnwnwEOTvCrJYUnGfPLv3pbtdtgxe+wzMZMOPTJjx02o"
            "eT0AaLySAmBako8lmfH7/3Dl8ruzcvndWbZwQX7yvQuzz6SpOeWsd2T3fYQAAO2rlIcAzkkyL885+T+fO29ZmM+c957Mu+J7jd8K"
            "AGpSQgD8dZILkgza3C/Y2NOTH371MyIAgLbV7gFwbJJPbOkXz77wc7n7tpsrXAcAmkM7B0BHkn9PP57nsLGnJ9//yqfS29tb3VYA"
            "0ATaOQBenuSQ/g5Zce+dWbbohgrWAYDm0c4B8OqqBi1ZMK+qUQDQFNo5AKZXNeju2xZXNQoAmkI7B8CYqgY98ejDVY0CgKbQzgGw"
            "2S/7ezHd3RuqGgUATaGdA2BFVYO2H7ljVaMAoCm0cwDcVNWgXffcp6pRANAU2jkAflTVoEkvO7KqUQDQFNo5AL6d5L7+DtluxKgc"
            "ePiLfoQAALSUdg6Ap5N8uL9DTj7j7AwaMqSCdQCgebRzACTJF5J8eUu/+JBjTsq042dWuA4ANId2D4AkeVf6Hg54SaYeeVxee865"
            "DVgHAOq3xR+U00KeSXJmkl8kOS/JyE39x1tvOzwnvebNmf6KP0tHR8dA7AcAA66EAEiS3iT/keRrSd6a5FVJDksyJEm6Bg3K7vtM"
            "zKRDj8q040/JsG22rW9TABgApQTAbz2a5OPP/kqS0R/8/KWrttluRI0rAcDAK+E5AJvykJM/ACUqPQAAoEgCAAAKJAAAoEACAAAK"
            "JAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAAoEACAAAKJAAA"
            "oEBddS9Ac/jAue+ue4WmtOrBlZXOW7zw127rF7B40Y2VzvvW17+ca666vNKZ0E4EAEmSuVfNqXuFIqx6cKXbeoAsWXRjllQcFdBO"
            "SgyAaUn+NMnBScZ+8u/elu132DFj9t4vkw87OrvvM6Hm9QCg8UoKgGlJPp7kmN//hyuX352Vy+/O0oULMvf7F2fc/gdm1hv/UggA"
            "0NZKeRLgOUnm5Tkn/+dz162L8pnz3pNrf/itxm8FADUpIQDem+SCJIM29ws29vRkzsVfyLzLv9e4rQCgRu0eAMcl+bct/eLZF30u"
            "d926qLptAKBJtHMAbJXkk0k6t3TAxp6e/OCrn05vb291WwFAE2jnAJiZvmf698uKe+/M0oULKlgHAJpHOwfAq6satGTBvKpGAUBT"
            "aOcAOLKqQfcsXVLVKABoCu0cALtVNeiJRx+uahQANIV2DoDtqxr09No1VY0CgKbQzgEAALwAAQAABRIAAFAgAQAABRIAAFAgAQAA"
            "BRIAAFCgrroXoDmc/4lP171CU1qy8MZ86+tfqmze5AMPzplveWtl89rJJV//chYv/HVl8957+Ik5cuy4yua1k9Mv/ULdK9AEBABJ"
            "khNOPqXuFYqw8y67uq1fwDVXXZ4srG7eEWP3zusmHVLdwHZyad0L0Aw8BAAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIA"
            "AFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAg"
            "AQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAA"
            "BRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABRIAAFAgAQAABeqqewGaw9yr5tS9QlNasvDGSuc9uHKF2/oFrFq5"
            "ou4VoCgCgCTJB859d90rFGHJohvd1kBT8BAAABRIAABAgQQAABRIAABAgQQAABRIAABAgQQAABRIAABAgQQAABRIAABAgQQAABRI"
            "AABAgQQAABRIAABAgQQAABRIAABAgQQAABRIAABAgbrqXoDmcMLJp9S9QlNa9eDKLF7468rm7bTzLpky9ZDK5rWTxYtuzKqVK+pe"
            "A4ohAEiSnP+JT9e9QlOae9WcLD63ugCYMvUQt/UL+MD73pO5Ky+rew0ohocAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBA"
            "AgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAA"
            "CiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQA"
            "AKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACiQAAKBAAgAACtRV9wI0h+kHjKt7hSLMvWpO5rqtB8QZ"
            "l34xZ1z6xbrXgKblCgAAFEgAAECBBAAAFEgAAECBBAAAFEgAAECBBAAAFEgAAECBBAAAFEgAtKjBQ4fVvQJAhg7buu4V2EICoEVt"
            "P3JU3SsAZLuRO9a9AltIALSoMePG170CQMbu476oVQmAFjX50Ol1rwDgvqiFCYAWNWXa0Rm1y5i61wAKtsNOu2bSy46qew22kABo"
            "UZ2dXZn1hrfXvQZQsNPe/Ffp7PKp8q1KALSwKdOOyYxTT697DaBAx73yTJf/W5wAaHGnnHVOZpx2Rt1rAAU57pVnZObr31b3GvST"
            "azctrqOjI7POOid7jZ+c2d+4II+svL/ulYA2NWqXMTn1je/wk3+bEABtYvJh0zPxkMOzZMH8LLlhfu6/6/Y8tvqhrH/m6bpXA1rU"
            "4KHDMmKH0Rkzbr9MOezoTDr0qHR2Om20C9/JNtLZ2ZUDj5iRA4+YUfcqADQ5zwEAgAIJAAAokAAAgAIJAAAokAAAgAK1cwCsr3JY"
            "T3d3leMAaIDuDRuqHrmu6oHNop0DYE2Vw9Z5PT1A01v3zFNVj3yy6oHNop0DoNJvWgP+UgFQsXVPC4DNJQA2d9ijj1Q5DoAGePKx"
            "1ZWPrHpgsxAAm+mhFfdVOQ6ABnjogeVVjxQALWhllcNWVf+XCoCKNeC+utJzSTNp5wBYVuWw++++vcpxADTAfXdVetefJEurHtgs"
            "2jkAKv2m3X3boka8vASAinRv2JB7ly2peqwAaEGVftM2rFuX5XfeVuVIACp077Il2bC+8pftV35JoVm0cwBUfrZe/KufVT0SgIrc"
            "fP11jRjrCkALWp3knioH3jjv6vT0eEdAgGbT092dhb+4tuqxdyV5tOqhzaKdAyBJ5lY5bM0Tj2XpTb+qciQAFbjtxuuz9snHqx5b"
            "6Tmk2bR7AFxT+cAffLPqkQD0009nf7sRYwVAC7u66oH3Lrsld926qOqxAGyhOxb/OvcsXVz12N404IfIZtLuAbAiDXgy4FXf/kp6"
            "e3urHgvAS9Tb25srv/3VRoy+JW38JkBJ+wdAkny36oF33booN86r/OICAC/Rf//0yka89j9pwLmj2ZQQABc2Yujsiz6Xp9e27VtE"
            "AzS9p558Ipdd/IVGjO5NclEjBjeTEgJgWZLrqx665vFH863P/KuHAgBq0Nvbm+98/uNZ+8RjjRj/8yR3NGJwM+mse4EBMiTJKVUP"
            "fXjFfdl6+PDsse/+VY8GYBOuu+w7mX/FfzVq/P9N8t+NGt4sSrgCkCTfTPJUIwZfdtEFuf3mtv97AtA0brvpV7nim19q1Pi1SRry"
            "msJmU8oVgKeTjE5yRNWDezduzM2/ui77Tj44I0aNrno8AL9n+Z1L85WP/VO6N6xv1CH+M8kPGzW8mZQSAEmyOMm7knRVPXhjT09u"
            "ueHn2WfyQdl+hx2rHg9AkuV33JYvffT9eeaptY06xDNJzkyyplEHaCYlBcCTScYmObQRwzesX5eb5l+dMePGZ8ddxjTiEADFuv3m"
            "X+fLH/vHPLO2oefmz6WQy/9JWQGQJEuSvDMN+v/u6enOol9em6HDtsnu+05MR0dHIw4DUIze3t787LLv5juf+7dGfNTv71ufvp/+"
            "K/9AgWZVWgA8lmR4kumNOkDvxo1ZunBBVvzmzkyYemgGDR7SqEMBtLWnnnwiF//nv2T+ld9Pb+/GRh/uo0ka9rKCZlTij6hbp+8t"
            "Hvds+IG2HZ6Zr39bpp0wy9UAgM3U29ubX//sx7nsoguypjGv83+u3ySZlL5XABSj1LPSazKAb/O498QDcvLpZ2efSVMH6pAALemO"
            "JTfmyku+0qi3930hf5rkBwN5wGZQagAkyeVJXjGQB9xrwpTMOO30TDz48HR2Vv5iBICW1NPdndtuvD7X/uiSgT7xJ8nsJKcN9EGb"
            "QckBMDbJjUkG/HV722w3IgcddXymTDsme+43KV2DBg30CgC16t6wPvcuuyU3/+pnWfjza7L2yVqee7cqycFJHqjj4HUrOQCSZGaS"
            "y1Lj7TBo8JDsNWFyxo6bkNG7js3o3fbI8BEjM3TrbTNk6LB0drlSALSmnu7urHv6qTzz9No8+djqrLr/N3loxX25/+5luWfpkkY/"
            "q//FbEzfOeCqOpeoU+kBkCT/muQf6l4CgAH1L0k+UPcSdRIAfe8MeE2So+teBIAB8dMkJyXprnuROgmAPqOS/CyJj/UDaG+3JDkm"
            "yeq6F6mbAPidsUnmJ9mj7kUAaIj70/dGcPfWvUgzKOXjgDfHfel7QkjxVQjQhh5Pckqc/P+HAPhDt6TvL4gIAGgfq5O8PMmiuhdp"
            "Jh4CeH6TklyRZPe6FwGgX1ak703fnPyfQwC8sN3SFwEH1L0IAFvk1vSd/H9T9yLNyEMAL+yBJCek79UBALSWn6bv5d1O/i+gtI8D"
            "fqmeSnJhkt4kx8YVE4Bm15vkU0nelMI+3e+lckLbfCcmuSjJLnUvAsDzejjJm9P3YW+8CA8BbL6rkxyaZE7diwDwR2YnmRon/80m"
            "AF6a+5PMSvLKJPfUuwoA6btffkv6PtK3yE/121KeA7BlliX5Yvpuv2lxOwIMtPVJPprk9CQ31LxLS3Li2nIbkvwkydfTdzsemGRQ"
            "rRsBtL/1SS5O34n/u+m7L2YLeBJgdXZK8s4k702yXc27ALSbtUm+lORj6bvsTz8JgOqNTHJG+l6CF4nfUAAAAJNJREFUclTNuwC0"
            "st4kv0jfy7EvSfJoveu0FwHQWPsleWOS1ySZXPMuAK1icZJL0/fS6ztq3qVtCYCBs1OSGUlOSt+7U02qdx2AprEiybz0Pa/q8iTL"
            "612nDAKgPiOTTEgyMcn4Z/+8c5JtkwxPMuLZPw+ua0GAflqfZE2Sx5I8+eyfV6bvlVRLk9z27J9d2q/B/wen2LaQ9/IxDgAAAABJ"
            "RU5ErkJggg==")
        with open("icon.png", 'wb') as f:
            f.write(image_bytes)
        photo = PhotoImage(file="icon.png")
        window.iconphoto(False, photo)

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
