# sudo apt-get install python3-pyqt5 pyqt5-dev-tools
# sudo apt-get install x2x
# ssh -XC pi@192.168.1.104 x2x -east -to :0.0
import os
import sys
from multiprocessing import Process
from functools import partial
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
def run_x2x(direction,conn_to):
    print("new PID: "+str(os.getpid())+" direction: "+direction);
    os.system("ssh -XC "+conn_to+" x2x -"+direction+" -to :0.0");
    return 0;
class x2x_qt(QWidget):
    def __init__(self):
        super().__init__();
        self.initUI();
        self.running_dirs = list();
    def dir_button_clicked(self,btn_obj):
        for btn in [self.n_btn,self.e_btn,self.w_btn]:
            btn.setStyleSheet("");
        btn_obj.setStyleSheet("border:3px solid #bc7360;");
        self.selected_button = btn_obj;
    def xconnect(self):
        if not hasattr(self,"selected_button"):
            print("before doing connection, please specify direction");
            return;
        if not self.iline.text():
            print("before doing connection, please username@ip_addr");
            return;
        self.running_dirs.append(Process(
            target=run_x2x,args=(self.selected_button.text(),self.iline.text())))
        self.running_dirs[-1].start();
    def dir_buttons_init(self):
        self.n_btn  = QPushButton('north', self);
        self.e_btn  = QPushButton('east' , self);
        self.w_btn  = QPushButton('west' , self);
        for btn in [self.n_btn,self.e_btn,self.w_btn]:
            btn.resize(btn.sizeHint());
            btn.clicked.connect(partial(self.dir_button_clicked,btn));
        self.n_btn.move(self.win_w/2 - self.n_btn.size().width()/2, 10);
        self.w_btn.move(10,10);
        self.e_btn.move(self.win_w-10-self.e_btn.size().width(),10);
    def ip_addr_input_init(self):
        self.iline = QLineEdit(self);
        self.iline.move(10,20+self.n_btn.size().height());
        self.iline.resize(185,self.n_btn.size().height());
        self.conn_btn = QPushButton('conn', self);
        self.conn_btn.move(self.win_w-10-self.e_btn.size().width(),
                           20+self.n_btn.size().height());
        self.conn_btn.setStyleSheet("background-color : #bc7360");
        self.conn_btn.clicked.connect(self.xconnect);
    def initUI(self):
        self.setGeometry(300, 300, 300, 100);
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
