# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


def cm2inch(value):
    return value/2.54

data = {
    0: 0,
    1: 5795,
    2: 12150,
    3: 19118,
    4: 26760,
    5: 35140,
    6: 44328,
    7: 54405,
    8: 65455,
    9: 77572,
    10: 90859,
    11: 105429,
    12: 121407,
    13: 138928,
    14: 158142,
    15: 179211,
    16: 202315,
    17: 227650,
    18: 255432,
    19: 285898,
    20: 319306,
    21: 355941,
    22: 396115,
    23: 440168,
    24: 488477,
    25: 541451,
    26: 599541,
    27: 663242,
    28: 733096,
    29: 809697,
    30: 893696,
    31: 985807,
    32: 1086816,
    33: 1197580,
    34: 1319042,
    35: 1452236,
    36: 1598294,
    37: 1758459,
    38: 1934093,
    39: 2126691,
    40: 2337890,
    41: 2569488,
    42: 2823455,
    43: 3101951,
    44: 3407345,
    45: 3742236,
    46: 4109471,
    47: 4512176,
    48: 4953776,
    49: 5438027,
    50: 5969049,
    51: 6551359,
    52: 7189912,
    53: 7890138,
    54: 8657995,
    55: 9500015,
    56: 10423360,
    57: 11435887,
    58: 12546207,
    59: 13763766,
    60: 15098922,
    61: 16563033,
    62: 18168554,
    63: 19929143,
    64: 21859777,
    65: 23976879,
    66: 26298460,
    67: 28844269,
    68: 31635962,
    69: 34697288,
    70: 38054290,
    71: 41735525,
    72: 45772309,
    73: 50198982,
    74: 55053202,
    75: 60376262,
    76: 66213445,
    77: 72614407,
    78: 79633600,
    79: 87330736,
    80: 95771293
}

# image size in cm, and dpi
fig = plt.figure(figsize=(cm2inch(15), cm2inch(8)), dpi=200)
# position of axes in fraction of image (l,b,w,h)
ax = fig.add_axes([0.2, 0.2, .75, .75])
# semilogyaxis
ax.set_yscale("log")
line, = ax.plot(data.keys(), data.values(), color='red')
ax.fill_between(data.keys(), 0, data.values(), facecolor='red')
ax.set_xlim(0, 80)
ax.set_ylim(0, 100000000)
ax.grid(False)
plt.xlabel(u"Année")
plt.ylabel(u"$Q(t-t_{0})=\int_{t_{0}}^t DU(t) \, dt$")
handles, labels = ax.get_legend_handles_labels()
plt.legend([line], [u"$Q(t-t_{0})=\int_{t_{0}}^t DU(t) \, dt$"], loc=2)
plt.show()
