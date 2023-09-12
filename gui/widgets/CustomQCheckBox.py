import PySide6.QtCore
import PySide6.QtGui
from qt_core import *

class CustomQCheckBox(QCheckBox):
    def __init__(
        self,
        width = 50,
        height = 20,
        bg_color = '#777',
        circle_color = "#DDD",
        active_color = "#2ce31b",
        animation_curve = QEasingCurve.OutQuint
    ):
        QCheckBox.__init__(self)

        self.setFixedSize(width, height)
        self.setCursor(Qt.PointingHandCursor)

        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)

        self.stateChanged.connect(self.start_transition)

    @Property(float)
    def circle_position(self):
        return self._circle_position
    
    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()
    
    def start_transition(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width()-self.height())
        else:
            self.animation.setEndValue(3)

        self.animation.start()
        print(f"Status: {self.isChecked()}")

    def hitButton(self, pos: QPoint) -> bool:
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height()/2, self.height()/2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 2, self.height()-4, self.height()-4)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height()/2, self.height()/2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 2, self.height()-4, self.height()-4)

        p.end()
