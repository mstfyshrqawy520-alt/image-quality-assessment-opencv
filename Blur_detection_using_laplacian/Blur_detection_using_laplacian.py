import cv2
# if variance is less than the set threshold
# image is blurred otherwise not
def variance_fn(var):
    if var < 120:
        s = 'Image is Blurred'
    else:
        s = 'Image is not Blurred'
    return s

# Read the image
img = cv2.imread('images/input.jpg')
# Convert to greyscale
grey_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# make sure that you have saved it in the same folder
# You can change the kernel size as you want
blurImg = cv2.blur(img,(10,10))
grey_2 = cv2.cvtColor(blurImg, cv2.COLOR_BGR2GRAY)

# Find the laplacian of this image and
# calculate the variance
var_1 = cv2.Laplacian(grey_1, cv2.CV_64F).var()

var_2 = cv2.Laplacian(grey_2, cv2.CV_64F).var()

print("1st image: ",variance_fn(var_1))
print("2nd image: ",variance_fn(var_2), end="")


import numpy as np

def contrast_level(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contrast = grey.std()  # الانحراف المعياري = التباين
    print("Contrast Level:", contrast)
    if contrast < 50:
        print("⚠️ الصورة ذات تباين منخفض (باهتة)")
    else:
        print("✅ الصورة ذات تباين جيد")

contrast_level(img)


def brightness_level(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mean_brightness = grey.mean()
    print("Average Brightness:", mean_brightness)
    if mean_brightness < 70:
        print("🌑 الصورة مظلمة جدًا")
    elif mean_brightness > 180:
        print("☀️ الصورة ساطعة جدًا")
    else:
        print("✅ السطوع مناسب")

brightness_level(img)



import numpy as np

def noise_level(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(grey, cv2.CV_64F)
    noise = lap.std()
    print("Noise Level:", noise)
    if noise > 15:
        print("⚠️ الصورة تحتوي على ضوضاء عالية")
    else:
        print("✅ الصورة نظيفة")

noise_level(img)

