import requests
BASE_URL='http://127.0.0.1:8000/'
#ENDPOINT='apijson'
ENDPOINT='apijsoncbv/'
resp=requests.get(BASE_URL+ENDPOINT)
#resp=requests.post(BASE_URL+ENDPOINT)
# for post method we mske a comment in settings.py file csrftoken
resp=requests.put(BASE_URL+ENDPOINT)
#resp=requests.delete(BASE_URL+ENDPOINT)
#print(resp.json())
data=resp.json()
#print('Django Application access by api')
#print('*'*40)
#print('Employee Number ::',data['eno'])
#print('Employee Name ::', data['ename'])
#print('Employee Salary ::',data['esal'])
#print('Employee Address ::',data['eaddr'])
#print('*'*40)
print(data)
