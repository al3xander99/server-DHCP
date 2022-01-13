from PyQt5 import QtCore, QtGui, QtWidgets
import interfata_eleganta_2005
from Server import DHCP_server
from queue import Queue
import threading


def func(out_q):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = interfata_eleganta_2005.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.completariStatice()

    def mor():
        data = out_q.get()
        if(data):
            ui.adaugaText(data)
        else:
            pass
    timer = QtCore.QTimer()
    timer.timeout.connect(mor)
    timer.start(2000)
    sys.exit(app.exec_())


if __name__ == "__main__":
    q = Queue()
    dhcp_server = DHCP_server()
    x = threading.Thread(target=dhcp_server.server, args=(q,)).start()
    y = threading.Thread(target=func, args=(q,)).start()
