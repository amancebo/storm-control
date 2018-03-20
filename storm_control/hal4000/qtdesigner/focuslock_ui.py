# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'focuslock.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 242)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(10000, 10000))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.modeBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeBox.sizePolicy().hasHeightForWidth())
        self.modeBox.setSizePolicy(sizePolicy)
        self.modeBox.setObjectName("modeBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.modeBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.modeComboBox = QtWidgets.QComboBox(self.modeBox)
        self.modeComboBox.setObjectName("modeComboBox")
        self.verticalLayout.addWidget(self.modeComboBox)
        spacerItem = QtWidgets.QSpacerItem(151, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lockLabel = QtWidgets.QLabel(self.modeBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lockLabel.sizePolicy().hasHeightForWidth())
        self.lockLabel.setSizePolicy(sizePolicy)
        self.lockLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lockLabel.setObjectName("lockLabel")
        self.horizontalLayout_4.addWidget(self.lockLabel)
        self.lockTargetSpinBox = QtWidgets.QSpinBox(self.modeBox)
        self.lockTargetSpinBox.setMinimum(-100000)
        self.lockTargetSpinBox.setMaximum(100000)
        self.lockTargetSpinBox.setObjectName("lockTargetSpinBox")
        self.horizontalLayout_4.addWidget(self.lockTargetSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lockButton = QtWidgets.QPushButton(self.modeBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lockButton.sizePolicy().hasHeightForWidth())
        self.lockButton.setSizePolicy(sizePolicy)
        self.lockButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lockButton.setCheckable(True)
        self.lockButton.setObjectName("lockButton")
        self.horizontalLayout.addWidget(self.lockButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.modeBox)
        self.jumpControlBox = QtWidgets.QGroupBox(Dialog)
        self.jumpControlBox.setObjectName("jumpControlBox")
        self.gridLayout = QtWidgets.QGridLayout(self.jumpControlBox)
        self.gridLayout.setObjectName("gridLayout")
        self.jumpSpinBox = QtWidgets.QDoubleSpinBox(self.jumpControlBox)
        self.jumpSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.jumpSpinBox.setMinimum(0.0)
        self.jumpSpinBox.setMaximum(100.0)
        self.jumpSpinBox.setSingleStep(0.01)
        self.jumpSpinBox.setObjectName("jumpSpinBox")
        self.gridLayout.addWidget(self.jumpSpinBox, 0, 0, 1, 1)
        self.jumpLabel = QtWidgets.QLabel(self.jumpControlBox)
        self.jumpLabel.setObjectName("jumpLabel")
        self.gridLayout.addWidget(self.jumpLabel, 0, 1, 1, 1)
        self.jumpPButton = QtWidgets.QPushButton(self.jumpControlBox)
        self.jumpPButton.setObjectName("jumpPButton")
        self.gridLayout.addWidget(self.jumpPButton, 1, 0, 1, 1)
        self.jumpNButton = QtWidgets.QPushButton(self.jumpControlBox)
        self.jumpNButton.setObjectName("jumpNButton")
        self.gridLayout.addWidget(self.jumpNButton, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.jumpControlBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lockDisplayWidget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lockDisplayWidget.sizePolicy().hasHeightForWidth())
        self.lockDisplayWidget.setSizePolicy(sizePolicy)
        self.lockDisplayWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.lockDisplayWidget.setObjectName("lockDisplayWidget")
        self.verticalLayout_3.addWidget(self.lockDisplayWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HAL-4000 Focus Lock"))
        self.modeBox.setTitle(_translate("Dialog", "Mode"))
        self.lockLabel.setText(_translate("Dialog", "Locked To:"))
        self.lockButton.setText(_translate("Dialog", "Lock"))
        self.jumpControlBox.setTitle(_translate("Dialog", "Jump Control"))
        self.jumpLabel.setText(_translate("Dialog", "Offset (um)"))
        self.jumpPButton.setText(_translate("Dialog", "Jump (+)"))
        self.jumpNButton.setText(_translate("Dialog", "Jump (-)"))
        self.okButton.setText(_translate("Dialog", "Ok"))

