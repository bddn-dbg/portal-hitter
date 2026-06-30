import requests
import random
import time

urls = [
    "https://bddn.online",
    "https://bddn.in",
    
    #MindMap
    "https://thriving-otter-f0f8c2.netlify.app/",
    "https://brilliant-pegasus-a19ea7.netlify.app/",
    
    "https://imran41.github.io/portfolio/",
    "https://stockforecasting-home-imran.streamlit.app/",
    
    # Scorecard
    "https://scorecard-imran.streamlit.app/",
    "https://cute-douhua-27227e.netlify.app/",
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in urls:
    try:
        response = requests.get(url, headers=headers, timeout=20)

        print(url, response.status_code)

        time.sleep(random.randint(5, 15))

    except Exception as e:
        print(url, e)
