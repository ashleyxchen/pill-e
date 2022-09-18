import subprocess

#Display the image
image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "black", "-g", "1280x800", "/home/pi/images/pic01.jpg"])

# Do other stuff here...

# You can now close the image by doing
image.kill()