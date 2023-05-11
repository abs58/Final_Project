import pickle

file = [0,False]

def save(room,key): 
    with open('save.pickle', 'wb') as f:
        file[0] = room
        file[1] = key
        pickle.dump(file, f)
        print("Saved!")
def load():
    with open('save.pickle', 'rb') as f:
        file = pickle.load(f)
        return file