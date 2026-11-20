"""Crea el código QR del Puente Niza.  Uso:  python3 crear_qr.py https://TU_USUARIO.github.io/puente-niza/
Requiere: pip install "qrcode[pil]" """
import sys, qrcode
url = sys.argv[1] if len(sys.argv) > 1 else sys.exit("Indica la URL pública. Ej: python3 crear_qr.py https://usuario.github.io/puente-niza/")
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=16, border=4)
qr.add_data(url); qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save("qr_puente_niza.png")
print("QR guardado en qr_puente_niza.png ->", url)
