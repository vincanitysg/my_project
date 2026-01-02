import qrcode
from qrcode.constants import ERROR_CORRECT_M

def generate_qr(
    data: str,
    output_path: str,
    box_size: int = 10,
    border: int = 4,
):
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
