from django import forms   

    
class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    description = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        if title and description and title.lower() == description.lower():
            raise forms.ValidationError('Title and description must be different')
        return cleaned_data
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'python' in title.lower():
            raise forms.ValidationError('Слово "python" недоступно в заголовке')
        return title