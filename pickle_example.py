import pickle

parking_space = [[[],[]],[[],[]],[[],[]],[[],[]]]
f = open("test.pkl", "wb")
pickle.dump(parking_space, f)