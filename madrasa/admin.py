from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Students,Classes,Teachers,Product, Order,OrderItem,  Payment,  Address, Attendance,classAttendance
from .models import Subject, Course,Homework, Audio, Registration,RoomMember,Fees

admin.site.register(Students)
admin.site.register(Classes)
admin.site.register(Teachers)
admin.site.register(Attendance)
admin.site.register(classAttendance)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Homework)
admin.site.register(Audio)
admin.site.register(Registration)
admin.site.register(Fees)

admin.site.register(RoomMember)

admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Address)






