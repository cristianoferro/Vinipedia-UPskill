from django import forms
from .models import Evaluation


class EvaluationForm(forms.ModelForm):

    class Meta:
        model = Evaluation
        fields = ('description', 'score')


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200, label="",
                            widget=forms.TextInput(attrs={'placeholder': 'Search'}))
