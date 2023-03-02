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
            if cookie.expires is not None:
                cookie_expiration_time = datetime.datetime.fromtimestamp(cookie.expires) 
            if cookie_expiration_time:
                print("Cookie expiration time:", cookie_expiration_time)
            else:
                print("No cookies with expiration time found")
    else:
        print("This page does not use cookies")


    



   