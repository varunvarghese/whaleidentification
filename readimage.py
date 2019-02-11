import pandas as pd

df = pd.read_csv("train.csv")

from PIL import Image

im = Image.open("train/train/00022e1a.jpg").convert("RBG")
pix = im.load()
print(im.size)
print(pix[0,0])
print(im.mode)
pixel_values = list(im.getdata())
print(pixel_values[0])



images = []
for i in df.index:
    images.append((df.iloc[i]["Image"], df.iloc[i]["Id"]))

print(images[0])



