import tkinter as tk
from tkinter import filedialog
from Bio import SeqIO
from io import StringIO


def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("FASTA Files", "*.fasta")])
    if file_path:
        fasta_text.delete(1.0, tk.END)  # Clear the text area
        with open(file_path, "r") as fasta_file:
            # insert from end of old text(zerooo)
            fasta_text.insert(tk.END, fasta_file.read())

########################################            

def read_record():
    fasta_data = fasta_text.get(1.0, tk.END)
    record_id = entry_record_id.get()
    # check if there is a value
    if record_id:
        # to avoid write fasta code to new file
        fasta_file = StringIO(fasta_data)
        records = SeqIO.parse(fasta_file, "fasta")
        for record in records:
            if record.id == record_id or record.name == record_id:
                display_record(record)
                break
        else:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Record not found.")


########################################

def display_record(record):
    gc_content = (record.seq.count('G') + record.seq.count('C')) / len(record.seq) * 100
    reverse_complement = record.seq.reverse_complement()
    rna = record.seq.transcribe()

    # to customize output style
    output_text.tag_configure("header", font=("Arial", 12, "bold"))
    output_text.tag_configure("sequence", font=("Courier New", 11))
    output_text.tag_configure("result", font=("Arial", 11, "italic"))

    output_text.delete(1.0, tk.END)  # Clear the output area

    # Display the record details with formatting
    output_text.insert(tk.END, "ID: ", "header")
    output_text.insert(tk.END, record.id + "\n", "sequence")
    output_text.insert(tk.END, "Name: ", "header")
    output_text.insert(tk.END, record.name + "\n", "sequence")
    output_text.insert(tk.END, "Description: ", "header")
    output_text.insert(tk.END, record.description + "\n", "sequence")
    output_text.insert(tk.END, "Sequence: ", "header")
    output_text.insert(tk.END, record.seq + "\n", "sequence")
    output_text.insert(tk.END, "GC Content: ", "header")
    output_text.insert(tk.END, f"{gc_content:.2f}%\n", "result")
    output_text.insert(tk.END, "Reverse Complement: ", "header")
    output_text.insert(tk.END, reverse_complement + "\n", "sequence")
    output_text.insert(tk.END, "RNA: ", "header")
    output_text.insert(tk.END, rna + "\n", "sequence")


#########################################


# Create the main root
root = tk.Tk()
root.title("Bioinformatics Tool")
root.geometry("800x600") 
root.configure(bg="lightblue")



########################################################################
upload_label = tk.Label(root, text="FASTA File Content")
upload_label.pack(pady=5)
# Create a text area to display the FASTA file contents
fasta_text = tk.Text(root, height=10, width=70)
fasta_text.pack()



#upload a FASTA file Button
upload_button = tk.Button(root, text="Upload FASTA File", command=upload_file)
upload_button.pack()

#entry field to input the record ID
entry_record_id = tk.Entry(root)
entry_record_id.pack()

#button to read the record
read_button = tk.Button(root, text="Read Record", command=read_record,bg="yellow", relief=tk.RAISED, bd=3 )
read_button.pack()

#text area to display the output
output_text = tk.Text(root, height=15, width=79)
output_text.pack()
########################################################################




root.mainloop()
