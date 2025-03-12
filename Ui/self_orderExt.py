from Ui_Cadty.Ui.self_order import Ui_MainWindow


class SelfOrderExt(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        pass

    def showWindow(self):
        self.MainWindow.show()