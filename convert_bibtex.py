import numpy as np
import string as str
import bibtexparser

FILENAME = '_data/ref.bib'
OUTFILE = '_includes/bib.html'

def format_authors(al):
    al = np.str(al)
    al = al.replace("and",";")
    al = al.replace("{","")
    al = al.replace("}","")
    al = al.replace("~","")
    return al

def format_journal(jl):
    jl = np.str(jl)
    jl = jl.replace("\\apj","Astrophysical Journal")
    jl = jl.replace("\\apjl","Astrophysical Journal Letters")
    jl = jl.replace("\\mnras","Mon. Notice of Royal Astron. Soc.")
    jl = jl.replace("\\procspie","Proc. of SPIE")
    jl = jl.replace("\\nat","Nature")
    jl = jl.replace("\\natast","Nature Astronomy")
    jl = jl.replace("\\sci","Science")
    return jl

def format_title(ti):
    ti = np.str(ti)
    ti = ti.replace("{","")
    ti = ti.replace("}", "")
    return ti


def write_entry(ar,f,year=False):
    #writing the HTML code for each entry

    ar['title'] = format_title(ar['title'])

    try:
        journal = format_journal(ar['journal'])
    except KeyError:
        journal = ''

    if year:
        f.write('<h2> '+np.str(year)+'</h2>')


    f.write('<p style="margin-left: 40px;font-weight: bold">')
    f.write('<li>')
    try:
        f.write('<b><a target="_blank" href='+ar['link']+'>'+ar['title']+'</a></b>'+'   ('+ar['year']+')')
    except KeyError:
        try:
            f.write('<b><a target="_blank" href='+ar['adsurl']+'>'+ar['title']+'</a></b>'+'   ('+ar['year']+')')
        except KeyError:
            f.write(ar['title']+'   ('+ar['year']+')')

    f.write('</li></p>\n')
    f.write('<p style="margin-left: 70px;line-height: 95%;">')
    f.write(format_authors(ar['author']))
    f.write('<br>')
#     f.write('</p>')
    f.write('<font color="grey">')
    try:
        f.write('journal: '+journal+' | volume: '+ar['volume']+' | page: '+ar['pages'])
    except KeyError:
        f.write('journal: ' + journal  + ' | page: ' + ar['pages'])
    f.write('</font>')
    f.write('</p> \n')
    f.write('\n')
    return f



#reading bibtex
with open(FILENAME,'r') as database:
    data = bibtexparser.load(database)

#output file
out = open(OUTFILE,'w')


Ncite = len(data.entries)
print(Ncite)

years = []
for i in range(Ncite):
    years.append(np.int(data.entries[i]['year']))

min_year = np.min(years)
max_year = np.max(years)
yearline = np.arange(min_year,max_year+1)[::-1]


for year in yearline:
    yearmark = True
    # print('year idx ', year)
    for i in range(Ncite):
        if np.int(data.entries[i]['year']) == year:
            if yearmark:
                # print('yearmark ',year)
                write_entry(data.entries[i],f=out,year=year)
                yearmark = False
            else:
                # print(year)
                write_entry(data.entries[i],f=out)
