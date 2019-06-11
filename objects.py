import cv2

def get_objects(src):
  '''
  Reads an source image and return a list 
  of images which are objects inside source image
  '''
  #reading the image
  gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  gray = cv2.equalizeHist(gray)
  edged = cv2.Canny(gray, 100, 255)
  cv2.imshow("Edges", edged)
  cv2.waitKey(0)
      
  #applying closing function 
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
  closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
  cv2.imshow('Closed', closed)
  cv2.waitKey(0)
      
  #finding_contours 
  _, cnts, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  objs = []
  for c in cnts:
    # x, y, w, h = cv2.boundingRect(c)
    # if w > 100 and h > 100:
    #   new_src = src[y: y + h, x: x + w]
    #   if not objs.__contains__(new_src):
    #     objs.append(new_src)
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    cv2.drawContours(src, [approx], -1, (0, 255, 0), 2)
  return objs

img = cv2.imread('cenarios/cenario2.jpg')
objs = get_objects(img)
for i in objs:
  cv2.imshow(f'Object {1 + objs.index(i)}', i)
cv2.imshow('Output', img)
cv2.waitKey(0)