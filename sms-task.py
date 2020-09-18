from twilio.rest import Client


# Initial account to send SMS
ACCOUNT_ID = 'AC99537dc3c5c38549b4c10e3478f5645e'
AUTH_TOKEN = '79adffea594024825f819792146f6f18'


client = Client(ACCOUNT_ID, AUTH_TOKEN)

to_area_code = '+84'
to_number = '836144911' #Exclude 0, Eg. 0968094416 -> 968094416

from_area_code = '+1'
from_number = '7739007277' #Exclude 0, Eg. 07739007277 -> 7739007277

TO = to_area_code + to_number
FROM = from_area_code + from_number
BODY = """
    \nThông báo: 
    \nTôi nhắn để nhắc nhở bạn về lịch học của bạn hôm nay bao gồm:
    \n + Môn 1 - lúc 07:15 AM
    \n + Môn 2 - lúc 15:00 PM
    \n + Môn 3 - lúc 22:05 PM
    \nĐây là SMS test tính năng send SMS.
    I'm Bacdongg.
"""

client.messages.create(to=TO, from_=FROM, body=BODY)