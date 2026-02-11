from PySide6.QtWidgets import QApplication
from Window_Class import Window
import sys
app=QApplication(sys.argv)
window=Window()
window.show()
app.exec()