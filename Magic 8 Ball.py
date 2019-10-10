"""

-----------------------------------------------TASK-----------------------------------------------------------

    I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it
    right side up and it gives an answer by way of a floating die with responses written on it.

----------------------------------------------RULES-----------------------------------------------------------

    Allow the user to enter their question
    Display an in progress message( i.e. "thinking")
    Create 20 responses, and show a random response
    Allow the user to ask another question or quit
----------------------------------------------BONUS-----------------------------------------------------------
    A box for users to enter the question
    At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)

"""

import random
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot

#Dictionary for answer on question

answer = \
            {
                1: 'Answer1',
                2: 'Answer2',
                3: 'Answer3',
                4: 'Answer4',
                5: 'Answer5',
                6: 'Answer6',
                7: 'Answer7',
                8: 'Answer8',
                9: 'Answer9',
                10: 'Answer10',
                11: 'Answer11',
                12: 'Answer12',
                13: 'Answer13',
                14: 'Answer14',
                15: 'Answer15',
                16: 'Answer16',
                17: 'Answer17',
                18: 'Answer18',
                19: 'Answer19',
                20: 'Answer20',
            }
#Method for answer. Return string answer. Random number in range 1-20
def give_answer_gui():
    return 'My answer: {0}'.format(answer[random.randrange(1, 20)])

#Class for Qwidget with 4 buttons, 1 label, 1 lineEdit
#4 Methotds for push buttons
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        self.labelans = QLabel(self)
        self.labelans.setToolTip('')
        self.labelans.setText('')
        self.labelans.resize(150, 50)
        self.labelans.move(170, 37.5)

        self.textarea = QLineEdit(self)
        self.textarea.setToolTip('')
        self.textarea.resize(200, 25)
        self.textarea.move(50, 15)

        self.btnAns = QPushButton('SHOW ANSWER', self)
        self.btnAns.setToolTip('Press this button for answer')
        self.btnAns.resize(self.btnAns.sizeHint())
        self.btnAns.move(50, 50)
        self.btnAns.clicked.connect(self.on_click)

        self.btnClear = QPushButton('CLEAR', self)
        self.btnClear.setToolTip('Press this button for clear question')
        self.btnClear.resize(self.btnClear.sizeHint())
        self.btnClear.move(50, 85)
        self.btnClear.clicked.connect(self.on_clear)

        self.btnPlayAgain = QPushButton('PLAY AGAIN', self)
        self.btnPlayAgain.setToolTip('Press this button for play again')
        self.btnPlayAgain.resize(self.btnPlayAgain.sizeHint())
        self.btnPlayAgain.move(50, 120)
        self.btnPlayAgain.clicked.connect(self.on_playAgain)

        self.btnQuit = QPushButton('QUIT', self)
        self.btnQuit.setToolTip('Press this button for quit')
        self.btnQuit.resize(self.btnQuit.sizeHint())
        self.btnQuit.move(50, 155)
        self.btnQuit.clicked.connect(self.on_quit)

        self.setGeometry(350, 350, 350, 250)
        self.setWindowTitle('Tooltips')
        self.show()

    #Methods for buttons
    @pyqtSlot()
    def on_click(self):
        self.btnAns.setEnabled(False)
        self.labelans.setText(give_answer_gui())

    def on_clear(self):
        self.btnAns.setEnabled(True)
        self.labelans.setText('')
        self.textarea.setText('')

    def on_playAgain(self):
        self.btnAns.setEnabled(True)
        self.labelans.setText('')
        self.textarea.setText('')

    def on_quit(self):
        self.close()

if __name__ == '__main__':
    # Choose style Magic Ball
    print("Enter 1 for console style\nEnter 2 for gui style")
    try:
        cons_or_gui = int(input("Please, choose my style: "))
        if cons_or_gui == 1:
            question = input('Please, ask a question: ')
            print('I\'m thinking...')
            time.sleep(3)
            print('My answer: {0}'.format(answer[random.randrange(1, 20)]))
        elif cons_or_gui == 2:
            app = QApplication(sys.argv)
            ex = Example()
            sys.exit(app.exec_())
        else:
            print("Not 1 or 2 enter")
    except Exception:
        print('Fatal error')