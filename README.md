# Adjective Frequency Counter

A Python NLP tool for counting adjective frequency in selected NLTK corpus texts.

## Overview

This project uses NLTK part-of-speech tagging to identify adjectives in a selected corpus text and count how often each adjective appears.

The script lets the user choose a built-in NLTK corpus, select a text from that corpus, extract adjective tokens, and export adjective frequency results to a text file.

## Features

- Lists available NLTK corpora
- Lets the user choose a corpus and file
- Tokenizes and POS-tags text with NLTK
- Extracts standard, comparative, and superlative adjectives
- Counts total and unique adjective frequencies
- Exports results to a text file

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```
Download required NLTK data:
```python
import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("brown")
nltk.download("gutenberg")
nltk.download("inaugural")
nltk.download("reuters")
nltk.download("webtext")
```
## How to Run
```bash
python adjective_frequency_counter.py
```
You will be prompted to:
1. Choose a corpus
2. Choose a file from that corpus
3. Enter an output filename
### Example Output
```
Corpus: gutenberg
File: austen-emma.txt
Total adjectives: 1250
Unique adjectives: 438

Most common adjectives:
good: 42
little: 38
great: 31
young: 29
```
## Skills Demonstrated
* Python scripting
* Natural language processing
* Corpus analysis
* Part-of-speech tagging
* Frequency analysis
* Text file export

## Future Improvements
* Add command-line arguments
* Export results as CSV
* Normalize adjective counts per 1,000 words
* Compare adjective frequency across multiple texts
* Visualize the most frequent adjectives
