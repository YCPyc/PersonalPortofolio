from django.forms import ModelForm 
from .models import Project, Message

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','thumbnail','body']
    
    def __init__(self,*args,**kwargs):
        # relate projectform to self
        super(ProjectForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['body'].widget.attrs.update({'class': 'form-control'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']

    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['subject'].widget.attrs.update({'class':'form-control'})
        self.fields['body'].widget.attrs.update({'class':'form-control'})