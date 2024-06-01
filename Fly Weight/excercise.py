
class Sentence:
    def __init__(self, plain_text):
        self.plain_text=plain_text
        self.formatting=[self.WordToken() for i in range(len(self.plain_text.split(' ')))]

    class WordToken:
        def __init__(self):
            self.capitalize=False
       
    def __str__(self):
        result=self.plain_text.split(' ')
        for i in range(len(result)):
            if self.formatting[i].capitalize==True:
                result[i]=result[i].upper()
        return " ".join(result)
    
    def __getitem__(self,index):
        return self.formatting[index]
    
        


sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)  
    