import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number / 필요 선택자 조회
# select 를 이용해서 tr 들 불러오기

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')

# songs의 tr들 반복문 돌리기
for song in songs:
    # 문자열 슬라이싱, strip() 사용
    rank = song.select_one('td.number:not(span.rank)').text[0:2].strip()
    song_name = song.select_one('td.info > a.title').text.strip()
    singer = song.select_one('td.info > a.artist').text
    # print(rank, song_name, singer)
    # mongodb 저장
    doc = {
        'rank': rank,
        'song_name': song_name,
        'singer': singer
    }
    db.songs.insert_one(doc)
