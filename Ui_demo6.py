# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\360MoveData\Users\子嘿\Desktop\最终待用UI\UI文件\demo6.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import final_read
import string

class Ui_Form(object):
    def setupUi(self, Form,result,author_name):
        Form.setObjectName("Form")
        Form.resize(400, 302)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        lis2=[]
        for i in result:
                for k in final_read.getContent(i.value).values():
                    if 'author' in k:
                        for auth in k.get('author'):
                            if auth not in lis2:
                                lis2.append(auth)

                # for k in i.value:
                #     for arti in bPTree_article.search(k[0], k[0]):
                #         if 'author' in arti.value:
                #             for auth in arti.value.get('author'):
                #                 if auth not in lis2:
                #                     lis2.append(auth)
        if author_name in lis2:
            lis2.remove(author_name)
        stri=""
        i=0
        for name in lis2:
            stri=stri+name
            if(i<5):
                stri=stri+", "
                i=i+1
            else:
                self.textBrowser.append(stri)
                stri=""
                i=0
        if(i!=0):
            self.textBrowser.append(stri)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "搜索结果如下"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.pushButton.clicked.connect(self.jump_to_main)

    def jump_to_main(self):
        self.form.close()
