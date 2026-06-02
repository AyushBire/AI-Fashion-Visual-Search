import pickle
import numpy as np
import faiss

from feature_extractor import extract_features

with open("embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

with open("image_paths.pkl", "rb") as f:
    image_paths = pickle.load(f)


embeddings = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

print(f"FAISS Index Created with {index.ntotal} images")


def find_similar_images(query_image_path, k=5):
    """
    Returns k most similar images
    """


    query_features = extract_features(query_image_path)

    query_features = np.array([query_features]).astype("float32")

    distances, indices = index.search(query_features, k)

    results = []

    for i, idx in enumerate(indices[0]):
        results.append({
            "image_path": image_paths[idx],
            "distance": float(distances[0][i])
        })

    return results


if __name__ == "__main__":

    query_image = "dataset/shirt_1.jpg"  # change according to your image name

    results = find_similar_images(query_image)

    print("\nTop Similar Images:\n")

    for result in results:
        print(result["image_path"])