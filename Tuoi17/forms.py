from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'ho_ten_khai_sinh': forms.TextInput(attrs={'class': 'form-control'}),
            'ho_ten_thuong_dung': forms.TextInput(attrs={'class': 'form-control'}),
            'ngay_sinh': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'so_cmnd_cccd': forms.TextInput(attrs={'class': 'form-control'}),
            'noi_dang_ky_khai_sinh': forms.TextInput(attrs={'class': 'form-control'}),
            'que_quan': forms.TextInput(attrs={'class': 'form-control'}),
            'dan_toc': forms.TextInput(attrs={'class': 'form-control'}),
            'ton_giao': forms.TextInput(attrs={'class': 'form-control'}),
            'quoc_tich': forms.TextInput(attrs={'class': 'form-control'}),
            'noi_thuong_tru_gia_dinh': forms.TextInput(attrs={'class': 'form-control'}),
            'noi_o_hien_tai': forms.TextInput(attrs={'class': 'form-control'}),
            'thanh_phan_gia_dinh': forms.TextInput(attrs={'class': 'form-control'}),
            'ban_than': forms.TextInput(attrs={'class': 'form-control'}),
            'trinh_do': forms.TextInput(attrs={'class': 'form-control'}),
            'nghe_nghiep': forms.TextInput(attrs={'class': 'form-control'}),
            'ho_ten_cha': forms.TextInput(attrs={'class': 'form-control'}),
            'nam_sinh_cha': forms.NumberInput(attrs={'class': 'form-control'}),
            'tinh_trang_cha': forms.TextInput(attrs={'class': 'form-control'}),
            'nghe_nghiep_cha': forms.TextInput(attrs={'class': 'form-control'}),
            'noi_o_cha': forms.TextInput(attrs={'class': 'form-control'}),
            'ho_ten_me': forms.TextInput(attrs={'class': 'form-control'}),
            'nam_sinh_me': forms.NumberInput(attrs={'class': 'form-control'}),
            'tinh_trang_me': forms.TextInput(attrs={'class': 'form-control'}),
            'nghe_nghiep_me': forms.TextInput(attrs={'class': 'form-control'}),
            'noi_o_me': forms.TextInput(attrs={'class': 'form-control'}),
            'so_anh_em': forms.NumberInput(attrs={'class': 'form-control'}),
            'ten_anh_chi_em': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'hoc_luc_6_11': forms.TextInput(attrs={'class': 'form-control'}),
            'hoc_luc_11_15': forms.TextInput(attrs={'class': 'form-control'}),
            'hoat_dong_16_den_nay': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }