import PySimpleGUI as sg

# Popup message that the user must acknowledge
disclaimer_text = (
    'The information and/or software provided here is intended solely for educational purposes and legal penetration testing purposes. '
    'By accessing or using this information and/or software, you acknowledge and agree that you assume full responsibility for your actions '
    'and any consequences that may result from those actions. The creators, contributors, and providers of this information and/or software '
    'shall not be held liable for any misuse or damage arising from its application. It is your responsibility to ensure that your use complies '
    'with all applicable laws and regulations.'
)
sg.popup_ok(disclaimer_text)

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
    about_text = "DorkGen is a script for generating combinations of keywords typically used in web page URLs for various purposes such as web scraping, testing, or other security-related tasks.\n\nFor more information and updates please visit https://github.com/noarche/dorkGen\n\nBuild Information:\nMay 14 2024"
    sg.popup('About DorkGen', about_text)

layout = [
    [sg.Text('Page Name', text_color='white'), sg.Text('Page Format', text_color='white'), sg.Text('Page Type', text_color='white')],
    [sg.Multiline("cart\ncreditcard\npay\npayment\npayments\ncheckout\nshop\nshopping\nclothing\nrefund\npurchase\nshipment\nbitcoin\ngiftcard\npaypal", size=(20,10), key='-PAGE_NAME-', text_color='white', background_color='black'), sg.Multiline(".php?\n.aspx?\n.asp?\n.html?", size=(20,10), key='-PAGE_FORMAT-', text_color='white', background_color='black'), sg.Multiline("id=\narticle=\nforum_id=\nitem=\noption=\ncategory=\nPageid=\nindex=\ntitle=\ntopic=\nlist=\nGameID=\ngame=\nshowtopic=\nitem=\nnewsid=", size=(20,10), key='-PAGE_TYPE-', text_color='white', background_color='black')],
    [sg.Text('Results:', text_color='green')],
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

