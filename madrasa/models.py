

# Create your models here.
from django.db import models
from django.shortcuts import  reverse
from django.conf import settings
from django.shortcuts import reverse
from django_countries.fields import CountryField

''' models for admin use '''




level_categories =(
    ('1','Qaaidah'),
    ('2', 'Juz Amma'),
    ('3','Quran'),
    ('4', 'Tahfiz/Hifz'),
    ('5', 'N/A')
)

year_choices= (
    ('21/22', '21/22'),
    ('22/23', '22/23')
    
)

term_choices = (
    ('1','1'),
    ('2','2'),
    ('3','3')
)

heard_categories = (
    ('fb', 'Facebook'),
    ('wom', 'Word of Mouth')
)
session_categories =(
    ('1','9:45 - 11:45'),
    ('2', '12:00 - 14:00'),
    ('3','No Preference')
)


class Teachers(models.Model):
    id=models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postcode =models.CharField(max_length=8)
    phone = models.CharField('Phone Number',max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    
   
    def get_absolute_url(self):
        return '/manage_staff'
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('class' ,max_length=1)
    created = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return '/manage_class'
    def __str__(self):
        return self.title
 
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField('subject' ,max_length=30)
    created = models.DateTimeField(auto_now_add=True)
     
    def get_absolute_url(self):
        return '/manage_subject'
    def __str__(self):
        return self.subject

class Course(models.Model):
    id= models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teachers,  on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes,  on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,  on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return '/manage_course'
    def __str__(self):
        return "Class " +self.classes.title +" "+ self.subject.subject

class Audio(models.Model):
    id= models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teachers,  on_delete=models.CASCADE)
    audio = models.FileField(upload_to = "static/e-commerce/audios/")
    description = models.TextField(blank=True, null=True,)
    created = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return '/manage_audio'
    def __str__(self):
        return self.title

class Homework(models.Model):
    id= models.AutoField(primary_key=True)
    date = models.DateField()
    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    content = models.TextField()
    audio = models.ForeignKey(Audio,on_delete=models.DO_NOTHING,default= 1)
    created = models.DateTimeField(auto_now_add=True)
  
 

    def get_absolute_url(self):
        return '/manage_homework'
    def __str__(self):
        return str(self.date)

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    DOB = models.DateField("Date of Birth")
    photography =models.BooleanField(blank=True, null=True,default=False)
    previous_madrasa = models.CharField('Previous Madrasa', max_length=255,  blank=True,
    null=True,)
    level_of_study = models.CharField(max_length = 20,choices=level_categories,   blank=True,
    null=True,)
    # special_needs = models.CharField('Special needs', max_length=255, default='NO')
    address = models.CharField(max_length=255)
    postcode =models.CharField(max_length=8)
    which_class= models.ForeignKey( Classes, on_delete=models.DO_NOTHING,blank=True, null=True,)
    # parent1=models.CharField('Parent/Guardian' , max_length=30)
    # phone1= models.CharField('Phone Number', max_length=15)
    # parent2=models.CharField('Parent/Guardian'  , max_length=30)
    # phone2 = models.CharField('Phone Number',max_length=15)
    # gender =models.CharField(max_length=8)

    phone = models.CharField('Phone Number',max_length=15)
    # class_id = models.ForeignKey(Classes,  on_delete=models.DO_NOTHING)
    
 


    class Meta:
        ordering = ["which_class"]
    def get_absolute_url(self):
       return '/manage_student'
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    classes =models.ForeignKey(Classes,on_delete=models.DO_NOTHING)
    date=models.DateField()
    created=models.DateTimeField(auto_now_add=True)
  

    
    def get_absolute_url(self):
       return '/manage_attendance'
    def __str__(self):
        
        return str(self.date)
 
