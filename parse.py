import subprocess
import os

def getDependencies(sentance):
    startdir = os.getcwd()
    os.chdir("./stanford_tools/stanford-parser-full-2014-01-04/")

    temp_file = open('temp.txt', 'w')
    temp_file.write(sentance)
    temp_file.close()

    stanford_output = subprocess.check_output(["./lexparser.sh", "./temp.txt"])

    os.chdir(startdir)

    print stanford_output

def getPOS(sentance):
    startdir = os.getcwd()
    os.chdir("./stanford_tools/stanford-postagger-2014-01-04/")
    
    temp_file = open('temp.txt', 'w')
    temp_file.write(sentance)
    temp_file.close()

    stanford_output = subprocess.check_output(["./stanford-postagger.sh", "models/wsj-0-18-bidirectional-nodistsim.tagger", "./temp.txt"])

    os.chdir(startdir)

    print stanford_output

def findNE(sentance):
    startdir = os.getcwd()
    os.chdir("./stanford_tools/stanford-ner-2014-01-04/")
    
    temp_file = open('temp.txt', 'w')
    temp_file.write(sentance)
    temp_file.close()

    stanford_output = subprocess.check_output(["./ner.sh", "./temp.txt"])

    os.chdir(startdir)

    print stanford_output
