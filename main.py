from draw_turtle import DrawTurtle

x_pos = -260
y_pos = -250
colors = ("yellow", "deeppink", "indianred", "lightcoral", "salmon", "darksalmon", "lightsalmon",
          "crimson", "red", "firebrick", "darkred", "pink", "lightpink", "deeppink", "mediumvioletred",
          "palevioletred", "lightsalmon", "coral", "tomato", "orangered", "darkorange", "orange", "gold",
          "lightyellow", "lemonchiffon", "papayawhip", "moccasin", "peachpuff", "palegoldenrod", "khaki",
          "darkkhaki", "lavender", "thistle", "plum", "violet", "orchid", "fuchsia", "magenta", "mediumorchid",
          "blueviolet", "darkviolet", "darkorchid", "darkmagenta", "purple", "indigo", "slateblue", "darkslateblue",
          "mediumslateblue", "greenyellow", "chartreuse", "lawngreen", "lime", "limegreen", "palegreen", "lightgreen",
          "springgreen", "mediumseagreen", "seagreen", "forestgreen", "green", "darkgreen","yellowgreen", "olivedrab",
          "olive", "darkolivegreen", "mediumaquamarine", "darkseagreen", "lightseagreen","darkcyan", "teal", "aqua",
          "cyan", "lightcyan", "paleturquoise", "aquamarine", "turquoise", "mediumturquoise","darkturquoise",
          "cadetblue", "steelblue", "lightsteelblue", "powderblue", "lightblue", "skyblue","lightskyblue",
          "dodgerblue", "cornflowerblue", "mediumslateblue", "royalblue", "mediumblue","darkblue",
          "navy", "midnightblue", "cornsilk", "blanchedalmond", "bisque", "navajowhite", "burlywood", "tan",
          "rosybrown", "sandybrown", "darkgoldenrod", "peru", "chocolate", "saddlebrown", "sienna",
          "brown", "maroon", "black", "white", "snow", "honeydew", "mintcream", "azure", "aliceblue", "ghostwhite",
          "seashell", "beige", "oldlace", "floralwhite", "ivory", "antiquewhite", "linen", "mistyrose")


shape = "circle"
size_screen = (500, 500)


my_drawing = DrawTurtle(x_pos_init=x_pos,
                        y_pos_init=y_pos,
                        color=colors,
                        shape=shape,
                        size_screen=size_screen)


my_drawing.show_screen()
my_drawing.full_screen(50, 50)
