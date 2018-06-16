#!/usr/bin/python3

# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

plt.switch_backend("agg")

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2, 1.03*height, "%s" % float(height), ha="center")

num_list = [0.328795, 0.32313, 0.160494]

plt.xlabel(u"Algorithm")

plt.ylabel(u"the value of running time")

plt.title(u"Time variance")

rect = plt.bar(range(len(num_list)), num_list, color="blue")

plt.xticks((0,1,2),(u'Random', u'Round', u'GA'))

autolabel(rect)

plt.show()

plt.savefig("compare.jpg")
