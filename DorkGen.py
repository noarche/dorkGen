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
#
#  _.··._.·°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°°·.·°·._.··._
# ███╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗██╗  ██╗███████╗
# ████╗  ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝
# ██╔██╗ ██║██║   ██║███████║██████╔╝██║     ███████║█████╗  
# ██║╚██╗██║██║   ██║██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  
# ██║ ╚████║╚██████╔╝██║  ██║██║  ██║╚██████╗██║  ██║███████╗
# ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
# °°°·._.··._.·°°°·.°·..·°¯°··°¯°·.·°.·°°°°·.·°·._.··._.·°°°

import PySimpleGUI as sg
import os

# File paths
config_dir = './config/'
page_types_file = os.path.join(config_dir, 'page_types.txt')
page_formats_file = os.path.join(config_dir, 'page_formats.txt')
page_names_file = os.path.join(config_dir, 'page_names.txt')

# Popup message that the user must acknowledge
disclaimer_text = (
    'The information and/or software provided here is intended solely for educational purposes and legal penetration testing purposes. '
    'By accessing or using this information and/or software, you acknowledge and agree that you assume full responsibility for your actions '
    'and any consequences that may result from those actions. The creators, contributors, and providers of this information and/or software '
    'shall not be held liable for any misuse or damage arising from its application. It is your responsibility to ensure that your use complies '
    'with all applicable laws and regulations.'
)
sg.popup_ok(disclaimer_text)

def read_config_file(filepath):
    """Reads the content of a text file."""
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return file.read().strip()
    else:
        sg.popup_error(f"File not found: {filepath}")
        return ""

# Read the text from the configuration files
page_names = read_config_file(page_names_file)
page_formats = read_config_file(page_formats_file)
page_types = read_config_file(page_types_file)

def combine_texts(values):
    text1 = values['-PAGE_NAME-'].split('\n')
    text2 = values['-PAGE_FORMAT-'].split('\n')
    text3 = values['-PAGE_TYPE-'].split('\n')

    output_text = []
    for line1 in text1:
        for line2 in text2:
            for line3 in text3:
                output_text.append(line1 + line2 + line3)

    window['-OUTPUT-'].update('\n'.join(output_text))

def save_as(values):
    file_path = sg.popup_get_file('Save As', save_as=True, default_extension='.txt', file_types=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        with open(file_path, 'w') as f:
            lines = list(set(window['-OUTPUT-'].get().split('\n')))
            f.write('\n'.join(lines))

def copy_to_clipboard(values):
    sg.clipboard_set(values['-OUTPUT-'])

def show_about():
    about_text = "DorkGen is a script for generating combinations of keywords typically used in web page URLs for various purposes such as web scraping, testing, or other security-related tasks.\n\nFor more information and updates please visit https://github.com/noarche/dorkGen\n\nBuild Information:\nMay 14 2024\n\nUpdated Release | OCT 06 2024\nAdded ability to change default values by editing the files located in ./configs/"
    sg.popup('About DorkGen', about_text)

layout = [
    [sg.Text('Page Name', text_color='black', size=(19,1)), sg.Text('Page Format', text_color='black', size=(19,1)), sg.Text('Page Type', text_color='black', size=(19,1))],
    [sg.Multiline(page_names, size=(20,10), key='-PAGE_NAME-', text_color='white', background_color='black'),
     sg.Multiline(page_formats, size=(20,10), key='-PAGE_FORMAT-', text_color='white', background_color='black'),
     sg.Multiline(page_types, size=(20,10), key='-PAGE_TYPE-', text_color='white', background_color='black')],
    [sg.Text('Results:', text_color='black')],
    [sg.Multiline('..press generate for results..', size=(68,10), key='-OUTPUT-', text_color='white', background_color='black')],
    [sg.Button('Generate', size=(10,1)), sg.Button('Save As', size=(10,1)), sg.Button('Copy to Clipboard', size=(15,1)), sg.Button('About', size=(10,1))]
]

# Set the alpha channel for semi-transparency
window = sg.Window('DorkGen', layout, background_color='black', alpha_channel=0.94, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Generate':
        combine_texts(values)
    elif event == 'Save As':
        save_as(values)
    elif event == 'Copy to Clipboard':
        copy_to_clipboard(values)
    elif event == 'About':
        show_about()

window.close()
