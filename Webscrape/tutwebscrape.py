from bs4 import BeautifulSoup
import requests

website = 'https://thsconline.github.io/s/v/2670/2005%20HSC'
result = requests.get(website)


content = result.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

"""
this is the getting the HMTL

1.ID
2.CLASS NAME
3.TAG nAME,css select
4.Xpath


"""
#order to find is that we need to 

box = soup.find('div', class_='textLayer')
#reference



questions = box.find('span').get_text(strip=True, separator=' ')
print(questions)


with open(f'{questions}.txt', 'w') as file:     
          
#title + txt
    file.write(questions)
#txt files




# apparent but cannot acess document (https://script.google.com/macros/s/AKfycbx69GPoJtf9sSevsUbWtPr46vpa01u4oNkHjFmkkWxmj62AZ0q-/exec?&export=view&field=2003%20HSC&base=2670)