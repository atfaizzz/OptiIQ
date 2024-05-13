import pandas as pd
import preprocessing
import tfidf_extraction
import keyword_extraction

def print_results(idx, keywords, df):
    print("\n=====Title=====")
    print(df['title'][idx])
    print("\n=====Abstract=====")
    print(df['abstract'][idx])
    print("\n===Keywords===")
    for k in keywords:
        print(k, keywords[k])

if __name__ == "__main__":
    df = pd.read_csv('papers.csv')
    docs = df['paper_text'].apply(lambda x: preprocessing.pre_process(x))
    cv, tfidf_matrix, feature_names = tfidf_extraction.tfidf_extraction(docs)
    idx = 941
    keywords = keyword_extraction.get_keywords(idx, docs, cv)
    print_results(idx, keywords, df)
