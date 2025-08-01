# Accent Translator

## Overview
Accent Translator is a powerful tool designed to translate text into various dialects and accents. It features a FastAPI backend for processing translations and a VS Code extension for seamless integration into your development workflow.

## Features
- Translate text into dialects like British, Australian, Pirate, and more.
- Modular backend with support for adding new dialects.
- VS Code extension for translating comments directly in your code.
- Configurable and extensible architecture.

## Installation

### Backend
1. Clone the repository:
   ```bash
   git clone https://github.com/AzizBahloul/accent-translator.git
   cd accent-translator/backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend (VS Code Extension)
1. Navigate to the `frontend` directory:
   ```bash
   cd ../frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Compile the extension:
   ```bash
   npm run compile
   ```
4. Launch the extension in VS Code:
   - Open the `frontend` folder in VS Code.
   - Press `F5` to start a new Extension Development Host.

## Usage

### Backend API
- **Endpoint**: `/translate`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "comment": "The color of the center is optimized for visibility.",
    "dialect": "british",
    "context": "design discussion"
  }
  ```
- **Response**:
  ```json
  {
    "translated_comment": "The colour of the centre is optimised for visibility."
  }
  ```

### VS Code Extension
1. Open a file in VS Code.
2. Select the text you want to translate.
3. Use the command palette (`Ctrl+Shift+P`) and run `Accent Translator: Translate Comments`.
4. Choose a dialect from the list.

## Adding New Dialects
1. Create a new JSON file in `backend/data/dialect_mappings`.
2. Define the vocabulary, replacements, and sentence structure rules. Example:
   ```json
   {
       "vocabulary": {
           "hello": "howdy"
       },
       "replacements": [
           ["\\bcolor\\b", "colour"]
       ],
       "sentence_structure": {
           "preferred_terms": ["y'all"]
       }
   }
   ```
3. Restart the backend server to load the new dialect.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework.
- [VS Code API](https://code.visualstudio.com/api) for the extension development.
- [spaCy](https://spacy.io/) for NLP processing.