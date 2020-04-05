"""
CP1404 Practical
a program that allows you to look up hexadecimal colour codes
#note the program currently only has 10 colours.
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "Aquamarine1": "#7fffd4", "beige": "#f5f5dc",
                "Black": "#000000", "BlanchedAlmond": "#ffebcd", "CornflowerBlue": "#6495ed",
                "DarkGreen": "#006400", "DarkKhaki": "#bdb76b", "DarkViolet": "#9400d3", "LimeGreen": "#32cd32"}

colour_name = input("Enter a colour name:  ")
while colour_name != "":
    print("The Hexadecimal Colour Code for {} is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a Colour name:  ")
    #if COLOUR_CODES.get(colour_name) != "None":
    #   print("The Hexadecimal Colour Code for {} is {}".format(colour_name,COLOUR_CODES.get(colour_name)))
    #else:
    #    print("That colour cannot be found")
    #colour_name = input("Enter a Colour name:  ")
