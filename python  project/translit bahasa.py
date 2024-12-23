import sys
import os
import random
from deep_translator import GoogleTranslator
import gtts

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

class Translator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        vb = QVBoxLayout() 
        self.setLayout(vb)

        font = QFont("Times", 14)

        self.insert_text = QTextEdit()
        self.insert_text.setFont(font)
        vb.addWidget(self.insert_text)

        self.show_translation = QTextEdit()
        self.show_translation.setFont(font)
        vb.addWidget(self.show_translation)

        self.translatebtn = QPushButton("Translate")
        self.translatebtn.setFont(font)
        vb.addWidget(self.translatebtn)

        self.playsoundbtn = QPushButton("Play Sound")
        self.playsoundbtn.setFont(font)
        vb.addWidget(self.playsoundbtn)

        self.combo = QComboBox()
        self.combo.setFont(font)
        bahasa = ["Arabic", "English", "French", "Indonesia", "Japanese", "Korean", "Afrikaans", "Malay", "Thai"]
        self.combo.addItems(bahasa)
        self.combo.setEditable(True)
        from PyQt5.QtCore import Qt
        self.combo.lineEdit().setAlignment(Qt.AlignCenter)
        vb.addWidget(self.combo)
        self.target = {"Arabic":"ar", "English":"en","French":"fr", "Indonesia":"id", "Japanese":"ja", "Korean":"ko", "Afrikaans":"af","Malay":"ms", "Thai":"th"}

        self.player = QMediaPlayer()
        self.translatebtn.clicked.connect(self.translate_text)
        self.playsoundbtn.clicked.connect(self.play_sound)

    def translate_text(self):
        global mp3
        mp3 = random.randint(10000, 1000000)
        target = self.target[self.combo.currentText()]
        text = self.insert_text.toPlainText()
        translated = GoogleTranslator(source="auto", target=target).translate(text)
        self.show_translation.clear()
        self.show_translation.setText(translated)
        tts = gtts.gTTS(translated, lang=target)
        tts.save(str(mp3)+'.mp3')

    def play_sound(self):
        path = os.path.join(os.getcwd(), str(mp3) + '.mp3')

        from PyQt5.QtCore import QUrl
        url = QUrl.fromLocalFile(path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()



def main():
    app = QApplication(sys.argv)
    gui = Translator()
    gui.resize(800, 500)
    gui.move(100, 100)

    gui.setWindowTitle("indra python project 2024")
    gui.show()
    sys.exit(app.exec_())




if __name__ == "__main__":
    main()

