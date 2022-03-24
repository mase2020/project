"""maktab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from madrasa import views
from django.conf.urls.static import static
from tuition_project import settings

urlpatterns = [
    
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    path('madrasa', views.index, name = 'home1'),
    path("account/", include("django.contrib.auth.urls"), name="login"),
    path('admins', views.admin, name = 'admin'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout", views.logout_view, name="logout"),
    #admin dashboard
    path('attendance', views.attendance, name="attendance"),
    path('admin_home',views.admin_home,name="admin_home"),
    #Application forms
    path('application_form', views.Application.as_view(),name="application_form"),
    path('manage_applications', views.ApplicationList.as_view(),name='manage_applications'),
    path('save_student/<pk>', views.save_student, name = 'save_student'),
    path('delete_application/<pk>', views.ApplicationDelete.as_view(), name= 'delete_application'), 
    #Class routes
    path('add_class', views.ClassesCreate.as_view(),name="add_class"),
    path('manage_class', views.ClassesList.as_view(),name="manage_class"),
    path('edit_class/<pk>', views.ClassUpdate.as_view(), name="edit_class"),
    path('classes/delete/<pk>', views.ClassDelete.as_view(), name="classdelete"),
    #Student routes
    path('add_student', views.StudentsCreate.as_view(),name="add_student"),
    path('manage_student',views.StudentList.as_view(),name="manage_student"),
    path('edit_student/<pk>', views.StudentUpdate.as_view(),name="edit_student"),
    path('students/delete/<pk>', views.StudentDelete.as_view(), name="studentdelete"),
    #Subject routes
    path('add_subject', views.SubjectCreate.as_view(),name="add_subject"),
    path('manage_subject', views.SubjectList.as_view(),name="manage_subject"),
    path('edit_subject/<pk>', views.SubjectUpdate.as_view(),name="edit_subject"),
    path('subject/delete/<pk>', views.SubjectDelete.as_view(), name="subjectdelete"),
    #Course routes
    path('add_course', views.CourseCreate.as_view(),name="add_course"),
    path('manage_course', views.CourseList.as_view(),name="manage_course"),
    path('edit_course/<pk>', views.CourseUpdate.as_view(), name="edit_course"),
    path('course/delete/<pk>', views.CourseDelete.as_view(), name="coursedelete"),
    #Staff routes  
    path('add_staff', views.TeachersCreate.as_view(), name='add_staff'),
    path('manage_staff', views.TeacherList.as_view(), name="manage_staff"),
    path('edit_staff/<pk>', views.TeacherUpdate.as_view(), name="edit_staff"),
    path('staff/delete/<pk>', views.TeacherDelete.as_view(), name="staffdelete"),
    #Attendance routes
    path('manage_attendance', views.AttendanceList.as_view(),name="manage_attendance"),
    path('edit_attendance/<pk>', views.AttendanceUpdate.as_view(), name="edit_attendance"),
    path('attendance/delete/<pk>', views.AttendanceDelete.as_view(), name="attendancedelete"),
    path('manage_class_attendance', views.ClassAttendanceList.as_view(),name="manage_class_attendance"),
    path('edit_class_attendance/<pk>', views.ClassAttendanceUpdate.as_view(), name="edit_class_attendance"),
    path('class_attendance/delete/<pk>', views.ClassAttendanceDelete.as_view(), name="classattendancedelete"),
    # Take attendance
    path('take_attendance', views.take_attendance, name="take_attendance"),
    path('get_students_register', views.get_students_register, name="get_students_register"),
    path('save_attendance_data', views.save_attendance_data, name="save_attendance_data"),
    # Update attendance
    path('update_attendance', views.update_attendance, name="update_attendance"),
    path('get_students', views.get_students, name="get_students"),
    path('update_attendance_data', views.update_attendance_data, name="update_attendance_data"), 
    # Homework routes
    path('get_homework', views.get_homework, name= 'get_homework'),
    path('homework', views.homework, name= 'homework'),
    path('add_homework', views.add_homework.as_view(), name='add_homework'),
    path('manage_homework', views.HomeworkList.as_view(), name="manage_homework"),
    path('edit_homework/<pk>', views.HomeworkUpdate.as_view(), name="edit_homework"),
    path('delete_homework/<pk>', views.HomeworkDelete.as_view(), name="homeworkdelete"),
    # Audio routes
    path('add_audio', views.AudioCreate.as_view(),name="add_audio"),
    path('manage_audio', views.AudioList.as_view(),name="manage_audio"),
    path('edit_audio/<pk>', views.AudioUpdate.as_view(), name="edit_audio"),
    path('audio/delete/<pk>', views.AudioDelete.as_view(), name="audiodelete"),
    # Fees Routes
    path('add_fees', views.FeesCreate.as_view(), name='add_fees'),
    path('manage_fees', views.FeesList.as_view(), name="manage_fees"),
    path('edit_fees/<pk>', views.FeesUpdate.as_view(), name="edit_fees"),
    path('generate_invoice/<pk>',views.Generate_fees_invoice.as_view(), name = 'generate_invoice'),
    path('delete_fees/<pk>', views.FeesDelete.as_view(), name="feesdelete"),
    path('check_fees', views.check_fees, name="check_fees"),
    path('get_fees', views.get_fees, name="get_fees"),
    path('remaining_fees',views.remaining_fees, name="remaining_fees"),
    path('get_fees_remaining', views.get_fees_remaining, name="get_fees_remaining"),

    # E-Commerce routes

    
    # Product routes
    path('add_product', views.ProductCreate.as_view(), name='add_product'),
    path('manage_products', views.ProductList.as_view(), name="manage_products"),
    path('edit_product/<pk>', views.ProductUpdate.as_view(), name="edit_product"),
    path('delete_product/<pk>', views.ProductDelete.as_view(), name="delete_product"),
    # Customer catalogue view page
    path('products', views.Products.as_view(), name='products'),
    # Product detail routes, checkout routes
    path('product_detail/<slug>', views.ProductDetails.as_view(), name='product_detail'),
    path('cart', views.cart.as_view(), name='cart'),
    path('add_cart/<slug>', views.add_cart, name='add_cart'),
    path('remove_cart/<slug>', views.remove_cart, name='remove_cart'),
    path('remove_quantity/<slug>', views.remove_quantity, name='remove_quantity'),
    path('checkout', views.checkout.as_view(), name="checkout"),
    path('payments', views.Payment, name="payments"),
    path('confirmation', views.paymentSuccessful.as_view(), name= 'payment_success'),
    path('failed', views.paymentFailed, name= 'payment_failed'),
    path('print_invoice', views.print_invoice.as_view(), name= 'print_invoice'),
    path('generate_pdf', views.generate_pdf, name= 'generate_pdf'),
    path('send_email', views.send_email, name= 'send_email'),
    # path('payment_complete', views.payment_complete, name='payment_complete'),

# Code taken from a Youtube tutorial
# Ivy, D., 2022. GitHub - divanov11/mychat:
# A video group video calling application using a Django backend with the Agora Web SDK. [online] GitHub. 
# Available at: <https://github.com/divanov11/mychat> [Accessed 21 March 2022].
# https://www.youtube.com/watch?v=Oxnz8Us1QAQ

   path('lobby/', views.lobby, name= 'lobby'),
    path('room/', views.room),
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),



    path('send_email_customer',views.customer_email, name= 'send_email_customer'),
    path('send_email_student',views.student_email, name= 'send_email_student'),
    path('message', views.message, name='message'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('send_application_email',views.application_email, name= 'send_application_email'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

