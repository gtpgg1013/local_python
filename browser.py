import webbrowser

url = "https://search.naver.com/search.naver?query="

keyword = ["IU","전효성","폴킴"]

for k in keyword:
    webbrowser.open(url+k)
