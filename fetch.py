import requests

# Send a GET request to the API endpoint
# response = requests.get('https://643fb836b9e6d064befc8b51.mockapi.io/mahabbatsapi/tasks0205')
# data = []
# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Extract the data from the response
#     data = response.json()

#     # Process the data as needed
#     for item in data:
#         print(item)  # Example: print each item in the response data
# else:
#     print('Error:', response.status_code)
# # data= {'name': 'Orxan123', 'image': 'https://loremflickr.com/640/480', 'id': '32'}


data= {'name': 'Anora'}

# response = requests.post("https://643fb836b9e6d064befc8b51.mockapi.io/mahabbatsapi/tasks0205", data=data)
requests.patch("https://643fb836b9e6d064befc8b51.mockapi.io/mahabbatsapi/tasks0205/33",data=data)
