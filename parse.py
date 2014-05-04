import subprocess
import os
import nltk
import re
import fcntl
import time

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

class syntaxParser:

    def __init__(self, ner_socket, pos_socket, servers_running):
        self.NERhasrun = 0

        pos_path = os.path.join("./", "stanford_tools", "stanford-postagger-2014-01-04")
        ner_path = os.path.join("./", "stanford_tools", "stanford-ner-2014-01-04")
        parse_path = os.path.join("./", "stanford_tools", "stanford-parser-full-2014-01-04")

        parse_command = "java -mx150m -cp " + os.path.join(parse_path, "stanford-parser.jar") + " edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat \"penn,typedDependencies\" -sentences newline " + os.path.join(parse_path, "englishPCFG.ser.gz") + " -"
        self.parse_process = subprocess.Popen(parse_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

        if not servers_running:
            ner_server_command = "java -mx500m -cp " + os.path.join(ner_path, "stanford-ner.jar") + " edu.stanford.nlp.ie.NERServer -port " + str(ner_socket) + " -loadClassifier " + os.path.join(ner_path, "classifiers", "english.all.3class.distsim.crf.ser.gz")
            self.ner_server = subprocess.Popen(ner_server_command, shell=True)
        ner_command = "java -cp " + os.path.join(ner_path, "stanford-ner.jar") + " edu.stanford.nlp.ie.NERServer -port " + str(ner_socket) + " -client"
        self.ner_process = subprocess.Popen(ner_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

        if not servers_running:
            pos_server_command = "java -mx300m -cp " + os.path.join(pos_path, "stanford-postagger.jar") + " edu.stanford.nlp.tagger.maxent.MaxentTaggerServer -model " + os.path.join(pos_path, "models", "wsj-0-18-bidirectional-nodistsim.tagger") + " -port " + str(pos_socket)
            self.pos_server = subprocess.Popen(pos_server_command, shell=True)
        pos_command = "java -cp " + os.path.join(pos_path, "stanford-postagger.jar") + " edu.stanford.nlp.tagger.maxent.MaxentTaggerServer -client -port " + str(pos_socket)
        self.pos_process = subprocess.Popen(pos_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

        fcntl.fcntl(self.parse_process.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)
        fcntl.fcntl(self.pos_process.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)
        fcntl.fcntl(self.ner_process.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)

    def analyzeSentence(self, sentence):

        if sentence[-1] != "\n":
            sentence += "\n"

        analysis = []
        posdict = self.getPOS(sentence)
        nedict = self.findNE(sentence)

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

        dependlist = self.getDependencies(sentence)

        for d in dependlist:
            parentnum = int(d[2]) - 1
            childnum = int(d[4]) - 1
            if parentnum > -1:
                analysis[parentnum].dependencies[d[0]] = analysis[childnum]

        return analysis

    def getDependencies(self, sentence):

        if sentence[-1] != "\n":
            sentence += "\n"

        stanford_output = ""
        self.parse_process.stdout.flush()
        self.parse_process.stdin.write(sentence)
        time.sleep(1)
        try:
            stanford_output = self.parse_process.stdout.read()
        except IOError:
            pass
        
        dependlist = [d for d in stanford_output.split("\n") if len(d) > 0 and d[0].islower()]
        dependlist = [re.findall('([a-z]+)\(([a-z|A-Z|0-9|\']+)-([0-9]+), ([a-z|A-Z|0-9|\']+)-([0-9]+)\)', d)[0] for d in dependlist]

        return dependlist

    def getPOS(self, sentence):

        if sentence[-1] != "\n":
            sentence += "\n"

        stanford_output = ""
        self.pos_process.stdout.flush()
        self.pos_process.stdin.write(sentence)
        time.sleep(1)
        try:
            stanford_output = self.pos_process.stdout.read()
        except IOError:
            pass

        print stanford_output

        poslist = (stanford_output.strip(" \n")).split(" ")
        poslist = [word.split("_") for word in poslist]

        posdict = {word[0] : word[1] for word in poslist}

        return posdict

    def findNE(self, sentence):

        if sentence[-1] != "\n":
            sentence += "\n"

        stanford_output = ""
        if not self.NERhasrun:
            try:
                stanford_output = self.ner_process.stdout.read()
            except IOError:
                pass
            
        self.ner_process.stdout.flush()
        self.ner_process.stdin.write(sentence)
        time.sleep(1)
        try:
            stanford_output = self.ner_process.stdout.read()
        except IOError:
            pass

        nelist = (stanford_output.strip(" \n")).split(" ")
        nelist = [word.split("/") for word in nelist]

        nedict = {word[0] : word[1] for word in nelist}

        return nedict
