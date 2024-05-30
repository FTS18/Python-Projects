import qrcode
import qrcode.constants
import os

def generate_qr_code(d, f):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(d)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    os.makedirs("out", exist_ok=True)
    i = 1
    while True:
        f = f"{f_prefix}{i}.png"
        fp = os.path.join("out", f)
        if not os.path.exists(fp):
            break
        i += 1
    img.save(fp)
    print(f"A QR code has been generated and saved at out/ as `{f}'")

# Example usage
data = input("URL: ")
f_prefix = "qr"
generate_qr_code(data, f_prefix)
