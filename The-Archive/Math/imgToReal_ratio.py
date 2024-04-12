from math import *

for i in range(181):
    print("i:" + "%.4f"%(cos(radians(i))), "at", i, "degrees")

""" javascript ---
for (var i = 0; i < 181; i++) {
    console.log("i:" + (Math.round(Math.cos(radians(i))*10000)/10000) + " at " + i + " degrees")
}
"""
