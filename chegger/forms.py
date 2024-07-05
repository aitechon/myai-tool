from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Ask your question..."}),
        max_length=255,
    )
