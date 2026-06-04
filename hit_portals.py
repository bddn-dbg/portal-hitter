import requests
import random
import time

urls = [
    "https://bddn.online",
    "https://dynamic-portal-omega.vercel.app",
    "https://dynamic-portal-bddn-web.netlify.app",
    "https://demo-ecommerce-bddn.netlify.app",
    "https://imran41.github.io/portfolio/",
    "https://silly-buttercream-70d93e.netlify.app/",
    "https://mb-data-collection.vercel.app/",
    "https://bddn-dbg.github.io/fancydata/",
    "https://bihar-digital-data-and-network-hnou.vercel.app/",
    "https://bddn.online/bddn-institute.github.io/",
    "https://stockforecasting-home-imran.streamlit.app/"
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
