#!/usr/bin/python

# rcnt - rcnt.py
#
# Copyright (c) 2019, TheLastBilly
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import cv2, sys, os

def store_results(file_name, rotations, time, revs, b_avg):
    if(file_name.find('/')):
        file_name = file_name[file_name.rfind('/') +1 :] + str(".txt")
    if (os.path.exists(file_name)):
        os.remove(file_name)
    results_file = open(file_name, "+a")
    results_file.write("Rotations: " + str(rotations) + "\nTime: " + str(time) + "\nRevolutions per second: " + str(revs) + "\nAverage brightness: " + str(b_avg))
    results_file.close()

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
    print("Average brightness: " + str(average))
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
    print("Rotations detected: " + str(peaks))
    duration = video_feed.get(cv2.CAP_PROP_FRAME_COUNT) / video_feed.get(cv2.CAP_PROP_FPS)
    store_results(sys.argv[1], peaks, duration, peaks/duration, average)
    video_feed.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
