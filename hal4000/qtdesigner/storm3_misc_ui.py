# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storm3-misc.ui'
#
# Created: Tue Mar 25 10:37:35 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(322, 392)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(322, 392))
        Dialog.setMaximumSize(QtCore.QSize(322, 392))
        self.TIRFgroupBox = QtGui.QGroupBox(Dialog)
        self.TIRFgroupBox.setGeometry(QtCore.QRect(9, 9, 304, 111))
        self.TIRFgroupBox.setObjectName(_fromUtf8("TIRFgroupBox"))
        self.leftLargeButton = QtGui.QPushButton(self.TIRFgroupBox)
        self.leftLargeButton.setGeometry(QtCore.QRect(53, 20, 31, 24))
        self.leftLargeButton.setObjectName(_fromUtf8("leftLargeButton"))
        self.rightSmallButton = QtGui.QPushButton(self.TIRFgroupBox)
        self.rightSmallButton.setGeometry(QtCore.QRect(106, 20, 21, 24))
        self.rightSmallButton.setObjectName(_fromUtf8("rightSmallButton"))
        self.positionLabel = QtGui.QLabel(self.TIRFgroupBox)
        self.positionLabel.setGeometry(QtCore.QRect(210, 20, 81, 16))
        self.positionLabel.setObjectName(_fromUtf8("positionLabel"))
        self.positionText = QtGui.QLabel(self.TIRFgroupBox)
        self.positionText.setGeometry(QtCore.QRect(230, 40, 46, 14))
        self.positionText.setText(_fromUtf8(""))
        self.positionText.setObjectName(_fromUtf8("positionText"))
        self.EPIButton = QtGui.QPushButton(self.TIRFgroupBox)
        self.EPIButton.setGeometry(QtCore.QRect(10, 20, 41, 24))
        self.EPIButton.setObjectName(_fromUtf8("EPIButton"))
        self.TIRFButton = QtGui.QPushButton(self.TIRFgroupBox)
        self.TIRFButton.setGeometry(QtCore.QRect(160, 20, 41, 24))
        self.TIRFButton.setObjectName(_fromUtf8("TIRFButton"))
        self.rightLargeButton = QtGui.QPushButton(self.TIRFgroupBox)
        self.rightLargeButton.setGeometry(QtCore.QRect(128, 20, 31, 24))
        self.rightLargeButton.setObjectName(_fromUtf8("rightLargeButton"))
        self.leftSmallButton = QtGui.QPushButton(self.TIRFgroupBox)
        self.leftSmallButton.setGeometry(QtCore.QRect(85, 20, 20, 24))
        self.leftSmallButton.setObjectName(_fromUtf8("leftSmallButton"))
        self.moveGroupBox = QtGui.QGroupBox(self.TIRFgroupBox)
        self.moveGroupBox.setGeometry(QtCore.QRect(10, 50, 191, 51))
        self.moveGroupBox.setObjectName(_fromUtf8("moveGroupBox"))
        self.tirSpinBox = QtGui.QDoubleSpinBox(self.moveGroupBox)
        self.tirSpinBox.setGeometry(QtCore.QRect(10, 20, 71, 22))
        self.tirSpinBox.setDecimals(3)
        self.tirSpinBox.setMaximum(25.0)
        self.tirSpinBox.setSingleStep(0.001)
        self.tirSpinBox.setProperty("value", 21.0)
        self.tirSpinBox.setObjectName(_fromUtf8("tirSpinBox"))
        self.tirGoButton = QtGui.QPushButton(self.moveGroupBox)
        self.tirGoButton.setGeometry(QtCore.QRect(98, 19, 75, 24))
        self.tirGoButton.setObjectName(_fromUtf8("tirGoButton"))
        self.dYAGGroupBox = QtGui.QGroupBox(Dialog)
        self.dYAGGroupBox.setGeometry(QtCore.QRect(9, 126, 304, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dYAGGroupBox.sizePolicy().hasHeightForWidth())
        self.dYAGGroupBox.setSizePolicy(sizePolicy)
        self.dYAGGroupBox.setObjectName(_fromUtf8("dYAGGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dYAGGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filter1Button = QtGui.QPushButton(self.dYAGGroupBox)
        self.filter1Button.setCheckable(True)
        self.filter1Button.setAutoExclusive(True)
        self.filter1Button.setObjectName(_fromUtf8("filter1Button"))
        self.horizontalLayout.addWidget(self.filter1Button)
        self.filter2Button = QtGui.QPushButton(self.dYAGGroupBox)
        self.filter2Button.setCheckable(True)
        self.filter2Button.setAutoExclusive(True)
        self.filter2Button.setObjectName(_fromUtf8("filter2Button"))
        self.horizontalLayout.addWidget(self.filter2Button)
        self.filter3Button = QtGui.QPushButton(self.dYAGGroupBox)
        self.filter3Button.setCheckable(True)
        self.filter3Button.setAutoExclusive(True)
        self.filter3Button.setObjectName(_fromUtf8("filter3Button"))
        self.horizontalLayout.addWidget(self.filter3Button)
        self.filter4Button = QtGui.QPushButton(self.dYAGGroupBox)
        self.filter4Button.setCheckable(True)
        self.filter4Button.setAutoExclusive(True)
        self.filter4Button.setObjectName(_fromUtf8("filter4Button"))
        self.horizontalLayout.addWidget(self.filter4Button)
        self.filter5Button = QtGui.QPushButton(self.dYAGGroupBox)
        self.filter5Button.setCheckable(True)
        self.filter5Button.setAutoExclusive(True)
        self.filter5Button.setObjectName(_fromUtf8("filter5Button"))
        self.horizontalLayout.addWidget(self.filter5Button)
        self.filter6Button = QtGui.QPushButton(self.dYAGGroupBox)
        self.filter6Button.setCheckable(True)
        self.filter6Button.setAutoExclusive(True)
        self.filter6Button.setObjectName(_fromUtf8("filter6Button"))
        self.horizontalLayout.addWidget(self.filter6Button)
        self.okButton = QtGui.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(237, 359, 77, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.iEyesGroupBox = QtGui.QGroupBox(Dialog)
        self.iEyesGroupBox.setGeometry(QtCore.QRect(10, 190, 304, 161))
        self.iEyesGroupBox.setObjectName(_fromUtf8("iEyesGroupBox"))
        self.iEyesSaveButton = QtGui.QPushButton(self.iEyesGroupBox)
        self.iEyesSaveButton.setGeometry(QtCore.QRect(10, 45, 77, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iEyesSaveButton.sizePolicy().hasHeightForWidth())
        self.iEyesSaveButton.setSizePolicy(sizePolicy)
        self.iEyesSaveButton.setObjectName(_fromUtf8("iEyesSaveButton"))
        self.iEyesLabel = QtGui.QLabel(self.iEyesGroupBox)
        self.iEyesLabel.setGeometry(QtCore.QRect(150, 22, 141, 16))
        self.iEyesLabel.setObjectName(_fromUtf8("iEyesLabel"))
        self.iEyesAutoSaveButton = QtGui.QPushButton(self.iEyesGroupBox)
        self.iEyesAutoSaveButton.setGeometry(QtCore.QRect(90, 45, 77, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iEyesAutoSaveButton.sizePolicy().hasHeightForWidth())
        self.iEyesAutoSaveButton.setSizePolicy(sizePolicy)
        self.iEyesAutoSaveButton.setObjectName(_fromUtf8("iEyesAutoSaveButton"))
        self.iEyesResetButton = QtGui.QPushButton(self.iEyesGroupBox)
        self.iEyesResetButton.setGeometry(QtCore.QRect(220, 45, 77, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iEyesResetButton.sizePolicy().hasHeightForWidth())
        self.iEyesResetButton.setSizePolicy(sizePolicy)
        self.iEyesResetButton.setObjectName(_fromUtf8("iEyesResetButton"))
        self.iEyesROILabel = QtGui.QLabel(self.iEyesGroupBox)
        self.iEyesROILabel.setGeometry(QtCore.QRect(12, 74, 281, 20))
        self.iEyesROILabel.setObjectName(_fromUtf8("iEyesROILabel"))
        self.iEyesBackgroundSpinBox = QtGui.QSpinBox(self.iEyesGroupBox)
        self.iEyesBackgroundSpinBox.setGeometry(QtCore.QRect(90, 131, 61, 22))
        self.iEyesBackgroundSpinBox.setMaximum(10000)
        self.iEyesBackgroundSpinBox.setSingleStep(1)
        self.iEyesBackgroundSpinBox.setObjectName(_fromUtf8("iEyesBackgroundSpinBox"))
        self.iEyesBackgroundLabel = QtGui.QLabel(self.iEyesGroupBox)
        self.iEyesBackgroundLabel.setGeometry(QtCore.QRect(10, 133, 71, 16))
        self.iEyesBackgroundLabel.setObjectName(_fromUtf8("iEyesBackgroundLabel"))
        self.iEyesAccumulateLabel = QtGui.QLabel(self.iEyesGroupBox)
        self.iEyesAccumulateLabel.setGeometry(QtCore.QRect(159, 133, 81, 16))
        self.iEyesAccumulateLabel.setObjectName(_fromUtf8("iEyesAccumulateLabel"))
        self.iEyesAccumulateSpinBox = QtGui.QSpinBox(self.iEyesGroupBox)
        self.iEyesAccumulateSpinBox.setGeometry(QtCore.QRect(234, 131, 61, 22))
        self.iEyesAccumulateSpinBox.setMinimum(1)
        self.iEyesAccumulateSpinBox.setObjectName(_fromUtf8("iEyesAccumulateSpinBox"))
        self.iEyesLineEdit = QtGui.QLineEdit(self.iEyesGroupBox)
        self.iEyesLineEdit.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.iEyesLineEdit.setObjectName(_fromUtf8("iEyesLineEdit"))
        self.iEyesClearROIButton = QtGui.QPushButton(self.iEyesGroupBox)
        self.iEyesClearROIButton.setGeometry(QtCore.QRect(10, 99, 77, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iEyesClearROIButton.sizePolicy().hasHeightForWidth())
        self.iEyesClearROIButton.setSizePolicy(sizePolicy)
        self.iEyesClearROIButton.setObjectName(_fromUtf8("iEyesClearROIButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "HAL-4000 Miscellaneous Controls", None))
        self.TIRFgroupBox.setTitle(_translate("Dialog", "TIRF Control", None))
        self.leftLargeButton.setText(_translate("Dialog", "<<", None))
        self.rightSmallButton.setText(_translate("Dialog", ">", None))
        self.positionLabel.setText(_translate("Dialog", "Current Postion:", None))
        self.EPIButton.setText(_translate("Dialog", "EPI", None))
        self.TIRFButton.setText(_translate("Dialog", "TIRF", None))
        self.rightLargeButton.setText(_translate("Dialog", ">>", None))
        self.leftSmallButton.setText(_translate("Dialog", "<", None))
        self.moveGroupBox.setTitle(_translate("Dialog", "Move To", None))
        self.tirGoButton.setText(_translate("Dialog", "Go", None))
        self.dYAGGroupBox.setTitle(_translate("Dialog", "Filter Wheel", None))
        self.filter1Button.setText(_translate("Dialog", "1", None))
        self.filter2Button.setText(_translate("Dialog", "2", None))
        self.filter3Button.setText(_translate("Dialog", "3", None))
        self.filter4Button.setText(_translate("Dialog", "4", None))
        self.filter5Button.setText(_translate("Dialog", "5", None))
        self.filter6Button.setText(_translate("Dialog", "6", None))
        self.okButton.setText(_translate("Dialog", "Ok", None))
        self.iEyesGroupBox.setTitle(_translate("Dialog", "Imagine Eyes", None))
        self.iEyesSaveButton.setText(_translate("Dialog", "Save Frame", None))
        self.iEyesLabel.setText(_translate("Dialog", "filename", None))
        self.iEyesAutoSaveButton.setText(_translate("Dialog", "Auto Save", None))
        self.iEyesResetButton.setText(_translate("Dialog", "Reset", None))
        self.iEyesROILabel.setText(_translate("Dialog", "TextLabel", None))
        self.iEyesBackgroundLabel.setText(_translate("Dialog", "Background:", None))
        self.iEyesAccumulateLabel.setText(_translate("Dialog", "Accumulate:", None))
        self.iEyesLineEdit.setText(_translate("Dialog", "img.ch00", None))
        self.iEyesClearROIButton.setText(_translate("Dialog", "Reset ROI", None))

