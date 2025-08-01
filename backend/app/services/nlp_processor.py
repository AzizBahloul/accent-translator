import re
import spacy
from app.services.dialect_registry import DIALECT_REGISTRY
from app.services.validator import validate_technical_accuracy
from app.utils.logger import logger

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def process_translation(comment: str, dialect: str, context: str = "") -> str:
    # Validate dialect
    if dialect not in DIALECT_REGISTRY:
        raise ValueError(f"Unsupported dialect: {dialect}")
    
    # Get dialect rules
    rules = DIALECT_REGISTRY[dialect]
    
    # Apply transformations
    translated = apply_transformations(comment, rules)
    
    # Preserve technical accuracy
    validated = validate_technical_accuracy(translated, context)
    
    logger.debug(f"Translated '{comment}' to '{validated}' ({dialect})")
    return validated

def apply_transformations(text: str, rules: dict) -> str:
    logger.debug(f"Original text: {text}")
    # Apply regex replacements
    for pattern, replacement in rules.get("replacements", []):
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        logger.debug(f"After regex '{pattern}': {text}")

    # Apply vocabulary mappings
    for word, replacement in rules.get("vocabulary", {}).items():
        text = re.sub(rf'\\b{word}\\b', replacement, text, flags=re.IGNORECASE)
        logger.debug(f"After vocabulary '{word}': {text}")

    # Apply syntactic patterns
    if "sentence_structure" in rules:
        text = restructure_sentences(text, rules["sentence_structure"])
        logger.debug(f"After sentence structure: {text}")

    return text

def restructure_sentences(text: str, patterns: dict) -> str:
    doc = nlp(text)
    sentences = []

    for sent in doc.sents:
        sent_text = sent.text
        # Apply preferred terms if specified in patterns
        for term in patterns.get("preferred_terms", []):
            if term in sent_text:
                logger.debug(f"Applying preferred term: {term}")
                sent_text = sent_text.replace(term, term.upper())  # Example transformation
        sentences.append(sent_text)

    return " ".join(sentences)
