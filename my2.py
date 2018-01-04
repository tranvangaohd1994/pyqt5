import Config
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication,
    QGraphicsDropShadowEffect,QFrame)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal,QRect,QDateTime,QDate
from PyQt5.QtGui import QIcon, QPixmap,QColor,QTransform
from time import strftime
import sys, random


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global hourpixmap, minpixmap, secpixmap
        global hourpixmap2, minpixmap2, secpixmap2
        global lastmin, lastday, lasttimestr
        global clockrect
        global datex, datex2, datey2, pdy
        self.setWindowTitle('demo clock')

        self.setGeometry(0,0,width,height)
        #background
       
        xscale = float(width) / 1024.0
        yscale = float(height) / 600.0
        frames = []
        framep = 0

        frame1 = QFrame(self)
        frame1.setObjectName("frame1")
        frame1.setGeometry(0, 0, width, height)
        frame1.setStyleSheet("#frame1 { background-color: black; border-image: url(" +
                            Config.background + ") 0 0 0 0 stretch stretch;}")
        frames.append(frame1)

        frame2 = QFrame(self)
        frame2.setObjectName("frame2")
        frame2.setGeometry(0, 0, width, height)
        frame2.setStyleSheet("#frame2 { background-color: transparent; border-image: url(" +
                            Config.background + ") 0 0 0 0 stretch stretch;}")
        frame2.setVisible(False)
        frames.append(frame2)

        clockface = QFrame(frame1)
        clockface.setObjectName("clockface")
        clockrect = QRect(
            width / 2 - height * .4,
            height * .52 - height * .42,
            height * .78,
            height * .78)
        clockface.setGeometry(clockrect)
        clockface.setStyleSheet(
            "#clockface { background-color: transparent; border-image: url(" +
            Config.clockface +
            ") 0 0 0 0 stretch stretch;}")

        self.hourhand = QLabel(frame1)
        self.hourhand.setObjectName("hourhand")
        self.hourhand.setStyleSheet("#hourhand { background-color: transparent; }")

        self.minhand = QLabel(frame1)
        self.minhand.setObjectName("minhand")
        self.minhand.setStyleSheet("#minhand { background-color: transparent; }")

        self.sechand = QLabel(frame1)
        self.sechand.setObjectName("sechand")
        self.sechand.setStyleSheet("#sechand { background-color: transparent; }")

        hourpixmap = QPixmap(Config.hourhand)
        hourpixmap2 = QPixmap(Config.hourhand)
        minpixmap = QPixmap(Config.minhand)
        minpixmap2 = QPixmap(Config.minhand)
        secpixmap = QPixmap(Config.sechand)
        secpixmap2 = QPixmap(Config.sechand)


        datex = QLabel(frame1)
        datex.setObjectName("datex")
        datex.setStyleSheet("#datex { font-family:sans-serif; color: " +
                            Config.textcolor +
                            "; background-color: transparent; font-size: " +
                            str(int(50 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        datex.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        datex.setGeometry(0, 20 * xscale, width, 100)

        datex2 = QLabel(frame2)
        datex2.setObjectName("datex2")
        datex2.setStyleSheet("#datex2 { font-family:sans-serif; color: " +
                            Config.textcolor +
                            "; background-color: transparent; font-size: " +
                            str(int(50 * xscale)) + "px; " +
                            Config.fontattr +
                            "}")
        datex2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        datex2.setGeometry(800 * xscale, 780 * yscale, 640 * xscale, 100)
        datey2 = QLabel(frame2)
        datey2.setObjectName("datey2")
        datey2.setStyleSheet("#datey2 { font-family:sans-serif; color: " +
                            Config.textcolor +
                            "; background-color: transparent; font-size: " +
                            str(int(50 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        datey2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        datey2.setGeometry(800 * xscale, 840 * yscale, 640 * xscale, 100)

                
        ypos = -10
        wxicon = QLabel(frame1)
        wxicon.setObjectName("wxicon")
        wxicon.setStyleSheet("#wxicon { background-color: transparent; }")
        wxicon.setGeometry(75 * xscale, ypos * yscale, 150 * xscale, 150 * yscale)

        wxicon2 = QLabel(frame2)
        wxicon2.setObjectName("wxicon2")
        wxicon2.setStyleSheet("#wxicon2 { background-color: transparent; }")
        wxicon2.setGeometry(0 * xscale, 750 * yscale, 150 * xscale, 150 * yscale)

        ypos += 130
        wxdesc = QLabel(frame1)
        wxdesc.setObjectName("wxdesc")
        wxdesc.setStyleSheet("#wxdesc { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(35 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        wxdesc.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        wxdesc.setGeometry(3 * xscale, ypos * yscale, 300 * xscale, 100)

        wxdesc2 = QLabel(frame2)
        wxdesc2.setObjectName("wxdesc2")
        wxdesc2.setStyleSheet("#wxdesc2 { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(50 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        wxdesc2.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        wxdesc2.setGeometry(400 * xscale, 800 * yscale, 400 * xscale, 100)


        ypos += 25
        temper = QLabel(frame1)
        temper.setObjectName("temper")
        temper.setStyleSheet("#temper { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(100 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        temper.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        temper.setGeometry(3 * xscale, ypos * yscale , 300 * xscale, 100)

        temper2 = QLabel(frame2)
        temper2.setObjectName("temper2")
        temper2.setStyleSheet("#temper2 { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(100 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        temper2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        temper2.setGeometry(125 * xscale, 780 * yscale, 300 * xscale, 100)

        ypos += 115
        humidity = QLabel(frame1)
        humidity.setObjectName("humidity")
        humidity.setStyleSheet("#humidity { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(30 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        humidity.setAlignment(Qt.AlignHCenter | Qt.AlignTop) 
        humidity.setGeometry(3 * xscale, ypos * yscale, 300 * xscale, 100)

        ypos += 30
        indoorTemp = QLabel(frame1)
        indoorTemp.setObjectName("indoorTemp")
        indoorTemp.setStyleSheet("#indoorTemp { background-color: transparent; color: " +
                            Config.indoorTextColor +
                            "; font-size: " +
                            str(int(70 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        indoorTemp.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        indoorTemp.setGeometry(3 * xscale, ypos * yscale, 300 * xscale, 100)

        ypos += 75
        indoorHumi = QLabel(frame1)
        indoorHumi.setObjectName("wind")
        indoorHumi.setStyleSheet("#wind { background-color: transparent; color: " +
                        Config.textcolor +
                        "; font-size: " +
                        str(int(30 * xscale)) +
                        "px; " +
                        Config.fontattr +
                        "}")
        indoorHumi.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        indoorHumi.setGeometry(3 * xscale, ypos * yscale, 300 * xscale, 100)

        ypos += 20
        wind2 = QLabel(frame1)
        wind2.setObjectName("wind2")
        wind2.setStyleSheet("#wind2 { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(20 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        wind2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        wind2.setGeometry(3 * xscale , ypos * yscale , 300 * xscale, 100)

        ypos += 20
        wdate = QLabel(frame1)
        wdate.setObjectName("wdate")
        wdate.setStyleSheet("#wdate { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(15 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        wdate.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        wdate.setGeometry(3 * xscale, ypos * yscale, 300 * xscale, 100)


        bottom = QLabel(frame1)
        bottom.setObjectName("bottom")
        bottom.setStyleSheet("#bottom { font-family:sans-serif; color: " +
                            Config.textcolor +
                            "; background-color: transparent; font-size: " +
                            str(int(30 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        bottom.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        bottom.setGeometry(0, height - 50, width, 50)

        temp = QLabel(frame1)
        temp.setObjectName("temp")
        temp.setStyleSheet("#temp { font-family:sans-serif; color: " +
                        Config.textcolor +
                        "; background-color: transparent; font-size: " +
                        str(int(30 * xscale)) +
                        "px; " +
                        Config.fontattr +
                        "}")
        temp.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        temp.setGeometry(0, height - 100, width, 50)
        self.tick()
        ctimer = QTimer(self)
        ctimer.timeout.connect(self.tick)
        ctimer.start(1000)
        self.show()
        

    def tick(self):
        print('tick')
        global hourpixmap, minpixmap, secpixmap
        global hourpixmap2, minpixmap2, secpixmap2
        global lastmin, lastday, lasttimestr
        global clockrect
        global datex, datex2, datey2, pdy
        now_second = int(strftime("%S"))
        angle = now_second * 6
        ts = secpixmap.size()
        secpixmap2 = secpixmap.transformed(
            QTransform().scale(
                float(clockrect.width()) / ts.height(),
                float(clockrect.height()) / ts.height()
            ).rotate(angle),
            Qt.SmoothTransformation
        )
        self.sechand.setPixmap(secpixmap2)
        ts = secpixmap2.size()
        self.sechand.setGeometry(
            clockrect.center().x() - ts.width() / 2,
            clockrect.center().y() - ts.height() / 2,
            ts.width(),
            ts.height()
        )
        now_minute = int(strftime('%M'))
        now_hour = int(strftime('%H'))
        if now_minute != lastmin:
            lastmin = now_minute
            angle = now_minute * 6
            ts = minpixmap.size()
            minpixmap2 = minpixmap.transformed(
                QTransform().scale(
                    float(clockrect.width()) / ts.height(),
                    float(clockrect.height()) / ts.height()
                ).rotate(angle),
                Qt.SmoothTransformation
            )
            self.minhand.setPixmap(minpixmap2)
            ts = minpixmap2.size()
            self.minhand.setGeometry(
                clockrect.center().x() - ts.width() / 2,
                clockrect.center().y() - ts.height() / 2,
                ts.width(),
                ts.height()
            )

            angle = ((now_hour % 12) + now_minute / 60.0) * 30.0
            ts = hourpixmap.size()
            hourpixmap2 = hourpixmap.transformed(
                QTransform().scale(
                    float(clockrect.width()) / ts.height(),
                    float(clockrect.height()) / ts.height()
                ).rotate(angle),
                Qt.SmoothTransformation
            )
            self.hourhand.setPixmap(hourpixmap2)
            ts = hourpixmap2.size()
            self.hourhand.setGeometry(
                clockrect.center().x() - ts.width() / 2,
                clockrect.center().y() - ts.height() / 2,
                ts.width(),
                ts.height()
            )

        dy = strftime("0:%I:%M %p")
        if dy != pdy:
            pdy = dy
            datey2.setText(dy)
        now_day = int(strftime("%d"))
        if now_day != lastday:
            lastday = now_day
            # date
            sup = 'th'
            if (now_day == 1 or now_day == 21 or now_day == 31):
                sup = 'st'
            if (now_day == 2 or now_day == 22):
                sup = 'nd'
            if (now_day == 3 or now_day == 23):
                sup = 'rd'
            if Config.DateLocale != "":
                sup = ""
            ds = strftime("%A %B %d %Y")
            datex.setText(ds)
            datex2.setText(ds)



lastmin = -1
lastday = -1
pdy = ""
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    desktop = app.desktop()
    rec = desktop.screenGeometry()
    height = rec.height()
    width = rec.width()
    myApp = App()    
    sys.exit(app.exec_())    