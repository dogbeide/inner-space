from django.forms import ModelForm, Textarea
from .models import Comment

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['message']
        labels = {
         'message': 'New Comment:',
        }
        widgets = {
            'message': Textarea(attrs={'placeholder': 'Max characters: 256'}),
        }
