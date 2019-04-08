COLOURS = {"black": "#000000", "bisque1": "#ffe4c4", "blue1": "#0000ff", "blue4": "#00008b", "azure3": "#c1cdcd",
           "BlueViolet": "#8a2be2", "brown2": "#ee3b3b", "CadetBlue": "#5f9ea0", "brown4": "#8b2323",
           "CadetBlue2": "#8ee5ee"}
colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in COLOURS:
        print(colour, "is", COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").lower()
