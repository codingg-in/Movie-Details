# IMDB Movie Bot
A bot to scrap details of movies from the IMDB official website.

## Introduction
A web scrapping bot dedicated to work on IMDB website for scraping detials like title, raiting, duration, genre, cast etc of the movie name provided as the argument. It display the result in console in the colourful format for some exciting look and this program also implement the logic of multi-threading for real-time fetching of data and displaying the progress bar for it.

## Implemantion
Major Implementation of idea using:
1. BeautifulSoup<br>
Used BeautifulSoup library to scrap the web page and while parsing it find the required content to be displayed.

2. Colorama<br>
Used Colorama library to give the coloured console output. 

3. Threding<br>
Used threading library to use the concept of multi-threading for real time fetching and progress bar.

## Usage

##### Scraping
    Syntax: python main.py < movie_name >

    > Scrap the details of movie name from IMDB.

        Positional Arguments:
                movie_name    :    name of the movie whose details to be fetched

>**NOTE** : May give partial information for video other than movies like TV Series as content may be different.

### Usage Examples:
    Scraping Example: Scrap details of 'Aquaman' and display in console 
                      Command: 'python main.py aquaman
                      The program will run and display detials of movie 'Aquaman'
### Output:
![Screenshot](https://user-images.githubusercontent.com/32950502/58820393-22bf9f80-8650-11e9-9ec2-c6809b5407b9.png)

## References
1. [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [Colorama Documentation](https://he-arc.github.io/livre-python/colorama/colorama.html)
3. [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)

## Dependencies 

This program depends on Python3 BeautifulSoup, requests, colorama.

##### Installation Using Pip:
    sudo apt-get install python3-pip
    sudo apt-get install beautifulsoup4
    sudo apt-get install requests
    sudo apt-get install colorama
    
## License

This project is licensed under the MIT License - see the LICENSE file for details
