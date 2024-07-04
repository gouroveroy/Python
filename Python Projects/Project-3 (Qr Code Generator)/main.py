import qrcode
from PIL import Image

def generate_qr_code(data, file_name):
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr_code.add_data(data)
    qr_code.make(fit=True)
    img = qr_code.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    
def main():
    data = input("Enter the data to be stored in the QR Code: ")
    file_name = input("Enter the file name with extension (Eg: qr_code.png): ")
    generate_qr_code(data, file_name)
    print(f"QR Code generated successfully and saved as {file_name}")

if __name__ == "__main__":
    main()
