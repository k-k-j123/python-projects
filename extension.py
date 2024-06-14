import random
import pyautogui as pg
import time
from selenium import webdriver

random_words = [
    "Paris", "Tokyo", "New York", "Sydney", "Rome", "Cairo", "London", "Rio de Janeiro", "Mumbai", "Venice",
    "Barcelona", "Moscow", "Cape Town", "Bangkok", "Dubai", "Toronto", "Buenos Aires", "Amsterdam", "Seoul", "Istanbul",
    "Albert Einstein", "Leonardo da Vinci", "Oprah Winfrey", "Nelson Mandela", "William Shakespeare", "Marie Curie",
    "Michael Jackson", "Amelia Earhart", "Mahatma Gandhi", "Madonna", "Martin Luther King Jr.", "Queen Elizabeth II",
    "Elon Musk", "Pablo Picasso", "Marilyn Monroe", "Winston Churchill", "Cleopatra", "Steve Jobs", "Frida Kahlo",
    "Albert Einstein", "Leonardo DiCaprio", "Malala Yousafzai", "Vincent van Gogh", "Serena Williams", "Isaac Newton",
    "J.K. Rowling", "Barack Obama", "Audrey Hepburn", "Muhammad Ali", "Mother Teresa"
]
browser = webdriver.Edge()
time.sleep(8)

for i in range(35):
    a=random.choice(random_words)
    time.sleep(5)
    matched_elements = browser.get("https://www.bing.com/search?q=" +a)
