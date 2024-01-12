import cv2 as cv

def wrapper_cv(func):
    camera = cv.VideoCapture(0)
    def warpper():
        _, frame = camera.read()
        res = func(frame)
        camera.release()
        return res
    return warpper

@wrapper_cv
def use_contour(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return contours
contours = use_contour()
print(contours)

@wrapper_cv
def use_threshold(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_ = cv.adaptiveThreshold(imgray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    return image_
image_threshold = use_threshold()
print(image_threshold)