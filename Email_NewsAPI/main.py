import requests
import os
from send_email import send_email

topic = "tesla"

api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-12-02&sortBy=publishedAt&apiKey={api_key}&language=en"

request = requests.get(url)
content = request.json()

# Build the HTML body
html_body = "<html><body>"
html_body += "<h1>Today's News</h1>"

for article in content["articles"][:20]:
    if article["title"] is not None:
        # Format the title in bold and add other elements
        html_body += f"<p><b>{article['title']}</b><br>"
        html_body += f"{article['description']}<br>"
        html_body += f"<a href='{article['url']}'>Read more</a></p><br>"

html_body += "</body></html>"

# Send the email
send_email(subject="Today's News", message=html_body)
