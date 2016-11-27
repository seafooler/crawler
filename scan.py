#encoding=utf-8
import urllib2,urllib
import BeautifulSoup
import socket
socket.setdefaulttimeout(3)
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

url = 'http://www.xicidaili.com/nn/1'
req = urllib2.Request(url, headers=header)
res = urllib2.urlopen(req).read()

soup = BeautifulSoup.BeautifulSoup(res)
ips = soup.findAll('tr')
count = 0
with open("proxy", "w") as f:
	for x in range(1, len(ips)):
		if count >10:
			break
		ip = ips[x]
		tds = ip.findAll("td")
		url_check = "http://ip.chinaz.com/getip.aspx"
		proxy_host = "http://"+tds[1].contents[0]+":"+tds[2].contents[0]
		proxy_temp = {"http":proxy_host}
		try:
			res = urllib.urlopen(url_check, proxies = proxy_temp).read()
			ip_temp = tds[1].contents[0] + "\t"+tds[2].contents[0]+"\n"
			f.write(ip_temp)
			count += 1
			print count
		except Exception,e:
			print proxy_temp
			print e
			continue