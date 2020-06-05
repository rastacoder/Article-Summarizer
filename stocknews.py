import os
import sys
import nltk
from newspaper import Article


def summary():
    url = str(input("Please enter the URL of the article: "))
    article = Article(url)

    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()
    print(article.summary)

    file_save = input("Would you like to save the summary ?").upper()
    if file_save == "YES":
        file_name = str(input("What would you like to save the file as? "))
        f = open(file_name + ".txt", "w")
        article_summary = str(article.summary)
        f.write(article_summary)

def main():
    summary()

    while True:
        again = input("Would you like to summarize another article? ").upper()
        if again == "YES":
            summary()
        else:
            quit()

main()
