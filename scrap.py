from bs4 import BeautifulSoup
import requests
import csv
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

try:
    src = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    src.raise_for_status()
    soup = BeautifulSoup(src.text, 'html.parser')
    
    #movies=soup.find_all('ul',class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 dHaCOW compact-list-view ipc-metadata-list--base')
    movies = soup.find_all('li',class_="ipc-metadata-list-summary-item sc-10233bc-0 TwzGn cli-parent")
    print(len(movies))
    csv_file ='movies_data.csv'
    with open(csv_file,mode='w',newline='',encoding='utf-8=sig') as file:
        writer=csv.writer(file)
        headers =['Rank','name','year','Rating']
        writer.writerow(headers)
        for m in movies:
            name= m.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 bnSrml cli-title").a.text.split('.')[1]
            rank= m.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 bnSrml cli-title").a.text.split('.')[0]
            year = m.find('span',class_="sc-b189961a-8 hCbzGp cli-title-metadata-item").text
            rating= m.find('span',class_='ipc-rating-star--rating').text
            writer.writerow([rank,name,year,rating])
    print(f"data has been written on the csv file: {csv_file}")    
except Exception as e:
    print(e)
    
    
