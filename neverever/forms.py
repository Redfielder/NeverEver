from django import forms
from neverever.models import Statement, Category, Answer, Session, Player


class StatementForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Never have I ever ")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    no_answers = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    yes_answers = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    nsfw = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    category_list = []
    for cat in Category.objects.all():
        category_list.append((cat.id, cat))

    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                           choices=category_list)

    class Meta:
        model = Statement
        fields = ('title', 'nsfw', 'categories')


class SessionForm(forms.ModelForm):
    sid = forms.CharField(widget=forms.HiddenInput(), required=False)
    nsfw = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    category_list = []
    for cat in Category.objects.all():
        category_list.append((cat.id, cat))

    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                           choices=category_list)

    class Meta:
        model = Session
        fields = ('nsfw', 'categories')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)


class PlayerForm(forms.ModelForm):
    genders = (('', 'N/A'),('F', 'Female'), ('M', 'Male'),)
    gender = forms.ChoiceField(choices=genders, help_text="Gender", required=False)
    age = forms.IntegerField(help_text="Age", required=False)
    nationality = forms.CharField(max_length=128, help_text="Nationality", required=False)

    class Meta:
        model = Player
        fields = ('gender', 'age', 'nationality')