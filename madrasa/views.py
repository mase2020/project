
from http.client import HTTPResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import  messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import CourseUpdateForm, StudentsCreateForm,  ClassesCreateForm,CourseCreateForm,SubjectCreateForm, SubjectUpdateForm, TeachersCreateForm,StudentsUpdateForm,TeachersUpdateForm,ClassesUpdateForm,SubjectUpdateForm,CourseUpdateForm, CreateUserForm
from .models import Students,Classes,Teachers, Product, Order, OrderItem,Subject, Course,Registration,Audio
from .forms import  ProductCreateForm,ProductUpdateForm,CheckoutForm,RegistrationCreateForm,AudioCreateForm, AudioUpdateForm
from .models import  Address, Payment
from django.views.generic import ListView,DetailView, View
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django.utils import timezone
from django.db import connection
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML,CSS
import tempfile
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import AttendanceUpdateForm,ClassAttendanceUpdateForm,HomeworkCreateForm,HomeworkUpdateForm, FeesCreateForm,FeesUpdateForm      
from .models import Students,Classes,Attendance,classAttendance, Homework, Fees
from django.views.generic import ListView,DetailView, View
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import connection
from django.contrib.auth.decorators import login_required, permission_required

'''admin views'''

#login view
def login_view(request):
    context = {
    "login_view": "active"
  }

  # Both username and password are captured from the submitted log in form
    username = request.POST.get("username",'')
    password = request.POST.get('password', '')
 
  # Both username and password are passed into the authenticate() method to verify the user
    user = authenticate(request, username=username, password=password)
 
  # If the user is valid, then a user object is returned.
    if user is not None:

        login(request,user)
        return render('home')
    else:
      return HttpResponse("invalid credentials")
    return render(request, "registration/login.html", context)

#logout
def logout_view(request):
  # ... Other logic
  logout(request)
  return redirect("home")


#registration page
class SignUp(CreateView):

    form_class = CreateUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("login")
   
#home page
def index(req):
    context ={}
    return render(req,'madrasa/home-page/index.html', context)

@login_required(login_url= "/account/login/")
@permission_required('madrasa.view_choice', login_url='login')
def admin(req):
    return render(req,'madrasa/home-page/admin.html')



'''Management views'''

#CRUD for students

class StudentsCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Students
    form_class = StudentsCreateForm
    template_name = 'management/students/add_student_template.html'


class StudentList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Students

    def get(self, request,*args, **kwargs):
        students = Students.objects.all()
        context = {
            'name': 'STUDENTS',
            'students_list': students
        
        }
        return render(request,'management/students/manage_student_template.html',context)


class StudentUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Students
    template_name = 'management/students/edit_student_template.html'
    form_class= StudentsUpdateForm

