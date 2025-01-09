from requests import request

"""This function calls the server using http"""

def call_server(url:str):
   """This function calls the server using http/https
   params:
     url: string 
   
   Returns:
    a response
   """
   return request("GET","https://www.google.com")

# print(response.url)
# print(response.headers)