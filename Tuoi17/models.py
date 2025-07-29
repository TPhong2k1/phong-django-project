from django.db import models

class Registration(models.Model):
    ho_ten_khai_sinh = models.CharField("Họ tên khai sinh in hoa", max_length=255)
    ho_ten_thuong_dung = models.CharField("Họ và tên thường dùng", max_length=255)
    ngay_sinh = models.DateField("Ngày tháng năm sinh")
    GIOI_TINH_CHOICES = [
    ('Nam', 'Nam'),
    ('Nữ', 'Nữ'),
    ]
    gioi_tinh = models.CharField("Giới tính", max_length=100, choices=GIOI_TINH_CHOICES)
    so_cmnd_cccd = models.CharField("Số CMND hoặc CCCD", max_length=20)
    noi_dang_ky_khai_sinh = models.CharField("Nơi đăng ký khai sinh", max_length=255)
    que_quan = models.CharField("Quê quán", max_length=255)
    dan_toc = models.CharField("Dân tộc", max_length=100)
    ton_giao = models.CharField("Tôn giáo", max_length=100)
    quoc_tich = models.CharField("Quốc tịch", max_length=100)
    noi_thuong_tru_gia_dinh = models.CharField("Nơi thường trú của gia đình", max_length=255)
    noi_o_hien_tai = models.CharField("Nơi ở hiện tại của bản thân", max_length=255)
    thanh_phan_gia_dinh = models.CharField("Thành phần gia đình", max_length=100)
    ban_than = models.TextField("Thành phần Bản thân", blank=True, null=True)
    trinh_do = models.CharField("Trình độ học vấn", max_length=100)
    nghe_nghiep = models.CharField("Nghề nghiệp", max_length=100)

    ho_ten_cha = models.CharField("Họ tên cha", max_length=255)
    nam_sinh_cha = models.IntegerField("Năm sinh cha")
    tinh_trang_cha = models.CharField("Tình trạng (cha)", max_length=100)
    nghe_nghiep_cha = models.CharField("Nghề nghiệp (cha)", max_length=100)
    noi_o_cha = models.CharField("Nơi ở hiện tại của cha", max_length=255)

    ho_ten_me = models.CharField("Họ tên mẹ", max_length=255)
    nam_sinh_me = models.IntegerField("Năm sinh mẹ")
    tinh_trang_me = models.CharField("Tình trạng (mẹ)", max_length=100)
    nghe_nghiep_me = models.CharField("Nghề nghiệp (mẹ)", max_length=100)
    noi_o_me = models.CharField("Nơi ở hiện tại của mẹ", max_length=255)

    so_anh_em = models.IntegerField("Gia đình có bao nhiêu anh chị em")
    ten_anh_chi_em = models.TextField("Tên anh chị em ruột")
    hoc_luc_6_11 = models.CharField("6-11 tuổi học trường gì", max_length=255)
    hoc_luc_11_15 = models.CharField("11-15 tuổi học trường gì", max_length=255)
    hoat_dong_16_den_nay = models.TextField("Từ 16 tuổi đến nay làm gì")

    def __str__(self):
        return self.ho_ten_khai_sinh