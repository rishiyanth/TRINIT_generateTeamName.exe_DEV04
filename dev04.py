from turtle import heading
import requests
import bs4

email = input("Enter the email : ")

index3 = email.index('@')

name = email[:index3]
name = ''.join([i for i in name if not i.isdigit()])

text = name + " linkedin"
url = 'https://google.com/search?q=' + text

# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result = requests.get(url)

# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text,
                         "html.parser")
# print(soup)

heading_object = soup.find_all('a')

for info in heading_object:

    if("https://in.linkedin.com" in info.get('href')):

        indx = info.get('href').index('sa=')
        temp = info.get('href')[7:indx-1]
        # print(temp)

        indx1 = temp.index('in/')
        print("https://www.linkedin.com/in/" + temp[indx1+3:])
        print("------")