from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["name", "amount"]  # FIXME: 테스트로 모든 필드를 입력받습니다.
