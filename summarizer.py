from transformers import pipeline

# Load summarization pipeline using Hugging Face's pre-trained model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
