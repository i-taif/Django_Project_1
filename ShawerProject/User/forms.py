from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Profile
from .models import counselor


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم', max_length=30,
                               help_text='اسم المستخدم يجب ألا يحتوي على مسافات.')
    email = forms.EmailField(label='البريد الإلكتروني')
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label='الاسم الأخير')
    password1 = forms.CharField(
        label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم.')
        return cd['username']

class RegisterFormCon(UserCreationForm):
    class Meta:
        model = counselor
        fields = "__all__"

    username = forms.CharField(label='اسم المستخدم', max_length=30,help_text='اسم المستخدم يجب ألا يحتوي على مسافات.')
    email = forms.EmailField(label='البريد الإلكتروني')
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label='الاسم الأخير')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    start_date=forms.DateField(label='منذ عام')
    expertise_field=forms.CharField(label='التخصص')
    image=forms.ImageField(label="الصورة الشخصية")
    statment=forms.CharField(label='الخبرة')