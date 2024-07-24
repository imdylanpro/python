# Dylan Nelson
# July 19, 2024
# qr_code_generator.py

import qrcode
from PIL import ImageDraw, ImageFont
import tkinter as tk
from tkinter import Entry, Label, filedialog
from PIL import ImageTk

class QRCodeGenerator:
    """Overall class to manage assets and parameters"""

    def __init__(self):
        """Initialize all of the attributes and classes used throughout."""
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=2,
            border=4,
        )
        # Create the initial attributes for the data to be empty strings.
        self.qr_code_data = ""
        self.secondary_data = ""

        # Specify the font-size
        self.fontsize = 10

        # Create a variable to handle if a custom file is used.
        self.custom_file_select = False

        # Create a variable to handle if the program is on its first cycle.
        self.first_cycle = True

        # Specify the height and width of the GUI
        self.width = 570
        self.height = 250

    def _create_qr_code(self):
        """Creates a QR code based off of the data variable, then creates an image with the QR code on it.
        Adds the board number to the bottom of the image as well."""

        # Create the filepath name
        self.filepath = self.qr_code_data + '_' + self.secondary_data + '.png'
        self.short_filepath = self.filepath

        # Create the custom filepath name for the custom qr code.
        if self.custom_file_select:
            self.filepath = self.custom_filepath + self.qr_code_data + '_' + self.secondary_data + '.png'

        # Clear the current data inside the QR code and add the new data.
        self.qr.clear()
        self.qr.add_data(self.qr_code_data)
        self.qr.make(fit=True)

        # Create an image from the QR Code instance
        self.img = self.qr.make_image(fill='black', back_color='white')

        # Make the image bigger (double size)
        self.img = self.img.resize((2 * self.img.size[0], 2 * self.img.size[1] + self.fontsize))

        self.d = ImageDraw.Draw(self.img)
        self.font = ImageFont.truetype("arial.ttf", self.fontsize)

        # Add text
        self.d.text((17, self.img.size[1]//60), self.qr_code_data, font=self.font, fill=0)  # Changed fill color to grayscale
        self.d.text((17, 2 * self.img.size[1]//2.25), self.secondary_data, font=self.font, fill=0)  # Changed fill color to grayscale
        
        # Save the image
        self.img.save(f'{self.filepath}')

         # After successfully creating the png, then create a message for users that tells them it worked.
        self._create_labels()
        self._add_qr_to_gui()   

    def _create_labels(self):
        """Create the labels that show the successful saving of a file."""

        # If the program has already created the labels for successful file creation, delete them before making more.
        if not self.first_cycle:
            self.successful_file_creation_label1.place_forget()
            self.successful_file_creation_label2.place_forget()

        # Create the label that shows the new file created.
        self.successful_file_creation_label1 = tk.Label(self.canvas, text=f"File Creation Successful:", font=("Arial", 10), fg="green", bg="#F1F1F1")
        self.successful_file_creation_label2 = tk.Label(self.canvas, text=f"{self.short_filepath}", font=("Arial", 10), fg="green", bg="#F1F1F1")

        self.successful_file_creation_label1.place(x=(120), y=(190))
        self.successful_file_creation_label2.place(x=(120), y=(210))

        # Set the first cycle variable so that the labels will be properly unplaced.
        self.first_cycle = False

    def _add_qr_to_gui(self):
        """Add the recently created png image of the QR Code to the GUI."""
        # Load the png image
        self.png_image = self.img
        self.png_image = self.png_image.resize((200, 200))

        # Convert the image to a format that Tkinter can handle
        self.tk_image = ImageTk.PhotoImage(self.png_image)

        # Create a label to display the image
        self.label = Label(self.root, image = self.tk_image)
        self.label.pack()
        self.label.place(x = 350, y = ((self.height - self.png_image.size[1]) // 2))

    def _create_canvas(self):
        """Creates the objects for the GUI."""
        self.root = tk.Tk()
        self.root.title("QR Code Generator")
        # Builds the canvas for the GUI, this is the portion that the shapes will be drawn onto
        self.canvas = tk.Canvas(self.root, width = self.width, height = self.height)
        self.canvas.pack(fill=tk.BOTH, expand=False)
        # Sets the minimum allowed size for the canvas window
        self.root.minsize(self.width, self.height)
        self.root.maxsize(self.width, self.height)

    def _create_qr_code_entry_box(self):
        """Creates the entry box and the label for the QR code data."""
        self.qr_code_label = tk.Label(self.canvas, text="QR Code Contents", font=("Arial", 10), fg="black", bg="#F1F1F1")
        self.qr_code_label.place(x=(15), y=(15))
        self.qr_code_entry_box = Entry(self.root)
        self.qr_code_entry_box.pack()
        self.qr_code_entry_box.place(x=(15), y=(40), width=320)

    def _create_secondary_data_entry_box(self):
        """Creates the entry box and the label for the secondary data."""
        self.secondary_data_label = tk.Label(self.canvas, text="Secondary Contents", font=("Arial", 10), fg="black", bg="#F1F1F1")
        self.secondary_data_label.place(x=(15), y=(65))
        self.secondary_data_entry_box = Entry(self.root)
        self.secondary_data_entry_box.pack()
        self.secondary_data_entry_box.place(x=(15), y=(90), width=320)

    def _create_filepath_select_entry_box(self):
        """Creates the entry box and the label for the secondary data."""
        self.filepath_label = tk.Label(self.canvas, text="Custom Filepath (Optional)", font=("Arial", 10), fg="black", bg="#F1F1F1")
        self.filepath_label.place(x=(120), y=(125))
        self.filepath_entry_box = Entry(self.root)
        self.filepath_entry_box.pack()
        self.filepath_entry_box.place(x=(120), y=(150), width=215)
        self.filepath_entry_box.config(state='disabled')

    def _create_qr_code_button(self, color='#FFFFFF', outline="black"):
        """Creates the button that handles the event of turning the data into QR codes."""
        self.canvas.create_rectangle(15, 190, 115, 230, fill = color, outline=outline)
        self.canvas.create_text(65, 210, text = "Generate QR Code", fill="black", font=("Arial", 8))

    def _create_filepath_select_button(self, color='#FFFFFF', outline="black"):
        """Creates the button that handles the selection of a custom filepath."""
        self.canvas.create_rectangle(15, 130, 115, 170, fill = color, outline=outline)
        self.canvas.create_text(65, 150, text = "Select Filepath", fill="black", font=("Arial", 8))

    def _event_handler(self):
        """Handles events that the user can induce on the GUI."""
        self.canvas.bind("<Motion>", self._mouse_movement)
        self.canvas.bind("<Button-1>", self._mouse_left_click)
        self.canvas.bind("<Return>", self._keypress)

    def _mouse_movement(self, event = None):
        """Handles the mouse movement event."""
        
        # Assign the mouse coordinates to variables.
        mouse_x, mouse_y = event.x, event.y

        # If the mouse hovers over the coordinates associated with the 
        if 15 < mouse_x < 115 and 190 < mouse_y < 230:
            # Changes the color of the "Generate QR Code" button when the user hovers over it.
            self._create_qr_code_button(color = '#F1F1F1')
        else:
            self._create_qr_code_button()

        if not self.custom_file_select:
            if 15 < mouse_x < 115 and 130 < mouse_y < 170:
                # Changes the color of the "Generate QR Code" button when the user hovers over it.
                self._create_filepath_select_button(color = '#F1F1F1')
            else:
                self._create_filepath_select_button()

    def _mouse_left_click(self, event = None):
        """Handles the mouse right click event."""
        # Assign the mouse coordinates to variables.
        mouse_x, mouse_y = event.x, event.y

        if 15 < mouse_x < 115 and 190 < mouse_y < 230:
            # Uses the data that is present in the two entry boxes if the mouse is in the coordinates
            #   designated for the "Generate QR Code" button.
            self.qr_code_data = self.qr_code_entry_box.get()
            self.secondary_data = self.secondary_data_entry_box.get()
            self._create_qr_code()
        elif 15 < mouse_x < 115 and 130 < mouse_y < 170:
            if self.custom_file_select:
                self.custom_file_select = False
                self._create_filepath_select_button(color="#FFFFFF")
                self.filepath_entry_box.config(state='normal')
                self.filepath_entry_box.delete(0, 'end')
                self.filepath_entry_box.config(state='disabled')
            else:
                self._activate_custom_filepath()

    def _keypress(self, event = None):
        """Handles the pressing of the Enter key."""
        self.qr_code_data = self.qr_code_entry_box.get()
        self.secondary_data = self.secondary_data_entry_box.get()
        self.custom_filepath = self.filepath_entry_box.get() + '/'
        self._create_qr_code()
                       
    def _activate_custom_filepath(self):
        self.custom_file_select = True
        self._create_filepath_select_button(color="#ABF7B1")
        self.custom_filepath = filedialog.askdirectory()
        if self.custom_filepath:
            self.custom_filepath = self.custom_filepath + '/'
            self.filepath_entry_box.config(state='normal')
            self.filepath_entry_box.insert(0, f'{self.custom_filepath}')
            self.filepath_entry_box.config(state='disabled')

    def main_loop(self):
        # Create the canvas for the GUI
        self._create_canvas()
        # Create the entry box and label for the QR code data
        self._create_qr_code_entry_box()
        # Create the entry box and label for the Secondary data
        self._create_secondary_data_entry_box()
        # Create an entry box for an optional custom filepath
        self._create_filepath_select_entry_box()
        # Create the button to convert into a QR code
        self._create_qr_code_button()
        # Create the button to select the desired filepath
        self._create_filepath_select_button()
        # Create a helper method to handle events that the user can do on the GUI.
        self._event_handler()
        # This mainloop handles the loop for the GUI.
        self.root.mainloop()
            
if __name__ == '__main__':
    qrcg = QRCodeGenerator()
    qrcg.main_loop()
