from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import*

model = YOLO('yolo_models/yolov8l.pt')

class_names = [
    "person", "bicycle", "car", "airplane", "bus", "train", "truck",
    "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
    "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra",
    "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
    "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove",
    "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
    "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange",
    "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
    "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse",
    "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
    "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier",
    "toothbrush"
]


mask = cv2.imread ("videos/mask.png")

#Tracker from sort.py
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)


limitS = [12, 196, 404, 204]
limitN = [454, 174, 732, 166]

TS = []
TN = []

cap = cv2.VideoCapture("videos/traffic2.mp4")

while True:
    success, img = cap.read()
    videoRegion = cv2.bitwise_and(img,mask)
    results = model(videoRegion, stream=True)

    detections = np.empty((0,5))

    
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
            conf = math.ceil(box.conf[0] * 100) / 100
            
            cls = int(box.cls[0])

            req_class = class_names[cls]

            if req_class == "car" or req_class == "bus" or req_class == "truck" or req_class == "motorbike" and conf > 0.4:

                w, h = x2 - x1, y2 - y1

                currentArray = np.array([x1, y1, x2, y2 , conf])
                detections = np.vstack((detections, currentArray))

    resultsTracker = tracker.update(detections)

    cv2.line(img,(limitS[0], limitS[1]), (limitS[2], limitS[3]), (0,0,255),3)
    cv2.line(img,(limitN[0], limitN[1]), (limitN[2], limitN[3]), (0,0,255),3)

    for results in resultsTracker:

        x1, y1, x2, y2, id = results
        #print(results)
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=10, rt=3, colorR=(255,0,0))
        cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), max(35, y1)), scale=1, thickness=1, offset=3, colorR=(0, 165, 255))

        cx, cy = x1+w//2, y1+h//2

        cv2.circle(img,(cx,cy),4,(255,0,255), cv2.FILLED)

        if limitS[0] < cx < limitS[2] and (limitS[1]-15) < cy < (limitS[3]+15):
            if TS.count(id)==0:
                TS.append(id)
                cv2.line(img,(limitS[0], limitS[1]), (limitS[2], limitS[3]), (0,255,0),3)
                

        if limitN[0] < cx < limitN[2] and (limitN[1]-15) < cy < (limitN[3]+15):
            if TN.count(id)==0:
                TN.append(id)
                cv2.line(img,(limitN[0], limitN[1]), (limitN[2], limitN[3]), (0,255,0),3)
        
    cvzone.putTextRect(img, f'North Bound: {len(TN)}', (50,50), scale=1, thickness=2, offset=3, colorR=(0, 165, 255))
    cvzone.putTextRect(img, f'South Bound: {len(TS)}', (50,69), scale=1, thickness=2, offset=3, colorR=(0, 165, 255))
    cv2.imshow("Vehicle Counter", img) 
    cv2.waitKey(1)








