import requests
import pytz
from datetime import timedelta
from datetime import datetime
from datetime import time
from datetime import date
from django.db import models
from twilio.rest import Client

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    student_id = models.CharField(max_length = 10)
    status = models.BooleanField(default = True)
    slug = models.SlugField(max_length = 200, null = True)

    class Meta:
        verbose_name_plural = 'STUDENTS'

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


class Lecturer(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    lecturer_id = models.CharField(max_length = 10)
    status = models.BooleanField(default = True)
    slug = models.SlugField(max_length = 200, null = True)

    class Meta:
        verbose_name_plural = 'LECTURERS'

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


class Category(models.Model):
    name = models.CharField(max_length = 40)
    status = models.BooleanField(default = True)
    slug = models.SlugField(max_length = 40, null = True)

    class Meta:
        verbose_name_plural = 'CATEGORIES'

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length = 40)
    status = models.BooleanField(default = True)
    slug = models.SlugField(null = True)

    class Meta:
        verbose_name_plural = 'ROOM'

    def __str__(self):
        return self.name


class Subject(models.Model):
    sub_code = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    sub_unit = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)
    room = models.ForeignKey(Room, on_delete = models.CASCADE, null = True)
    status = models.BooleanField(default = True)
    slug = models.SlugField(max_length = 200, null = True)

    class Meta:
        verbose_name_plural = 'SUBJECTS'

    def __str__(self):
        return 'Tên học phần: %s' % (self.name, )


