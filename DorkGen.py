import PySimpleGUI as sg

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

def show_about():
    about_text = "DorkGen is a script for generating combinations of keywords typically used in web page URLs for various purposes such as web scraping, testing, or other security-related tasks.\n\nFor more information and updates please visit https://github.com/noarche/dorkGen\n\nBuild Information:\nMay 14 2024"
    sg.popup('About DorkGen', about_text)

layout = [
    [sg.Text('Page Name', text_color='white'), sg.Text('Page Format', text_color='white'), sg.Text('Page Type', text_color='white')],
    [sg.Multiline("cart\ncreditcard\npay\npayment\npayments\ncheckout\nshop\nshopping\nclothing\nrefund\npurchase\nshipment\nbitcoin\ngiftcard\npaypal", size=(20,10), key='-PAGE_NAME-', text_color='white', background_color='black'), sg.Multiline(".php?\n.aspx?\n.asp?\n.html?", size=(20,10), key='-PAGE_FORMAT-', text_color='white', background_color='black'), sg.Multiline("id=\narticle=\nforum_id=\nitem=\noption=\ncategory=\nPageid=\nindex=\ntitle=\ntopic=\nlist=\nGameID=\ngame=\nshowtopic=\nitem=\nnewsid=", size=(20,10), key='-PAGE_TYPE-', text_color='white', background_color='black')],
    [sg.Text('Gen Results', text_color='white')],
    [sg.Multiline('..press generate for results..', size=(80,10), key='-OUTPUT-', text_color='white', background_color='black')],
    [sg.Button('Generate', size=(10,1)), sg.Button('Save As', size=(10,1)), sg.Button('About', size=(10,1))]
]

window = sg.Window('DorkGen', layout, background_color='black', finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Generate':
        combine_texts(values)
    elif event == 'Save As':
        save_as(values)
    elif event == 'About':
        show_about()

window.close()
