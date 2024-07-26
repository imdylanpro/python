# Dylan Nelson
# July 25, 2024
# import_qrcode_document_creator.py

import os
import math
from docx import Document
from docx.shared import Inches

def insert_png_into_word(file_path, word_doc_path):
    # Initialize a Word document
    doc = Document()

    # Set the top and bottom margin to 0.5 inches
    section = doc.sections[0]
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)

    # Get a list of all PNG files in the specified directory
    png_files = [f for f in os.listdir(file_path) if f.lower().endswith(".png")]

    # 3 columns are always desired, but the number of rows is determined by the amount of pngs
    #   and the rows needs to be a multiple of three since 3 pngs can fit in a row.
    columns = 3
    rows = (len(png_files) / 3)
    rows = math.ceil(rows)
    cells = rows * columns

    # Add the table to the centered paragraph
    table = doc.add_table(rows=rows, cols=columns)

    # Set the preferred width of the table.
    for row in table.rows:
        # Set the height for each row.
        row.height = Inches(2.0)
        for cell in row.cells:
            # Set the width for each column.
            cell.width = Inches(2.63)

    row_index = 0
    col_index = 0

    for png_file in png_files:
      
        # Get the specific cell in the table
        cell = table.rows[row_index].cells[col_index]
        img_path = os.path.join(file_path, png_file)

        # Add the image to the cell
        paragraph = cell.add_paragraph()
        run = paragraph.add_run()
        run.add_picture(img_path, width=Inches(1.25))

        # Center the image that is placed into the cell.
        paragraph.alignment = 1

        # Increment the column index until it reaches 3 then reset
        #  then increment the row index.
        col_index += 1
        if col_index == 3:
            col_index = 0
            row_index += 1

    # Disable automatic resizing
    table.autofit = False

    # Center the table
    table.alignment = 1

    # Save the Word document
    doc.save(word_doc_path)

    print(f"PNG files inserted into {word_doc_path} successfully.")

# Specify the directory containing PNG files, and the output directory and file name.
png_directory = input("What is the filepath of your png images? ")
output_word_doc = input("What is the filepath where you want to store the png images? ")
output_word_doc_name = input("What do you want your file to be named? ")
output_word_doc = output_word_doc + '/' + output_word_doc_name + '.docx'

# Call the function to insert PNG files into the Word document
insert_png_into_word(png_directory, output_word_doc)
