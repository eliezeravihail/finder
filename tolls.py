
import os
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
