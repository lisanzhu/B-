# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\360MoveData\Users\子嘿\Desktop\最终待用UI\UI文件\demo5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_demo6


class Ui_Form(object):
    def setupUi(self, Form,bPTree_author):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.form=Form
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.bPTree_author=bPTree_author

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请在框中输入完整的作者姓名"))
        self.pushButton_2.setText(_translate("Form", "搜索"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.pushButton.clicked.connect(self.jump_to_main)
        self.pushButton_2.clicked.connect(self.search)

    def jump_to_main(self):
        self.form.close()

    def search(self):
        author_name=self.lineEdit.text()
        tem_result=self.bPTree_author.search(author_name, author_name)
        form1 = QtWidgets.QDialog()
        ui6 = Ui_demo6.Ui_Form()
        ui6.setupUi(form1,tem_result,author_name)
        form1.show()
        form1.exec_()
