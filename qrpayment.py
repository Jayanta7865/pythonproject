import qrcode
upi_id=input("Enter your UPI ID: ").strip()
phonepe_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
gpay_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
BHIM_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
phonepe_qr=qrcode.make(phonepe_url)
gpay_qr=qrcode.make(gpay_url)
BHIM_qr=qrcode.make(BHIM_url)
phonepe_qr.save("phonepe_qr.png")
gpay_qr.save("Gpay_qr.png")
BHIM_qr.save("BHIm_qr.png")
phonepe_qr.show()
gpay_qr.show()
BHIM_qr.show()
print("\nPlease scan the QR code using any UPI app...")


