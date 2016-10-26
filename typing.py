import requests
import time


file = open("SECRETS.txt","r");
secrets = {}
data = file.read()
for lines in data.split("\n"):
	if "=" in lines:
		vals = lines.strip().split('=', 1)
		secrets[vals[0]]=vals[1];

REQUEST_HEADERS = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, sdch',
    'accept-language': 'en-US,en;q=0.8,en-AU;q=0.6',
    'cookie': secrets["cookie"],
    'dnt': '1',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
}

def typing(receiver):
	data = {
		"typ":"1",
		"to":receiver,
		"fb_dtsg":secrets["fb_dtsg"],
	}
	resp = requests.post("https://www.facebook.com/ajax/messaging/typ.php?dpr=1",data=data,headers=REQUEST_HEADERS, allow_redirects=True,verify=False)
	return resp.text

while True:
	typing(secrets["target"])
	time.sleep(25)
