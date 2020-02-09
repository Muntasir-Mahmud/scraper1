import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://azure.microsoft.com/en-us/updates/?fbclid=IwAR1QQq1lEofwzyZ5N8EPWUN8vBFackGSKHqHqDrL99TzCySiLEuvYhM_l9w')

soup = BeautifulSoup(page.content,'html.parser')

updates =soup.find_all(class_='row update-row row-size6')


headlines= [item.find(class_='text-body2').get_text() for item in updates]

#print(headlines)

all_headlines = pd.DataFrame(

    {

        'headline':headlines,

    }
)
#print(all_headlines)
all_headlines.to_csv('headline.csv')
