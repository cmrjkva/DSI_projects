# Project 2 - Ames Housing Data and Kaggle Challenge

Welcome to Project 2! Let's model!

**Primary Learning Objectives:**
1. Creating and iteratively refining a regression model.
2. Using [Kaggle](https://www.kaggle.com/t/ff32f6689d5b45aeb23d1441122b7761) to practice the modeling process.
3. Providing business insights through reporting and presentation.

You are tasked with creating a machine learning model based on the Ames Housing Dataset. This model will predict the price of a house at sale.

The Ames Housing Dataset is contains over 70 columns of different features relating to houses.

---
## Deliverables 

- We are hosting a competition on Kaggle to give you the opportunity to practice your modeling skills. You must upload at least one of your model's predictions to the competition.
- You will submit a technical report and a presentation in your submission Repo. 
- You will present your findings to your classmates and instructors.

**You may find that the best model for Kaggle is not the best model to address your data science problem.**


## Set up

Before you begin working on this project, please do the following:

1. Sign up for an account on [Kaggle](https://www.kaggle.com/)
2. **IMPORTANT**: Click here: [Regression Challenge Sign Up](https://www.kaggle.com/c/dsir-1116-regression-challenge/) to **join** the competition (otherwise you will not be able to make submissions!)
3. Review the material on the Kaggle challenge site.
4. Review the [data description](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt).

## The Modeling Process

1. The train dataset has all of the columns that you will need to generate and refine your models. The test dataset has all of those columns except for the target that you are trying to predict in your Regression model.
2. Generate your regression model using the training data. We expect that within this process, you'll be making use of:
    - train-test split
    - cross-validation / grid searching for hyperparameters
    - strong exploratory data analysis to question correlation and relationship across predictive variables
    - code that reproducibly and consistently applies feature transformation (such as the preprocessing library)
3. Predict the values for your target column in the test dataset and submit your predictions to Kaggle to see how your model does against unknown data.
    - **Note**: Kaggle expects to see your submissions in a specific format. Check the challenge's page to make sure you are formatting your CSVs correctly!
    - **You are limited to models you've learned in class**. In other words, you cannot use XGBoost, Neural Networks or any other more advanced model for this project.
4. Evaluate your models!
    - consider your evaluation metrics
    - consider your baseline score
    - how can your model be used for inference?
    - why do you believe your model will generalize to new data?

## Submission

- Presentation will be delivered starting at 0900 on **Monday 14 December**. 
- Your technical report must be submitted in your submission repository by 23:59 on **Monday 14 December**.
- The Kaggle competition will close by midnight **Monday 14 December**.

Your technical report must include:

- A README.md (that isn't this file)
- Jupyter notebook(s) with your analysis and models (renamed to describe your project)
- Data files
- Presentation slides
- Any other necessary files (images, etc.)


---

## Presentation Structure

- **Must be within time limit established by local instructor.**
- Use Google Slides or some other presentation system (Keynote, Powerpoint, etc).
- Consider your audience. 
- Start with the **problem** you are solving.
- Use visuals that are appropriately scaled and interpretable.
- Talk about your procedure/methodology (high level).
- Talk about your primary findings.
- Make sure you provide **clear recommendations** that follow logically from your analyses and narrative and answer your data science problem.

Be sure to rehearse and time your presentation before class.

---

## Rubric
Your local instructor will evaluate your project (for the most part) using the following criteria.  You should make sure that you consider and/or follow most if not all of the considerations/recommendations outlined below **while** working through your project.

**Scores will be out of 27 points based on the 9 items in the rubric.** <br>
*3 points per section*<br>

| Score | Interpretation |
| --- | --- |
| **0** | *Project fails to meet the minimum requirements for this item.* |
| **1** | *Project meets the minimum requirements for this item, but falls significantly short of portfolio-ready expectations.* |
| **2** | *Project exceeds the minimum requirements for this item, but falls short of portfolio-ready expectations.* |
| **3** | *Project meets or exceeds portfolio-ready expectations; demonstrates a thorough understanding of every outlined consideration.* |

### The Data Science Process

**Problem Statement**
- Is it clear?
- Is it reasonable?
- Is the audience clearly identified?

**Data Cleaning and EDA**
- Are missing values dealt with?
- Are important distributions examined and described?
- Are outliers identified and addressed?
- Are appropriate summary statistics provided?
- Are possible modeling insights to investigate discussed?

**Preprocessing and Modeling**
- Are categorical variables one-hot encoded or encoded in another logical way?
- Are features engineered?
- Have the data been scaled appropriately?
- Does the student properly split the data for validation/training purposes?
- Does the student use feature selection to remove noisy or multi-collinear features?
- Does the student test and evaluate a variety of model types (**AT MINIMUM:** linear regression, lasso, and ridge)?
- Does the student defend their choice of the best model for this data and problem statement?
- Does the student explain how the model works and evaluate its performance successes/downfalls?

**Evaluation and Conceptual Understanding**
- Does the student accurately identify and explain the baseline score?
- Does the student select and use metrics relevant to the problem statement?
- Is more than one metric uses to better assess performance?
- Does the student correctly interpret the results of their model for purposes of inference?

**Conclusion and Recommendations**
- Are the conclusions/recommendations clearly stated?
- Does the conclusion answer the original problem statement?
- Is it clear how the final recommendations were reached? Do they follow logically?
- Does the student address how their suggestions will likely benefit stakeholders?
- Are future steps to move the project forward identified?

### Organization and Professionalism

**Project Organization**
- Are modules imported correctly (using appropriate aliases)?
- Are data imported/saved using relative paths (so someone can replicate your analysis)?
- Does the README provide a good executive summary of the project?
- Is Markdown formatting and comments used appropriately to communicate in the notebooks?
- Are files & directories organized?
- Are unnecessary files included?
- Do files and directories have well-structured, appropriate, consistent names?

**Visualizations**
- Are sufficient helpful visualizations provided?
- Are plots labeled properly?
- Are plots interpreted appropriately?
- Are plots formatted and scaled appropriately for inclusion in a notebook-based technical report?

**Python Syntax and Control Flow**
- Is care taken to write human readable code?
- Is the code syntactically correct (no runtime errors)?
- Does the code generate desired results (logically correct)?
- Does the code follow general best practices?

**Presentation**
- Is the problem statement clearly presented?
- Does the body of the presentation building address the problem statement and lead to the conclusion?
- Is the conclusion/recommendations clearly stated?
- Is the level of technicality appropriate for the intended audience?
- Does the student deliver their message clearly?
- Are appropriate visualizations generated for the intended audience?
- Are visualizations useful for supporting conclusions/explaining findings?

In order to pass the project, students must earn a minimum score of 1 for each category.
- Earning below a 1 in one or more of the above categories would result in a failing project.
- While a minimum of 1 in each category is the required threshold for graduation, students should aim to earn at least an average of 1.5 across each category. An average score below 1.5, while it may be passing, means students may want to solicit specific feedback in order to significantly improve the project before showcasing it as part of a portfolio or the job search.

### REMEMBER:

This is a learning environment and you are encouraged to try new things, even if they don't work out as well as you planned! While this rubric outlines what we look for in a _good_ project, it is up to you to go above and beyond to create a _great_ project. **Learn from your failures and you'll grow!**
