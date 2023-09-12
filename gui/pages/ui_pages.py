from qt_core import *

# IMPORT CUSTOM WIDGETS

from gui.pages.page_1 import Page_1
from gui.pages.page_2 import Page_2
from gui.pages.page_3 import Page_3
from gui.pages.page_4 import Page_4

class Ui_application_pages(object):
    def setupUi(self, root, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(1056, 657)

        application_pages.setStyleSheet("""
            #application_pages {
                margin: 50px 150px 50px 150px;
                background-color: rgba(255, 255, 255, 0.36);
                border-radius: 15px;
                padding: 30px 30px;
            }
            """
        )
              
        Page_1(self, root, application_pages)

        Page_2(self, root, application_pages)

        Page_3(self, root, application_pages)

        Page_4(self, root, application_pages)