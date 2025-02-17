# Text Analyzer

A web-based text utility application developed using **Django** that analyzes and corrects text. It detects grammatical errors, spelling mistakes, punctuation issues, and more. The tool provides users with real-time feedback and suggestions to improve their writing.

## Features

- **Text Analysis**: Identifies and highlights errors in the input text.
- **Spelling and Grammar Corrections**: Automatically corrects spelling and grammar mistakes.
- **Punctuation Check**: Detects missing or incorrect punctuation marks.
- **User-friendly Interface**: Simple and intuitive design for ease of use.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django

### Steps to Run Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/alsaif1431/Text-Analyzer.git
   cd Text-Analyzer
   ```

2. **Install dependencies**:

   It's recommended to create a virtual environment first:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

   Then install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Django server**:

   ```bash
   python manage.py runserver
   ```

4. **Access the application**:

   Once the server is running, open your browser and go to `http://127.0.0.1:8000/` to start using the tool.

## Usage

- Simply paste or type your text into the provided input box.
- The tool will automatically analyze the text and highlight any issues.
- Suggestions for corrections will be displayed, and the text will be corrected accordingly.

## Technologies Used

- **Django**: For building the web application.
- **Python**: The backend programming language.
- **HTML/CSS/JavaScript**: For frontend development.

