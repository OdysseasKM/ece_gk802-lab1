import requests
import datetime

url = input("please give the url: ")

with requests.get(url) as response:  
    print("response headers: ", response.headers)
    server_info = response.headers["Server"]
    print("Software: ", server_info)

    if response.cookies:
        print("This page uses cookies")
        for cookie in response.cookies:
            print("name of cookie: ", cookie.name)
            if cookie.expires :
                cookie_expiration_time = datetime.datetime.fromtimestamp(cookie.expires) - datetime.datetime.now()
                print("Cookie will be valid for :", cookie_expiration_time)
            else:
                print("No  expiration time found")
    else:
        print("This page does not use cookies")


    



   