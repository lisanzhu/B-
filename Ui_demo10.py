# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\360MoveData\Users\子嘿\Desktop\最终待用UI\UI文件\demo10.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form,hot):
        Form.setObjectName("Form")
        Form.resize(400, 299)
        self.form=Form
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 381, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.hot_word=hot
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        for year in sorted(self.hot_word):
            if(len(year)==4):
                self.textBrowser.append(year + ":")
                times = 0
                for k in sorted(self.hot_word[year], key=self.hot_word[year].__getitem__, reverse=True):
                    self.textBrowser.append(k+" :"+str(self.hot_word[year][k]))
                    times = times + 1
                    if times == 10:
                        break
                self.textBrowser.append("")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.label.setText(_translate("Form", "展示结果如下"))
        self.pushButton.clicked.connect(self.jump_to_main)

    def jump_to_main(self):
        self.form.close()
