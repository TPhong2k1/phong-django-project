import qrcode
from PIL import Image, ImageDraw

# Dữ liệu QR
data = "http://127.0.0.1:8000/"
# data = "Hé Lô"
# Tạo QR
qr = qrcode.QRCode(
    version=10, # Kích thước mã QR (1 nhỏ nhất, 40 lớn nhất)
    error_correction=qrcode.constants.ERROR_CORRECT_H, # Mức chịu lỗi: L, M, Q, H
    box_size=10, # Kích thước mỗi “hộp” trong QR
    border=4 # Viền trắng quanh QR (4 là mặc định)
)
qr.add_data(data)
qr.make(fit=True)

# Tạo ảnh QR
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
draw = ImageDraw.Draw(img)

# Tính toán vị trí các finder patterns
box_size = 10
border = 4
blue = (0, 102, 255)

def draw_finder(draw, top_left_x, top_left_y):
    size = 7 * box_size
    inner = 3 * box_size
    draw.rectangle([top_left_x, top_left_y, top_left_x + size, top_left_y + size], outline=blue, width=box_size)
    draw.rectangle(
        [top_left_x + 2*box_size, top_left_y + 2*box_size,
         top_left_x + 5*box_size, top_left_y + 5*box_size],
        fill=blue
    )

# Vẽ 3 cực: trên trái, trên phải, dưới trái
draw_finder(draw, border * box_size, border * box_size)  # top-left
draw_finder(draw, img.size[0] - (border + 7) * box_size, border * box_size)  # top-right
draw_finder(draw, border * box_size, img.size[1] - (border + 7) * box_size)  # bottom-left

# Lưu ảnh
img.save("Tuoi17/static/QR/QRcode.png")
print("Đã tạo mã QRcode Thành Công!")
