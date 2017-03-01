import urllib.request
import json
usergent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
url="https://oapi.dingtalk.com/robot/send?access_token="
headers={"User-Agent":usergent,
         "Content-Type":"application/json"}

postdata = {
            "msgtype": "link", 
            "link": {
                "text": "下午四点，该点餐了",
                "title": "下午四点，该点餐了", 
                "picUrl": "http://www.uufan.com/Public/home/images/logo.png",
                "messageUrl": "http://www.uufan.com/hetjj/"
            }
}

json_data = json.dumps(postdata).encode('utf8')

# url=url+"?"+data
request=urllib.request.Request(url,json_data,headers)

try:
    response = urllib.request.urlopen(request,timeout=2)
except urllib.error.URLError as error:
    print('Reason is ',error.reason)
except urllib.error.HTTPError as error:
    print('Data of  not retrieved because %s\n',  error)
    print('Code is ',error.code)
    
# except :
#     print ("Unexpected error:", sys.exc_info()[0])
else:
    data = response.read()
    print('Status:', response.status, response.reason, response.getcode())
    for k, v in response.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# if __name__ == '__main__':
    
