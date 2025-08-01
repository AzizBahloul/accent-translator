import ast
import tokenize
from io import BytesIO

def validate_technical_accuracy(translated_comment: str, context: str) -> str:
    """Ensure technical terms remain accurate"""
    # 1. Preserve code identifiers
    preserved_terms = extract_code_identifiers(context)
    
    for term in preserved_terms:
        translated_comment = translated_comment.replace(term, f"@@{term}@@")
    
    # 2. Validate against technical dictionary
    technical_terms = ["API", "HTTP", "SQL", "JSON"]
    for term in technical_terms:
        if term.lower() in translated_comment.lower():
            translated_comment = translated_comment.replace(term.lower(), term)
    
    # 3. Restore preserved terms
    for term in preserved_terms:
        translated_comment = translated_comment.replace(f"@@{term}@@", term)
    
    return translated_comment

def extract_code_identifiers(code: str) -> set:
    """Parse code to extract variable/function names"""
    if not code:
        return set()
    
    try:
        tree = ast.parse(code)
        identifiers = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                identifiers.add(node.id)
            elif isinstance(node, ast.FunctionDef):
                identifiers.add(node.name)
        return identifiers
    except:
        # Fallback to token-based extraction
        try:
            tokens = tokenize.tokenize(BytesIO(code.encode('utf-8')).readline)
            return {tok.string for tok in tokens if tok.type == tokenize.NAME}
        except:
            return set()
