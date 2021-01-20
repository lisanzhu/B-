# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\360MoveData\Users\子嘿\Desktop\最终待用UI\UI文件\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import copy
import xml.sax
import linecache
import os
import pickle
import sys
from bisect import bisect_right, bisect_left
from collections import deque
import xml.sax
import string
#demo1和2是功能一，3和4是功能二，5和6是功能三，7是功能四，8和9是功能五，10是功能6
import final_write
import Ui_demo1
import Ui_demo3
import Ui_demo5
import Ui_demo7
import Ui_demo8
import Ui_demo10
from final_read import KeyValue,Bptree

sys.setrecursionlimit(1000000000)



class Ui_Form(object):
    def setupUi(self, Form,b_article,b_author,author,title_lis,hot_w):
        Form.setObjectName("Form")
        Form.resize(484, 332)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.form=Form
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.bPTree_article=b_article
        self.bPTree_author=b_author
        self.author=author
        self.title_list=title_lis
        self.how_word=hot_w

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "文献管理系统1.0"))
        self.pushButton_2.setText(_translate("Form", "搜索文章"))
        self.pushButton_4.setText(_translate("Form", "展示文章数最多的作者"))
        self.pushButton.setText(_translate("Form", "搜索作者"))
        self.pushButton_3.setText(_translate("Form", "搜索作者合作关系"))
        self.pushButton_5.setText(_translate("Form", "部分匹配搜索"))
        self.pushButton_6.setText(_translate("Form", "展示各年热词"))

        self.pushButton.clicked.connect(self.jump_to_1)
        self.pushButton_2.clicked.connect(self.jump_to_2)
        self.pushButton_3.clicked.connect(self.jump_to_3)
        self.pushButton_4.clicked.connect(self.jump_to_4)
        self.pushButton_5.clicked.connect(self.jump_to_5)
        self.pushButton_6.clicked.connect(self.jump_to_6)


    def jump_to_1(self):#功能一
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = Ui_demo1.Ui_Form()
        ui.setupUi(form1,self.bPTree_author)
        form1.show()
        form1.exec_()
        self.form.show()

    def jump_to_2(self):
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = Ui_demo3.Ui_Form()
        ui.setupUi(form1,self.bPTree_article)
        form1.show()
        form1.exec_()
        self.form.show()

    def jump_to_3(self):
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = Ui_demo5.Ui_Form()
        ui.setupUi(form1,self.bPTree_author)
        form1.show()
        form1.exec_()
        self.form.show()

    def jump_to_4(self):
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = Ui_demo7.Ui_Form()
        ui.setupUi(form1,self.author)
        form1.show()
        form1.exec_()
        self.form.show()

    def jump_to_5(self):
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = Ui_demo8.Ui_Form()
        ui.setupUi(form1,self.title_list,self.bPTree_article)
        form1.show()
        form1.exec_()
        self.form.show()

    def jump_to_6(self):
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = Ui_demo10.Ui_Form()
        ui.setupUi(form1,self.how_word)
        form1.show()
        form1.exec_()
        self.form.show()


if __name__ == "__main__":
    f = open('data_articleTree.txt', 'rb')
    bPTree_article = pickle.load(f)
    f.close()
    f = open('data_authorTree.txt', 'rb')
    bPTree_author = pickle.load(f)
    f.close()
    f = open('data_author.txt', 'rb')
    author = pickle.load(f)
    f.close()
    f = open('title_list.txt', 'rb')
    title_list = pickle.load(f)
    f.close()
    f = open('hot_word.txt', 'rb')
    hot_word = pickle.load(f)
    f.close()
    app = QApplication(sys.argv)
    form = QtWidgets.QWidget()
    window = Ui_Form()
    window.setupUi(form,bPTree_article,bPTree_author,author,title_list,hot_word)
    form.show()
    sys.exit(app.exec_())