import subprocess
import os
import nltk
import re

#pos = part-of-speech
#ne = named entity

class Word:
    # not necessary but included for clarity
    fullword = ""
    lemma = ""
    pos = ""
    ne = ""

    def __init__(self, origin_word, lem, part, entity):
        self.fullword = origin_word
        self.lemma = lem
        self.pos = part
        self.ne = entity
        self.dependencies = {}

def analyzeSentence(sentence):

    analysis = []
    posdict = getPOS(sentence)
    nedict = findNE(sentence)

    wnl = nltk.WordNetLemmatizer()

    tokens = nltk.word_tokenize(sentence)

    wordnet_tags = {'NN':'n','JJ':'a','VB':'v','RB':'r'}

    for token in tokens:
        postag = posdict[token][:2]
        if postag not in wordnet_tags:
            lemma = wnl.lemmatize(token)
        else:
            lemma = wnl.lemmatize(token, wordnet_tags[postag])
        if nedict[token] == 'O':
            lemma = lemma.lower()
        analysis.append(Word(token, lemma, posdict[token], nedict[token]))

    dependlist = getDependencies(sentence)

    for d in dependlist:
        parentnum = int(d[2]) - 1
        childnum = int(d[4]) - 1
        if parentnum > -1:
            analysis[parentnum].dependencies[d[0]] = analysis[childnum]
    
    return analysis

def getDependencies(sentence):
    startdir = os.getcwd()
    
    os.chdir("./stanford_tools/stanford-parser-full-2014-01-04/")

    temp_file = open('temp.txt', 'w')
    temp_file.write(sentence)
    temp_file.close()

    stanford_output = subprocess.check_output(["./lexparser.sh", "./temp.txt"])

    print stanford_output

    os.chdir(startdir)

    dependlist = [d for d in stanford_output.split("\n") if len(d) > 0 and d[0].islower()]
    dependlist = [re.findall('([a-z]+)\(([a-z|A-Z|\']+)-([0-9]+), ([a-z|A-Z|\']+)-([0-9]+)\)', d)[0] for d in dependlist]

    return dependlist

def getPOS(sentence):
    startdir = os.getcwd()
    parsepath = os.path.join(startdir, "stanford_tools", "stanford-postagger-2014-01-04")
    os.chdir(parsepath)
    
    
    temp_file = open('temp.txt', 'w')
    temp_file.write(sentence)
    temp_file.close()
    stanford_output = subprocess.check_output(["./stanford-postagger.sh", "models/wsj-0-18-bidirectional-nodistsim.tagger", "./temp.txt"])
    
    os.chdir(startdir)

    poslist = (stanford_output.strip(" \n")).split(" ")
    poslist = [word.split("_") for word in poslist]

    posdict = {word[0] : word[1] for word in poslist}

    return posdict

def findNE(sentence):
    startdir = os.getcwd()
    os.chdir("./stanford_tools/stanford-ner-2014-01-04/")
    
    temp_file = open('temp.txt', 'w')
    temp_file.write(sentence)
    temp_file.close()

    stanford_output = subprocess.check_output(["./ner.sh", "./temp.txt"])
    
    os.chdir(startdir)

    nelist = (stanford_output.strip(" \n")).split(" ")
    nelist = [word.split("/") for word in nelist]

    nedict = {word[0] : word[1] for word in nelist}
    
    return nedict
