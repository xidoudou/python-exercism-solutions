COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]
RESISTORS = {
    "grey":"±0.05%",
    "violet":"±0.1%",
    "blue":"±0.25%",
    "green":"±0.5%",
    "brown":"±1%",
    "red":"±2%",
    "gold":"±5%",
    "silver":"±10%"
}
def c_index(color_str):
    return COLORS.index(color_str)

def r_value(color_key):
    return RESISTORS[color_key]

def format_num(num):
    if num == int(num):
        return str(int(num))
    else:
        return str(num)
    
def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    zeros = 10 ** (c_index(colors[-2]))
    i = 0
    value = 0
    for color in colors[-3::-1]:
        value += c_index(color) * (10**i)
        i += 1
    values = value * zeros

    resistor = r_value(colors[-1])
    if values >= 1_000_000_000:
        return f"{format_num(values / 1_000_000_000)} gigaohms {resistor}"
    elif values >= 1_000_000:
        return f"{format_num(values / 1_000_000)} megaohms {resistor}"
    elif values >= 1_000:
        return f"{format_num(values / 1_000)} kiloohms {resistor}"
    else:
        return format(values) + " ohms " + resistor

    