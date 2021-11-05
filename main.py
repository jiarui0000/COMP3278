from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import datetime, time
import random
import cv2, os
from faceCapture import faceCapture
from train import train
import mysql.connector
import ctypes

faceCapture("002")
train()