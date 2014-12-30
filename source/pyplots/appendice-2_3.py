# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


def cm2inch(value):
    return value/2.54

data = {
    0: 0.00,
    1: 1.00,
    2: 1.91,
    3: 2.74,
    4: 3.50,
    5: 4.19,
    6: 4.82,
    7: 5.40,
    8: 5.92,
    9: 6.40,
    10: 6.84,
    11: 7.24,
    12: 7.60,
    13: 7.93,
    14: 8.23,
    15: 8.51,
    16: 8.76,
    17: 8.99,
    18: 9.19,
    19: 9.38,
    20: 9.56,
    21: 9.72,
    22: 9.86,
    23: 9.99,
    24: 10.11,
    25: 10.22,
    26: 10.32,
    27: 10.41,
    28: 10.49,
    29: 10.57,
    30: 10.64,
    31: 10.70,
    32: 10.76,
    33: 10.81,
    34: 10.86,
    35: 10.90,
    36: 10.94,
    37: 10.98,
    38: 11.01,
    39: 11.04,
    40: 11.07,
    41: 11.09,
    42: 11.12,
    43: 11.14,
    44: 11.16,
    45: 11.17,
    46: 11.19,
    47: 11.20,
    48: 11.22,
    49: 11.23,
    50: 11.24,
    51: 11.25,
    52: 11.26,
    53: 11.27,
    54: 11.28,
    55: 11.28,
    56: 11.29,
    57: 11.29,
    58: 11.30,
    59: 11.30,
    60: 11.31,
    61: 11.31,
    62: 11.32,
    63: 11.32,
    64: 11.32,
    65: 11.33,
    66: 11.33,
    67: 11.33,
    68: 11.33,
    69: 11.33,
    70: 11.34,
    71: 11.34,
    72: 11.34,
    73: 11.34,
    74: 11.34,
    75: 11.34,
    76: 11.34,
    77: 11.34,
    78: 11.35,
    79: 11.35,
    80: 11.35,
    81: 10.35,
    82: 9.44,
    83: 8.60,
    84: 7.85,
    85: 7.16,
    86: 6.53,
    87: 5.95,
    88: 5.43,
    89: 4.95,
    90: 4.51,
    91: 4.12,
    92: 3.75,
    93: 3.42,
    94: 3.12,
    95: 2.85,
    96: 2.60,
    97: 2.37,
    98: 2.16,
    99: 1.97,
    100: 1.79,
    101: 1.64,
    102: 1.49,
    103: 1.36,
    104: 1.24,
    105: 1.13,
    106: 1.03,
    107: 0.94,
    108: 0.86,
    109: 0.78,
    110: 0.71,
    111: 0.65,
    112: 0.59,
    113: 0.54,
    114: 0.49,
    115: 0.45,
    116: 0.41,
    117: 0.37,
    118: 0.34,
    119: 0.31,
    120: 0.28,
    121: 0.26,
    122: 0.24,
    123: 0.22,
    124: 0.20,
    125: 0.18,
    126: 0.16,
    127: 0.15,
    128: 0.14,
    129: 0.12,
    130: 0.11,
    131: 0.10,
    132: 0.09,
    133: 0.09,
    134: 0.08,
    135: 0.07,
    136: 0.06,
    137: 0.06,
    138: 0.05,
    139: 0.05,
    140: 0.04,
    141: 0.04,
    142: 0.04,
    143: 0.03,
    144: 0.03,
    145: 0.03,
    146: 0.03,
    147: 0.02,
    148: 0.02,
    149: 0.02,
    150: 0.02,
    151: 0.02,
    152: 0.01,
    153: 0.01,
    154: 0.01,
    155: 0.01,
    156: 0.01,
    157: 0.01,
    158: 0.01,
    159: 0.01,
    160: 0.01
}

# image size in cm, and dpi
fig = plt.figure(figsize=(cm2inch(15), cm2inch(7)), dpi=200)
# position of axes in fraction of image (l,b,w,h)
ax = fig.add_axes([0.1, 0.2, .85, .75])
line, = ax.plot(data.keys(), data.values(), color='red')
ax.fill_between(data.keys(), 0, data.values(), facecolor='red')
ax.set_xlim(0, 160)
ax.grid(False)
plt.xlabel(u"Année")
plt.ylabel(u"$R(t-t_{0})$")
plt.legend([line], [u"$R(t-t_{0})$"], loc=4)
plt.show()
