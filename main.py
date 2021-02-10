import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.makeForm()

    def makeForm(self):
        # Define the fields that are available to be queried on
        queryFields = "Start Date (yyyymmddhhMMSS)", "End Date (yyyymmddhhMMSS)", "Client Short ID", "Message Type (MT, MO, NL)", "System Type (PE, XMS, CA, NOBILL)", "Site", "Country (2 letter ISO Code)", "Operator ID", "MO State", "MT State", "MT Status", "Limit", "Timeout", "Format (txt, csv, tsv)"
        entries = []

        # For each of those fields, add a label and a text entry box for the user
        for field in queryFields:
            row = tk.Frame()
            lab = tk.Label(row, width=30, text=field, anchor="w")
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))

        # Add a text box at the bottom of the window, this is where the resulting query will be displayed
        row = tk.Frame()
        textBox = tk.Text(row)
        row.pack(side=tk.BOTTOM)
        textBox.pack(side=tk.BOTTOM)
        textBox.config(state="disabled")

        # Add two buttons, one for exiting, one for generating the script based on the query parameters
        row = tk.Frame()
        quitButton = tk.Button(row, text="QUIT", command=self.master.destroy, fg="red")
        genButton = tk.Button(row, text="GENERATE SCRIPT", command=lambda: self.gen_script(entries, textBox), fg="green")
        row.pack()
        quitButton.pack(side=tk.LEFT)
        genButton.pack(side=tk.LEFT)

    def gen_script(self, entries, textBox):
        textBox.config(state="normal")
        textBox.delete("0.0", tk.END)
        i = 0
        script = "/opt/apps/etl/CliClient internal-search "

        for entry in entries:
            if entries[i][1].get() == "":
                i += 1
            else:
                if entries[i][0] == "Start Date (yyyymmddhhMMSS)":
                    script += "--start "
                elif entries[i][0] == "End Date (yyyymmddhhMMSS)":
                    script += "--end "
                elif entries[i][0] == "Client Short ID":
                    script += "--client-id "
                elif entries[i][0] == "Message Type (MT, MO, NL)":
                    script += "--kind "
                elif entries[i][0] == "System Type (PE, XMS, CA, NOBILL)":
                    script += "--system-type "
                elif entries[i][0] == "Site":
                    script += "--site "
                elif entries[i][0] == "Country (2 letter ISO Code)":
                    script += "--country "
                elif entries[i][0] == "Operator ID":
                    script += "--operator "
                elif entries[i][0] == "MO State":
                    script += "--mo-state "
                elif entries[i][0] == "MT State":
                    script += "--mt-state "
                elif entries[i][0] == "MT Status":
                    script += "--mt-status"
                elif entries[i][0] == "Limit":
                    script += "--limit "
                elif entries[i][0] == "Timeout":
                    script += "--timeout "
                elif entries[i][0] == "Format (txt, csv, tsv)":
                    script += "--format "
                script = script + entries[i][1].get() + " "
                i += 1

        # print(script)

        textBox.insert(tk.INSERT, script)

        textBox.config(state="disabled")


myapp = App()

myapp.master.title("My Application")

myapp.mainloop()
