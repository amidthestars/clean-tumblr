import io, json, sys, os, random
from tqdm import tqdm

def cleanhtml(s):
    s = s.replace("<p>", "")
    s = s.replace("</p>", "")
    if "&ldquo;" in s:
        s = s.replace("&ldquo;", '"')
    if "&rdquo;" in s:
        s = s.replace("&rdquo;", '"')
    if "&rsquo;" in s:
        s = s.replace("&rsquo;", "'")
    if "&hellip;" in s:
        s = s.replace("&hellip;", "...")
    if "<br/>" in s:
        s = s.replace("<br/>", "")
    if "\n\n" in s:
        s = s.replace("\n\n", "")
    if "&amp;" in s:
        s = s.replace("&amp;", "&")
    return s

folderpath = sys.argv[1] # folder path argument comes first
outputname = sys.argv[2] # then it's the output file name (add the prefix, like .txt)

dirs = os.listdir(folderpath) #this is only the names of the files though. will be accounted for later
outputf = io.open(outputname, mode = 'w',  encoding="utf-8") #the output file
messageArray = []
newLine = []
for onefile in tqdm(dirs, desc= "Cleaning"):
    if onefile.endswith('.json'): #cycle through the files
        whole_file = json.load(io.open(folderpath + "/" + onefile, mode="r", encoding="utf-8")) #load that json file (directory kinda hardcoded accounted for)
        for i in range(len(whole_file)): #json is a dict now. we only want the things from the "messages" portion
            if "href" in whole_file[i]:
                pass
            else:
                cleanedText = cleanhtml(whole_file[i])
                messageArray.append(cleanedText)
        

print(len(messageArray))
outputf.write("\n".join(messageArray)) #file writing time
'''
for i in tqdm(range(len(messageArray)), desc="Extracting fields"):
    newString = messageArray[i].replace('\\n','\n')
    outputf.write("\n"+"\n".join(extract_fields(newString))) #a Heckin' Chonker of an array
'''
#random.shuffle(messageArray) #randomization time
#print("Shuffling done.")
outputf.close()
