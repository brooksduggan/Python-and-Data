# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:08:13 2022

@author: 19496
"""

import time as t

def pong_ai(left_pad, hit_ball):
    
    if hit_ball.dx < 0:
        
        if hit_ball.ycor()<left_pad.ycor()+10 and hit_ball.ycor()>left_pad.ycor()-10:
            return "down"
        elif (hit_ball.ycor()>left_pad.ycor()-10 and hit_ball.ycor()>left_pad.ycor()+10):
            return "up"
        
        