<<<<<<< HEAD
from PyQt5 import QtWidgets, QtCore
class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        s = QtCore.QSize(150, 289) #THIS IS THE REAL SIZE OF THE TABS
        return s
=======
'''
TabWidget Class
Contains specification of the TabWidget class for the main window of the program.
'''
from PyQt5 import QtWidgets, QtCore #Needed imports
class TabBar(QtWidgets.QTabBar): #used within the TabWidget class.  This is the tabs on the side
    def tabSizeHint(self, index): #used for formatting
        s = QtWidgets.QTabBar.tabSizeHint(self, index) #get the size of this tab
        s.transpose() #rotate the tab
        return s #return it
>>>>>>> 8c5826452d6865ac469e6012a8aaf80d023d444c

    #how do we change the colors of the tabs?
    def paintEvent(self, event): #creates the tabs within the tab bar
        painter = QtWidgets.QStylePainter(self) #Creates the tab bars on the screen
        opt = QtWidgets.QStyleOptionTab() #Gives the tab bars their style

        for i in range(self.count()): #for each tab bar (here we have 2)
            self.initStyleOption(opt, i) #create style options
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt) #draw the tab
            painter.save() #save the tab

            s = opt.rect.size() #resize to specs
            s.transpose() #rotate the tab so it is sideways instead of vertical
            r = QtCore.QRect(QtCore.QPoint(), s) #shaped as a rectangle
            r.moveCenter(opt.rect.center()) #center text
            opt.rect = r #rectangle object is saved

            c = self.tabRect(i).center() #center rectangle object
            painter.translate(c) #move the tabs to align
            painter.rotate(90) #rotate the window that the tab is inside
            painter.translate(-c) #move tab back so now it is correct location and orientation
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt); #Label the tab
            painter.restore() #finish execution


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs) #init this object
        self.setTabBar(TabBar(self)) #create tab bar object and link it
        self.setTabPosition(QtWidgets.QTabWidget.West) #set on left side of window
