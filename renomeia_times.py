import re
from requests_html import HTMLSession


s = HTMLSession()
r = s.get('https://cbf.com.br/competicoes/brasileiro-serie-a/equipes/2018')
times = [x.attrs['title'] for x in r.html.find('div.cell')[0].find('a')]
times_renomeados = []

for time in times:
    if [x.split('-')[0] for x in times].count(time.split('-')[0]) >= 2:
        times_renomeados.append(re.sub(r"[\ *]?-[\ *]?", "", time))
    else:
        times_renomeados.append(time.split('-')[0])

print(times_renomeados)
