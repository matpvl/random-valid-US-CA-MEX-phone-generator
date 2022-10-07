import random
import phonenumbers


CANADA_REGIONAL_NUMBERS = [403, 587, 780, 825, 236, 250, 604, 672, 778, 204, 431,
                           506, 709, 782, 902, 226, 249, 289, 343, 365, 416, 437,
                           519, 548, 613, 647, 705, 807, 905, 367, 418, 438, 450,
                           514, 579, 581, 819, 873, 306, 639, 867]

US_REGIONAL_NUMBERS = [203, 860, 475, 959, 207, 339, 351, 413, 508, 617, 774, 781, 857, 978,
                       603, 201, 551, 609, 640, 732, 848, 856, 862, 908, 973, 212, 315, 332,
                       347, 516, 518, 585, 607, 631, 646, 680, 716, 718, 838, 845, 914, 917,
                       929, 934, 215, 223, 267, 272, 412, 484, 610, 717, 724, 814, 878, 401,
                       802, 217, 224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847, 872,
                       219, 260, 317, 574, 765, 812, 930, 319, 515, 563, 641, 712, 316, 620,
                       785, 913, 231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989,
                       679, 218, 320, 507, 612, 651, 763, 952, 314, 417, 573, 636, 660, 816,
                       308, 402, 531, 701, 216, 234, 326, 330, 380, 419, 440, 513, 567, 614,
                       740, 937, 220, 605, 262, 414, 608, 534, 715, 920, 274, 205, 251, 256,
                       334, 938, 479, 501, 870, 302, 239, 305, 321, 352, 386, 407, 561, 686,
                       727, 754, 772, 786, 813, 850, 863, 904, 941, 954, 229, 404, 470, 478,
                       678, 706, 762, 770, 912, 270, 364, 502, 606, 859, 225, 318, 337, 504,
                       985, 240, 301, 410, 443, 667, 228, 601, 662, 769, 252, 336, 704, 743,
                       828, 910, 919, 980, 984, 405, 580, 918, 539, 803, 843, 854, 864, 423,
                       615, 629, 731, 865, 901, 931, 210, 214, 254, 281, 325, 346, 361, 409,
                       430, 432, 469, 512, 682, 713, 726, 737, 806, 817, 830, 832, 903, 915,
                       936, 940, 956, 972, 979, 276, 434, 540, 571, 703, 757, 804, 604, 681,
                       907, 479, 501, 870, 209, 213, 279, 310, 323, 341, 408, 415, 424, 442,
                       510, 530, 559, 562, 619, 626, 628, 650, 657, 661, 669, 707, 714, 747,
                       760, 805, 818, 820, 831, 858, 909, 916, 925, 949, 951, 303, 719, 720,
                       970, 808, 208, 986, 406, 702, 725, 775, 505, 575, 503, 541, 971, 458,
                       435, 801, 385, 206, 253, 360, 425, 509, 564, 307]

USCA_REGIONAL_NUMBERS = CANADA_REGIONAL_NUMBERS + US_REGIONAL_NUMBERS

MEXICO_REGIONAL_NUMBERS = [55,
                           56,
                           81,
                           33,
                           656,
                           614,
                           618,
                           999,
                           990,
                           221,
                           222,
                           442,
                           446,
                           449,
                           663,
                           664,
                           612,
                           624,
                           844,
                           686,
                           667,
                           722,
                           729,
                           998,
                           871,
                           744,
                           444,
                           440,
                           833,
                           477,
                           479,
                           961,
                           662,
                           633,
                           645,
                           644,
                           642,
                           631,
                           229,
                           443,
                           921,
                           771,
                           981,
                           899,
                           868]


def RandomUSCAPhone():
    number = '+1'
    number += str(random.choice(USCA_REGIONAL_NUMBERS))
    the_rest = random.randrange(0000000, 9999999)
    number += str(the_rest)
    print(number)
    return number


def RandomMEXPhone():
    number = '+52'
    number += str(random.choice(MEXICO_REGIONAL_NUMBERS))
    the_rest = random.randrange(0000000, 9999999)
    number += str(the_rest)
    print(number)
    return number

RandomMEXPhone()

parsed = phonenumbers.parse('+526627770625')
print(phonenumbers.is_valid_number(parsed))
'''We can check the validity of a given number by using the python phonenumbers library'''
