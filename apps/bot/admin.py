from django.contrib import admin
from .models import Student
from .models import Lecturer
from .models import Category
from .models import Room
from .models import Subject
from .models import TimeTable

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'first_name', 'last_name', 'status', 'slug')
    list_filter = ('student_id', 'first_name', 'last_name', 'status', 'slug')
    search_fields = ('student_id', 'first_name', 'last_name', 'slug')


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'lecturer_id', 'first_name', 'last_name', 'status', 'slug')
    list_filter = ('lecturer_id', 'first_name', 'last_name', 'status', 'slug')
    search_fields = ('lecturer_id', 'first_name', 'last_name', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'slug')
    list_filter = ('name', 'status', 'slug')
    search_fields = ('name', 'status', 'slug')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'slug')
    list_filter = ('name', 'status', 'slug')
    search_fields = ('name', 'status', 'slug')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_code', 'name', 'category', 'sub_unit', 'status', 'slug')
    list_filter = ('sub_code', 'name', 'sub_unit', 'status', 'slug')
    search_fields = ('sub_code', 'name', 'status', 'slug')


class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'lecturer_id', 'subject_id', 'status', 'slug')
    list_filter = ('student_id', 'lecturer_id', 'subject_id', 'status', 'slug')
    search_fields = ('student_id', 'lecturer_id', 'subject_id', 'status', 'slug')



admin.site.register(Student, StudentAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(TimeTable, TimeTableAdmin)