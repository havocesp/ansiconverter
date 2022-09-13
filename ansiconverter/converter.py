""" Convert any color to the ANSI format to write in colors in your terminal."""

RESET = "\x1b[0m"


# class converter:
"""ANSI conversions and an additional function to convert RGB to HEX."""

RESET = "\x1b[0m"


def RGBtoANSI(
    text: str,
    foregound=[255, 255, 255],
    background=[],
):
    """Write a text in RGB color.

    Args:
        text (str): the text you want to write.
        foregound (list, optional): RGB foregound's color. Defaults to [255, 255, 255].
        background (list, optional): RGB background's color. Defaults to [].

    Raises:
        ValueError: the foregound color can't be an empty list.

    Returns:
        string: the ANSI code for the foreground and the background.
    """
    if foregound != []:
        if background == []:
            return f"\x1B[38;2;{foregound[0]};{foregound[1]};{foregound[2]}m{str(text)}{RESET}"
        else:
            return f"\x1B[38;2;{foregound[0]};{foregound[1]};{foregound[2]}m\x1B[48;2;{background[0]};{background[1]};{background[2]}m{str(text)}{RESET}"
    else:
        raise ValueError(
            "The foregound can't be an empty list!\nNo paramaters will write the text in write"
        )


def HEXtoRGB(fg="#000000"):
    """Convert a hexadecimal color to its RGB triplet.

    Args:
        fg (str, optional): Hexadecimal color value. Defaults to "#000000".

    Raises:
        ValueError: The color is not a correct hexadecimal value.

    Returns:
        list: triplet of RGB values.
    """
    foreground = ""
    while True:
        foreground = fg.lstrip("#").lower()
        if len(foreground) == 6:
            return list(int(foreground[i : i + 2], base=16) for i in (0, 2, 4))

        else:
            raise ValueError("Enter a valid hexadecimal value")
            return 1


def HEXtoANSI(text, foreground, background):
    foregroundRGB = HEXtoRGB(foreground)
    backgroundRGB = HEXtoRGB(background)
    return RGBtoANSI(text, foregroundRGB, backgroundRGB)


# Utility to convert to other color format


def RGBtoHEX(rgb=[255, 255, 255]):
    if rgb != []:
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
    else:
        raise (ValueError(f"The color can't be an empty list. Please retry."))