# IMPORT QT CORE
from qt_core import *

# IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages

# IMPORT CUSTOM WIDGETS
from gui.widgets.menu_push_button import MenuPushButton

# MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        # ///////////////////////////////////////////////////////////////
        parent.resize(1000, 520)
        parent.setMinimumSize(760, 440)

        # CREATE CENTRAL WIDGET
        # ///////////////////////////////////////////////////////////////
        self.central_frame = QFrame()

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # Set window opacity
        parent.setWindowOpacity(0.97)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)



        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")

        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)

        # TOP BTNS
        self.toggle_button = MenuPushButton(
            text = "Menu",
            icon_path = "menu.png"
        )
        self.btn_1 = MenuPushButton(
            text = "Gerar Ata e TR",
            is_active = True,
            icon_path = "documento-white.png"
        )
        self.btn_2 = MenuPushButton(
            text = "Gerar Texto de Publicação",
            icon_path = "editar-white.png"
        )
        self.btn_3 = MenuPushButton(
            text = "Scan de Pregão Em Andamento",
            icon_path = "pesquisar-alt-white.png"
        )
        self.btn_4 = MenuPushButton(
            text = "Preencher IRP",
            icon_path = "verificacao-de-lista-white.png"
        )

        # ADD BTNS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)
        self.left_menu_top_layout.addWidget(self.btn_3)
        self.left_menu_top_layout.addWidget(self.btn_4)

        # MENU SPACER
        # ///////////////////////////////////////////////////////////////
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # LABEL VERSION
        # ///////////////////////////////////////////////////////////////
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

        # ADD TO LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        # CONTENT
        # ///////////////////////////////////////////////////////////////
        self.content = QFrame()
        self.content.setObjectName("content")
        self.content.setStyleSheet("""
            #content {
                background-color: qlineargradient(x1:0.45, y1:0.9, x2:0.75, y2:0.2, stop:0 rgb(238, 9, 121), stop:1 rgb(255, 106, 0));
            }"""
        )

        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        # ///////////////////////////////////////////////////////////////
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

        # Left label
        self.top_label_left = QLabel("Interface produzida com PySide6")

        # Top spacer
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Right label
        self.top_label_right = QLabel(f"  Ata e Termos de Responsabilidade  ")
        self.top_label_right.setStyleSheet("""
            color: #21232d;
            font: 600 9pt 'Segoe UI';
            background-color: rgba(255, 255, 255, 0.75);
            border-radius: 8px;
            margin: 6px 0 6px 0;
            """
        )

        # Add to layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # Application pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("""
            font-size: 12pt;
            color: #f8f8f2;
        """)

        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(root=parent, application_pages=self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)

        # BOTTOM BAR
        # ///////////////////////////////////////////////////////////////
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)

        # Left label
        self.bottom_label_left = QLabel(">>>")

        # Top spacer
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Right label
        self.bottom_label_right = QLabel("© 2023")

        # Add to layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # Add to content layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WIDGETS TO APP
        # ///////////////////////////////////////////////////////////////
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)