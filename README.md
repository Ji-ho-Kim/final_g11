# Creating my own to-go restaurant list

## Brief overview

This is ossc final project of Group 11.
<br>
The name of our project is **"Creating my own to-go restaurant list"**.
<br>
By crawling data of one hundred data for each of the 25 boroughs in Seoul from _MangoPlate_(망고플레이트), Korea's trusted restaurant review site.
<br><br>
The crawled four items are as follows:

    - the borough which the restaurant belongs
    - restaurant name
    - rating by reviewers
    - restaurant type (Korean, Chinese, Western...)

Crawled data are stored in **Excel(.xlsx)** file.
<br>
(We excluded restaurants that don't have a rating.)

To start, when a user clicks on '파일 선택' button and select the downloaded xlsx file, a table appears in which restaurants throughout Seoul have high ratings.
<br>
Simply click on the section of the map above that you want to visit to see the results categorized by borough.
<br>
Enter one of the following in the text box: "한식, 양식, 일식, 중식, 디저트" to see the results categorized by restaurant type.
<br>
Finally, you can add the restaurant that you want to go to the list and manage your own list.
<br><br>
**Whenever you are wondering which restaurant to go to, visit this website and check your list! :)**

## Link of resources

1. crawling

-   https://m.blog.naver.com/owl6615/221518357627
-   https://galid1.tistory.com/478
-   https://hello-bryan.tistory.com/194

2. reading xlsx file in javascript

-   https://eblo.tistory.com/83
-   https://code.tutsplus.com/ko/tutorials/parsing-a-csv-file-with-javascript--cms-25626

3. mapping by region

-   https://woodstar.tistory.com/124

4. making my own list

-   https://github.com/e-/skku-todo-2.git

## Screenshots of the web page

<img width="565" alt="test6" src="https://user-images.githubusercontent.com/79782180/119431221-25d85c80-bd4d-11eb-93a3-1e31302d283b.PNG">
<img width="960" alt="test3" src="https://user-images.githubusercontent.com/79782180/119431073-e3168480-bd4c-11eb-8802-735b1b3ff4fc.PNG">
<img width="947" alt="test4" src="https://user-images.githubusercontent.com/79782180/119431076-e447b180-bd4c-11eb-9ee1-da704c10870b.PNG">
<img width="948" alt="test5" src="https://user-images.githubusercontent.com/79782180/119431079-e447b180-bd4c-11eb-9535-3fb1d11829c9.PNG">

## Short demo video link

>Making my own list by taking a look at restaurants in all of Seoul

   https://www.youtube.com/watch?v=-5eOaU17v1Y

>Making my own list by taking a look at restaurants within the selected borough

   https://www.youtube.com/watch?v=f5eYgoCO5Ws

## Installation

**CRAWL**

You can download the excel file from this git repo and use it, but if you want to do crawling on your own:

    1. Download CRAWL.py, seoul.txt, chromedriver.exe
    2. Edit seoul_file_path in CRWAL.py to your file path
    3. Edit chrome_driver_path in CRWAL.py to your file path
    4. Do 'pip install selenium' on command line
    5. Run CRAWL.py
    6. As the homepage of mangoplate comes up, you need to click the popup manually to crawl normally
    7. Check the excel file!

## Code of Conduct

- If you want to see the list of restaurants in all of Seoul . . .
```
1. Click on '파일 선택' button.
2. Enter one of the following in the text box: "한식, 양식, 일식, 중식, 디저트".
 ```       
- If you want to see the list of restaurants within the selected borough by restaurant type . . .
```
1. Click on '파일 선택' button.
2. Click on the image section that corresponds to the borough.
3. Enter one of the following in the text box: "한식, 양식, 일식, 중식, 디저트".
```

## Examples (of screenshots above)

Person A wants to visit '일식'(Japanese) restaurant in '은평구'! <br>
Then, A should follow the directions below:
```   
1. Click '파일 선택' button and select 'Mat-zip-list.xlsx' file
2. Click on '은평구' of the map above
3. Enter '일식'(Japanese) in the text box
4. Add the restaurant that you want to go to your own list!
```

## API reference

We directly parsed HTML page and crawled data without utilizing API...

## Releases (versions)

v1.0.1 (Latest release)

## How to contribute

    1. Fork our repo to your account
    2. Modify your own repo
    3. Write pull request
    4. We will decide whether to approve your pull request or not!

## License

    MIT license
