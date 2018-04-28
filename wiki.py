from PyQt5 import QtCore, QtGui, QtWidgets
import wolframalpha
import wikipedia
import speech_recognition as sr
import text_to_speech
from settings import Ui_Dialog as Settings
from time import sleep
import pickle
import os.path as path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 50, 251, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.runit)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 110, 671, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(290, 140, 401, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 91, 31))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 190, 721, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 651, 251))
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(310, 20, 151, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QPushButton(Dialog)
        self.label_6.setGeometry(QtCore.QRect(630, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.clicked.connect(self.open)
        self.label_6.setObjectName("label_6")
        if path.exists("settings.p"):
            if path.isfile("settings.p"):
                self.settings = pickle.load(open("settings.p", "rb"))
            else:
                self.settings = None
        else:
            self.settings = None
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wikibot"))
        self.pushButton_2.setText(_translate("Dialog", "CLICK TO ASK QUESTION"))
        self.label.setText(_translate("Dialog", "Click here to ask questions from Wikibot, and it will provide you appropiate answers using AI."))
        self.label_2.setText(_translate("Dialog", "You can type the question here"))
        self.label_3.setText(_translate("Dialog", "Response"))
        self.label_4.setText(_translate("Dialog", "..."))
        self.label_5.setText(_translate("Dialog", "WIKIBOT"))
        self.label_6.setText(_translate("Dialog", "Settings"))

    def open(self):
        Dialog = QtWidgets.QDialog()
        Dialog.ui = Settings()
        Dialog.ui.setupUi(Dialog)
        Dialog.exec_()
        Dialog.show()

    def runit(self):
        query = self.speech_to_text()
        if query is not None:
            sleep(0.05)
            self.lineEdit.setText(query)
            QtWidgets.QApplication.processEvents()
            # Create a new instance of the Firefox driver
            result_wiki = self.find(query)
            answer = self.find_wolfram(query)

            if answer and len(answer) >= 10:
                self.label_4.setText(answer)
                text_to_speech.speak_content(answer)
            elif result_wiki and len(result_wiki) > 10:
                self.label_4.setText(result_wiki)
                text_to_speech.speak_content(result_wiki)
            else:
                self.label_4.setText("No Search Result Found.")

    def find(self, query):
        try:
            summary = wikipedia.summary(query)
        except:
            summary = "Could you be more specific ?"
        return summary

    def find_wolfram(self, query):
        answer_text = None
        if self.settings is not None:
            app_id = self.settings.get('Wolfram ID')
        else:
            app_id = "VR3V3L-3LQ39KPVJA"
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        for data in res.pods:
            if data.get('@title') == 'Definitions':
                if data.get('subpod').get('img').get('@alt'):
                    answer_text = (data.get('subpod').get('img').get('@alt'))
                break
            elif data.get('@title') == 'Basic information':
                if data.get('subpod').get('img').get('@alt'):
                    answer_text = (data.get('subpod').get('img').get('@alt'))
                break
        return answer_text

    def speech_to_text(self):
        if self.settings is not None:
            config = {
                "url": "https://stream.watsonplatform.net/speech-to-text/api",
                "username": self.settings.get('Username'),
                "password": self.settings.get('Password')
            }
        else:
            config = {
                "url": "https://stream.watsonplatform.net/speech-to-text/api",
                "username": "f15abd3a-3703-4f7e-8967-cc2a2ad4e5ab",
                "password": "j4e3PFrUHbGK"
            }
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            sleep(0.05)
            self.label_4.setText("Listening...")
            QtWidgets.QApplication.processEvents()
            audio = r.listen(source, phrase_time_limit=5)  # read the entire audio file
        # Signup for IBM watson here https://www.ibm.com/watson/ and get the username and password.
        IBM_USERNAME = config[
            'username']  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
        IBM_PASSWORD = config['password']  # IBM Speech to Text passwords are mixed-case alphanumeric strings
        try:
            sleep(0.05)
            self.label_4.setText("Processing... ")
            QtWidgets.QApplication.processEvents()
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
            return text
        except sr.UnknownValueError:
            text = "IBM Speech to Text could not understand audio. Please try again."
            sleep(0.05)
            self.label_4.setText(text)
            QtWidgets.QApplication.processEvents()
            return None
        except sr.RequestError as e:
            print("Could not request results from IBM Speech to Text service; {0}".format(e))
            sleep(0.05)
            self.label_4.setText("Could not request results from IBM Speech to Text service; {0}".format(e))
            QtWidgets.QApplication.processEvents()
            return None
        except Exception as e:
            print(e)
            sleep(0.05)
            self.label_4.setText("Exception: {0}".format(e))
            QtWidgets.QApplication.processEvents()
            return None


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())