class classAttendance(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
       return '/manage_class_attendance'
    def __str__(self):
        
        return self.student_id.first_name
 
class Fees(models.Model):
    id = models.AutoField(primary_key=True)
    date= date = models.DateField(auto_now_add=True)
    amount = models.FloatField()
    year = models.CharField(max_length = 5,choices=year_choices)
    term = models.CharField(max_length = 1,choices=term_choices)
    description= models.TextField(blank=True, null=True,)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    

    def get_absolute_url(self):
       return '/manage_fees'
    def __str__(self):
        
        return self.student_id.first_name +" " + self.student_id.last_name

    def calculate_fees(self,year):
        total = 540
    
  
        total -= self.amount
        return total

class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    heard = models.CharField('Where did you hear about us?',max_length = 20,choices=heard_categories)
    referred = models.CharField("If referred, please include the child's name of the referrer.",max_length=255)
    session = models.CharField('Please specify your preferred session. This is not guaranteed',max_length = 20,choices=session_categories)
    first_name = models.CharField("First Name / Middle Names",max_length=255)
    last_name = models.CharField("Surname ",max_length=255)
    DOB = models.DateField("Date of Birth")
    # gender =models.CharField(max_length=8)
    #school year
    previous_madrasa = models.CharField('Previous Madrasa', max_length=255)
    level_of_study = models.CharField(max_length = 20,choices=level_categories)
    photography =models.BooleanField(blank=True, null=True,default=False)

    # special_needs = models.CharField('Special needs', max_length=255, default='NO')
    address = models.CharField(max_length=255)
    postcode =models.CharField(max_length=8)
 
    # parent1=models.CharField('Parent/Guardian' , max_length=30)
    # phone1= models.CharField('Phone Number', max_length=15)
    # parent2=models.CharField('Parent/Guardian'  , max_length=30)
    # phone2 = models.CharField('Phone Number',max_length=15)
    

    phone = models.CharField('Phone Number',max_length=15)
    # class_id = models.ForeignKey(Classes,  on_delete=models.DO_NOTHING)
    a1=models.BooleanField(default=False)
    a2=models.BooleanField(default=False)
    a3=models.BooleanField(default=False)
    a4=models.BooleanField(default=False)
    a5=models.BooleanField(default=False)


    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["created"]

    def get_absolute_url(self):
       return 'send_application_email'
    def __str__(self):
        return self.first_name + ' ' + self.last_name


  
   
   


''' e-commerce models '''


category_choices= (
    ('Books', 'Books'),
    ('Bags', 'Bags'),
    ('Clothes', 'Clothes'),
    ('Courses', 'Courses'),
    ('Perfumes', 'Perfumes')
    
)
class Product(models.Model):

    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length = 8,choices=category_choices)
    image = models.FileField(upload_to = "static/e-commerce/images/")
    description =models.TextField(blank=True, null=True,)
    shortdesc =models.CharField( blank=True, null=True,max_length=255)
    slug = models.SlugField()
  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return reverse('product_detail', kwargs={
           'slug':self.slug
       })
    def get_cart_url(self):
       return reverse('add_cart', kwargs={
           'slug':self.slug
       })
    def get_remove_cart_url(self):
       return reverse('remove_cart', kwargs={
           'slug':self.slug
       })

class OrderItem(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total(self):
        total = self.product.price * self.quantity
        return total

class Order(models.Model):
    slug = models.AutoField(primary_key=True)
   
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    products = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)

    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.user.username

    def get_total(self):
        total =0
        for p in self.products.all():
            total += p.get_total()
        return total
    def get_tax_total(self):
    
        return self.get_total() * 1.2

    def get_tax(self):
         
        return self.get_total() * 0.2

    class Meta:
        ordering = ["slug"]
  
class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)








# class Feedback(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     feedback = models.TextField()
#     feedback_reply = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()



# class NotificationStudent(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     message = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()



# class Management(models.Model):
#     id=models.AutoField(primary_key=True)
#     # admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     phone = models.CharField('Phone Number',max_length=15)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)
    
#     # def get_absolute_url(self):
#     #     return '/madrasa/teachers/list'
#     # def __str__(self):
#     #     return self.first_name + ' ' + self.last_name



class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name