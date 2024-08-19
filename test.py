import requests,io,PyPDF2

# try:
request = requests.get("https://takyuetinternational.com/pub/media/ShippingLabels/YunExpress_36000027987_1.pdf")
# request = requests.get("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
# request = requests.get("http://f0.yunexpress.com:81/PDF/45a0caac54f44bcda1326cb5a1cc75a6yt2321621904000978.pdf")
# request = requests.get("http://f0.yunexpress.com:81/PDF/17d609257c7d4afd8e5e3da9768973f8yt2321621904000976.pdf")
# request = requests.get("http://f0.yunexpress.com:81/PDF/70145313a73f4869b948826c173418eayt2321621904000973.pdf")
#request = requests.get("http://f0.yunexpress.com:81/PDF/a7c8ff9507004deb9713afae71ed8235yt2321221904001381.pdf")

pdf_file = io.BytesIO(request.content)
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
print("************************", pdf_reader)
# except Exception as e:
    # print("-------error----------------", e)