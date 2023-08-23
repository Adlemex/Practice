class Article:
    def __init__(self, date, topic, sender):
        self.date = date
        self.topic = topic
        self.sender = sender

class Journal:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def remove_article(self, index):
        del self.articles[index]

    def edit_article(self, index, article):
        self.articles[index] = article

    def search_article(self, keyword):
        for article in self.articles:
            if keyword in article.topic or keyword in article.sender:
                print(article.date, article.topic, article.sender)

    def sort_articles(self):
        self.articles.sort(key=lambda x: x.date)

    def display_journal(self):
        print("Journal number:", self.number)
        print("Journal name:", self.name)
        for article in self.articles:
            print(article.date, article.topic, article.sender)