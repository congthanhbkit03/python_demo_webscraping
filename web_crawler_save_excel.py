import requests, bs4, openpyxl
url = 'http://pdu.edu.vn/nss.php?name=DanhBa&search=true&hoten=&phongban=0&p='
i = 0 # bat dau trang 1
res = requests.get(url + str(i))
res.encoding = 'utf-8'
bsObject = bs4.BeautifulSoup(res.text, 'html.parser')

print(bsObject)
selectors = "tr[bgcolor='lightskyblue'], tr[bgcolor='lightyellow']"
danhsach = []
for row in bsObject.select(selectors):
    object = {}
    object['name'] = row.find_all("td")[0].get_text().strip()
    object['address'] = row.find_all("td")[3].get_text()
    object['phone'] = row.find_all("td")[4].get_text()
    object['email'] = row.find_all("td")[6].get_text()
    danhsach.append(object)

print(danhsach)

# ghi ra file excel
wb = openpyxl.Workbook()  # create a blank workbook
sheet = wb.active
sheet.title = "Danh bạ trường"
sheet['A1'] = "Họ tên"
sheet['B1'] = "Số điện thoại"
sheet['C1'] = "Địa chỉ"
sheet['D1'] = "Email"

for i in range(len(danhsach)):
    sheet['A' + str(i+2)] = danhsach[i]['name']
    sheet['B' + str(i+2)] = danhsach[i]['address']
    sheet['C' + str(i+2)] = danhsach[i]['phone']
    sheet['D' + str(i+2)] = danhsach[i]['email']

wb.save("danhba.xlsx")
