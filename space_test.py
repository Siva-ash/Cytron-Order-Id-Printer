from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
import subprocess
import os

def create_pdf(text, file_path='/tmp/temp_print.pdf'):
    c = canvas.Canvas(file_path, pagesize=landscape(letter))
    width, height = landscape(letter)  # Page dimensions in landscape mode
    
    # Set font and size
    c.setFont('Helvetica-Bold', 180)

    # Center text horizontally and vertically
    text_width = c.stringWidth(text, 'Helvetica-Bold', 180)
    text_height = 180  # Approximate height of text
    c.drawString((width - text_width) / 2, (height - text_height) / 2, text)

    c.save()

def print_pdf(file_path='/tmp/temp_print.pdf'):
    try:
        subprocess.run(['lp', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error printing PDF: {e}")

def main():
    print("Type something and press Enter to print. Type 'exit' to quit.")
    
    while True:
        user_input = input("Input: ")
        
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        
        pdf_path = '/tmp/temp_print.pdf'
        create_pdf(user_input, pdf_path)
        print_pdf(pdf_path)
        print("Sent to printer.")
        
        # Optionally, remove the temporary file after printing
        try:
            os.remove(pdf_path)
        except OSError as e:
            print(f"Error removing temporary file: {e}")

if __name__ == "__main__":
    main()