class TimeTable(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    # datetime = models.DateTimeField(null = True)
    start_time = models.TimeField(null = True)
    total_period = models.IntegerField(null = True)
    status = models.BooleanField(default = True)
    slug = models.SlugField(max_length = 200, null = True)

    class Meta:
        verbose_name_plural = 'TIME TABLE'

    def __str__(self):
        return self.slug

    @classmethod
    def get_today(self):
        today = datetime.today()
        Day = today.day
        Month = today.month
        Year = today.year

        return today


    @classmethod
    def is_date(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        wd = date.weekday(self.get_today())
        print('DAY: %s', days[wd])
        return days[wd]


    @classmethod
    def is_time(self):
        today = datetime.now()
        hour = today.hour
        minute = today.minute
        second = today.second

        return {
            "hour": hour,
            "minute": minute,
            "second": second,
        }


    @classmethod
    def has_subject(self):
        while True:
            current_day = self.is_date()
            print('========== HÔM NAY LÀ: %s ==========', current_day)
            print(datetime.now())
            if current_day == 'Monday':
                start_time = time(8, 50, 00)
                # start_ring = start_time - timedelta(
                #     days = 0, hours = 0, minutes = 45, weeks = 0)
                start_period = '3'
                sub_category = 'Lý thuyết'
                room = '1. A201'
                total_period = '3'
                subject = ['Đường lối cách mạng của ĐCS Việt Nam', ]
                # if self.is_time() == 
                textMessage = self.textMessage(
                    current_day, sub_category, room, start_period, str(start_time), total_period, suject)
            
            elif current_day == 'Tuesday':
                start_time = time(15, 50, 00)
                # start_ring = start_time - timedelta(
                #     days = 0, hours = 0, minutes = 45, weeks = 0)
                room = 'C. A306'
                sub_category = 'Lý thuyết'
                start_period = '9'
                total_period = '2'
                subject = ['Thiết kế giao diện', ]
                textMessage = self.textMessage(
                    current_day, sub_category, room, start_period, str(start_time), total_period, suject)

            elif current_day == 'Wednesday':
                start_time = time(9, 50, 00)
                # start_ring = start_time - timedelta(
                #     days = 0, hours = 0, minutes = 45, weeks = 0)
                room = 'C. E402'
                sub_category = 'Thực hành'
                start_period = '4'
                total_period = '2'
                subject = ['Thiết kế giao diện', ]
                textMessage = self.textMessage(
                    current_day, sub_category, room, start_period, str(start_time), total_period, suject)

            elif current_day == 'Thursday':
                start_time = time(13, 00, 00)
                # start_ring = start_time - timedelta(
                #     days = 0, hours = 0, minutes = 45, weeks = 0)
                room = 'C. E402'
                sub_category = 'Thực hành'
                start_period = '6'
                total_period = '2'
                subject = ['Công nghệ phần mềm', ]
                textMessage = self.textMessage(
                    current_day, sub_category, room, start_period, str(start_time), total_period, suject)

                start_time_next = time(17, 40, 00)
                start_ring_next = start_time - timedelta(
                    days = 0, hours = 0, minutes = 45, weeks = 0)
                room_next = 'C. C103'
                sub_category_next = 'Lý thuyết'
                start_period_next = '11'
                total_period_next = '3'
                textMessage += self.textMessage(
                    current_day,
                    sub_category_next, 
                    room_next, 
                    start_period_next, 
                    str(start_time_next), 
                    total_period_next, 
                    suject,
                )

            elif current_day == 'Friday':
                print("Thời gian hiện tại là: ", self.is_time())
                now = self.is_time()
                print("Giờ hiện tại: ", now['hour'])
                # if now['hour'] == 12
                start_time = time(13, 00, 00)
                # start_ring = start_time - timedelta(
                #     days = 0, hours = 0, minutes = 45, weeks = 0)
                room = 'C. A503'
                sub_category = 'Lý thuyết'
                start_period = '6'
                total_period = '3'
                subject = ['Cơ sở trí tuệ nhân tạo', ]
                textMessage = self.textMessage(
                    current_day, sub_category, room, start_period, str(start_time), total_period, subject)

                start_time_next = time(15, 50, 00)
                # start_ring_next = start_time - timedelta(
                #     days = 0, hours = 0, minutes = 45, weeks = 0)
                room_next = 'C. A102'
                sub_category_next = 'Thực hành'
                start_period_next = '9'
                total_period_next = '2'
                textMessage += self.textMessage(
                    current_day,
                    sub_category_next, 
                    room_next, 
                    start_period_next, 
                    str(start_time_next), 
                    total_period_next, 
                    subject,
                )

            elif current_day == 'Saturday':
                start_time = time(7, 00, 00)
                # start_ring = start_time - timedelta(
                #     days = 0, hours = 0, minutes = 45, weeks = 0)
                room = 'C. B105'
                sub_category = 'Lý thuyết'
                start_period = '1'
                total_period = '3'
                subject = ['Phân tích thiết kế hướng đối tượng', ]
                textMessage = self.textMessage(
                    current_day, sub_category, room, start_period, str(start_time), total_period, subject)

                start_time_next = time(9, 50, 00)
                # start_ring_next = start_time - timedelta(
                #     days = 0, hours = 0, minutes = 45, weeks = 0)
                room_next = 'C. E402'
                sub_category_next = 'Thực hành'
                start_period_next = '4'
                total_period_next = '2'
                textMessage += self.textMessage(
                    current_day,
                    sub_category_next, 
                    room_next, 
                    start_period_next, 
                    str(start_time_next), 
                    total_period_next, 
                    subject,
                )

            else:
                textMessage = "Tin nhắn rỗng"
                print("Thời gian hiện tại là: ", self.is_time())
                # textMessage = """
                #     \nTHÔNG BÁO: Hôm nay là cuối tuần bạn không có lịch học
                #     hãy ngồi dậy tập thể dục vận động cơ thể đi nào!
                #     \nChúc bạn có một ngày cuối tuần vui vẻ!
                #     \n"Jira - Trợ lí ảo (bot) được tạo bởi Bacdongg"
                # """

            self.send_message_to_telegram(textMessage)
            self.send_message_to_facebook(textMessage)
            self.send_sms(textMessage)


    @classmethod
    def textMessage(self, current_day, sub_category, room, start_period, start_time, total_period, *args):
        message = "\n==============================\n"
        message = "\nTHÔNG BÁO:"
        message += "\nHôm nay là %s \nBạn có lịch học như sau:" % (current_day, )
        message += "\n> LỊCH HỌC <"

        for item in args:
            message += "\n\t -> Tên môn học: %s" % (item, )
            message += "\n\t -> Loại tiết học: %s" % (sub_category, )
            message += "\n\t -> Tại phòng: %s" % (room, )
            message += "\n\t -> Tiết bắt đầu: %s" % (start_period, )
            message += "\n\t -> Thời gian bắt đầu: %s" % (str(start_time), )
            message += "\n\t -> Số tiết học: %s" % (total_period, )

        message += "\n\nChúc bạn có một buổi học thật tốt!\n\n"

        return message


    @classmethod
    def send_message_to_telegram(self, textMessage):
        TOKEN = '1146893191:AAGc6MKgH-xNWSEPEpEPwAu5KKE3tzbDXmU'
        METHOD = 'sendMessage'
        CHAT_ID = '1275541186'
        TEXT = textMessage
        API_URL = 'https://api.telegram.org/bot%s/%s?chat_id=%s&text=%s' % (TOKEN, METHOD, CHAT_ID, TEXT)

        result = requests.get(API_URL)
        print('==========\n %s \n==========', result)


    @classmethod
    def send_message_to_facebook(self, textMessage):
        pass


    @classmethod
    def send_sms(self, textMessage):
        # ACCOUNT_ID = 'AC99537dc3c5c38549b4c10e3478f5645e'
        # AUTH_TOKEN = '79adffea594024825f819792146f6f18'

        # client = Client(ACCOUNT_ID, AUTH_TOKEN)

        # to_area_code = '+84'
        # to_number = '915272291'

        # from_area_code = '+1'
        # from_number = '7739007277'

        # TO = to_area_code + to_number
        # FROM = from_area_code + from_number
        # BODY = textMessage

        # client.messages.create(to=TO, from_=FROM, body=BODY)
        pass


TimeTable.has_subject()