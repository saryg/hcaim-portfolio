# Student Performance - Statistical Analysis

Does drinking more during the week actually hurt your grades? Does having family support at home make a difference? Does free time help, and does that depend on whether you're male or female?

This project investigates data from secondary school students in Portugal across Maths and Portuguese subjects. The dataset includes grades, demographic information, and self-reported lifestyle variables.

Findings were mixed, but much can be learned about a dataset through exploration. Knowing that family support doesn't predict grades, or that family size can't be read from a final grade, is a finding in itself.

---

## Notebooks

### [a1 — Analysis Design](a1_analysis_design.ipynb)

Defines five hypotheses before touching the data and evaluates threats to validity upfront. Worth noting: the sample is two schools in one region of Portugal, responses are self-reported, and grades alone may not capture ability.

---

### [a2 — Data Description](a2_data_description.ipynb)

Cleaning and exploration. Several variables were duplicated across the Maths and Portuguese versions of the dataset; some rows had conflicting values for things that should logically match (like alcohol consumption or family relationship quality), so those were removed. Most dichotomous variables are heavily imbalanced, and a cluster of zero grades appears throughout that becomes relevant in later diagnostics.

---

### [a3 — Confidence Intervals & Hypothesis Testing](a3_ci_and_htm.ipynb)

Tests whether the average final grade is meaningfully different from the midpoint of the grading scale. Students were doing noticeably better in Portuguese than Maths, where the average sat right at the middle of the scale. A useful baseline before the more complex analysis.

---

### [a4 — Assumption Testing](a4_assumption_testing.ipynb)

Before testing whether alcohol affects grades, the grade distributions need to be checked for normality and variance homogeneity, because the choice of test depends on it. Four methods are used to check normality. Both grade variables come out non-normal, which rules out parametric tests for the rest of the project.

---

### [a5 — Relationship Testing](a5_relationship_testing.ipynb)

Tests three hypotheses using non-parametric methods. Previous grades strongly predicted final grades in both subjects. Weekday alcohol was significantly associated with worse Portuguese grades but not Maths. Family support made no significant difference. The choice of test varied depending on whether the variable was continuous, ordinal, or binary.

---

### [a6 — Linear Regression](a6_linear_regression.ipynb)

Quantifies how well previous grades and alcohol consumption predict the final Portuguese grade. The second-year grade dominates. Adding the first year barely changes anything. Alcohol is a statistically significant predictor but explains very little variance in practice. In all three models, the normality and homoskedasticity assumptions were not met, which is flagged and limits what can be concluded from the coefficients.

---

### [a7 — ANOVA](a7_anova.ipynb)

Tests whether free time affects final grades and whether that effect differs by sex. Sex had a significant effect; free time did not. The interaction was not significant. The normality assumption for residuals was not met, which is noted as a limitation.

---

### [a8 — Logistic Regression](a8_logistic_regression.ipynb)

Tests whether final Portuguese grade can identify students from larger families. It cannot. The model always predicted the majority class and performed identically to a baseline with no predictor.

---

### [a9 — PCA](a9_pca.ipynb)

Reduces the numeric variables to their principal components to see which features explain the most variance. The first component captures a performance axis: grade variables on one side, failure counts and alcohol variables on the other. This is consistent with the relationship testing results from a5 and gives a useful overview of how the variables cluster.

---

## Dataset

[Student Performance Data Set](https://archive.ics.uci.edu/ml/datasets/student+performance) UCI Machine Learning Repository  
P. Cortez and A. Silva, 2008. *Using Data Mining to Predict Secondary School Student Performance.*

---

## Tools

Python · pandas · numpy · matplotlib · seaborn · scipy · statsmodels · scikit-learn