class StudentDelete(LoginRequiredMixin,PermissionRequiredMixin,  DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Students
    template_name = 'management/students/student_delete_form.html'
    success_url = '/manage_student'

 # CRUD for Staff

class TeachersCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Teachers
    form_class = TeachersCreateForm
    template_name = 'management/teachers/add_staff_template.html'

class TeacherList(LoginRequiredMixin,PermissionRequiredMixin,  ListView):
    
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Teachers
    def get(self, request,*args, **kwargs):
        students = Teachers.objects.all()
        context = {
            'name': 'Teachers',
            'teachers_list': students
        
        }
        return render(request,'management/teachers/manage_staff_template.html',context)


class TeacherUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Teachers
    template_name = 'management/teachers/edit_staff_template.html'
    form_class= TeachersUpdateForm

class TeacherDelete(LoginRequiredMixin,PermissionRequiredMixin,  DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Teachers
    template_name = 'management/teachers/teacher_delete_form.html'
    success_url = '/manage_staff'




# CRUD for Classes

class ClassesCreate(LoginRequiredMixin,PermissionRequiredMixin,  CreateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Classes
    form_class = ClassesCreateForm
    template_name = 'management/classess/add_class_template.html'


class ClassesList(LoginRequiredMixin,PermissionRequiredMixin,  ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Classes
    def get(self, request,*args, **kwargs):
        classes = Classes.objects.all()
        context = {
            'name': 'CLASSES',
            'classes_list': classes
        
        }
        return render(request,'management/classess/manage_class_template.html',context)

class ClassUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Classes
    template_name = 'management/classess/edit_class_template.html'
    form_class= ClassesUpdateForm

class ClassDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Classes
    template_name = 'management/classess/class_delete_form.html'
    success_url = '/manage_class'



# CRUD for Courses
class CourseCreate(LoginRequiredMixin,PermissionRequiredMixin,  CreateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Course
    form_class = CourseCreateForm
    template_name = 'management/courses/add_course_template.html'

class CourseList(LoginRequiredMixin,PermissionRequiredMixin,  ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Course
    def get(self, request,*args, **kwargs):
        courses = Course.objects.all()
        context = {
            'name': 'COURSES',
            'course_list': courses
        
        }
        return render(request,'management/courses/manage_course_template.html',context)

class CourseUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Course
    template_name = 'management/courses/edit_course_template.html'
    form_class= CourseUpdateForm


class CourseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Course
    template_name = 'management/courses/course_delete_form.html'
    success_url = '/manage_class'


# CRUD for Subjects
class SubjectCreate(LoginRequiredMixin,PermissionRequiredMixin,  CreateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Subject
    form_class = SubjectCreateForm
    template_name = 'management/subjects/add_subject_template.html'



class SubjectList(LoginRequiredMixin,PermissionRequiredMixin,  ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Subject
    def get(self, request,*args, **kwargs):
        subjects = Subject.objects.all()
        context = {
            'name': 'SUBJECTS',
            'subject_list': subjects
        
        }
        return render(request,'management/subjects/manage_subject_template.html',context)



class SubjectUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Subject
    template_name = 'management/subjects/edit_subject_template.html'
    form_class= SubjectUpdateForm
  



class SubjectDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Subject
    template_name = 'management/subjects/subject_delete_form.html'
    success_url = '/manage_class'



# CRUD for Applications


class Application( CreateView):
    
    model = Registration
    form_class = RegistrationCreateForm
    template_name = 'registration/application_form.html'


class ApplicationList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Registration

    def get(self, request,*args, **kwargs):
        students = Registration.objects.all()
        context = {
            'name': 'STUDENTS',
            'students_list': students
        
        }
        return render(request,'registration/manage_applications.html',context)

def save_student(req, pk,LoginRequiredMixin, PermissionRequiredMixin,):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    cursor = connection.cursor()
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO madrasa_students(madrasa_students.first_name,
    madrasa_students.last_name, madrasa_students.email,
    madrasa_students.photography,
    madrasa_students.phone,madrasa_students.address,
    madrasa_students.postcode,madrasa_students.DOB, 
    madrasa_students.created)
    SELECT   madrasa_registration.first_name, madrasa_registration.last_name,
    madrasa_registration.email, madrasa_registration.photography, 
    madrasa_registration.phone, madrasa_registration.address,
    madrasa_registration.postcode, madrasa_registration.DOB, 
    FROM  madrasa_registration
    where madrasa_registration.id =  %s
        ''',[ pk])

    return redirect("manage_applications")


class ApplicationDelete(LoginRequiredMixin,PermissionRequiredMixin,  DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Registration
    template_name = 'registration/delete_application.html'
    success_url = '/manage_applications'




''' E-Commerce Views'''

def product_detail(req):
    context ={}
    return render(req,'e-commerce/product-detail.html', context)


class cart(ListView):
    model= Order
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'e-commerce/shopping-cart.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")




class Products(  ListView):
    
    
    model= Product
    def get(self, request,*args, **kwargs):
        items = Product.objects.all()
        context = {
            
            'items': items
        
        }
        return render(request,'e-commerce/product.html', context)





class ProductCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Product
    form_class = ProductCreateForm
    template_name = 'e-commerce/add_product.html'



class ProductList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Product

    def get(self, request,*args, **kwargs):
        products = Product.objects.all()
        context = {
            'name': 'Products',
            'items': products
        
        }
        return render(request,'e-commerce/manage_product.html',context)
  


class ProductUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Product
    template_name = 'e-commerce/update_product.html'
    form_class= ProductUpdateForm

class ProductDelete(LoginRequiredMixin,PermissionRequiredMixin,  DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Product
    template_name = 'e-commerce/delete_product.html'
    success_url = '/products'







class ProductDetails( DetailView):
    model = Product
    template_name ='e-commerce/product-detail.html'

# Update quantity of products in OrderItems
    
@login_required(login_url= "/account/login/")
def add_cart(req,slug):
   product= get_object_or_404(Product, slug=slug)
   order_item, created = OrderItem.objects.get_or_create(
        user=req.user,
        product=product,
       
        ordered=False
    )
   order_qs = Order.objects.filter( user=req.user,ordered=False)
   if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(req, "This item quantity was updated.")
            return redirect("cart"
        )
        else:
            order.products.add(order_item)
            messages.info(req, "This item was added to your cart.")
            return redirect("cart"
        )
   else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=req.user,
             ordered_date=ordered_date)
        order.products.add(order_item)
        messages.info(req, "This item was added to your cart.")
        return redirect("cart"
        )



@login_required(login_url= "/account/login/")
def remove_quantity(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_item = OrderItem.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.products.remove(order_item)
            messages.info(request, "This item quantity was updated.")
    
            return redirect("cart"
        )
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("cart"
        )
    else:
        messages.info(request, "You do not have an active order")
        return redirect("cart"
        )

@login_required(login_url= "/account/login/")
def remove_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_item = OrderItem.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            order.products.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("cart"
        )
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("cart"
        )
    else:
        messages.info(request, "You do not have an active order")
        return redirect("cart"
        )


# Checkout Views

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid




class checkout(View, LoginRequiredMixin,):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order,
       
            }
  
            return render(self.request, "e-commerce/checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("products")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():

        
                    print("User is entering a new shipping address")
                    shipping_address1 = form.cleaned_data.get(
                        'shipping_address')
                    shipping_address2 = form.cleaned_data.get(
                        'shipping_address2')
                    shipping_country = form.cleaned_data.get(
                        'shipping_country')
                    shipping_zip = form.cleaned_data.get('shipping_zip')

                    if is_valid_form([shipping_address1, shipping_country, shipping_zip]):
                        shipping_address = Address(
                            user=self.request.user,
                            street_address=shipping_address1,
                            apartment_address=shipping_address2,
                            country=shipping_country,
                            zip=shipping_zip,
                            
                        )
                        shipping_address.save()

                        order.shipping_address = shipping_address
                        order.save()

                        payment = Payment()
                     
                        payment.user = self.request.user
                        payment.amount = order.get_total()
                        payment.save()

                # assign the payment to the order

                        order_items = order.products.all()
                        order_items.update(ordered=True)
                        for item in order_items:
                              item.save()

                       
                        order.payment = payment
                        order.ordered = True
                        order.save()

                        messages.success(self.request, "Your order was successful!")
                        return redirect("payment_success")

                

                    else:
                        messages.info(
                            self.request, "Please fill in the required shipping address fields")

               

        
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("cart")



class paymentSuccessful(View, LoginRequiredMixin,):

    def get(self, *args, **kwargs):
            orders = Order.objects.latest('slug')
           
            order = Order.objects.get(user=self.request.user, slug = orders.slug)
            context = {
            'payment_status':'success',
            'order': order
            # TODO: Edit this section for the confirmation view
        
        }

  
            return render(self.request, 'e-commerce/confirmation.html', context)

 
@login_required(login_url= "/account/login/")
def paymentFailed(req):
    context = {
        'payment_status':'failed'

    }
    return render(req, 'e-commerce/confirmation.html', context)


class print_invoice(View,LoginRequiredMixin,):

    def get(self, *args, **kwargs):
            orders = Order.objects.latest('slug')
           
            order = Order.objects.get(user=self.request.user, slug = orders.slug)
            context = {
            'payment_status':'success',
            'order': order
            # TODO: Edit this section for the confirmation view
        
        }

  
            return render(self.request, 'e-commerce/invoice-print.html', context)





#home page
def attendance(req):
    context ={}
    return render(req,'madrasa/attendance/demo.html', context)











@login_required(login_url= "/account/login/")
def generate_pdf(request):
    """Generate pdf."""
    # Model data
    orders = Order.objects.latest('slug')
           
    order = Order.objects.get(user=request.user, slug = orders.slug)
        
    context = {
            'payment_status':'success',
            'order': order
    }
            # TODO: Edit this section for the confirmation view
        

    # Rendered
    html_string = render_to_string('e-commerce/pdf.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=invoice.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
       

        # https://stackoverflow.com/questions/43539702/attach-img-file-in-pdf-weasyprint

    return response


@login_required(login_url= "/account/login/")
def send_email(req):

    
         # Model data
    orders = Order.objects.latest('slug')
           
    order = Order.objects.get(user=req.user, slug = orders.slug)
        
    context = {
            'payment_status':'success',
            'order': order
    }
            # TODO: Edit this section for the confirmation view
        

    # Rendered
    html_string = render_to_string('e-commerce/pdf.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=invoice.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
        pdf = HTML(string=html_string, base_url='http://8d8093d5.ngrok.io/users/process/').write_pdf(
            stylesheets=[CSS(string='body { font-family: serif}')])
        to_emails = ['masum07@hotmail.co.uk']
        subject = "Certificate from Nami Montana"
        email = EmailMessage(subject, body=pdf, from_email=settings.EMAIL_HOST_USER, to=to_emails)
        email.attach('invoice.pdf', pdf, "application/pdf")
        email.content_subtype = "pdf"  # Main content is now text/html
        email.encoding = 'us-ascii'
        email.send()

        # https://stackoverflow.com/questions/43539702/attach-img-file-in-pdf-weasyprint

    return response




'''Attendace Management'''


# code for taking attendance
@login_required(login_url= "/account/login/")
def take_attendance(req):
    classes = Classes.objects.all
    
    context = {
        'classes': classes,
   
    }
   
    return  render(req,"management/attendance/take_attendance.html",context)


@csrf_exempt
@login_required(login_url= "/account/login/")
def get_students_register(req):
    class_id = req.POST.get('class')
    classes = Classes.objects.get(id = class_id)

    students = Students.objects.filter(which_class = classes.id)

    list_data=[]

    for student in students:
        data_small={"id":student.id,"name":student.first_name+" "+student.last_name}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

    
@csrf_exempt
@login_required(login_url= "/account/login/")
def save_attendance_data(request):
    student_ids=request.POST.get("student_ids")

    attendance_date=request.POST.get("attendance_date")
    class_id=request.POST.get("class_id")

    classes=Classes.objects.get(id=class_id)
    
    json_sstudent=json.loads(student_ids)
   


    try:
        attendance=Attendance(classes=classes ,date=attendance_date)
        attendance.save()

        for stud in json_sstudent:
             student=Students.objects.get(id=stud['id'])
             attendance_report=classAttendance(student_id=student,attendance_id=attendance,status=stud['status'])
             attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("ERR")


# View and update current attendance records

class AttendanceList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Attendance

    def get(self, request, *args, **kwargs):
        attendance = Attendance.objects.all()
        context = {
            'name': 'Attendance',
            'attendance_list': attendance
        
        }
        return render(request,'management/attendance/attendance_view_template.html',context)

class AttendanceUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Attendance
    template_name = 'management/attendance/edit_attendance_template.html'
    form_class= AttendanceUpdateForm



class AttendanceDelete(LoginRequiredMixin,PermissionRequiredMixin,  DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Attendance
    template_name = 'management/attendance/attendance_delete_form.html'
    success_url = '/manage_attendance'






# CRUD for student attendance records
class ClassAttendanceList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= classAttendance

    def get(self, request, *args, **kwargs):
        attendance = classAttendance.objects.all()
        context = {
            'name': 'Class Attendance',
            'attendance_list': attendance
        
        }
        return render(request,'management/attendance/manage_class_attendance.html',context)

class ClassAttendanceUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = classAttendance
    template_name = 'management/attendance/edit_class_attendance.html'
    form_class= ClassAttendanceUpdateForm



class ClassAttendanceDelete(LoginRequiredMixin,PermissionRequiredMixin,  DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = classAttendance
    template_name = 'management/attendance/class_attendance_delete_form.html'
    success_url = '/manage_class_attendance'

@csrf_exempt
@login_required(login_url= "/account/login/")
def get_students(req):
    class_id = req.POST.get('class')
    date = req.POST.get('date')
    # date = date.replace('\"' , '\'')


    cursor = connection.cursor()

    cursor = connection.cursor()

    cursor.execute('''SELECT madrasa_students.id, madrasa_students.first_name, madrasa_students.last_name, 
madrasa_classattendance.status  FROM madrasa_students
    INNER JOIN madrasa_classattendance on madrasa_students.id = madrasa_classattendance.student_id_id
    inner join madrasa_attendance on madrasa_classattendance.attendance_id_id = madrasa_attendance.id

    INNER JOIN madrasa_classes on madrasa_attendance.classes_id = madrasa_classes.id 


    where madrasa_attendance.classes_id = %s AND madrasa_attendance.date = %s''',[class_id, date])
    row = cursor.fetchall()
    list_data=[]
   
    for student in row:

        data_small={"id":student[0],"name":student[1] + " " + student[2], "status1": student[3]}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@login_required(login_url= "/account/login/")
def update_attendance(req):
    classes = Classes.objects.all
    attendance = Attendance.objects.all
    context = {
        'classes': classes,
        'attendance':attendance
    }
   
    return  render(req,"management/attendance/update_attendance.html",context)



@csrf_exempt
@login_required(login_url= "/account/login/")
def update_attendance_data(req):
    student_ids=req.POST.get("student_ids")
    class_id = req.POST.get("classes")

    
    
    date = req.POST.get('date')
 

    
    json_sstudent=json.loads(student_ids)
    #print(data[0]['id'])


    try:
        attendance=Attendance.objects.get(date= date, classes_id = class_id)
     
       
        
       

        for stud in json_sstudent:
             student=Students.objects.get(id=stud['id'])
             attendance_report=classAttendance.objects.get(student_id=student.id,attendance_id=attendance.id)
             attendance_report.status = stud['status']
             attendance_report.save()

        return HttpResponse("OK")
    except:
        return HttpResponse("ERR")




















''' Homework Views '''

# Student views to check their homework
@login_required(login_url= "/account/login/")
def homework(req):
    classes = Classes.objects.all
    
    context = {
        'classes': classes,
   
    }
   
    return  render(req,"management/homework/hw.html",context)


@csrf_exempt
@login_required(login_url= "/account/login/")
def get_homework(req):
    class_id = req.POST.get('class')
    date = req.POST.get('date')


    cursor = connection.cursor()
  

    cursor.execute('''Select madrasa_subject.subject, madrasa_homework.content, madrasa_audio.audio, madrasa_audio.description
     from madrasa_homework
     inner join madrasa_audio on madrasa_homework.audio_id = madrasa_audio.id
inner join madrasa_course on madrasa_homework.course_id = madrasa_course.id
inner join madrasa_classes on madrasa_course.classes_id = madrasa_classes.id
inner join madrasa_subject on madrasa_course.subject_id = madrasa_subject.id
where  madrasa_classes.id = %s 
and madrasa_homework.date = %s ''',[class_id, date])

    row = cursor.fetchall()
    list_data=[]
    
 
  
    for row in row:
        
            if row[3] == "N/A":
                data_small={"subject":row[0],"content":row[1],"audio":"Not Applicable" }

            else:
                data_small={"subject":row[0],"content":row[1],"audio":row[2] }
       
            list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)
    




# View and CRUD for Homework

class add_homework (LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required= ('madrasa.add_homework')
    model = Homework
    form_class = HomeworkCreateForm
    template_name = 'management/homework/add_homework_template.html'



class HomeworkList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required= ('madrasa.view_homework')
    model= Homework

    def get(self, request, *args, **kwargs):
        homework = Homework.objects.all()
        context = {
            'name': 'Homework',
            'homework_list': homework
        
        }
        return render(request,'management/homework/manage_homework_template.html',context)

class HomeworkUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.change_homework')
    model = Homework
    template_name = 'management/homework/edit_homework_template.html'
    form_class= HomeworkUpdateForm



class HomeworkDelete(LoginRequiredMixin,PermissionRequiredMixin,  DeleteView):
    permission_required= ('madrasa.delete_homework')
    model = Homework
    template_name = 'management/homework/homework_delete_form.html'
    success_url = '/manage_homework'









''' fees Views '''

class FeesCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Fees
    form_class = FeesCreateForm
    template_name = 'management/fees/add_fees_template.html'


class FeesList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Fees

    def get(self, request,*args, **kwargs):
        fees = Fees.objects.all()
        context = {
            'name': 'Fees',
            'fees_list': fees
        
        }
        return render(request,'management/fees/manage_fees_template.html',context)


class FeesUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Fees
    template_name = 'management/fees/edit_fees_template.html'
    form_class= FeesUpdateForm

class FeesDelete(LoginRequiredMixin,PermissionRequiredMixin,  DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Fees
    template_name = 'management/fees/fees_delete_form.html'
    success_url = '/manage_fees'



#Check fees paid and remaing amount by class and year
@login_required(login_url= "/account/login/")
def check_fees(req):
    classes = Classes.objects.all
    fees = Fees.objects.all
    
    context = {
        'classes': classes,
        'year':fees
   
    }
   
    return  render(req,"management/fees/check_fees.html",context)


@csrf_exempt
@login_required(login_url= "/account/login/")
def get_fees(req):
    class_id = req.POST.get('class')
    date = req.POST.get('year')


    cursor = connection.cursor()
    cursor = connection.cursor()

    cursor.execute('''Select madrasa_students.first_name,madrasa_students.last_name, sum(madrasa_fees.amount) from madrasa_fees
    inner join madrasa_students on madrasa_fees.student_id_id = madrasa_students.id
    inner join madrasa_classes on madrasa_students.which_class_id = madrasa_classes.id
    where  madrasa_classes.id = %s
    AND madrasa_fees.year = %s
    group by madrasa_students.first_name , madrasa_students.last_name''',[class_id, date])

    row = cursor.fetchall()
    list_data=[]
  
    for row in row:

        data_small={"first_name":row[0],"last_name":row[1],"amount": " %.2f" % row[2], "remaining": " %.2f" % (540-row[2])}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)
    





#Check fees paid and remaing amount for all students by year
@login_required(login_url= "/account/login/")
def remaining_fees(req):
    classes = Classes.objects.all
    fees = Fees.objects.all
    
    context = {
        'classes': classes,
        'year':fees
   
    }
   
    return  render(req,"management/fees/remaining.html",context)    

@csrf_exempt
@login_required(login_url= "/account/login/")
def get_fees_remaining(req):
   
    date = req.POST.get('year')
    amount = req.POST.get('amount')


    cursor = connection.cursor()
    cursor = connection.cursor()

    cursor.execute('''Select madrasa_students.first_name,madrasa_students.last_name, sum(madrasa_fees.amount) from madrasa_fees
    inner join madrasa_students on madrasa_fees.student_id_id = madrasa_students.id
    inner join madrasa_classes on madrasa_students.which_class_id = madrasa_classes.id
    where  madrasa_fees.year = %s

    group by madrasa_students.first_name , madrasa_students.last_name
    Having sum(madrasa_fees.amount) < %s
    ''',[ date, amount])

    row = cursor.fetchall()
    list_data=[]
  
    for row in row:

        data_small={"first_name":row[0],"last_name":row[1],"amount": " %.2f" % row[2], "remaining": " %.2f" % (540-row[2])}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)
    







'''Sending emails


from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

  email = EmailMessage('Hello', 'hello', settings.EMAIL_HOST_USER,['masum07@hotmail.co.uk'],)
    email.fail_silently = False
    email.send()
'''





class Generate_fees_invoice(View):
    def get(self, request,*args, **kwargs):
    
    
    # Model data
        orders = Fees.objects.get(id=self.kwargs['pk'])
            
        
            
        context = {
            
                'order': orders
        }
                # TODO: Edit this section for the confirmation view
            

        # Rendered
        html_string = render_to_string('management/fees/fees_pdf.html', context)
        html = HTML(string=html_string)
        result = html.write_pdf()

        # Creating http response
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=invoice.pdf'
        response['Content-Transfer-Encoding'] = 'binary'
        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())
        

            # https://stackoverflow.com/questions/43539702/attach-img-file-in-pdf-weasyprint

        return response



class AudioCreate(LoginRequiredMixin,PermissionRequiredMixin,  CreateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Audio
    form_class = AudioCreateForm
    template_name = 'management/audio/add_audio_template.html'


class AudioList(LoginRequiredMixin,PermissionRequiredMixin,  ListView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model= Audio
    def get(self, request,*args, **kwargs):
        classes = Audio.objects.all()
        context = {
            'name': 'Audio',
            'classes_list': classes
        
        }
        return render(request,'management/audio/manage_audio_template.html',context)

class AudioUpdate(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Audio
    template_name = 'management/audio/edit_audio_template.html'
    form_class= AudioUpdateForm

class AudioDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required= ('madrasa.add_student', 'madrasa.change_student', 'madrasa_delete_student', 'madrasa.view_student')
    model = Classes
    template_name = 'management/audio/audio_delete_form.html'
    success_url = '/manage_audio'




from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt



'''
Code taken from a Youtube tutorial
Ivy, D., 2022. GitHub - divanov11/mychat:
A video group video calling application using a Django backend with the Agora Web SDK. [online] GitHub. 
Available at: <https://github.com/divanov11/mychat> [Accessed 21 March 2022].
https://www.youtube.com/watch?v=Oxnz8Us1QAQ
'''

def lobby(request):
    return render(request, 'video/lobby.html')

def room(request):
    return render(request, 'video/room.html')

import os
def getToken(request):
    appId = os.environ.get("APP_ID")
    appCertificate = os.environ.get("APP_CERT")
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)

'''
The above code was taken from a Youtube tutorial
Ivy, D., 2022. GitHub - divanov11/mychat:
A video group video calling application using a Django backend with the Agora Web SDK. [online] GitHub. 
Available at: <https://github.com/divanov11/mychat> [Accessed 21 March 2022].
https://www.youtube.com/watch?v=Oxnz8Us1QAQ
'''




def admin_home(request):
    return render(request,"management/management_template/home_content.html")



def message(req):

    return render(req,'madrasa/home-page/message.html' )

def student_email(req):
    if req.method == 'POST':
        message = req.POST['message']
        email_ad = req.POST['email_ad']
        subject = req.POST['name1']
        to_emails = ['weekendmadrasa@madinamasjiddocklands.org.uk']
        email = EmailMessage('Name: ' +subject + '  From: '+ email_ad , body='From: '+ email_ad + '\n \n' + message, from_email=settings.EMAIL_HOST_USER, to=to_emails)
    
        email.encoding = 'us-ascii'
        email.send()
        messages.info(req, "Thank you for your message, We aim to respond promptly.")
        return redirect('message')
    else:
        messages.info(req, "Error sending message.")
        return redirect('message')

      

    

def contact_us(req):
    return render(req, 'e-commerce/contact.html')


def customer_email(req):
    if req.method == 'POST':
        message = req.POST['message']
        email_ad = req.POST['email_ad']
        subject = req.POST['name1']
        to_emails = ['weekendmadrasa@madinamasjiddocklands.org.uk']
        email = EmailMessage('Name: ' +subject + '  From: '+ email_ad , body='From: '+ email_ad + '\n \n' + message, from_email=settings.EMAIL_HOST_USER, to=to_emails)
    
        email.encoding = 'us-ascii'
        email.send()
        messages.info(req, "Thank you for your message, We aim to respond promptly.")
        return redirect('contact_us')
    else:
        messages.info(req, "Error sending message.")
        return redirect('contact_us')

      