import PyPDF2
import tabula
from bs4 import BeautifulSoup
import sys
import math
import json

def get_scores():
    tab = tabula.read_pdf("score.pdf", pages='all')

    tab_0 = tab[0].to_html()
    tab_1 = tab[1].to_html()

    soup0 = BeautifulSoup(tab_0,'html.parser')
    soup1 = BeautifulSoup(tab_1, 'html.parser')

    tr0 = soup0.find_all('tr')
    tr1 = soup1.find_all('tr')
    res = []
    i = 5
    while i < len(tr0):
        tmp = tr0[i].contents
        txt = tmp[3].text
        flo = float(tmp[len(tmp)-2].text)
        if i < len(tr0) and math.isnan(flo) and tr0[i+1].contents[3].text == 'NaN':
            t = tr0[i+1].contents
            flo = float(t[len(t)-2].text)
            i+=1
        res.append((txt,flo))
        i+=1
    
    i = 0
    while i < len(tr1):
        tmp = tr1[i].contents
        txt = tmp[3].text
        flo = float(tmp[len(tmp)-2].text)
        if i < len(tr1) and math.isnan(flo) and tr1[i+1].contents[3].text == 'Nan':
            t = tr1[i+1].contents
            flo = float(t[len(t)-2].text)
            i+=1
        res.append((txt,flo))
        i+=1

    return res


def sort_scores(scores):
    res =[]

    for s in scores:
        i = 0
        if math.isnan(s[1]):
            res.append(s)
        else:
            while i < len(res) and s[1] < res[i][1]:
                i+=1
            res.insert(i,s)
    return res

def get_rank(scores, stud_id):
    rank = 1
    for elm in scores:
        if elm[0] == stud_id:
            return (rank,elm[1])
        rank+=1
    raise Exception("Your student ID is not in the PDF !")

def compute(stud_id):
    sorted_scores = load_json()
    r = get_rank(sorted_scores, stud_id)
    print("Rank : ",r[0])
    print("Score : ",r[1])
    return

def get_tab():
    sorted_scores = load_json()
    r = 1
    print("     Student ID         Score")
    print("---------------------------------")
    while r< len(sorted_scores) and r < 10:
        print(r," | " + sorted_scores[r-1][0] +'         ', sorted_scores[r-1][1])
        r+=1
    while r< len(sorted_scores):
        print(r,"| " + sorted_scores[r-1][0] +'         ', sorted_scores[r-1][1])
        r+=1

def save_json():
    scores = get_scores()
    s_scores = sort_scores(scores)
    json_obj = json.dumps(s_scores,indent = 4)
    f = open("saved_scored.json",'w',encoding = 'utf-8')
    f.write(json_obj)

def load_json():
    f = open("saved_scored.json","r",encoding = 'utf-8')
    return json.load(f)

