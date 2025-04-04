from fastapi import FastAPI
import random
from jokes_data import urdu_jokes

app = FastAPI(title="Pakistani Joke Generator", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pakistani Joke Generator! Use /random-joke"}

@app.get("/random-joke")
def get_random_joke():
    """Returns a random Pakistani joke in Urdu."""
    return random.choice(urdu_jokes)

@app.get("/all-jokes")
def get_all_jokes():
    """Returns all jokes."""
    return {"jokes": urdu_jokes}






















# from fastapi import FastAPI
# import random

# app = FastAPI()

# # we will build two simple get endpoints
# # side_hustles
# #  money_quotes

# side_hustles = [
#     "Freelance Python Developer - Offer your Python skills on platforms like Upwork, Fiverr, or Toptal.",
#     "Build and Sell APIs        - Create RESTful APIs using FastAPI or Flask and sell them on marketplaces like RapidAPI.",
#     "Automation Scripts for Businesses - Develop Python scripts to automate repetitive tasks for small businesses",
#     "Create and Sell Python Courses - If you’re proficient in Python, create tutorials or courses on platforms like Udemy, Teachable, or YouTube.",
#     "Develop and Sell Python Libraries - Build reusable Python libraries or packages and publish them on PyPI.",
#     "Data Analysis and Visualization Services - Use Python libraries like Pandas, NumPy, and Matplotlib to analyze and visualize data for clients.",
#     "Chatbot Development         - Build chatbots using Python frameworks like Rasa or ChatterBo",
#     "Web Scraping Services       -  Use Python libraries like BeautifulSoup or Scrapy to extract data from websites.",
#     "Build and Sell SaaS Products - Develop a Software-as-a-Service (SaaS) product using Python frameworks like Django or FastAPI.",
#     "Python Tutoring or Mentorship  -  Offer one-on-one Python tutoring or mentorship sessions.",
#     "Create Python-Based Games - Develop simple games using Python libraries like Pygame.",
# ]

# money_quotes = [
#    "Code is currency. Write it wisely, and it will pay dividends.",
#    "Python isn’t just a language; it’s a goldmine for those who know how to use it.",
#    "Automate the boring stuff, and you’ll have time to focus on the profitable stuff.",
#    "In the world of tech, Python is the Swiss Army knife—versatile, powerful, and always in demand.",
#    "Your next side hustle could be just one Python script away.",
#    "Don’t just code for fun; code for funds.",
#    "Python developers don’t just solve problems—they create opportunities.",
#    "The best investment you can make is in your Python skills—it pays compound interest.",
#    "From freelancing to SaaS, Python opens doors to endless income streams.",
#    "The more you automate, the more you can accumulate.",
#    "Python is the language of the future, and the future is profitable.",

# ]

# @app.get("/side_hustles")
# def get_side_hustles(apiKey: str):
#     """Returns a random side hustle idea"""
#     if apiKey != "1234567890":
#         return {"error": "Invalid API key"}
#     return {"side_hustle": random.choice(side_hustles)}

# @app.get("/money_quotes")
# def get_money_quotes(apiKey: str):
#     """Returns a random side money quote"""
#     if apiKey != "1234567890":
#         return {"error": "Invalid API key"}
#     return {"money_quote": random.choice(money_quotes)}