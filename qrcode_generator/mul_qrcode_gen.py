import qrcode
from qrcode.image.pil import Image, PilImage
from PIL import Image, ImageDraw

def mul_gen_qrcode():
	print("Generate QR codes!")
	
	while True:
		url = input("Enter text or url to generate QR code or 'q' to quit: ").strip()
		if url == 'q':
			break
		else:
			qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
			border=4,
		)
			qr.add_data(url)
			qr.make(fit=True)
			fill_color = input("Input the fill color for QR image: ").strip()
			back_color = input("Input the back color for QR image: ").strip()
			img = qr.make_image(fill_color=fill_color, back_color=back_color)

			file_name = input("Enter the image filename (.jpg|.png) for qr code: ").strip()
			img.save(file_name)		

mul_gen_qrcode()