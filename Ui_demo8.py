# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\360MoveData\Users\子嘿\Desktop\最终待用UI\UI文件\demo8.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_demo9


class Ui_Form(object):
    def setupUi(self, Form,tit,art):
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
        self.title_list=tit
        self.bPTree_article=art

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请在框中输入关键词"))
        self.pushButton_2.setText(_translate("Form", "搜索"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.pushButton.clicked.connect(self.jump_to_main)
        self.pushButton_2.clicked.connect(self.search)

    def jump_to_main(self):
        self.form.close()

    def search(self):
        s=self.lineEdit.text()
        titles=[]
        for i in range(len(self.title_list)):
            if s in self.title_list[i]:
                titles.append(self.title_list[i])
        form1 = QtWidgets.QDialog()
        ui = Ui_demo9.Ui_Form()
        ui.setupUi(form1,titles,self.bPTree_article)
        form1.show()
        form1.exec_()

