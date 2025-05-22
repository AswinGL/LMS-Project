# Model Forms
from django import forms

from .models import Course ,  CategoryChoices , LevelChoices , Typechoice

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = ['title', 'description', 'image', 'category', 'level', 'fee', 'offer_fee']
        # fields = '_all_'
        exclude = ['instructor','active_status','uuid']

        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Course Title',
                'required' : 'required',
            }),

            'image' : forms.FileInput(attrs={
                'class' : 'form-control',
                
            }),

            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Course Description',
                'required' : 'required',
            }),
            

            'fee' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'required' : 'required',
                'placeholder': 'Enter Course Fee'
            }),

            'offer_fee' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Enter Offer Fee'
            }),

        }

    category = forms.ChoiceField(choices=CategoryChoices.choices,widget=forms.Select(attrs={
        'class' : 'form-control',
        'required' : 'required',
    }))

    level = forms.ChoiceField(choices=LevelChoices.choices,widget=forms.Select(attrs={
        'class' : 'form-control',
        'required' : 'required',
    }))

    type = forms.ChoiceField(choices=Typechoice.choices,widget=forms.Select(attrs={
        'class' : 'form-control',
        'required' : 'required',
    }))


    def clean(self):

        validated_data = super().clean()

        if validated_data.get('fees')  and validated_data.get('fees') < 0:

            self.add_error('fees', 'course fee must be greaterthan Zero')

        if validated_data.get('offer_fee') and validated_data.get('offer_fee') < 0:

            self.add_error('offer_fee', 'course fee must be greaterthan Zero')
        

        print(validated_data)
        return validated_data
    
    def __init__(self,*args,**kwargs):

        super(CourseCreateForm,self).__init__(*args,**kwargs)

        if not self.instance :

            self.fields.get('image').widget.attrs['required']='required'