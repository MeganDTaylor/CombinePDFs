import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfMerger


def select_pdfs():
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(
        title="Select PDF files to combine", filetypes=[("PDF files", "*.pdf")]
    )
    return list(files)


def combine_selected_pdfs(pdf_files, output_filename="combined.pdf"):
    if not pdf_files:
        print("No PDF files selected.")
        return

    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_filename)
    merger.close()
    print(f"Combined PDF saved as: {output_filename}")


if __name__ == "__main__":
    selected_pdfs = select_pdfs()
    if selected_pdfs:
        root = Tk()
        root.withdraw()
        output_filename = filedialog.asksaveasfilename(
            title="Save Combined PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialdir=os.path.dirname(selected_pdfs[0]),
        )
        if output_filename:
            combine_selected_pdfs(selected_pdfs, output_filename)
