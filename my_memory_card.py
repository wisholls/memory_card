from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup
from random import randint
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Как называют животное которое передвигается прыжком?', "кенгуру", 'леопард', 'кролик', 'антилопа'))
question_list.append(Question('Какой вид у рыся?', 'млекопитающие', 'земноводные', 'парнокопытные', 'птицы'))
question_list.append(Question('Какое животное известно как царь зверей', 'лев', 'тигр', 'гепард', 'леопард'))
question_list.append(Question('Какое животное является самым высоким сухопутным животным?', 'слон', 'жираф', 'бегмот', 'носорог'))
question_list.append(Question('Самое маленькое животное в мире?', 'Калибри', 'тушканчик', 'хомяк', 'Свиносная летучая мышь'))
question_list.append(Question('Самое большое животное в мире?', 'Слон', 'Кит', 'Акула', 'динозавр'))
question_list.append(Question('Какое животное купается в грязи?', 'свинья', 'собака', 'кошка', 'обезьяна'))
question_list.append(Question('Сколько пород собак существует?', '100', 'около 400', '130', '260'))
question_list.append(Question('У какой кошки нет шерсти?', 'Британская', 'Сиамская', 'Сфинкс', 'Мейн-кун'))
question_list.append(Question('Какого животного не существует?', 'Единорог', 'тритон', 'утконос', 'бобер'))
question_list.append(Question('Какой раскрас у леопарда?', 'черные пятна', 'в полоску', 'нету', 'в крапинку'))
question_list.append(Question('Какое животное известно своей способностью менять цвет кожи?', 'хамелеон', 'змея', 'ящерица', 'червяк'))
question_list.append(Question('Какое животное самое быстрое в воде?', 'акула', 'парусник-рыба', 'горбуша', 'кит'))
question_list.append(Question('Какое животное известно своими длинными ушами и быстрыми ногами?', 'Лев', 'кролик', 'жираф', 'мышь'))
question_list.append(Question('Какойхищник имеет черные и белые полоски?', 'Зебра', 'Тигр', 'Леопард', 'кошка'))
question_list.append(Question('Какое животное откладывает яйца и имеет чешую?','Змея', 'Птица', 'Рыба', 'Яшерица'))
question_list.append(Question('Какое животное является смучтатым?','коала', 'свинья', 'обезьяна', 'ленивец'))
question_list.append(Question('Какой вид насекомых имеет шесть ног и прозрачные крылья?','бабочка', 'пчела', 'муравей', 'комар'))
question_list.append(Question('Какое животное является земноводным?','лягушка', 'крокодил', 'черепаха', 'рыба'))
question_list.append(Question('Какой вид птиц не умеет летать?','страус', 'орел', 'воробей', 'голубь'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.move(900,70)
main_win.resize(400,200)
text = QLabel('Как называют животное которое передвигается прыжком?')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton("кенгуру")
rbtn_2 = QRadioButton("леопард")
rbtn_3 = QRadioButton("кролик")
rbtn_4 = QRadioButton("антилопа")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
button = QPushButton('Ответить')

AnsGroupBox = QGroupBox('результат теста')
RadioGroupBox.show()
AnsGroupBox.hide()
#RadioGroupBox.hide() временно прячем вариантов ответов
result = QLabel('правильно/неправильно')
itog = QLabel('правильный ответ')

layout_res = QHBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog)
AnsGroupBox.setLayout(layout_res)





line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(text, alignment=Qt.AlignHCenter | Qt.AlignVCenter )
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3.addWidget(button, alignment=Qt.AlignHCenter | Qt.AlignVCenter)

glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)

def show_result(): #панель ответов
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('следующий вопрос')

def show_question(): #панель с вопросом и вариантами ответов
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #сбросить выблор кнопки

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers) #метод для перемешивания списка из кнопок
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question) #вопрос
    itog.setText(q.right_answer) #ответ
    show_question() #функция с панелью вопросов и варинатов ответов

def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неверно')
def next_question():
    main_win.cur_question += 1 #переход к следующему вопросу
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0 #обнуляем счетчик
    q = question_list[main_win.cur_question] #взяли
    ask(q) #спросили

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


main_win.cur_question = -1 #номер отображающего вопроса


q = Question('Как называют животное которое передвигается прыжком?', "кенгуру", 'леопард', 'кролик', 'антилопа')



button.clicked.connect(click_ok)
next_question()
main_win.setLayout(glav)
main_win.show()
app.exec_()