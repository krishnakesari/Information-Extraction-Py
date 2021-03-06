# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np

# Read in the data
df = pd.read_csv('~/Downloads/Amazon_Unlocked_Mobile.csv')

# Sampling data
df = df.sample(frac = 0.1, random_state = 10)
df.head()


# %%
# Dropping missing values
df.dropna(inplace= True)

# Removing Neutral ratings = 3
df = df[df['Rating'] != 3]

# Encode 4s and 5s as 1 (rated positive)
# Encode 1s and 2s as 0 (rated poorly)
df['Positively Rated'] = np.where(df['Rating'] > 3,1,0)
df.head(10)


# %%
# Most ratings are positive
df['Positively Rated'].mean() # Shows we have imbalanced review ratings


# %%
from sklearn.model_selection import train_test_split

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['Reviews'],
                                                    df['Positively Rated'],
                                                    random_state = 0)


# %%
print('X_train first entry:\n\n', X_train.iloc[0])
print('\n\nX_train shape: ', X_train.shape)


# %%
# Count Vectorizer - converting a collection of documents into matrix of word counts - It helps in building vocabulary


# %%
from sklearn.feature_extraction.text import CountVectorizer

# Converts all the letters to lower case
# Fit the count vectorizer to the training data 
vect = CountVectorizer().fit(X_train)


# %%
vect.get_feature_names()[::2000]


# %%
len(vect.get_feature_names())


# %%
# Transforms the documents in the training data to a document-term matrix
X_train_vectorized = vect.transform(X_train)
X_train_vectorized


# %%
from sklearn.linear_model import LogisticRegression

# train the model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)


# %%
from sklearn.metrics import roc_auc_score

# Predict the transformed test documents
predictions = model.predict(vect.transform(X_test))

print('AUC: ', roc_auc_score(y_test, predictions))


# %%
# Get feature names as numpy array
feature_names = np.array(vect.get_feature_names())

# Sort the coefficients from the model
sorted_coef_index = model.coef_[0].argsort()

# Find the 10 smallest and 10 largest coefficients
# The 10 largest coefficients are being indexed using [:-11:-1]

print('Smallest Coefs:\n{}\n'.format(feature_names[sorted_coef_index[:10]]))

print('Largest Coefs:\n{}'.format(feature_names[sorted_coef_index[:-11:-1]]))


# %%
# Different approach
# TFIDF - is to weight words on how important they are in the document

from sklearn.feature_extraction.text import TfidfVectorizer

# Fit Tfidf vectorizer to the training data specifying minumum document frequency
# min_df = 5 eliminates words that are not appear more than 5 documents
vect = TfidfVectorizer(min_df = 5).fit(X_train)
len(vect.get_feature_names())


# %%
X_train_vectorized = vect.transform(X_train)

model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

predictions = model.predict(vect.transform(X_test))

print('AUC: ', roc_auc_score(y_test, predictions))


# %%
feature_names = np.array(vect.get_feature_names())

sorted_tfidf_index = X_train_vectorized.max(0).toarray()[0].argsort()

print('Smallest tfidf:\n{}\n'.format(feature_names[sorted_tfidf_index[:10]]))

print('Largest tfidf:\n{}'.format(feature_names[sorted_tfidf_index[:-11:-1]]))


# %%
sorted_coef_index = model.coef_[0].argsort()

print('Smallest Coef:\n{}\n'.format(feature_names[sorted_coef_index[:10]]))

print('Largest Coef:\n{}'.format(feature_names[sorted_tfidf_index[:-11:-1]]))


# %%
# These reviews are treated the same by our current model
print(model.predict(vect.transform(['not an issue, phone is working', 'an issue, phone is not working'])))


# %%
# n - grams
## Fit count vectorizer to the training data specifying a minimum
## document frequency of 5 and extracting 1-grams and 2-grams

vect = CountVectorizer(min_df=5, ngram_range=(1,2)).fit(X_train)

X_train_vectorized = vect.transform(X_train)

len(vect.get_feature_names())


# %%
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

predictions = model.predict(vect.transform(X_test))

print('AUC: ', roc_auc_score(y_test, predictions))


# %%
feature_names = np.array(vect.get_feature_names())

sorted_coef_index = model.coef_[0].argsort()

print('Smallest Coefs :\n{}\n'.format(feature_names[sorted_coef_index[:10]]))
print('Largest Coefs: \n{}'.format(feature_names[sorted_coef_index[:-11:-1]]))


# %%
# Checking whethere these reviews are correctly identified
print(model.predict(vect.transform(['not an issue, phone is working',
                                    'an issue, phone is not working'])))

