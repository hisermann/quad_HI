import numpy as np

def getTrajectory(filename):
    obj = np.load(filename, allow_pickle=True)
    return obj

def populateNamespace(obj):
    for key in obj.keys():
        globals().update({key: obj[key]})
        print(f'Loaded {key}')

if __name__ == '__main__':
    populateNamespace(getTrajectory('results.pkl'))
