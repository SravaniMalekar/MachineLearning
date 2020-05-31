#importing required libraries
import requests as rq
import bs4 as b
import re
import nltk
#Scraping Amazon Reviews
url='https://www.amazon.in/dp/B07HHHMWQG/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=5FJ11P9YPY8ME3RSBQSK&pf_rd_t=101&pf_rd_p=428cd22f-b362-46d4-aa3b-7b2c8ea18e0c&pf_rd_i=21405369031'
header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
page=rq.get(url,headers=header)
soup=b.BeautifulSoup(page.content,'html.parser')
html=list(soup.children)
body=list(soup.children)[54]
#Looking for the reviews
review= body.findAll('span',{"data-hook":"review-body"})

goodcomment=0
badcomment=0
#Traversing through the list of reviews to check if a review is positive or not
for i in range(len(review)):
    x=review[i].findAll('span')[0].get_text
    ##cont.append(x)
    
    p=str(x)
    p=p.lower()#converting the reviews to lower case
    p=re.sub("<br/>"," ",str(p))#removing <br/> tags
    p=re.sub("<span>"," ",str(p))#removing <span> tags
    p=re.sub("</span>"," ",str(p))
    p=re.sub(r"[^a-zA-Z0-9]"," ",str(p))#removing all the special characters and numbers
    
    lemmer=nltk.stem.WordNetLemmatizer()
    word_tokens=nltk.word_tokenize(p)
    sent_tokens=nltk.sent_tokenize(p)
    usercomment = list(word_tokens)
    print(usercomment)
    #usercomment=p.split()
    #usercomment=re.sub(r"[^a-zA-Z0-9]"," ",str(usercomment))
  
    #usercomment = usercomment.split()
    good_comment=['good','best','amazing','awesome','excellent','great','love','satisfied']
    bad_comment=['worse','useless','bad','hate','waste','unsatisfactory']
    countgood=0
    countbad=0
        
    for i in range(len(usercomment)):
        for j in range(len(good_comment)):
            if good_comment[j]==usercomment[i]:
                countgood+=1

        for j in range(len(bad_comment)):
            if bad_comment[j]==usercomment[i]:
                countbad+=1

    if(countgood>countbad):
        goodcomment +=1
    else:
        badcomment +=1

print('Goodreviews:'+str(goodcomment))
print('Badreviews:'+str(badcomment))
if(goodcomment>badcomment):
    print('Product is recommended')
else:
    print('Not recommended')
