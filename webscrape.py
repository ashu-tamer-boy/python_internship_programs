import csv
from requests_html import HTMLSession
s =HTMLSession()

fields = ['Location', 'temperatur', 'Humidity']  
    
# data rows of csv file  
rows = [ ]  
    
# name of csv file  
filename = "temp.csv"
    





final = []
l = []
st = input('enter the cities to find the temperature else enter\n')
while len(st) != 0:
    st = input('enter the cities to find the temperature else enter\n')
    l.append(st)
    
query =''
for q in l:
    url =f'https://www.google.com/search?q=temperature+{q}'

    r = s.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})

    final =[]
    temp = r.html.find('span#wob_tm',first=True).text
    final.append(q)
    #symbol = r.html.find('div.vk_bk span.wob_t',first=True).text
    humid = r.html.find('div.wtsRwe span#wob_hm',first=True).text
    final.append(temp)
    final.append(humid)
    rows.append(final)
    

# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows)

    

