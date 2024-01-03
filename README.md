# UAV

this is a direcotry for my Unmanned Aerial Vehicle in Mobile Networks course.

## how to run the program
to run the program you will have to clone the repo into your local computer, and run the following commands.

```bash
git clone https://github.com/leoochenn/UAV.git
```
clone the repo into your loacal computer (it might take a few minits......)

```bash
git clone https://github.com/ultralytics/yolov5.git yolov5
```
because the directory yolov5 is yolo's repo, so we will have to clone that too if we want to use it.

```bash
mv weight/best.pt yolov5
```
move the custom weight (best.pt) file into yolov5 project directory.

```bash
mv main.py yolov5
```
move the main.py file into yolov5 project dirtctory.

```bash
cd yolov5
```
change directory into yolov5.

```bash
python3 detect.py --weight best.pt --source data/images
```
press ENTER, then your result will be stored in runs/detect/exp_ .
*** note that you can change the photos inside the yolov5/data/images directory to detect othere things.
