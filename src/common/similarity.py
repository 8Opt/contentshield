"""Sentence-BERT for evaluate semantic similarity"""

from sentence_transformers import SentenceTransformer, util

bert_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)  # Use a lightweight sentence-transformer


def get_bert_similarity(response, ground_truth):
    # Encode the query and text
    query_embedding = bert_model.encode(response, convert_to_tensor=True)
    text_embedding = bert_model.encode(ground_truth, convert_to_tensor=True)

    # Compute the cosine similarity between the query and text
    cosine_score = util.pytorch_cos_sim(query_embedding, text_embedding)

    return cosine_score.item()
