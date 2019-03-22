import cv2
import os
from average import average_color
from knn import colorrec
import pycuber as pc
from pycuber.solver import CFOPSolver
from time import sleep

directory = 'img'
if not os.path.isdir(directory):
    os.mkdir(directory)
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

img_counter = 0
xpos = 125
ypos = 185
size = 50
faces_solve = []
colpredict = colorrec()
while rval and img_counter !=6:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 32:
        imgname = "img"+str(img_counter)+".png"
        frame = frame[ypos:ypos + 3*size,xpos:xpos+3*size]
        cv2.imwrite(os.path.join(directory,imgname), frame)
        print("Face {} taken".format(img_counter+1))
        cubeFace = average_color(frame)
        col1 = cubeFace.face1()
        col2 = cubeFace.face2()
        col3 = cubeFace.face3()
        col4 = cubeFace.face4()
        col5 = cubeFace.face5()
        col6 = cubeFace.face6()
        col7 = cubeFace.face7()
        col8 = cubeFace.face8()
        col9 = cubeFace.face9()
        faces = []
        faces.append(str(colpredict.color(col1)))
        faces.append(str(colpredict.color(col2)))
        faces.append(str(colpredict.color(col3)))
        faces.append(str(colpredict.color(col4)))
        faces.append(str(colpredict.color(col5)))
        faces.append(str(colpredict.color(col6)))
        faces.append(str(colpredict.color(col7)))
        faces.append(str(colpredict.color(col8)))
        faces.append(str(colpredict.color(col9)))
        cubeFace.makeface(faces,size,img_counter)
        k = input('Is this face correct?(Y/N)\n')
        if str(k) == str('N'):
            img_counter = img_counter - 1
        else:
            faces_solve.append(faces)
            img_counter = img_counter + 1

    else:
        cv2.rectangle(img=frame, pt1=(xpos, ypos),pt2=(xpos+size,ypos+size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + size, ypos),pt2=(xpos + 2*size,ypos+size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + 2*size, ypos),pt2=(xpos + 3*size,ypos+size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos, ypos + size),pt2=(xpos+size,ypos+ 2*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + size, ypos + size),pt2=(xpos + 2*size,ypos+2*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + 2*size, ypos + size),pt2=(xpos + 3*size,ypos+2*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos, ypos + 2*size),pt2=(xpos+size,ypos+3*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + size, ypos+2*size),pt2=(xpos + 2*size,ypos+3*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + 2*size, ypos + 2*size),pt2=(xpos + 3*size,ypos+3*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)

vc.release()
cv2.destroyWindow("preview")

array_default = '000000000111111111222222222333333333444444444555555555'

array = faces_solve

cube_default = pc.Cube()

cubie = pc.array_to_cubies(array)

cube_main = pc.Cube(cubie)

print(cube_main)

solver = CFOPSolver(cube_main)

steps = solver.solve()

step_list = list(steps)
print(steps)
print(len(steps))

cube_solve = pc.Cube(cubie)

for i in range(len(step_list)):
    cube_solve(steps[i])
    print(cube_solve)
    sleep(0.3)
