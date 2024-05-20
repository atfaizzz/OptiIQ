# OptiIQ (Keyword Extraction - NLP Model)

OptiIQ is a keyword extraction project using the TF-IDF algorithm. This project demonstrates how to extract keywords from textual data, such as research papers, using NLP techniques. This repository contains a set of scripts to preprocess text from research papers, compute TF-IDF scores, and extract keywords. The primary goal is to identify significant keywords from the text of academic papers.

## Files in the Repository

1. **preprocessing.py**: Handles text preprocessing tasks such as cleaning, tokenizing, and lemmatizing.
2. **tfidf_extraction.py**: Computes the TF-IDF matrix from the preprocessed text documents.
3. **keyword_extraction.py**: Extracts keywords from the TF-IDF matrix for a given document.
4. **main.py**: The main script that orchestrates the entire keyword extraction process, from reading the CSV file to printing the extracted keywords.
5. **papers.csv**: Contains the dataset of research papers, including fields like 'title', 'abstract', and 'paper_text'.
6. **paper_authors.csv**: For Reference
7. **authors.csv**: For Reference


## Output:
The output of this process includes the top keywords extracted from the document in the dataset, along with their TF-IDF scores. 
These keywords represent the most important terms in each document and can be used for various purposes such as document summarization, content categorization, and information retrieval.

## Using it as an SEO Model:
This keyword extraction model can be used for SEO purposes by adapting it to analyze web page content in the following proposed steps:
1) Web Scraping: Collecting textual content from web pages using a web scraper.
2) Preprocessing: Cleaning the collected text data by removing HTML tags, special characters, and stopwords.
3) Keyword Extraction: Applying the keyword extraction model to extract important keywords and phrases from the web page content.
4) SEO Analysis: Utilizing the extracted keywords to optimize various SEO elements such as meta tags.
5) Content Optimization: Optimizing the web page content based on the extracted keywords to improve its relevance and visibility in search engine results.
6) Monitoring: Continuously monitoring the SEO performance of the web page and iterating on the keyword extraction and content optimization process to enhance SEO effectiveness over time.
