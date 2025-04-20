import bibtexparser
import time
from datetime import datetime
import sys

if __name__ == "__main__":
    bib_path = input("Input full path of bibText: ")

with open(bib_path, encoding='UTF-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

bib_text = bib_database.entries[0]

path_text = bib_path.split('/')[:-1]

md_path = '/'.join(path_text)+'/index.md'

with open(md_path, 'w') as md_file:
    md_file.write('---'+'\n')
    md_file.write('title: "'+bib_text['title']+'"'+"\n"*2) #add title
    md_file.write('authors:'+'\n') #add author
    name_list = bib_text['author'].split(' and ')
    for name in name_list:
        md_file.write('- '+name+'\n')
    md_file.write('\n')
    md_file.write('#author_notes:'+'\n'+'#- "Equal contribution"'+'\n'*2) #add equal contribution if needed
    notes = bib_text['note'].split('. ')
    page_tag = ':'+bib_text['pages']
    pubdate = [i for i in notes if page_tag in i]
    pubdate = pubdate[0].split(';')[0]
    pubdate = pubdate.split(' ')
    if len(pubdate)==2:
        pubdate.append('01')
    elif len(pubdate)<2 or len(pubdate)>3:
        print('provided date is wrong!')
    pubdate = ' '.join(pubdate)
    pubdate = datetime.strptime(pubdate, '%Y %b %d')
    formatted_pubdate = pubdate.strftime('%Y-%m-%dT%H:%M:%SZ') 
    #md_file.write('data: "'+formatted_pubdate+'"'+'\n'*2)#add publication published date
    md_file.write('doi: "'+bib_text['doi']+'"'+'\n'*2)#add doi
    #md_publishdata = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime())#add md file publish date
    md_file.write('publishDate: "'+formatted_pubdate+'"'+'\n'*2)
    md_file.write('publication_types: ["'+bib_text['type']+'"]'+'\n'*2)#add publication type
    md_file.write('publication: "'+bib_text['journal']+'"'+'\n'*2)#add journal name
    md_file.write('abstract: "'+bib_text['abstract']+'"'+'\n'*2)#add abstract
    md_file.write('featured: false'+'\n'*2)
    md_file.write('#url_pdf: http://arxiv.org/pdf/1512.04133v1'+'\n'+'#url_code: https://github.com/HugoBlox/hugo-blox-builder'+'\n')#add any url if needed: url_name
    md_file.write('\n')
    md_file.write('#image:'+'\n'+'# caption: '+'\n')#add image if needed
    md_file.write('---'+'\n')
    md_file.close()