#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license

# Title: PyQt5 lesson 14              Version: 1.0
# Date: 09-01-17                      Language: python3
# Description: pyqt5 gui and opening files
# pythonprogramming.net from PyQt4 to PyQt5
###############################################################
# do something
import re
import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 180, 230)
        self.setWindowTitle('C4d Comp-Simple Hum')
        self.setWindowIcon(QIcon('pic.png'))

        extractAction = QAction('Quit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)

        openEditor = QAction('&Editor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = QAction('&Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)

        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)

        extractAction = QAction(QIcon('pic.png'), 'flee the scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar('extraction')
        self.toolBar.addAction(extractAction)

        self.file  = None
        self.run = QAction(QIcon('down.png'), 'Run', self)
        self.run.triggered.connect(self.advice)

        self.toolBar = self.addToolBar('extraction')
        self.toolBar.addAction(self.run)

        self.home()

    def editor(self):
        print(self.file)
        self.run.triggered.disconnect(self.advice)
        self.run.triggered.connect(self.encoder)        
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)



    def file_open(self):
        # need to make name an tupple otherwise i had an error and app crashed
        try:
            self.name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
            self.file = open(self.name, 'r')
            self.editor()


            with self.file:
                text = self.file.read()
                self.textEdit.setText(text)

        except:pass

    def encoder(self):
        R2 = []
        R = []
        l = []
        new = []

        def splitter(t):
            l = ''.join(str(x) for x in t)
            res = []
            for x in str(l):
                if x not in ["'","]"]:
                    res.append(x)
            return res

        def converter(R):
            new = []
            for m in R:               
                try:
                    if m in ['0','1']: new.append(int(m))
                    else: new.append(float(m[:4]))
                except:
                    if m != '':
                        new.append(m)
            return new

        file = open(self.name, 'r')
        for x in ''.join(file):
            l.append(x)   
        file.close()


        for x in range(len(l)):
            if x+4 == len(l):break
            if l[x] + l[x+1] + l[x+2]+ l[x+3]+ l[x+4] in ['point','coordIndex']:
                local = []
                for z in l[x+7:]:
                    if z == ']': 
                        R = (''.join(local))
                        break  
                    elif z != '':
                        local.append(z)
                ender = R[::]
                R  = re.split(r'(;|,|\s)\s*', R)
                R2 = converter(R)
                counter = 0 
                
                #l[len(splitter(ender))+7+x] = 'LEONARDO'
                l[x+7:len(splitter(ender))+7+x] = splitter(R2)
                
                counter += 1
                

        EXPORT = open('result.wrl','w+')
        EXPORT.write(''.join(l))
        EXPORT.close()

##End of code problem

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(50, 100)



        sf = QPushButton('Select File', self)
        sf.clicked.connect(self.file_open)
        sf.resize(btn.sizeHint())
        sf.move(50, 150)


        self.show()

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)




    def close_application(self):

        choice = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            print('quit application')
            sys.exit()
        else:
            pass
    def advice(self):
        choice = QMessageBox.question(self, 'Message',
                                     "No file selected", QMessageBox.Ok)

if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
