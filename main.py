import cv2
from djitellopy import Tello
import time
import os
import subprocess
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def takePic():
    tello = Tello()
    tello.connect()
    time.sleep(2)
    
    tello.streamon()
    
    frame_read = tello.get_frame_read()
    
    length = input("enter you length:") 
    length = int(length) 
    
    tello.takeoff()
    
    counter = 1 
    while counter <= length:
        print("I will take a picture in 2 seconds")
        time.sleep(1)
        print("I will take a picture in 1 seconds")
        time.sleep(1)
        filename = f"tello-picture-{counter}.png"
        destination_path = os.path.join(os.path.expanduser("~"), "Desktop/final/yolov5/data/images") 
        full_path = os.path.join(destination_path, filename)
        cv2.imwrite(full_path, frame_read.frame)
        tello.move_right(100)
        counter += 1 
    
    tello.land()
    tello.streamoff()


def send_email(subject, body):
    sender_email = "92leochenp@gmail.com"
    rec_email = "41097A011@gms.ndhu.edu.tw"
    password = "gobx bqgq smif luim "

    #-------password-------#
    #   this password is called "app password",
    #   you need to get the password form your Google account.
    #   this is for the safety of the account you'r using.
    #----------------------#

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = rec_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("connected to server")
    server.login(sender_email, password)
    print("login succeed")
    server.sendmail(sender_email, rec_email, message.as_string())
    print("email has been sent to ", rec_email)


def count(result):
    output_lines = result.stderr.splitlines()
    total_sum = 0
    
    for line in output_lines:
        match = re.search(r'(\d+)\s+tomato', line)
        if match:
            total_sum += int(match.group(1))
    
    # 輸出加總結果
    print("總和:", total_sum)

    subject = "以YOLOv5計算番茄產量！！！"
    body = "你有" + str(total_sum) + "顆番茄"
    #send_email(subject, body)



def yolo():
    script_path = os.path.expanduser("detect.py")
    #os.system(f"python3 {script_path} --weights best.pt --source data/images")
    command = f"python3 {script_path} --weights best.pt --source data/images"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("STDERR:", result.stderr)
    # note that yolo output is in the stderr, not in stdout
    count(result)

if __name__ == "__main__":
    #takePic()
    yolo()

