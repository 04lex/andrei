import PyQt5 as Pq
import sys
from PyQt5.QtWidgets import QApplication, QWidget
import PySide 

# create window and title
app = Pq.QtWidgets.QApplication(sys.argv)
window = Pq.QtWidgets.QWidget()
window.setWindowTitle("Hello World")
window.show()

#mainloop
sys.exit(app.exec_())