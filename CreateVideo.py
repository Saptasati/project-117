import os 
import cv2

path = "PRO-C105-Project-Images-main"

Images = []

for file in path:
    os.listdir(path)
    name, ext = os.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path + '/' + file
        print(file_name)
        
        Images.append(file_name)

        
count = len(Images)
frame = cv2.imread(Images[0])
width, height, channels = frame.shape
size = (width, height)
print(size)
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0, count-1):
    frame = cv2.imread(Images[i])
    out.write(frame)
print("Done")    
