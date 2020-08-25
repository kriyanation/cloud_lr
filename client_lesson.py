import requests


from base64 import b64encode
from json import dumps

url = "http://learning-room-285708.el.r.appspot.com/lesson/?username=1&lesson_id=8&class_id=24"
title_image = "zero.png"
title_image1 = "spacebackground.jpg"
with open(title_image, 'rb') as open_file:
    byte_content = open_file.read()
base64_bytes = b64encode(byte_content)
base64_string = base64_bytes.decode("utf-8")

with open(title_image1, 'rb') as open_file:
    byte_content1= open_file.read()
base64_bytes1 = b64encode(byte_content1)
base64_string1 = base64_bytes1.decode("utf-8")
#print(base64_string)
#http://learning-room-285708.el.r.appspot.com/auth/users/1/
data = '''{
    "lesson_id": 12,
    "class_id": 22,
    "user": "http://learning-room-285708.el.r.appspot.com/auth/users/1/",
    "title": "",
    "title_image": "'''+base64_string+'''",
    "title_video": null,
    "title_description": "",
    "term1": "",
    "term1_description": "",
    "term1_image": "'''+base64_string+'''",
    "term2": "",
    "term2_description": "",
    "term2_image": "'''+base64_string+'''",
    "term3": "",
    "term3_description": "",
    "term3_image": "'''+base64_string+'''",
    "number_of_steps": null,
    "step1_description": "",
    "step1_image": "'''+base64_string+'''",
    "step2_description": "",
    "step2_image": "'''+base64_string+'''",
    "step3_description": "",
    "step3_image": "'''+base64_string+'''",
    "step4_description": "",
    "step4_image": "'''+base64_string+'''",
    "step5_description": "",
    "step5_image": "'''+base64_string+'''",
    "step6_description": "",
    "step6_image": "'''+base64_string+'''",
    "step7_description": "",
    "step7_image": "'''+base64_string+'''",
    "step8_description": "",
    "step8_image": "'''+base64_string+'''",
    "questions": "woooo-hooo"
}'''

#json_data = dumps(data)
headers = {'Content-Type': 'application/json'}
#response = requests.get(url)
#print (response.status_code)
#print(response.json())
#curl -X POST http://127.0.0.1:8000/auth/token/login/ --data 'username=djoser4&password=alpine12'
#curl -X POST http://learning-room-285708.el.r.appspot.com/auth/token/login/ --data 'username=djoser4&password=alpine12'

headers1 = {'Content-Type': 'application/json','Authorization':'Token 78b5275ff6af2b3b62d7e46c93da90e2072e4118' }#9754c1aab05cb0538acb59dd67dc37b1af62e3f2'
url_put = "http://learning-room-285708.el.r.appspot.com/lesson/?username=1&lesson_id=11&class_id=24" #http://127.0.0.1:8000/lesson/?username=9&lesson_id=9&class_id=24"

#url_put = "http://learning-room-285708.el.r.appspot.com/lesson/5/?username=1&lesson_id=11&class_id=24" #http://127.0.0.1:8000/lesson/?username=9&lesson_id=9&class_id=24"
print(url_put)
response = requests.post(url_put,headers=headers1,data=data)
print(response.status_code)
print(response.text)
