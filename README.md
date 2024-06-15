Interview Response Analysis
This Python script analyzes interview responses to provide sentiment analysis, key phrase extraction, and quality assessment based on expected key phrases.

Dependencies
Python 3.x
spaCy (v3.x recommended)
TextBlob
Install dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Usage
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/interview-response-analysis.git
cd interview-response-analysis
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Prepare input files:

Place your interview responses in sample_responses.txt.
Define expected key phrases in expected_key_phrases.txt.
Run the script:

bash
Copy code
python interview_analysis.py
Follow the prompts:

Choose whether to read responses from sample_responses.txt or enter them manually.
Enter responses manually if selected, type 'done' to finish.
View analysis results:

Sentiment analysis (Positive, Negative, Neutral).
Extracted key phrases.
Matched key phrases with expected key phrases.
Quality assessment (High, Moderate, Low) based on key phrase relevance.
Example Output
vbnet
Copy code
Response 1:
Text: (Your interview response text)
Sentiment: Positive
Extracted Key Phrases: ['key', 'phrases', 'extracted']
Matched Key Phrases: ['matched', 'key', 'phrases']
Total Relevance: 0.50
Quality: High

Final Quality Counts:
High: 2
Moderate: 1
Low: 0
Contributing
Contributions are welcome! If you have suggestions, open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
