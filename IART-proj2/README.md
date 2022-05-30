# IART 2021/2022: Credit Card Fraud - Supervised Learning

## Team members
- Juan Bellon [201908142]
- Luísa Araújo [201904996]
- Nuno Castro [202003324]

## Checkpoint 2

Power point:

1 - Specification of the work to be performed (definition of the machine learning problem to address); <br>
2 - Related work with references to works found in a bibliographic search (articles, web pages and/or source code); <br>
3 - Description of the tools and algorithms to use in the assignment; <br>
4 - Implementation work already carried; <br>

## What to do

- An initial exploratory data analysis should be carried out (class distribution, values per attribute, and
so on).
- Evaluation metrics: performance during learning, confusion matrix, precision, recall, accuracy, F1 measure and the time
spent to train/test the models

## Steps

- Dataset analysis 
- Identification of the target concept
- Definition of the train and test sets
- Selection and parameterization of the learning algorithms to employ
- Evaluation of the learning process
- Results comparsion: Matplotlib or Seaborn

## Algorithms

- Decision Trees
- Neural Networks
- K-Nearest Neighbour Classifier
- Support Vector Machine
- Logistic Regression
- Rnadom Forest
- Naive Bayes

Note: Use Scikit-Learn Python library to compare.


## Preprocessing

### FIRST

- Integration of data from various sources
- Bringing integrated data into common format

### SECOND

- Dealing with missing data
- Remove noise
- Remove outliers 
- Dealing with duplicated data
- Remove inconsistences

### THIRD

- Feature Scaling
- Dealing with Categorical data
- Dealing with Imbalanced data
- Dimension Reduction
- Feature Engineering
- Train test split of data


## Useful packages

- RapidMiner
- WEKA
- R
- Python libraries (see below)
- SPSS
- KNIME
- SAS Enterprise Miner
- Insightful Miner

## Python libraries/packages

- NumPy
- SciPy
- MatPlotLib
- IPython
- Pandas
- scikit learn
- OpenAI Gym (for unsupervised learning i think)
- TensorFlow
- Keras
- Machine Learning Agents

## Dataset

- Distance from home (where the transaction happened)
- Distance from the last transaction
- Ratio of purchased pirce to median purchased price
- Repeat Retailer (Bought from that retailer before)
- Used chip (used credit card)
- Used pin (used pin number)
- Online order
- Fraud
