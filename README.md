# YOLO V8 Based North and South Bound Vehicle Counter

## Introduction
This project is based on Murtaza's Workshop - Robotics and AI's work. I expanded on it to count vehicles moving in multiple directions instead of only one. This was done to perform traffic analysis on a multi-directional road like highways or cross roads. The project uses YOLOV8l, and the current torch listed in the requirements only installs torch for CPU. Install it for your appropriate GPU to get better performance or switch to YOLOV8n, which is also pre-downloaded in the files.

Additionally, Canva was used to create a mask for the video so that only the portion which is required is used by YOLO, and all other unnecessary regions are cut out.

![Mask Image](https://github.com/LoneDragonII/Yolo-V8-Vehicle-Counter/blob/main/videos/mask.png)

For the line in the video, it's a simple line. To find the pixel values of the points from where you want to draw the lines, I have included a simple code to find it in my project. Just give it a frame of your video and click on the points whose pixel values you need to know to draw the line which updates the vehicle counter once it's crossed.

Video Demonstration of the project:
[![Vehicle Counter](https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg)](https://github.com/LoneDragonII/Yolo-V8-Vehicle-Counter/blob/main/videos/final%20result.mp4)
