import tkinter as tk

class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master=master
            self.pack()

            queryFields = "Start Date (yyyymmddhhMMSS)", "End Date (yyyymmddhhMMSS)", "Client Short ID", "Message Type (MT, MO, NL)", "System Type (PE, XMS, CA, NOBILL)", "Site", "Country (2 letter ISO Code)", "Operator ID", "MO State", "MT State", "MT Status", "Limit", "Timeout", "Format (txt, csv, tsv)"

            outputFields = "field1"

            buttonTypes = "GENERATE SCRIPT", "QUIT"

            self.make_form(queryFields, buttonTypes, outputFields)

        def make_form(self, queryFields, buttonTypes, outputFields):
            self.create_fields(queryFields)
            self.create_buttons(buttonTypes)

        def create_fields(self, queryFields):
            entries = []
            for field in queryFields:
                row = tk.Frame()
                lab = tk.Label(row, width=30, text=field, anchor="w")
                ent = tk.Entry(row)
                row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                lab.pack(side=tk.LEFT)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
                entries.append((field, ent))
            return entries

        def create_buttons(self, buttonTypes):
            buttons = []
            for button in buttonTypes:
                row = tk.Frame()
                if button == "QUIT":
                    but = tk.Button(self, text=button, command=self.master.destroy, fg="red")
                elif button == "GENERATE SCRIPT":
                    but = tk.Button(self, text=button, command=self.gen_script(), fg="green")
                row.pack(side=tk.TOP)
                but.pack(side=tk.TOP)

        def gen_script(self):
            return True
