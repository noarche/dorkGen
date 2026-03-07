# Disclaimer:
# This code/script/application/program is solely for educational and learning purposes.
# All information, datasets, images, code, and materials are presented in good faith and
# intended for instructive use. However, noarche make no representation or warranty, 
# express or implied, regarding the accuracy, adequacy, validity, reliability, availability,
# or completeness of any data or associated materials.
# Under no circumstance shall noarche have any liability to you for any loss, damage, or 
# misinterpretation arising due to the use of or reliance on the provided data. Your utilization
# of the code and your interpretations thereof are undertaken at your own discretion and risk.
#
# By executing script/code/application, the user acknowledges and agrees that they have read, 
# understood, and accepted the terms and conditions (or any other relevant documentation or 
#policy) as provided by noarche.
#
#Visit https://github.com/noarche for more information.

import sys
import os

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QPushButton,
    QFileDialog, QMessageBox, QGridLayout
)
from PyQt5.QtGui import QClipboard

# File paths
config_dir = './config/'
page_types_file = os.path.join(config_dir, 'page_types.txt')
page_formats_file = os.path.join(config_dir, 'page_formats.txt')
page_names_file = os.path.join(config_dir, 'page_names.txt')

disclaimer_text = (
    'The information and/or software provided here is intended solely for educational purposes and legal penetration testing purposes. '
    'By accessing or using this information and/or software, you acknowledge and agree that you assume full responsibility for your actions '
    'and any consequences that may result from those actions. The creators, contributors, and providers of this information and/or software '
    'shall not be held liable for any misuse or damage arising from its application. It is your responsibility to ensure that your use complies '
    'with all applicable laws and regulations.'
)

def read_config_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return file.read().strip()
    else:
        QMessageBox.critical(None, "Error", f"File not found: {filepath}")
        return ""

class DorkGen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("DorkGen")
        self.setStyleSheet("background-color: black; color: white;")

        self.init_ui()

    def init_ui(self):

        # Labels
        label_name = QLabel("Page Name")
        label_format = QLabel("Page Format")
        label_type = QLabel("Page Type")
        label_results = QLabel("Results:")

        # Text areas
        self.page_name = QTextEdit()
        self.page_format = QTextEdit()
        self.page_type = QTextEdit()
        self.output = QTextEdit()

        for box in [self.page_name, self.page_format, self.page_type, self.output]:
            box.setStyleSheet("background-color: black; color: white;")

        self.output.setText("..press generate for results..")

        # Load config values
        self.page_name.setText(read_config_file(page_names_file))
        self.page_format.setText(read_config_file(page_formats_file))
        self.page_type.setText(read_config_file(page_types_file))

        # Buttons
        btn_generate = QPushButton("Generate")
        btn_save = QPushButton("Save As")
        btn_copy = QPushButton("Copy to Clipboard")
        btn_about = QPushButton("About")

        btn_generate.clicked.connect(self.combine_texts)
        btn_save.clicked.connect(self.save_as)
        btn_copy.clicked.connect(self.copy_to_clipboard)
        btn_about.clicked.connect(self.show_about)

        # Layout
        layout = QGridLayout()

        layout.addWidget(label_name, 0, 0)
        layout.addWidget(label_format, 0, 1)
        layout.addWidget(label_type, 0, 2)

        layout.addWidget(self.page_name, 1, 0)
        layout.addWidget(self.page_format, 1, 1)
        layout.addWidget(self.page_type, 1, 2)

        layout.addWidget(label_results, 2, 0)

        layout.addWidget(self.output, 3, 0, 1, 3)

        layout.addWidget(btn_generate, 4, 0)
        layout.addWidget(btn_save, 4, 1)
        layout.addWidget(btn_copy, 4, 2)
        layout.addWidget(btn_about, 5, 1)

        self.setLayout(layout)

    def combine_texts(self):

        text1 = self.page_name.toPlainText().split('\n')
        text2 = self.page_format.toPlainText().split('\n')
        text3 = self.page_type.toPlainText().split('\n')

        output_text = []

        for line1 in text1:
            for line2 in text2:
                for line3 in text3:
                    output_text.append(line1 + line2 + line3)

        self.output.setText("\n".join(output_text))

    def save_as(self):

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save As",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if file_path:
            lines = list(set(self.output.toPlainText().split('\n')))
            with open(file_path, 'w') as f:
                f.write("\n".join(lines))

    def copy_to_clipboard(self):

        clipboard = QApplication.clipboard()
        clipboard.setText(self.output.toPlainText())

    def show_about(self):

        about_text = (
            "DorkGen is a script for generating combinations of keywords typically used "
            "in web page URLs for various purposes such as web scraping, testing, or other "
            "security-related tasks.\n\n"
            "For more information and updates please visit https://github.com/noarche/dorkGen\n\n"
            "Build Information:\n"
            "May 14 2024\n\n"
            "Updated Release | OCT 06 2024\n"
            "Added ability to change default values by editing the files located in ./configs/"
        )

        QMessageBox.information(self, "About DorkGen", about_text)


def show_disclaimer():

    msg = QMessageBox()
    msg.setWindowTitle("Disclaimer")
    msg.setText(disclaimer_text)
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    show_disclaimer()

    window = DorkGen()
    window.resize(700, 500)
    window.show()

    sys.exit(app.exec_())