# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\360MoveData\Users\子嘿\Desktop\最终待用UI\UI文件\demo4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import final_read


class Ui_Form(object):
    def setupUi(self, Form,result):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.form=Form
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.result=result

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        for k in self.result:
            for k in result:
                dic=final_read.getContent(k.value)
                for num, imformation in dic.items():
                    for k,v in imformation.items():
                        if(type(v)==list):
                            lis=""
                            for i in v:
                                lis=lis+i
                                lis=lis+", "
                            self.textBrowser.append(k+":"+lis)
                        else:
                            self.textBrowser.append(k+":"+v)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "搜索结果如下"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.pushButton.clicked.connect(self.jump_to_main)

    def jump_to_main(self):
        self.form.close()
