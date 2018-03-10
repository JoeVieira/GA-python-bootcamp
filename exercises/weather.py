import urllib.request
import json

try:
    url = urllib.request.urlopen("http://sampls.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22")
    data = json.loads(url.read().decode())

    f = open("weather","w")

    weather = data['weather']
    need_header = True
    for day in data['weather']:
        if need_header:
            f.write("\"main\""+","+"\"desc\"\n")
            need_header = False
        f.write("\""+day['main']+"\",")
        f.write("\""+day['description']+"\"");

    f.close()
except Exception:
    print("sorry something went wrong")
    