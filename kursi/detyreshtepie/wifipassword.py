import wifi_qrcode_generator.generator

qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid='CGA2121_bws3c8Q', hidden=False, authentication_type='WPA', password='FE93Fz9akPCjJWspZB'
)

qr_code.print_ascii()
qr_code.make_image().save('qr.png')