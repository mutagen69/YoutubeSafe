from flask import Flask, request, abort
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
session = requests.Session()

proxies = { 'https' : 'modeler_PHwLLO:XWREGXIgY01n@103.57.251.138:12347' }

@app.route("/")
def start_session():
    headers = {
        "Accept-Language": "ru,en;q=0.9", 
        "Cache-Control": "max-age=0", 
        "Priority": "u=0, i", 
        "Sec-Ch-Ua": '"Not-A.Brand";v="99", "Chromium";v="124"', 
        "Sec-Ch-Ua-Arch": '"x86"', 
        "Sec-Ch-Ua-Bitness": '"64"', 
        "Sec-Ch-Ua-Form-Factors": '"Desktop"', 
        "Sec-Ch-Ua-Full-Version": '"124.0.6367.243"', 
        "Sec-Ch-Ua-Full-Version-List": '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6367.243"', 
        "Sec-Ch-Ua-Mobile": "?0", 
        "Sec-Ch-Ua-Model": '""', 
        "Sec-Ch-Ua-Platform": '"Windows"', 
        "Sec-Ch-Ua-Platform-Version": '"10.0.0"', 
        "Sec-Ch-Ua-Wow64": "?1", 
        "Sec-Fetch-Dest": "document", 
        "Sec-Fetch-Mode": "navigate", 
        "Sec-Fetch-Site": "none", 
        "Sec-Fetch-User": "?1", 
        "Service-Worker-Navigation-Preload": "true", 
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36", 
    }
    r = requests.get('https://youtube.com/', proxies=proxies, headers=headers)
    return r.content

@app.errorhandler(404)
def page_not_found(e):
    r = requests.get('https://youtube.com'+request.path, proxies=proxies)
    return r.content

if __name__=='__main__':
    app.run(debug=True)