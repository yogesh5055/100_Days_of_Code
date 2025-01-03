import requests
from datetime import datetime

token = "your token"
user_name = "your name"
graph = "your graph id"
pixela_endpoint = "https://pixe.la/v1/users"


user_parameter ={
    "token":token,
    "username":user_name,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

#POST
#requests.post(url=pixela_endpoint,json=user_parameter)


graph_endpoint = f"https://pixe.la/v1/users/{user_name}/graphs"

graph_config = {
    "id":graph,
    "name":"Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color": "ajisai",

}
#requests.post(url=graph_endpoint,json=graph_config)

header = {
    "X-USER-TOKEN":token
}



pixela_creation_point = f"{pixela_endpoint}/{user_name}/graphs/{graph}"
today = datetime.now()

pixel_data = {

    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many kilometers did you cycle today?"),
}

response = requests.post(url=pixela_creation_point,json=pixel_data,headers=header)
print(response.text)


update_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "4.5"
}