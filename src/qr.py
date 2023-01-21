import os
import pyqrcode as qr

# creating url for the qr code
img = qr.create("https://github.com/NwizuEmmanuel?tab=repositories")

# saving qrcode as png and svg
img.png("qr.png", scale=5)
img.svg("qr.svg", scale=5)

# opening both files on the pc (only for windows PC)
os.system("qr.png")
os.system("qr.svg")