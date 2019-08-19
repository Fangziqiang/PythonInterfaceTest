import cv2

def getImageVar(imgPath):
    image = cv2.imread(imgPath);
    img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
    return imageVar

print getImageVar("1.jpg")
print getImageVar("2.jpg")
print getImageVar("3.jpg")
print getImageVar("3.jpg")
print getImageVar("3.jpg")