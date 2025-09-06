from datasets import load_dataset

def load_sentiment_data():
    # Example: IMDb movie reviews for sentiment
    return load_dataset("imdb")

def load_spiritual_texts():
    # You can curate your own later—for now, we mock it
    spiritual_samples = [
        "The soul always knows what to do to heal itself.",
        "Be mindful of the space between thoughts.",
        "Where there is light, there can be no fear."
    ]
    return spiritual_samples

if __name__ == "__main__":
    print("Loading sentiment data...")
    print(load_sentiment_data())
    
    print("\nLoading spiritual texts...")
    print(load_spiritual_texts())