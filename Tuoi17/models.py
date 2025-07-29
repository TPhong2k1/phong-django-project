from django.db import models

class Registration(models.Model):
    ho_ten_khai_sinh = models.CharField("Họ tên khai sinh in hoa", blank=True, null=True)
    ho_ten_thuong_dung = models.CharField("Họ và tên thường dùng", blank=True, null=True)
    ngay_sinh = models.DateField("Ngày tháng năm sinh", blank=True, null=True)
    GIOI_TINH_CHOICES = [
    ('Nam', 'Nam'),
    ('Nữ', 'Nữ'),
    ]
    gioi_tinh = models.CharField("Giới tính", max_length=100, choices=GIOI_TINH_CHOICES, default='Nam')
    so_cmnd_cccd = models.CharField("Số CMND hoặc CCCD", blank=True, null=True)
    noi_dang_ky_khai_sinh = models.CharField("Nơi đăng ký khai sinh", blank=True, null=True)
    que_quan = models.CharField("Quê quán", blank=True, null=True)
    dan_toc = models.CharField("Dân tộc", blank=True, null=True)
    ton_giao = models.CharField("Tôn giáo", blank=True, null=True)
    quoc_tich = models.CharField("Quốc tịch", blank=True, null=True)
    noi_thuong_tru_gia_dinh = models.CharField("Nơi thường trú của gia đình", blank=True, null=True)
    noi_o_hien_tai = models.CharField("Nơi ở hiện tại của bản thân", blank=True, null=True)
    thanh_phan_gia_dinh = models.CharField("Thành phần gia đình", blank=True, null=True)
    ban_than = models.TextField("Thành phần Bản thân", blank=True, null=True)
    trinh_do = models.CharField("Trình độ học vấn", blank=True, null=True)
    nghe_nghiep = models.CharField("Nghề nghiệp", blank=True, null=True)

    ho_ten_cha = models.CharField("Họ tên cha", blank=True, null=True)
    nam_sinh_cha = models.IntegerField("Năm sinh cha", blank=True, null=True)
    tinh_trang_cha = models.CharField("Tình trạng (cha)", blank=True, null=True)
    nghe_nghiep_cha = models.CharField("Nghề nghiệp (cha)", blank=True, null=True)
    noi_o_cha = models.CharField("Nơi ở hiện tại của cha", blank=True, null=True)

    ho_ten_me = models.CharField("Họ tên mẹ", blank=True, null=True)
    nam_sinh_me = models.IntegerField("Năm sinh mẹ", blank=True, null=True)
    tinh_trang_me = models.CharField("Tình trạng (mẹ)", blank=True, null=True)
    nghe_nghiep_me = models.CharField("Nghề nghiệp (mẹ)", blank=True, null=True)
    noi_o_me = models.CharField("Nơi ở hiện tại của mẹ", blank=True, null=True)

    so_anh_em = models.IntegerField("Gia đình có bao nhiêu anh chị em", blank=True, null=True)
    ten_anh_chi_em = models.TextField("Tên anh chị em ruột", blank=True, null=True)
    hoc_luc_6_11 = models.CharField("6-11 tuổi học trường gì", blank=True, null=True)
    hoc_luc_11_15 = models.CharField("11-15 tuổi học trường gì", blank=True, null=True)
    hoat_dong_16_den_nay = models.TextField("Từ 16 tuổi đến nay làm gì", blank=True, null=True)

    def __str__(self):
        return self.ho_ten_khai_sinh