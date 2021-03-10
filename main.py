#Sistema criado para geração de QRCodes.

import pyqrcode as pqr
import png
import io

url = pqr.create('about.me')
with open('code.png', 'w') as fstream:
    url.png('code.png', scale=5)
url.png('code.png', scale=5)
buffer = io.BytesIO()
url.png(buffer)
print(list(buffer.getvalue()))
