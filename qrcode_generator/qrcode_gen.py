# install qrcode package ( pip install qrcode )
# Enter text or URL

import qrcode
from qrcode.image.pil import Image, PilImage
from PIL import Image, ImageDraw

def gen_qrcode():
	url = input("Enter text or url to generate QR code: ").strip()
	qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=4,
)
	qr.add_data(url)
	qr.make(fit=True)

	img = qr.make_image(fill_color="red", back_color="white")

	file_name = input("Enter the image filename (.jpg|.png) for qr code: ").strip()
	img.save(file_name)

gen_qrcode()