from tkinter import *
from tkinter import filedialog


import nltk
from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
stemmer=PorterStemmer()



class clean:
    def openFile(self):
        self.tf = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/", 
            title="Open Text file", 
            filetypes=(("text Files", "*.txt"),)
            )
        self.temp=self.tf
        pathh.insert(END, self.temp)
        self.temp = open(self.temp)  
        data = self.temp.read()
        txtarea.insert(END, data)
        


    def clean_space(self):
        file = open(self.tf)
        z=("")
        for i in file:
            cleaned_string = " ".join(i.split())
            print(cleaned_string)

    def upper(self):
        file = open(self.tf)
        for i in file:
            file1=i.upper()
            print(file1)
    
                         
    def lower(self):
        file = open(self.tf)
        for i in file:
            file1=i.lower()
            print(file1)
            
    def tokenize(self):
        file = open(self.tf)
        for i in file:
         tokens = word_tokenize(i)
         print(tokens)

    def staming(self):
        file = open(self.tf)
        words = file.read()
        s = words.split()
        for word in s:
            print(word, "; ",stemmer.stem(word))

    def mapping(self):
        file = open(self.tf)
        x = file.read()
        y = x.split()
        for name in list(map(lambda text: f"- {text.strip().capitalize()} -", y)):
            print(name)
x = clean()

root = Tk()
root.title(" clean ")
bu1=Button(root,text="clean space",command=x.clean_space)
bu1.pack()

bu2=Button(root,text="upper",command=x.upper)
bu2.pack()

bu3=Button(root,text="lower",command=x.lower)
bu3.pack()

bu4=Button(root,text="tokenize",command=x.tokenize)
bu4.pack()



bu6=Button(root,text="Staming",command=x.staming)
bu6.pack()

bu7=Button(root,text="Mapping",command=x.mapping)
bu7.pack()





ws = Tk()
ws.title("Txt File")
ws.geometry("400x400")
ws['bg']='#fb0'

txtarea = Text(ws, width=30, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



Button(
    ws, 
    text="Open File", 
    command=x.openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)





root.mainloop()