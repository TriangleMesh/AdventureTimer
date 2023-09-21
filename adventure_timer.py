#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 18:24:04 2022

@author: TriangleMesh
"""

import time
import datetime
import vlc
import os



media_player = vlc.MediaPlayer()
class_begins = vlc.Media("MusicNameForClassBegins")
class_ends = vlc.Media("MusicNameForClassEnds")

# collect input
print("\nHi, welcome back! So excited to see you again!\n")
total_time = input("How long would you like to take adventure? (hh mm ss)\n")
t_h, t_m, t_s = total_time.split(' ')
choose_time = int(input("\nChoose between: \n1) day mode: 40m + 10m \n2) night mode: 1h20m + 15m \n3) others\nPlease type in number only. \n"))

#def
def countdown(h,m,s):
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end = "\r", flush=True)
        time.sleep(1)
        total_seconds -= 1
def countdown_with_play_music(h_with_music, m_with_music, s_with_music, music_name):
    countdown(h_with_music, m_with_music, s_with_music)
    media_player.set_media(music_name)
    media_player.play()
    os.system('clear')      
def print_i(i):
    if i > 1:
        print("Hooray! You have beaten", i, "enemies already. Let's have a rest! ")
    elif i == 1:
        print("Hooray! You have beaten 1 enemy already. Let's have a rest! ")
def print_remaining_i(remaining_i):
    if remaining_i == 1:
        print("Only 1 enemy is left. Fight until the end!\n")
    elif remaining_i > 1:
        print("Only", remaining_i, "enemies are left. Fight until the end!\n")
def time_loop(h1, m1, s1, h2, m2, s2): 
    i = 1
    total_input_time = int(t_h) * 3600 + int(t_m) * 60 + int(t_s)
    time_duration = 3600 * (h1+h2) + 60 * (m1 + m2) + (s1 + s2)
    num = total_input_time//time_duration
    os.system('clear')
    if num == 1:
        print("Merely 1 enemy this time. Hold on your weapon. Let's begin! \n")
    if num > 1:
        print("There are", num, "enemies coming. Hold on your weapon. Let's begin! \n")
    while i < num:
        remaining_i = num - i
        countdown_with_play_music(h1, m1, s1, class_ends)
        print_i(i)
        countdown_with_play_music(h2, m2, s2, class_begins)
        print("Adventure begins! ")
        print_remaining_i(remaining_i)
        i = i+1
    countdown_with_play_music(h1, m1, s1, class_ends)
    media_player.set_media(class_ends)
    media_player.play()
    # os.system('clear')
    if num == 1:
        print("Wow! You have beaten 1 enemy this time. ")
    if num > 1:
        print("Wow! You have beaten", num, "enemies this time. ")
    print("Adventure ends. May you have an energetic and peaceful day! \nLooking forward to see you again! \n")

# execute code
if choose_time == 1:
    time_loop(0, 40, 0, 0, 10, 0)
    # time_loop(0, 0, 10, 0, 0, 10)
if choose_time == 2:
    time_loop(0, 80, 0, 0, 15, 0)
if choose_time == 3:
    lesson_time = input("\nPlease type the adventure duration. (hh mm ss)\n")
    l_h1, l_m1, l_s1 = lesson_time.split(' ')
    lh1, lm1, ls1 = int(l_h1), int(l_m1), int(l_s1)
    break_time = input("\nPlease type the break time. (hh mm ss)\n")
    b_h2, b_m2, b_s2 = break_time.split(' ')
    bh2, bm2, bs2 = int(b_h2), int(b_m2), int(b_s2)
    time_loop(lh1, lm1, ls1, bh2, bm2, bs2)

