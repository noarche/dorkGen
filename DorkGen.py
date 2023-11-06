import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

def combine_texts():
    text1 = input_box1.get("1.0", tk.END).splitlines()
    text2 = input_box2.get("1.0", tk.END).splitlines()
    text3 = input_box3.get("1.0", tk.END).splitlines()

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

root = tk.Tk()
root.title("DorkGen")
root.geometry("640x590")
root.configure(bg='black')
root.resizable(False, False)  


frame = tk.Frame(root, bg='black')
frame.pack(pady=20)


tk.Label(frame, text="Page Name", fg='white', bg='black').grid(row=0, column=0, pady=10, padx=5)
input_box1 = scrolledtext.ScrolledText(frame, width=20, height=10, fg="white", bg="black", insertbackground='white')
input_box1.insert("1.0", "cart\ncreditcard\npay\npayment\npayments\ncheckout\nshop\nshopping\nclothing\nrefund\npurchase\nshipment\nbitcoin\ngiftcard\npaypal")
input_box1.grid(row=1, column=0, pady=10, padx=5)


tk.Label(frame, text="Page Format", fg='white', bg='black').grid(row=0, column=1, pady=10, padx=5)
input_box2 = scrolledtext.ScrolledText(frame, width=20, height=10, fg="white", bg="black", insertbackground='white')
input_box2.insert("1.0", ".php?\n.aspx?\n.asp?\n.html?")
input_box2.grid(row=1, column=1, pady=10, padx=5)


tk.Label(frame, text="Page Type", fg='white', bg='black').grid(row=0, column=2, pady=10, padx=5)
input_box3 = scrolledtext.ScrolledText(frame, width=20, height=10, fg="white", bg="black", insertbackground='white')
input_box3.insert("1.0", "id=\narticle=\nforum_id=\nitem=\noption=\ncategory=\nPageid=\nindex=\ntitle=\ntopic=\nlist=\nGameID=\ngame=\nshowtopic=\nitem=\nnewsid=")
input_box3.grid(row=1, column=2, pady=10, padx=5)


tk.Label(root, text="Gen Results", fg='white', bg='black').pack(pady=10)
output_box = scrolledtext.ScrolledText(root, width=60, height=10, fg="white", bg="black", insertbackground='white')
output_box.insert("1.0", "..press generate for results..")
output_box.pack(pady=10)


process_btn = tk.Button(root, text="Generate", command=combine_texts, fg="white", bg="black")
process_btn.pack(pady=5, side=tk.LEFT, padx=20)

save_btn = tk.Button(root, text="Save As", command=save_as, fg="white", bg="black")
save_btn.pack(pady=5, side=tk.LEFT)

root.mainloop()
