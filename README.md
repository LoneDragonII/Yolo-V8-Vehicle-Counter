# YOLO V8 Based North and South Bound Vehicle Counter

## Introduction
This project is based of Murtaza's Workshop - Robotics and AI's work i expanded on it to count vehicles moving in multiple directions instead of only one. This was done so that a to see how to perform traffic analysis on a multi-directional road like highways or cross roads. The project is using YOLOV8l and the current torch listed in requirements only installs torch to CPU. install it for your appropriate GPU to get better pperformance or just switch to YOLOV8n which is also predownloaded in the files.

Additionally Canva was used to create a mask for the video so that only the portiuon which is required is only used by YOLO and all other uncesserray regions are cut out.

![Mask Image](https://github.com/LoneDragonII/Yolo-V8-Vehicle-Counter/blob/main/videos/mask.png)

for the line in the video its a simple line. To find the pixel values of the points from where you want to draw the lines, i have included a simple code to find it in my project just give it a frame of your video and it click on the points who's pixel values you need to know to draw the line which updates the vehicle counter once it's crossed.

Video Demonstration of the project:
[![Vehicle Counter](https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg)](https://github.com/LoneDragonII/Yolo-V8-Vehicle-Counter/blob/main/videos/final%20result.mp4)
