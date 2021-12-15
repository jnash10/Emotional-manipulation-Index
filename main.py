import stanza 
from joblib import load
from transcripts import get_transcript
import math


## ratio function
def ratios(file, stopwords):
    nlp =stanza.Pipeline(lang = 'en',processors='tokenize,pos')
    with open(file,errors='ignore') as file:
        adj,adv,pro=0,0,0
        doc = nlp(file.read())
        for sent in doc.sentences:
            for token in sent.words:
                if token.text not in stopwords:
                    if token.upos=="ADJ":
                        adj+=1
                    elif token.upos=="ADV":
                        adv+=1
                    elif token.upos=="PRON":
                        pro+=1
                    
    return adv/adj,adj/pro

## loading the ML model
loreg = load('r_loreg.joblib')


link = input("please paste youtube link: ")
get_transcript(link)

file = "transcript.txt"

##generating frequency table
text = open(file, 'r')

special = stanza.Pipeline(lang = 'en', processors='tokenize')
freq_Table = {}
sdoc = special(text.read())
total_words = 0
for sent in sdoc.sentences:
    for word in sent.words:
        total_words+=1
        if word.text in freq_Table:
            freq_Table[word.text]+=1
        else:
            freq_Table[word.text]=1


## removing stopwords
percentile = 98

abc = sorted(freq_Table, key=freq_Table.get)
abc = abc[::-1]
count = math.floor((1-percentile/100)*len(abc))
stopwords = abc[:count]
#print(stopwords)


#calculating final ratios and then score
RAA,RAP = ratios(file,stopwords)
r_RAA = RAA/(RAA+RAP)
r_RAP = RAP/(RAA+RAP)

score = loreg.predict_proba([[r_RAA,r_RAP]])[0][1]
print("\n"*3,"fictometer rating: ",score)


