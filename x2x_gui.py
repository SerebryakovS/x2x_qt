#sudo apt-get install python3-pyqt5 pyqt5-dev-tools
import sys
from functools import partial
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
class x2x_qt(QWidget):
    def __init__(self):
        super().__init__();
        self.initUI();
    def dir_button_clicked(self,btn_obj):
        print(btn_obj);
        btn_obj.setStyleSheet("border:5px solid #ff0000;");
    def dir_buttons_init(self):
        self.n_btn = QPushButton('north', self);
        self.e_btn  = QPushButton('east' , self);
        self.w_btn  = QPushButton('west' , self);
        for btn in [self.n_btn,self.e_btn,self.w_btn]:
            btn.resize(btn.sizeHint());
            btn.clicked.connect(partial(self.dir_button_clicked,btn));
        self.n_btn.move(self.win_w/2 - self.n_btn.size().width()/2, 10);
        self.w_btn.move(10,self.win_h/2 - self.w_btn.size().height()/2);
        self.e_btn.move(self.win_w-10-self.e_btn.size().width(),
                        self.win_h/2 - self.e_btn.size().height()/2);
    def ip_addr_input_init(self):
        lbl = QLabel("Введите IP-адрес", self);
        lbl.move(10,self.win_h-lbl.size().height()-10);
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])";
        ipRegex = QRegExp("^"+ipRange+"\\."+ipRange+"\\."+ipRange+"\\."+ipRange+"$");
        ipValidator = QRegExpValidator(ipRegex, self);
        lineEdit = QLineEdit(self);
        lineEdit.setValidator(ipValidator);
        lineEdit.move(150,self.win_h-lineEdit.size().height()-10);
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 150);
        self.win_w = self.frameGeometry().width();
        self.win_h = self.frameGeometry().height();
        self.dir_buttons_init();
        self.ip_addr_input_init();
        self.setWindowTitle(self.__class__.__name__);
        self.show();
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = x2x_qt()
    sys.exit(app.exec_())
