import os
import pickle
from feature_extractor import extract_features

dataset_folder = "dataset"

embeddings = []
image_paths = []

for filename in os.listdir(dataset_folder):

    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):

        img_path = os.path.join(dataset_folder, filename)

        try:
            features = extract_features(img_path)

            embeddings.append(features)
            image_paths.append(img_path)

            print(f"Processed: {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

with open("embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

with open("image_paths.pkl", "wb") as f:
    pickle.dump(image_paths, f)

print("\nEmbeddings saved successfully!")
print(f"Total images processed: {len(image_paths)}")