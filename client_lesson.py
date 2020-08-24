import requests


from base64 import b64encode
from json import dumps

url = "http://learning-room-285708.el.r.appspot.com/lesson/?username=1&lesson_id=8&class_id=24"
title_image = "zero.png"
with open(title_image, 'rb') as open_file:
    byte_content = open_file.read()
base64_bytes = b64encode(byte_content)
base64_string = base64_bytes.decode("utf-8")
#print(base64_string)
#http://learning-room-285708.el.r.appspot.com/auth/users/1/
data = '''{
    "lesson_id": 11,
    "class_id": 24,
    "user": "http://learning-room-285708.el.r.appspot.com/auth/users/1/",
    "title": "",
    "title_image": "'''+base64_string+'''",
    "title_video": null,
    "title_description": "",
    "term1": "",
    "term1_description": "",
    "term1_image": "",
    "term2": "",
    "term2_description": "",
    "term2_image": "",
    "term3": "",
    "term3_description": "",
    "term3_image": "",
    "number_of_steps": null,
    "step1_description": "",
    "step1_image": "",
    "step2_description": "",
    "step2_image": "",
    "step3_description": "",
    "step3_image": "",
    "step4_description": "",
    "step4_image": "",
    "step5_description": "",
    "step5_image": "",
    "step6_description": "",
    "step6_image": "",
    "step7_description": "",
    "step7_image": "",
    "step8_description": "",
    "step8_image": "",
    "questions": "woooo-hooo"
}'''

#json_data = dumps(data)
headers = {'Content-Type': 'application/json'}
#response = requests.get(url)
#print (response.status_code)
#print(response.json())
#curl -X POST http://127.0.0.1:8000/auth/token/login/ --data 'username=djoser4&password=alpine12'

headers1 = {'Content-Type': 'application/json','Authorization':'Token 78b5275ff6af2b3b62d7e46c93da90e2072e4118'}
url_put = "http://learning-room-285708.el.r.appspot.com/lesson/?username=1&lesson_id=11&class_id=24" #http://127.0.0.1:8000/lesson/?username=9&lesson_id=9&class_id=24"

#url_put = "http://learning-room-285708.el.r.appspot.com/lesson/5/?username=1&lesson_id=11&class_id=24" #http://127.0.0.1:8000/lesson/?username=9&lesson_id=9&class_id=24"
print(url_put)
response = requests.post(url_put,headers=headers1,data=data)
print(response.status_code)
print(response.text)
