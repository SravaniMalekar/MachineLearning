#importing required libraries
import requests as rq
import bs4 as b

#Scraping data from the url using beautiful soup
page=rq.get('https://www.lipsum.com/')
print(page.content)#printing the content of the url
soup=b.BeautifulSoup(page.content,'html.parser')

html=list(soup.children)[2]#Converting scraped data into list 
body=list(html.children)[3]#Converting the children of html conetent into a list

p=body.findAll('p')[0].get_text()#finding all the <p> tags
#replacing '.' ',' '\' by ' '
p=p.replace('.','')
p=p.replace(',','')
p=p.replace('\'','')

usercomment=p.split()#Converting scraped data into a list
#Storing keywords for analysis
good_comment=['Lorem','ipsum','industry','more']
bad_comment=['worse','not ok','grow up','rethink','hate']
countgood=0
countbad=0
for i in range(len(usercomment)):
    for j in range(len(good_comment)):
        if good_comment[j]==usercomment[i]:#Checking if scraped data has the stored keywords
            countgood+=1

    for j in range(len(bad_comment)):
        if bad_comment[j]==usercomment[i]:#Checking if scraped data has the stored keywords
            countbad+=1

if(countgood>countbad):
    print('article is good')
else:
    print('article is bad')

print(countgood)
print(countbad)
print(usercomment)
