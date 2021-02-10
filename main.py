import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.makeForm()

    def makeForm(self):
        queryFields = "Start Date (yyyymmddhhMMSS)", "End Date (yyyymmddhhMMSS)", "Client Short ID", "Message Type (MT, MO, NL)", "System Type (PE, XMS, CA, NOBILL)", "Site", "Country (2 letter ISO Code)", "Operator ID", "MO State", "MT State", "MT Status", "Limit", "Timeout", "Format (txt, csv, tsv)"

        for field in queryFields:
            row = tk.Frame()
            lab = tk.Label(row, width=30, text=field, anchor="w")
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

        row = tk.Frame()
        textBox = tk.Text(row)
        row.pack(side=tk.BOTTOM)
        textBox.pack(side=tk.BOTTOM)

        row = tk.Frame()
        quitButton = tk.Button(row, text="QUIT", command=self.master.destroy, fg="red")
        genButton = tk.Button(row, text="GENERATE SCRIPT", command=lambda: self.gen_script(textBox), fg="green")
        row.pack()
        quitButton.pack(side=tk.LEFT)
        genButton.pack(side=tk.LEFT)

    def gen_script(self, textBox):
        textBox.insert(tk.INSERT, "1")


myapp = App()

myapp.master.title("My Application")

myapp.mainloop()
