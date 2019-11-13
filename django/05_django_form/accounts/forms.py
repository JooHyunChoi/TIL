from django import forms
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        '''
            user클래스를 바로 가져와 사용하는것이 아니라 , get_user_model()을 사용해서
            User쿨래스를 참조한다.
        '''
        model = get_user_model()
        ''' UserChangeForm-> User클래스 -> AbstractUser클래스 
            django 공식문서 : 
        '''
        fields = ('email' , 'last_name' , 'first_name',)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username' , 'password1' , 'password2' , 'email',)