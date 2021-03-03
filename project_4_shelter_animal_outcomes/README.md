# project-4-shelter-animal
project-4-shelter-animal-team-3

### Project 4: Classification of Animal Shelter Outcomes


### Problem Statement

The goal of the project is to build a classifier which will correctly predict the outcome for a shelter animal based on select characteristics of animals.
The problem is a multi-class classification with the labels being: 'Adoption', 'Return_to_owner','Transfer', 'Euthanasia', and 'Died'.

### Summary

The project  consisted of four distinct steps, each of which is documented in a separate notebook (all included in the `code` subfolder):
1. Data Cleaning
2. EDA
3. Classification

Three models were fit and scored as part of "Classification": Logistic Regression, K-Nearest Neighbors, and Random Forest Classifier.

### Data Dictionary

The independent variables used for modeling are:
- "month" (the month of the year),
- "agemths" (age of animal, in months),
- "sex" (whether the animal is male or female),
- "speutered" (whether the animal was fixed),
- "black"	(yes or no),
- "unpopular" (binary variable for several breeds which we know tend to be difficult when it comes to adoptions)

### Conclusions and Recommendations

The current model requires further work. The next steps outlined below will be performed before the model is considered "final".

---
### Next Steps

1. Apply additional estimators, e.g. Bagging Classifier, XGBoost, AdaBoost, SVM, and Voting Classifier
2. Fit and optimize hyperparameters for transformer + estimator pipelines for classifiers with highest accuracy
3. Score models and evaluate their production readiness

---
