from django.forms import ModelForm
from news.models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['nickname', 'email', 'text', ]