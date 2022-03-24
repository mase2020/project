from cProfile import label
from .models import Students,Classes,Teachers, Product, Subject, Course, Attendance, classAttendance,Homework,Fees,Registration,Audio
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
import datetime

class StudentsCreateForm(forms.ModelForm):

    photography = forms.BooleanField(label='', label_suffix=" : ",
                                  required=True, disabled=False,
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  help_text='<span class="my-class textinfo"> We would like to upload digital photos/audio recordings/videos of our students on our website www.madinamadrasa.co.uk <br>and other mediums to celebrate their achievements and publicity purposes. Do you give your consent for this?</span>',
                                  error_messages={'required': "Please check the box"})
    class Meta:
        model = Students
        fields = ('email','first_name', 'last_name', 'DOB', 'previous_madrasa','level_of_study','photography', 'address', 'postcode', 'which_class' , 'phone')
     

        widgets= {
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'DOB':forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
             'previous_madrasa':forms.TextInput(attrs={'class': 'form-control'}),
            'level_of_study':forms.Select(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'postcode':forms.TextInput(attrs={'class': 'form-control'}),
            'which_class':forms.Select(attrs={'class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            # 'parent1':forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone1':forms.TextInput(attrs={'class': 'form-control'}),
            # 'parent2':forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone2':forms.TextInput(attrs={'class': 'form-control'}),
      
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            # 'special_needs':forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class TeachersCreateForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ('first_name', 'last_name',  'address','postcode', 'phone', 'email' )

        widgets= {
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'postcode':forms.TextInput(attrs={'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
              'email':forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class ClassesCreateForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ('title',)

        widgets= {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            
            
        }


class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('subject',)

        widgets= {
            'subject':forms.TextInput(attrs={'class': 'form-control'}),
          
            
        }

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('classes' ,'subject', 'teacher' )

        widgets= {
            'subject':forms.Select(attrs={'class': 'form-control'}),
            'teacher':forms.Select(attrs={'class': 'form-control'}),
            'classes':forms.Select(attrs={'class': 'form-control'}),
          
            
        }


class StudentsUpdateForm(forms.ModelForm):
    photography = forms.BooleanField(label='', label_suffix=" : ",
                                  required=True, disabled=False,
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  help_text='<span class="my-class textinfo"> We would like to upload digital photos/audio recordings/videos of our students on our website www.madinamadrasa.co.uk <br>and other mediums to celebrate their achievements and publicity purposes. Do you give your consent for this?</span>',
                                  error_messages={'required': "Please check the box"})
    class Meta:
        model = Students
        fields = ('email','first_name', 'last_name', 'DOB', 'previous_madrasa','level_of_study','photography', 'address', 'postcode', 'which_class' , 'phone')
        widgets= {
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'DOB':forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
             'previous_madrasa':forms.TextInput(attrs={'class': 'form-control'}),
            'level_of_study':forms.Select(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'postcode':forms.TextInput(attrs={'class': 'form-control'}),
            'which_class':forms.Select(attrs={'class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            # 'parent1':forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone1':forms.TextInput(attrs={'class': 'form-control'}),
            # 'parent2':forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone2':forms.TextInput(attrs={'class': 'form-control'}),
      
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            # 'special_needs':forms.Textarea(attrs={'class': 'form-control'}),
            
        }



class TeachersUpdateForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ('first_name', 'last_name',  'address','postcode', 'phone')

        widgets= {
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'postcode':forms.TextInput(attrs={'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class ClassesUpdateForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ('title', )

        widgets= {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            
           
        
        }


class SubjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('subject',)

        widgets= {
            'subject':forms.TextInput(attrs={'class': 'form-control'}),
          
            
        }

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('classes' ,'subject', 'teacher' )

        widgets= {
            'subject':forms.TextInput(attrs={'subject': 'form-control'}),
            'teacher':forms.Select(attrs={'teacher': 'form-control'}),
            'classes':forms.Select(attrs={'class': 'form-control'}),
          
            
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']


class AttendanceCreateForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('classes',  )

        widgets= {
           'classes':forms.Select(attrs={'class': 'form-control'}),
       
        
           
            
        }


class AttendanceUpdateForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('classes', )

        widgets= {
           'classes':forms.Select(attrs={'class': 'form-control'}),
             
        
           
            
        }



class AudioCreateForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('title','teacher','audio','description'  )

        widgets= {
           
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'teacher':forms.Select(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
                   
        }


class AudioUpdateForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('title','teacher','audio','description'  )

        widgets= {
           
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'teacher':forms.Select(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
                   
        }

class ClassAttendanceCreateForm(forms.ModelForm):
    class Meta:
        model = classAttendance
        fields = ('student_id','attendance_id', 'status'  )

        widgets= {
           'student_id':forms.Select(attrs={'class': 'form-control'}),
           'attendance_id':forms.Select(attrs={'class': 'form-control'}),
           'status':forms.TextInput(attrs={'class': 'form-control'}),
       
        
           
            
        }


class ClassAttendanceUpdateForm(forms.ModelForm):
    class Meta:
        model = classAttendance
        fields = ('student_id','attendance_id', 'status'  )

        widgets= {
           'student_id':forms.Select(attrs={'class': 'form-control'}),
           'attendance_id':forms.Select(attrs={'class': 'form-control'}),
           'status':forms.TextInput(attrs={'class': 'form-control'}),
       
        
           
            
        }





class HomeworkCreateForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('date', 'course','content','audio')

        widgets= {
            'date':forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'course':forms.Select(attrs={'class': 'form-control'}),
            'content':forms.Textarea(attrs={'class': 'form-control'}),
        }


class HomeworkUpdateForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('date', 'course','content','audio')

        widgets= {
            'date':forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'course':forms.Select(attrs={'class': 'form-control'}),
            'content':forms.Textarea(attrs={'class': 'form-control'}),
        }



class FeesCreateForm(forms.ModelForm):
    class Meta:
        model = Fees
        fields = ('student_id','year', 'term','amount','description')

        widgets= {
            
            'student_id':forms.Select(attrs={'class': 'form-control'}),
            'year':forms.Select(attrs={'class': 'form-control'}),
            'term':forms.Select(attrs={'class': 'form-control'}),
            'amount':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
        }


class FeesUpdateForm(forms.ModelForm):
    class Meta:
         model = Fees
         fields = ('student_id','year', 'term','amount','description')

         widgets= {
            
            'student_id':forms.Select(attrs={'class': 'form-control'}),
            'year':forms.Select(attrs={'class': 'form-control'}),
            'term':forms.Select(attrs={'class': 'form-control'}),
            'amount':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
        }


#e-commerce


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price','category','shortdesc','description','slug','image' )

        widgets= {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'price':forms.TextInput(attrs={'class': 'form-control'}),
            'category':forms.Select(attrs={'class': 'form-control'}),
            'shortdesc':forms.Textarea(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
            'slug':forms.TextInput(attrs={'class': 'form-control'}),
        
           
            
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
         model = Product
         fields = ('title', 'price','category','shortdesc','description','slug','image' )

         widgets= {
           'title':forms.TextInput(attrs={'class': 'form-control'}),
            'price':forms.TextInput(attrs={'class': 'form-control'}),
            'category':forms.Select(attrs={'class': 'form-control'}),
            'shortdesc':forms.Textarea(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
            'slug':forms.TextInput(attrs={'class': 'form-control'}),
        
            
           
            
            
        }


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)



class classForm(forms.Form):
     shipping_address = forms.CharField(required=False)


class RegistrationCreateForm(forms.ModelForm):

    a1 = forms.BooleanField(label='', label_suffix=" : ",
                                  required=True, disabled=False,
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  help_text='<span class="my-class textinfo">I hereby agree that my answers are true & complete to the best of my knowledge.</span>',
                                  error_messages={'required': "Please check the box"})
    a2 = forms.BooleanField(label='', label_suffix=" : ",
                                  required=True, disabled=False,
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  help_text='<span class="my-class textinfo">I also agree to follow the rules and regulations of Madina Masjid Weekend Madrasa.</span>',
                                  error_messages={'required': "Please check the box"})
    a3 = forms.BooleanField(label='', label_suffix=" : ",
                                  required=True, disabled=False,
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  help_text='<span class="my-class textinfo">I will endeavour to support my child in preparing homework & ensure my child’s attendance at the allocated time.</span>',
                                  error_messages={'required': "Please check the box"})
    a4 = forms.BooleanField(label='', label_suffix=" : ",
                                  required=True, disabled=False,
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  help_text='<span class="my-class textinfo">I  will also ensure my child is in full uniform as described in the dress code policy.</span>',
                                  error_messages={'required': "Please check the box"})


    a5 = forms.BooleanField(label='', label_suffix=" : ",
                                  required=True, disabled=False,
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  help_text='<span class="my-class textinfo">I understand and will adhere to the policies in place for my child while he/she is attending class.</span>',
                                  error_messages={'required': "Please check the box"})

    photography = forms.BooleanField(label='', label_suffix=" : ",
                                  required=False, disabled=False,
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  help_text='<span class="my-class textinfo"> We would like to upload digital photos/audio recordings/videos of our students on our website www.madinamadrasa.co.uk <br>and other mediums to celebrate their achievements and publicity purposes. Do you give your consent for this?</span>',
                                  error_messages={'required': "Please check the box"})
    class Meta:
        model = Registration
        fields = ('email','heard','referred' , 'session','first_name', 'last_name', 'DOB', 'previous_madrasa','level_of_study','photography',\
             'address', 'postcode',  'phone', 'a1', 'a2', 'a3', 'a4', 'a5')
        help_texts = {
        'session': "<br><hr/><div class='textinfo'><div><strong>DETAILS ABOUT THE CHILD</strong></div><div>Information provided on this form will be used for short listing for your child's placement at our establishment.</div><br>",
    }

        widgets= {
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'heard':forms.Select(attrs={'class': 'form-control'}),
            'referred':forms.TextInput(attrs={'class': 'form-control'}),
            'session':forms.Select(attrs={'class': 'form-control'}),
  
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'DOB':forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'previous_madrasa':forms.TextInput(attrs={'class': 'form-control'}),
            'level_of_study':forms.Select(attrs={'class': 'form-control'}),
           
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'postcode':forms.TextInput(attrs={'class': 'form-control'}),
           
            # 'parent1':forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone1':forms.TextInput(attrs={'class': 'form-control'}),
            # 'parent2':forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone2':forms.TextInput(attrs={'class': 'form-control'}),
      
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            # 'special_needs':forms.Textarea(attrs={'class': 'form-control'}),
            
            
        }
