from tkinter import *
from tkinter import filedialog
from PIL import Image


# ---------------------------- CONSTANTS ------------------------------- #
BG = "#534340"
INSTRUCTION_TEXT_1 = "1. Select image directory to add watermark"
INSTRUCTION_TEXT_2 = "2. Select watermark directory"

FG = "#ffffff"

INSTRUCTION_TEXT_3 = "3. Select directory to save image"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Watermarking app")
window.config(padx=100, pady=50, bg=BG)


def create_watermark_file():
    # Instruction Label -1
    label = Label(text=INSTRUCTION_TEXT_1, fg=FG, bg=BG)
    label.grid(column=1, row=1)
    img = Image.open(filedialog.askopenfilename())
    label.destroy()
    # Instruction Label -2
    label = Label(text=INSTRUCTION_TEXT_2, fg=FG, bg=BG)
    label.grid(column=1, row=1)
    watermark_img = Image.open(filedialog.askopenfilename())
    label.destroy()
    width, height = img.size
    wat_width, wat_height = watermark_img.size
    img.paste(watermark_img, (width-wat_width, height-wat_height), mask=watermark_img)
    label = Label(text=INSTRUCTION_TEXT_3, fg=FG, bg=BG)
    label.grid(column=1, row=1)
    save_img = img.save(filedialog.asksaveasfilename(), "JPEG")
    label.destroy()


# Start Image Watermarking
start_watermarking = Button(text="Start watermarking", highlightthickness=0, command=create_watermark_file)
start_watermarking.grid(column=1, row=2)


window.mainloop()