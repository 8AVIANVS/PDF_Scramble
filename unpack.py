import pikepdf
from fontTools.ttLib import TTFont
from io import BytesIO

# decompresses stream and saves
with pikepdf.open("aapl43.pdf") as pdf:
    pdf.save(
        "aapl43_unpacked.pdf",
    object_stream_mode=pikepdf.ObjectStreamMode.disable,
    compress_streams=False
    )

# decoding font /F4
# not being used currently
pdf = pikepdf.open("aapl43.pdf")
page = pdf.pages[0]
f4_ref = page.obj['/Resources']['/Font']['/F4']
f4      = f4_ref['/ToUnicode']
print(f4)

