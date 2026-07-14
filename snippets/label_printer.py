import barcode
from barcode.writer import ImageWriter

def print_barcode(data, filename):
    # Choose the barcode format (e.g., 'ean13', 'upca', 'isbn10')
    EAN = barcode.get('ean13', data, writer=ImageWriter())
    
    # Save the barcode as an image file
    full_filename = f"{filename}.png"
    EAN.save(full_filename)
    
    print(f"Barcode saved as {full_filename}")

# Example usage:
print_barcode("5901234123457", "barcode")