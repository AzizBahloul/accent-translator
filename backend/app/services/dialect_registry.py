import json
import logging
from pathlib import Path

DIALECT_REGISTRY = {}

# Initialize logger
logger = logging.getLogger("dialect_registry")

# Load dialect mappings
data_dir = Path(__file__).parent.parent.parent / "data" / "dialect_mappings"

# Load dialect mappings with error handling
for file_path in data_dir.glob("*.json"):
    dialect_name = file_path.stem
    try:
        with open(file_path, 'r') as f:
            DIALECT_REGISTRY[dialect_name] = json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Malformed JSON in {file_path}: {e}")
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")

# Example: data/dialect_mappings/british.json
"""
{
    "vocabulary": {
        "color": "colour",
        "optimize": "optimise",
        "center": "centre"
    },
    "replacements": [
        [r"\b([A-Za-z]+)ize\b", "\\1ise"],
        [r"\b([A-Za-z]+)yze\b", "\\1yse"]
    ],
    "sentence_structure": {
        "preferred_terms": ["brilliant", "lovely", "cheers"]
    }
}
"""
