import pickle as pk


def finding(name):

    with open(r'./loaded.pkl','rb') as mki:   


        data =    list(
            filter(lambda a : a[0].split('/')[8] != name, pk.load(mki))


            )
        
        if len(data) == 0 :
            return [] 

        else: 
            return data
        

        # subash

# print(
#     finding()
# )


def uploading():
    '''
    name related to finding(name='Brindha'|'subash')
    '''
    upolader = finding("raj")

    with open('./loaded.pkl','wb') as mci:
        # print(upolader)
        if len(upolader) == 0:
            print("dosn't exist"
                  )
        else:
       
            pk.dump(
                obj=upolader,
                file=mci)
    

uploading()
        

def testing():
    with open('./bon.pkl','rb') as cvi:
        print(pk.load(cvi))


# testing()
        

def code():
    with open('./loaded.pkl','rb') as bnk:
        print(
           list (map(
                lambda a :a[0].split('/')[8] ,pk.load(bnk)
            ))
        )


code()

