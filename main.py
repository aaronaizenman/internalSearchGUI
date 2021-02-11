import tkinter as tk
from math import floor

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.makeForm()

    def makeForm(self):
        # Define the fields that are available to be queried on
        queryFields = "Start Date (yyyymmddhhMMSS)", "End Date (yyyymmddhhMMSS)", "Client Short ID", "Message Type (MT, MO, NL)", "System Type (PE, XMS, CA, NOBILL)", "Site", "Country (2 letter ISO Code)", "Operator ID", "MO State", "MT State", "MT Status", "Limit", "Timeout", "Format (txt, csv, tsv)"

        # Define the fields that are eligible for output
        outputFields = "Day", "SinchMessageID", "associations.kind", "Site (EU3C, EU1C, etc...)", "Client Account ID", "Client Short ID", "Connection ID", "Connection Internal ID", "Client ID", "ALC_ID", "client_in", "client_out", "country", "dfb_on", "dfb_rec", "dr_error", "MSISDN", "Operator ID", "State", "Status Ind", "Supp In", "Supp Out", "Virtual Number", "NPI", "TON", "Timestamp", "Batch ID", "Site (EU1X, EU3X, etc...)", "System", "Type"

        # Create all of my frames to arrange the window
        topFrame = tk.Frame()
        topFrame.pack(side=tk.TOP)

        bottomFrame = tk.Frame()
        bottomFrame.pack(side=tk.BOTTOM)

        queryFrame = tk.Frame(topFrame)
        queryFrame.pack(side=tk.LEFT)

        outputFrame = tk.Frame(topFrame)
        outputFrame.pack(side=tk.RIGHT, fill=tk.X)

        outputFileFrame = tk.Frame(outputFrame)
        outputFileFrame.pack(side=tk.BOTTOM)

        buttonFrame = tk.Frame(bottomFrame)
        buttonFrame.pack(side=tk.TOP, fill=tk.X)

        scriptFrame = tk.Frame(bottomFrame)
        scriptFrame.pack(side=tk.BOTTOM)

        # For each of the query fields, add a label and a text entry box for the user
        queryEntries = []
        for field in queryFields:
            row = tk.Frame(queryFrame)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            ent = tk.Entry(row)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            lab = tk.Label(row, width=30, text=field, anchor="w")
            lab.pack(side=tk.LEFT)
            queryEntries.append((field, ent))

        # For each of the output fields, add a label and a checkbox
        outputEntries = []
        i = 0
        for field in outputFields:
            var = tk.IntVar()
            cell = tk.Frame(outputFrame)
            cell.grid(row=floor(i/2), column=(i%2))
            box = tk.Checkbutton(cell, text=field, variable=var)
            box.pack()
            outputEntries.append((field, var))
            i += 1

        row = tk.Frame(outputFileFrame)
        row.pack()
        ent = tk.Entry(row)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        lab = tk.Label(row, width=30, text="filepath/filename", anchor="w")
        lab.pacl(side=tk.LEFT)

        # Add a text box at the bottom of the window, this is where the resulting query will be displayed
        row = tk.Frame(scriptFrame)
        row.pack(side=tk.BOTTOM)

        textBox = tk.Text(row)
        textBox.pack(side=tk.BOTTOM)
        textBox.config(state="disabled")

        # Add three buttons, one for exiting, one for generating the script based on the query parameters, and one for debugging various parameters

        row = tk.Frame(buttonFrame)
        row.pack(side=tk.BOTTOM)

        quitButton = tk.Button(row, text="QUIT", command=self.master.destroy, fg="red")
        quitButton.pack(side=tk.LEFT)

        genButton = tk.Button(row, text="GENERATE SCRIPT", command=lambda: self.gen_script(queryEntries, outputEntries, textBox), fg="green")
        genButton.pack(side=tk.LEFT)

        debugButton = tk.Button(row, text="debug", command=lambda: self.debug(outputEntries), fg="green")
        debugButton.pack(side=tk.LEFT)

    def gen_script(self, queryEntries, outputEntries, textBox):
        textBox.config(state="normal")
        textBox.delete("0.0", tk.END)

        i = 0
        script = "/opt/apps/etl/CliClient internal-search "

        #Add each query parameter to the script where specified
        for entry in queryEntries:
            if queryEntries[i][1].get() == "":
                i += 1
            else:
                if queryEntries[i][0] == "Start Date (yyyymmddhhMMSS)":
                    script += "--start "
                elif queryEntries[i][0] == "End Date (yyyymmddhhMMSS)":
                    script += "--end "
                elif queryEntries[i][0] == "Client Short ID":
                    script += "--client-id "
                elif queryEntries[i][0] == "Message Type (MT, MO, NL)":
                    script += "--kind "
                elif queryEntries[i][0] == "System Type (PE, XMS, CA, NOBILL)":
                    script += "--system-type "
                elif queryEntries[i][0] == "Site":
                    script += "--site "
                elif queryEntries[i][0] == "Country (2 letter ISO Code)":
                    script += "--country "
                elif queryEntries[i][0] == "Operator ID":
                    script += "--operator "
                elif queryEntries[i][0] == "MO State":
                    script += "--mo-state "
                elif queryEntries[i][0] == "MT State":
                    script += "--mt-state "
                elif queryEntries[i][0] == "MT Status":
                    script += "--mt-status"
                elif queryEntries[i][0] == "Limit":
                    script += "--limit "
                elif queryEntries[i][0] == "Timeout":
                    script += "--timeout "
                elif queryEntries[i][0] == "Format (txt, csv, tsv)":
                    script += "--format "
                script = script + queryEntries[i][1].get() + " "
                i += 1

        i=0
        script = script + "--columns "

        #Define the output columns based on the checkboxes
        for entry in outputEntries:
            if outputEntries[i][1].get() == 0:
                i += 1
            else:
                if outputEntries[i][0] == "Day":
                    script += "2,"
                elif outputEntries[i][0] == "SinchMessageID":
                    script += "3,"
                elif outputEntries[i][0] == "associations.kind":
                    script += "4,"
                elif outputEntries[i][0] == "Site (EU3C, EU1C, etc...)":
                    script += "5,"
                elif outputEntries[i][0] == "Client Account ID":
                    script += "6,"
                elif outputEntries[i][0] == "Client Short ID":
                    script += "7,"
                elif outputEntries[i][0] == "Connection ID":
                    script += "8,"
                elif outputEntries[i][0] == "Connection Internal ID":
                    script += "9,"
                elif outputEntries[i][0] == "Client ID":
                    script += "10,"
                elif outputEntries[i][0] == "ALC_ID":
                    script += "11,"
                elif outputEntries[i][0] == "client_in":
                    script += "12,"
                elif outputEntries[i][0] == "client_out":
                    script += "13,"
                elif outputEntries[i][0] == "country":
                    script += "14,"
                elif outputEntries[i][0] == "dfb_on":
                    script += "15,"
                elif outputEntries[i][0] == "dfb_rec":
                    script += "16,"
                elif outputEntries[i][0] == "dr_error":
                    script += "17,"
                elif outputEntries[i][0] == "MSISDN":
                    script += "18,"
                elif outputEntries[i][0] == "Operator ID":
                    script += "19,"
                elif outputEntries[i][0] == "State":
                    script += "20,"
                elif outputEntries[i][0] == "Status Ind":
                    script += "21,"
                elif outputEntries[i][0] == "Supp In":
                    script += "22,"
                elif outputEntries[i][0] == "Supp Out":
                    script += "23,"
                elif outputEntries[i][0] == "Virtual Number":
                    script += "24,"
                elif outputEntries[i][0] == "NPI":
                    script += "25,"
                elif outputEntries[i][0] == "TON":
                    script += "26,"
                elif outputEntries[i][0] == "Timestamp":
                    script += "27,"
                elif outputEntries[i][0] == "Batch ID":
                    script += "28,"
                elif outputEntries[i][0] == "Site (EU1X, EU3X, etc...)":
                    script += "29,"
                elif outputEntries[i][0] == "System":
                    script += "30,"
                elif outputEntries[i][0] == "Type":
                    script += "31,"

                i += 1

        #Remove the trailing comma


        #If specified, add the filepath of the output file. Otherwise just print to console

        textBox.insert(tk.INSERT, script)
        textBox.config(state="disabled")

    def debug(self, array):
        print(array)

myapp = App()

myapp.master.title("My Application")

myapp.mainloop()
