# IMPORT MODULES
import sys

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import UI_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bot para licitação")

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Btn home
        self.ui.btn_1.clicked.connect(self.show_page_1)

        # Btn widgets
        self.ui.btn_2.clicked.connect(self.show_page_2)

        # Btn widgets
        self.ui.btn_3.clicked.connect(self.show_page_3)

        # Btn widgets
        self.ui.btn_4.clicked.connect(self.show_page_4)

        self.ui.left_menu.installEventFilter(self)

        # EXIBI A NOSSA APLICAÇÃO
        self.show()

    def update_margin(self, margin):
        return (
            """
            #application_pages {{
                margin: {margin};
                background-color: rgba(255, 255, 255, 0.36);
                border-radius: 15px;
                padding: 30px 30px;
            }}
            """.format(margin=margin)
        )

    # Reset BTN Selection
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def current_page(self):
        name = self.ui.pages.currentWidget().objectName()
        self.ui.top_label_right.setText(f"  {name}  ")
    
    # Btn home function
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.pages.setStyleSheet(self.update_margin("50px 150px 50px 150px"))
        self.ui.btn_1.set_active(True)
        self.current_page()

    # Btn widgets function
    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.pages.setStyleSheet(self.update_margin("100px 150px 100px 150px"))
        self.ui.btn_2.set_active(True)
        self.current_page()

    # Btn pase gettings
    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.pages.setStyleSheet(self.update_margin("100px 150px 100px 150px"))
        self.ui.btn_3.set_active(True)
        self.current_page()

    # Btn pase gettings
    def show_page_4(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)
        self.ui.pages.setStyleSheet(self.update_margin("30px 150px 30px 150px"))
        self.ui.btn_4.set_active(True)
        self.current_page()

    # Toggle button
    def animate_menu(self, target_width):

        menu_actual_width = self.ui.left_menu.width()

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_actual_width)
        self.animation.setEndValue(target_width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    def eventFilter(self, obj, event):
        if obj == self.ui.left_menu:
            if event.type() == QEvent.Enter:
                self.animate_menu(target_width=240)

            elif event.type() == QEvent.Leave:
                # Ação quando o mouse sai da label1
                self.animate_menu(target_width=50)

        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())