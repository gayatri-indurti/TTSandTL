
from tkinter import *

from googletrans import Translator

from gtts import gTTS
import os

#basic interface

root = Tk()

root.title("Translator and TTS")

root.geometry("400x400")

translator = Translator()


#Translator and TTS heading

mylabel=Label(root,text="Translator and TTS")
mylabel.pack()


mylabel1 = Label (root, text= "Enter what needs to be Translated:")
mylabel1.pack()

e = Entry(root, width=30)
e.pack()
e.insert(0, "Enter text")

mylabel=Label(root,text="                   ")
mylabel.pack()



options = [
"am",
"ar",
"eu",
"bn",
"en",
"pt",
"bg",
"ca",
"chr",
"hr",
"cs",
"da",
"nl",
"et",
"fil",
"fi",
"fr",
"de",
"el",
"gu",
"iw",
"hi",
"hu",
"is",
"id",
"it",
"ja",
"kn",
"ko",
"lv",
"lt",
"ms",
"ml",
"mr",
"no",
"pl",
"ro",
"ru",
"sr",
"zh-CN",
"sk",
"sl",
"es",
"sw",
"sv",
"ta",
"te",
"th",
"zh-TW",
"tr",
"ur",
"uk",
"vi",
"cy",
]

clicked = StringVar()

clicked.set("The language entered to be translated is?")

drop = OptionMenu(root, clicked, *options)
drop.pack()

e1 = Entry(root, text=clicked)
e1.pack()
e1.config(state=DISABLED)



mylabel=Label(root,text="                  ")
mylabel.pack()



options1 = [
"am",
"ar",
"eu",
"bn",
"en",
"pt",
"bg",
"ca",
"chr",
"hr",
"cs",
"da",
"nl",
"et",
"fil",
"fi",
"fr",
"de",
"el",
"gu",
"iw",
"hi",
"hu",
"is",
"id",
"it",
"ja",
"kn",
"ko",
"lv",
"lt",
"ms",
"ml",
"mr",
"no",
"pl",
"ro",
"ru",
"sr",
"zh-CN",
"sk",
"sl",
"es",
"sw",
"sv",
"ta",
"te",
"th",
"zh-TW",
"tr",
"ur",
"uk",
"vi",
"cy",
]

clicked1 = StringVar()

clicked1.set("Enter the language to be translated to:")

drop = OptionMenu(root, clicked1, *options1)
drop.pack()

e2 = Entry(root, text=clicked1)
e2.pack()
e2.config(state=DISABLED)


mylabel=Label(root,text="                  ")
mylabel.pack()



def myclick2():
   sentence = e.get()
   lang1=e1.get()
   lang2=e2.get()

   translated_sentence = translator.translate(sentence, src=lang1, dest=lang2)

   mytext = translated_sentence.text
   mylabel=Label(root,text= mytext)
   mylabel.pack()

myButton=Button(root,text="Translated text",command=myclick2)
myButton.pack()


mylabel=Label(root,text="                            ")
mylabel.pack()


def myclick3():
   sentence = e.get()
   lang1 = e1.get()
   lang2 = e2.get()

   translated_sentence = translator.translate(sentence, src=lang1, dest=lang2)
   mytext = translated_sentence.text

   output = gTTS(text=mytext, lang=lang2, slow=False)

   output.save("output.mp3")

   os.system("start output.mp3")

myButton=Button(root,text="Output in speech format",command=myclick3)
myButton.pack()

mylabel=Label(root,text="                            ")
mylabel.pack()


def clicker():
   global pop
   pop = Toplevel(root)
   pop.title("List of Languages")
   pop.geometry("300x300")


   my_frame = Frame(pop)
   my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)


   my_listbox = Listbox(my_frame,yscrollcommand = my_scrollbar.set)

   my_scrollbar.config(command= my_listbox.yview)
   my_scrollbar.pack(side=RIGHT, fill=Y)
   my_frame.pack()

   my_listbox.pack(pady=50,padx=30)



   my_list = [
       "Amharic:am",
       "Arabic:ar",
       "Basqu:eu",
       "Bengali:bn",
       "English:en",
       "Portuguese (Brazil):pt",
       "Bulgarian:    bg",
       "Catalan:  ca",
       "Cherokee: chr",
       "Croatian: hr",
       "Czech:    cs",
       "Danish:   da",
       "Dutch:    nl",
       "Estonian: et",
       "Filipino: fil",
       "Finnish:  fi",
       "French:   fr",
       "German:   de",
       "Greek:    el",
       "Gujarati: gu",
       "Hebrew:   iw",
       "Hindi:    hi",
       "Hungarian:    hu",
       "Icelandic:    is",
       "Indonesian:   id",
       "Italian:  it",
       "Japanese: ja",
       "Kannada:  kn",
       "Korean:   ko",
       "Latvian:  lv",
       "Lithuanian:   lt",
       "Malay:    ms",
       "Malayalam:    ml",
       "Marathi:  mr",
       "Norwegian:    no",
       "Polish:   pl",
       "Romanian: ro",
       "Russian:  ru",
       "Serbian:  sr",
       "Chinese (PRC):    zh-CN",
       "Slovak:   sk",
       "Slovenian:    sl",
       "Spanish:  es",
       "Swahili:  sw",
       "Swedish:  sv",
       "Tamil:    ta",
       "Telugu:   te",
       "Thai:th",
       "Chinese (Taiwan):zh-TW",
       "Turkish:tr",
       "Urdu:ur",
       "Ukrainian:uk",
       "Vietnamese:vi",
       "Welsh:cy"
   ]



   for item in my_list:
       my_listbox.insert ("end", item)

my_button = Button(root, text="Help!", command=clicker)
my_button.pack()

button_quit = Button(root, text="Exit program", command= root.quit)
button_quit.pack()


root.mainloop()

