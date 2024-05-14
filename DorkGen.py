import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox

def combine_texts():
    text1 = input_boxes[0].get("1.0", tk.END).splitlines()
    text2 = input_boxes[1].get("1.0", tk.END).splitlines()
    text3 = input_boxes[2].get("1.0", tk.END).splitlines()

    output_text = []
    for line1 in text1:
        for line2 in text2:
            for line3 in text3:
                output_text.append(line1 + line2 + line3)

    output_box.delete("1.0", tk.END)
    output_box.insert("1.0", '\n'.join(output_text))

def save_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_path:
        return
    with open(file_path, 'w') as f:
        lines = list(set(output_box.get("1.0", tk.END).splitlines()))
        f.write('\n'.join(lines))

def show_about():
    about_text = "DorkGen is a script for generating combinations of keywords typically used in web page URLs for various purposes such as web scraping, testing, or other security-related tasks.\n\nFor more information and updates please visit https://github.com/noarche/dorkGen\n\nBuild Information:\nMay 14 2024"
    messagebox.showinfo("About DorkGen", about_text)

root = tk.Tk()
root.title("DorkGen")
root.geometry("800x600")
root.configure(bg='black')
root.resizable(False, False)  

# Main frame
main_frame = tk.Frame(root, bg='black')
main_frame.pack(pady=20)

# Labels and input boxes
labels = ["Page Name", "Page Format", "Page Type"]
input_texts = [
    "cart\ncreditcard\npay\npayment\npayments\ncheckout\nshop\nshopping\nclothing\nrefund\npurchase\nshipment\nbitcoin\ngiftcard\npaypal",
    ".php?\n.aspx?\n.asp?\n.html?",
    "id=\narticle=\nforum_id=\nitem=\noption=\ncategory=\nPageid=\nindex=\ntitle=\ntopic=\nlist=\nGameID=\ngame=\nshowtopic=\nitem=\nnewsid="
]
input_boxes = []

for i, (label_text, default_text) in enumerate(zip(labels, input_texts)):
    label = tk.Label(main_frame, text=label_text, fg='white', bg='black')
    label.grid(row=0, column=i, pady=10, padx=5)
    input_box = scrolledtext.ScrolledText(main_frame, width=20, height=10, fg="white", bg="black", insertbackground='white')
    input_box.insert("1.0", default_text)
    input_box.grid(row=1, column=i, pady=10, padx=5)
    input_boxes.append(input_box)

# Generate results label and output box
tk.Label(root, text="Gen Results", fg='white', bg='black').pack(pady=10)
output_box = scrolledtext.ScrolledText(root, width=80, height=10, fg="white", bg="black", insertbackground='white')
output_box.insert("1.0", "..press generate for results..")
output_box.pack(pady=10)

# Buttons
process_btn = tk.Button(root, text="Generate", command=combine_texts, fg="white", bg="gray10")
process_btn.pack(pady=5, side=tk.LEFT, padx=20)

save_btn = tk.Button(root, text="Save As", command=save_as, fg="white", bg="gray10")
save_btn.pack(pady=5, side=tk.LEFT)

about_btn = tk.Button(root, text="About", command=show_about, fg="white", bg="gray10")
about_btn.pack(pady=5, side=tk.LEFT)

root.mainloop()
