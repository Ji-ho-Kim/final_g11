#!/usr/bin/env python
# coding: utf-8

# # 네이버 플레이스 API로 맛집 크롤링
# - https://liveyourit.tistory.com/244 를 참고하여 코드 작성
# - 서울 열린데이터 광장 '서울시 주민등록인구 (동별) 통계' 데이터 이용 

# In[1]:


import pandas as pd
import sys
import json
import time
import requests
import csv
import re
import numpy as np

#서울시 동 정보 데이터 로드
seoul_df = pd.read_csv('../data/서울시 주민등록인구 (동별) 통계.txt',sep="\t")
seoul_df = seoul_df[['자치구', '동']].drop([0, 1], axis=0) #크롤링에 필요한 행정지역 정보만 추출

#불순물 데이터 제거
del_list1 = seoul_df[seoul_df['동'] == '미상'].index
del_list2 = seoul_df[seoul_df['동'] == '소계'].index
seoul_df.drop(del_list1, inplace=True)
seoul_df.drop(del_list2, inplace=True)
seoul_df= seoul_df.groupby('자치구')['동'].apply(list)

seoul_dict = {}

#구를 key값으로, 동을 value 값으로
for gu in seoul_df.index:
    seoul_dict[gu] = seoul_df[gu]

# In[2]:


#크롤링 시 -- 1동으로 검색하는 것보다, 숫자를 제거한 동을 검색하는것이 일반적이므로 숫자를 제거
for gu, dong_list in seoul_dict.items():
    dong_list_modi = []
    for dong in dong_list:
        dong_list_modi.append(re.sub('[0-9.]','',dong))
    seoul_dict[gu] = set(dong_list_modi)

# In[3]:


#key값이 존재할때에만 value값 반환
def get_json_value(key, i):
    try:
        if key in data['items'][i]:
            values = data['items'][i][key]
            write.append(values)
        else:
            write.append('None')
    except:
        stop = 1

# In[7]:


write = []

f = open('서울시 맛집.csv'.format(gu), 'w', encoding='utf-8-sig', newline='')
f.close()

for gu in seoul_dict.keys():
        print('-' +gu)
        for dong in seoul_dict[gu]:
            print('   -'+ dong)
            gu_dong = gu+ '+' +dong+ '+' +u'맛집'
            display =100 # 한 페이지에 표시할 데이터 수
            stop = 0

            for start in range(1, 10):
                try:
                    url = 'https://store.naver.com/sogum/api/businesses?'
                    query = {'start': str(start),
                            'display' : str(display),
                            'query' : gu_dong,
                            'sortingOrder' : 'reviewCount'} 

                    time.sleep(5) #원활한 크롤링을 위해 sleep 지정
                    data = requests.get(url,query)

                    if data.status_code == 500:
                            #status_code가 200일 때, 성공적으로 가져온다
                            break

                    data = json.loads(data.text)

                    for i in range(display):
                            write.append(gu)
                            write.append(dong)
                            get_json_value('name', i) # 이름
                            get_json_value('businessCategory', i) #카테고리 대분류
                            get_json_value('category',i) #카테고리 소분류
                            get_json_value('x',i) # x좌표
                            get_json_value('y',i) # y좌표
                            get_json_value('microReview',i)
                            get_json_value('roadAddr',i) #주소
                            get_json_value('blogCafeReviewCount',i) # 블로그 리뷰 수 
                            get_json_value('bookingReviewCount',i) # 예약 리뷰 수
                            get_json_value('visitorReviewCount',i) # 방문자 리뷰 수
                            get_json_value('visitorReviewScore',i) # 방문자 리뷰 점수
                            get_json_value('totalReviewCount',i) # 전체 리뷰 수
                            get_json_value('moreBookingReviewsPath',i) # 예약 리뷰 url
                            get_json_value('moreUGCReviewsPath',i) # UGC 리뷰 url
                            get_json_value('moreFsasReviewsPath',i) # Fsas 리뷰 url 
                            get_json_value('tags',i) # 태그정보
                            get_json_value('priceCategory',i) #가격대

                            if stop == 1:
                                break

                            with open('서울시 맛집.csv'.format(gu), 'a', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(write)

                            write = []
                except:
                    print(gu +' '+ dong + ' ' + i)

# In[ ]:


# 맛집 정보 불러오기
place_df = pd.read_csv('서울시 맛집.csv')

# In[ ]:


#크롤링한 csv파일의 첫 행이 컬럼이 되는 문제 해결 & 컬럼 재배정
def make_df(df):
    first = np.array(df.columns).reshape(1,-1)
    df.columns = ['구', '동', '이름', '카테고리', '세부카테고리', 'x좌표', 'y좌표', '마이크로리뷰', '주소','블로그리뷰수', '예약리뷰수','방문자리뷰수','방문자리뷰점수', '전체리뷰수', '예약리뷰url', 'UGC리뷰url', 'Fsas리뷰url', '태그','가격대'] 
    first_df = pd.DataFrame(first, columns = list(df.columns))
    df = df.append(first_df)
    return df

place_df = make_df(place_df)

# In[ ]:


#예약리뷰 url이 존재하는 리스트만 출력
place_df = place_df[place_df['예약리뷰url'] != 'None']

#결측치 삭제
place_df = place_df.dropna()

#중복행 삭제 - 동일한 가게가 다른 지역에 이중으로 삽입되는 문제 해결을 위해 구, 동을 제외하고 중복가게를 제거 (동일한 이름에 동일한 주소를 사용한다면 같은 가게일 확률이 높다) 
place_df = place_df[place_df.columns[2:]].drop_duplicates()

# 예약리뷰수 사이의 쉼표 제거 & 타입 변경, 
place_df['예약리뷰수'] = place_df['예약리뷰수'].apply(lambda x:  re.sub(',','',x) if type(x) == str else x).astype(int)

#예약리뷰가 많은 순으로 정렬
place_df = place_df.sort_values('예약리뷰수', ascending=False)

# # 크롤링에 필요한 businessID 추출
# - 크롤링의 변수인 businessID가 예약리뷰 url 사이에 존재 -> re를 활용하여 추출

# In[ ]:


review_list = list(place_df['예약리뷰url'])

review_list_modi = []
for url in review_list:
    try:
        review_list_modi.append(re.findall('bookingBusinessId=(.+?)\&',url)[0])
    except:
        review_list_modi.append('None')
        
place_df['business_id'] = review_list_modi

# In[ ]:


write = []
f = open('맛집리뷰.csv', 'w', encoding='utf-8-sig', newline='')
f.close()
cnt = 0

for num_review, bus_id in zip(place_df['예약리뷰수'], place_df['business_id']):
    
    stop = 0
    display = 100 #한 페이지에 출력할 리뷰 수
    pages = num_review // display + 1 #총 리뷰수와 display로 최종 페이지 결정
    cnt += 1
    print(cnt)
    
    for page in range(pages):
        url = 'https://store.naver.com/sogum/api/bookingReviews?'
        query = {'bookingBusinessId' : bus_id , 
                'display': str(display), 
                'page': page}

        time.sleep(5)
        data = requests.get(url ,query)

        if data.status_code == 500:
          break

        data = json.loads(data.text)

        for i in range(display):
            get_json_value('reviewBody', i) # 리뷰 내용
            get_json_value('score', i) # 리뷰 점수
            get_json_value('replyBody', i) # 해당 가게의 답변
            get_json_value('bookingItemName', i) # 예약 메뉴
            get_json_value('bookingBusinessName', i) # 가게 이름

            if stop == 1:
                 break

            with open('맛집리뷰.csv', 'a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(write)

            write = []
