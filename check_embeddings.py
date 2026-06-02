import pickle

with open("image_paths.pkl", "rb") as f:
    image_paths = pickle.load(f)

print("Total Images:", len(image_paths))
print(image_paths[:5])