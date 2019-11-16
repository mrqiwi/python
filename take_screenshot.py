#!/usr/bin/python3
import mss
import mss.tools

# screen shot part of the monitor
with mss.mss() as sct:
    monitor = {"top": 0, "left": 870, "width": 1050, "height": 1050}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    sct_img = sct.grab(monitor)

    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)