from bs4 import BeautifulSoup
import pandas as pd
import requests

date = input("please enter a Date in the following format MM/DD/YYYY:")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}#")

def main(page):
    src=page.content
    soup = BeautifulSoup(src,"lxml")
    matches_details = []

    championships = soup.find_all('div',{'class':'matchCard'})

    def get_match_info(championships):
        #for championship in championships :
        championship_title = championships.contents[1].find("h2").text.strip()
        all_matches = championships.contents[3].find_all("div",{'class': 'item'})
        number_of_matches = len(all_matches)
        for i in range(number_of_matches):
            #get teams names
            team_a = all_matches[i].find('div',{'class':'teams teamA'}).text.strip()
            team_b = all_matches[i].find('div',{'class':'teams teamB'}).text.strip()

            #get_score
            match_result = all_matches[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"

            #get_time
            match_time = all_matches[i].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()
            
            #get_all matches_details
            matches_details.append({'Championsip Title':championship_title,"Team A":team_a,"Team B":team_b,"Match Time":match_time,'Score':score})

    for i in range(len(championships)):
        get_match_info(championships[i]) 
    
    df = pd.DataFrame(matches_details)
    df.to_excel('matches.xlsx', index=False)


main(page)    