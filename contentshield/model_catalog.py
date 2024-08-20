BINARY_CLASSIFIER = {
    "hatebert": "GroNLP/hateBERT", 
    "toxdect-roberta-large": "Xuhui/ToxDect-roberta-large", 

    # my re-trained models on Toxigen dataset, 
    "toxigen-distilbert": "", 
    "toxigen-albert": ""
}

# TODO: Re-train model on mutli-label dataset.
MULTI_CLASS_CLASSIFIER = {

}



"""
    CONFIGURATION FOR TRANSLATION MODEL
"""
TRANSLATION_CONFIG = {
    'max_new_tokens': 40, 
    'do_sample': True, 
    'top_k': 30, 
    'top_p': 0.95
}


# TODO: Collect light-weight translate model. 
TRANSLATION_MODEL = {

}