from requests import get
from re import sub

SBHS = 'http://www.sydneyboyshigh.com'

r = get(SBHS)
print("\nStatus: {}\n".format(r.status_code))

html = (r.text).split('<tr>')[1:9]
#Gives events from index 0-7

x = 0
for i in html:
    event = (html[x].split('">')[2:7])

    title = sub(r'<b>', '', (sub( r'</b>', '', event[2].split('</a')[0])))
    date = event[0].split('</span')[0]
    link = (SBHS + event[1].split('"')[1])

    q = get(link)
    event_html = (q.text).split('<td colspan="4">')[1].split('</td>')[0].split('<script')[0]
    info = sub(r'</a></b>', '', sub(r'" target="_blank">', '\n', sub(r'<b><a href="', '\n', sub(r'/>', '',sub(r'<br', '', event_html)))))

    print("Title: {}".format(title))
    print("Date: {}".format(date))
    print("Link: {}".format(link))
    print("Event Info:\n{}\n".format(info))
    
    x += 1