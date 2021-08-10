
import os
def gimatrya(word:str)->set:
  gimHash = dict()
  gimHash["א"]="1"
  gimHash["ב"]="2"
  gimHash["ג"]="3"
  gimHash["ד"]="4"
  gimHash["ה"]="5"
  gimHash["ו"]="6"
  gimHash["ז"]="7"
  gimHash["ח"]="8"
  gimHash["ט"]="9"
  gimHash["י"]="10"
  gimHash["כ"]="20"
  gimHash["ל"]="30"
  gimHash["מ"]="40"
  gimHash["נ"]="50"
  gimHash["ס"]="60"
  gimHash["ע"]="70"
  gimHash["פ"]="80"
  gimHash["צ"]="90"
  gimHash["ק"]="100"
  gimHash["ר"]="200"
  gimHash["ש"]="300"
  gimHash["ת"]="400"
  gimHash["ך"]="500"
  gimHash["ם"]="600"
  gimHash["ן"]="700"
  gimHash["ף"]="800"
  gimHash["ץ"]="900"
  chars = list(word)
  return {gimHash[x] for x in chars}
    
def classesbyWord(word:str, classes:dict):
  gimclasses = gimatrya(word)
  return set([str(classIndex[x]) for x in gimclasses])

def detectWord(word):
  # word = list(word)
  # word.reverse()
  # word = "".join(word)
  #reset memory and detect:
  treshold = 0.9
  myweights = "/content/drive/MyDrive/finishProject/Allweights/Char1000_good_result_on_alfabeta/last.pt"
  myclasses = " ".join(classesbyWord(word,classIndex))
  command = f"\
  python detect.py\
    --save-txt\
    --conf-thres {treshold}\
    --line-thickness 1\
    --source /content/drive/MyDrive/finishProject/Allweights/tanya5.jpg\
    --img 2000\
    --weights {myweights}\
    --classes {myclasses}\
    --word {word}"

  os.system(command)


!rm -rf runs/detect
detectWord("אחד")
Image(filename='runs/detect/exp/tanya5.jpg', width=800)
