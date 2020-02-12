import pickle
def save():
     dhiraj={'key':'dhiraj','name':'dhiraj roy','age':20}
     bibek={'key':'bibek','name':'bibek yadav','age':21}
     db={}
     db['dhiraj']=dhiraj
     db['bibek']=bibek
#pickling
     file=open('xyz.txt','ab')
     pickle.dump(db,file)
     file.close()
def load():
    file=open('xyz.txt','rb')
    db=pickle.load(file)
    for keys in db:
        print(keys,':',db[keys])
    file.close()
save()
load()
