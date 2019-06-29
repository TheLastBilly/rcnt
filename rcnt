#!/usr/bin/python

import cv2
import numpy
import sys

def main():
    if(len(sys.argv) != 2):
        print("rcnt needs only one argument (video_file_name).")
    video_feed = cv2.VideoCapture(sys.argv[1])
    brightness = []
    if(video_feed.isOpened() == False):
        print("Could not open video file.")
    frame_count = 1
    while(video_feed.isOpened()):
        ret, frame = video_feed.read()
        try:
            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            MeanVal = cv2.mean(frame)
            bg = int(MeanVal[0])
            print("Frame " + str(frame_count) + ": " + str(bg))
            brightness.append(bg)
            frame_count += 1
        except:
            break
    average = sum(brightness)/frame_count
    print("Average brihtness: " + str(average))
    enter = False
    out = True
    peaks =0
    for val in brightness:
        if(out and val >= average):
            enter = True
            out = False
        if(enter and val < average):
            peaks += 1
            enter = False
            out = True
    print(peaks)

    video_feed.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
