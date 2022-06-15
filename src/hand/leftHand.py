import math
import operator

import cv2
from src.common.base import PEN
from src.common.constant import *
from src.hand.finger import fingerMap
from src.hand.hand import Hand, HandTag
from src.image.draw import *

left_select = [0, 1, 1, 0, 0]  # 选择状态23指并拢
first = [0, 1, 0, 0, 0]
second = [0, 1, 1, 0, 0]
third = [0, 1, 1, 1, 0]
fourth = [0, 1, 1, 1, 1]
closeOperation = [1, 1, 1, 1, 1]  # 关闭展开栏


class LeftHand(Hand):
    def __init__(self):
        super().__init__()
        self.tag = HandTag.LEFT

    def judgeCurve(self, finger):
        var = fingerMap.get(finger)
        if finger == 0:
            return True if self.lms[var][1] < self.lms[var - 1][1] else False
        return True if self.lms[var][2] > self.lms[var - 2][2] else False

    def judgeSelect(self):  # 判断是否为左手选择状态
        id1, x1, y1 = self.getSecond()
        id2, x2, y2 = self.getThird()
        return abs(x1 - x2) <= 80

    def checkSelect(self, img):
        fingers = self.getFingers()
        if fingers is not None and len(fingers) != 0:
            if operator.eq(fingers, left_select) and self.judgeSelect():
                id2, x2, y2 = self.getSecond()
                id3, x3, y3 = self.getThird()
                # 这里画一个矩形
                cv2.rectangle(img, (x3-10, y3-10), (x2+10, y2 + 10), PEN.penColor, cv2.FILLED)
                return True
        else:
            return False

    def penWidth(self, mainWindow):
        fingers = self.getFingers()
        if self.judgeNull():
            return
        if operator.eq(fingers, first):
            PEN.penThickness = PenThickness1
            Hand.SecondFlag=1
        elif operator.eq(fingers, second):
            PEN.penThickness = PenThickness2
            Hand.SecondFlag = 2
        elif operator.eq(fingers, third):
            PEN.penThickness = PenThickness3
            Hand.SecondFlag = 3
        elif operator.eq(fingers, closeOperation):
            mainWindow.penBoardHide()
            Hand.FirstFlag = 0

    def erase(self):
        if self.judgeNull():
            return
        PEN.penColor = BLACK

    def shape(self, mainWindow, img):
        fingers = self.getFingers()
        if self.judgeNull():
            return
        id2, x2, y2 = self.getSecond()
        # 正方形
        if operator.eq(fingers, first):
            id, x, y = self.getOneFinger(5)
            angle = math.atan((y - y2) / (x - x2))
            drawRectangle(img, x2, y2, Rectangle_Length, Rectangle_Width, angle)
            Hand.SecondFlag = 1
        # 圆形
        elif operator.eq(fingers, second):
            drawCircle(img,x2,y2,Circle_Radius)
            Hand.SecondFlag = 2
        elif operator.eq(fingers, third):
            pass
        elif operator.eq(fingers, fourth):
            pass
        elif operator.eq(fingers, closeOperation):
            mainWindow.shapeBoardHide()
            Hand.FirstFlag = 0

    def penColor(self, mainWindow):
        fingers = self.getFingers()
        if self.judgeNull():
            return
        if operator.eq(fingers, first):
            PEN.penColor = GREEN
            Hand.SecondFlag = 1
        elif operator.eq(fingers, second):
            PEN.penColor = PURPLE
            Hand.SecondFlag = 2
        elif operator.eq(fingers, third):
            PEN.penColor = RED
            Hand.SecondFlag = 3
        elif operator.eq(fingers, fourth):
            PEN.penColor = GREEN
            Hand.SecondFlag = 4
        elif operator.eq(fingers, closeOperation):
            mainWindow.colorBoardHide()
            Hand.FirstFlag = 0

    def newFile(self):
        fingers = self.getFingers()
        if self.judgeNull():
            return
        return

    def saveFile(self):
        pass

    def process(self, img, mainWindow=None):

        if not self.judgeNull():
            if self.checkSelect(img) and Hand.FirstFlag == 0:
                print("select")
                id2, x2, y2 = self.getSecond()
                if x2 < 150 and y2 < 100:  # 画笔粗细
                    mainWindow.penBoardShow()
                    self.penWidth(mainWindow)
                    Hand.FirstFlag = 1
                elif x2 < 150 and 100 < y2 < 200:  # 橡皮擦
                    mainWindow.eraserBtn()
                    self.erase()
                    Hand.FirstFlag = 2
                elif x2 < 150 and 200 < y2 < 300:  # 形状
                    mainWindow.shapeBoardShow()
                    self.shape(mainWindow,img)
                    Hand.FirstFlag = 3
                elif x2 < 150 and 300 < y2 < 400:  # 画笔颜色
                    mainWindow.colorBoardShow()
                    self.penColor(mainWindow)
                    Hand.FirstFlag = 4
                elif x2 < 150 and 400 < y2 < 500:  # 新建
                    mainWindow.newBtn()
                    self.newFile()
                    Hand.FirstFlag = 5
                elif x2 < 150 and 600 < y2 < 700:  # 保存
                    mainWindow.saveBtn()
                    self.saveFile()
                    Hand.FirstFlag = 6

            elif not self.checkSelect(img):
                if Hand.FirstFlag == 1:
                    self.penWidth(mainWindow)
                elif Hand.FirstFlag == 2:
                    self.erase()
                elif Hand.FirstFlag == 3:
                    self.penColor(mainWindow)
                elif Hand.FirstFlag == 4:
                    self.penColor(mainWindow)
                elif Hand.FirstFlag == 5:
                    self.newFile()
                elif Hand.FirstFlag == 6:
                    self.saveFile()
