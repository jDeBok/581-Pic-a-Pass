import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QSplashScreen,
    QFormLayout,
    QGridLayout
)

class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt);
            painter.restore()


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QtWidgets.QTabWidget.West) #set on left side of window

class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap("Pic-a-Pass_logo.png")  # Replace with your image path
        self.setPixmap(pixmap)

        # Optional: Add text to the splash screen
        label = QLabel("Loading...", self)
        label.setStyleSheet("color: white; font-size: 16px;")
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, pixmap.height() - 30, pixmap.width(), 30)

# Signup Screen class
class SignupScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up")
        self.setFixedSize(300, 200)

        # Layout setup
        layout = QVBoxLayout()

        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter password")
        layout.addWidget(self.password_input)

        # Password confirmation input
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setPlaceholderText("Confirm password")
        layout.addWidget(self.confirm_password_input)

        # Signup button
        self.signup_button = QPushButton("Sign Up", self)
        self.signup_button.clicked.connect(self.signup)
        layout.addWidget(self.signup_button)

        # Status label for feedback
        self.status_label = QLabel("", self)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def signup(self):
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if password != confirm_password:
            self.status_label.setText("Passwords do not match.")
            return

        if not password:
            self.status_label.setText("Password cannot be empty.")
            return

        # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Save the hashed password to a file
        try:
            with open("hashed_password.pap", "w") as file:
                file.write(hashed_password)
            self.status_label.setText("Sign-up successful!")
            self.close()  # Close the signup screen
        except IOError as e:
            self.status_label.setText("Error saving password.")
            print(f"Error: {e}")

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pic-A-Pass")
        #create central widget, everything is on this
        wid = QWidget( self )
        self.setCentralWidget( wid )
        main_layout = QGridLayout()
        wid.setLayout(main_layout)
        
        #password page
        pw_page = QWidget(self)
        layout = QFormLayout()
        pw_page.setLayout(layout)
        layout.addRow('First Name:', QLineEdit(self))
        layout.addRow('Last Name:', QLineEdit(self))
        layout.addRow('DOB:', QDateEdit(self))
        #breach page
        breach_page = QWidget(self)
        layout = QFormLayout()
        breach_page.setLayout(layout)
        layout.addRow('Phone Number:', QLineEdit(self))
        layout.addRow('Email Address:', QLineEdit(self))
        #Tabs
        w = TabWidget()
        w.setStyleSheet( "QTabBar::tab {width: 100px; height: 200px;}" ); #set stylesheet for tab sizes
        w.addTab( pw_page, "Passwords") #set the widget of this tab to the password page widget
        w.addTab( breach_page, "Breaches") #set the widget of this tab to the breach page widget
        w.resize(900, 600) #width, height
        #add to layout
        main_layout.addWidget( w )
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.

def main():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()

    # Simulate loading process
    import time
    time.sleep(3)

    login_window = LoginWindow()
    login_window.show()
    splash.finish(login_window)

    window = MainWindow(  )
    window.resize( 900, 600 ) #width, height
    window.show()
    #splash.finish(window)
    
   
    app.exec()
    
if __name__ == "__main__":
    main() #call main
