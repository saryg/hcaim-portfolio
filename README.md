# MSc Human-Centred AI - TU Dublin

A selection of coursework from my MSc in Human-Centred Artificial Intelligence (2023–2024), which covered machine learning, deep learning, statistics, and AI ethics. Projects span different data types: images (medical and facial), tabular health and survey data, and text.

Key focus areas for projects:
- **Dataset selection:** considering licensing, absence of PII, suitability for research use, and checking for class imbalances and other potential sources of bias before any modelling began
- **Modelling:** monitoring for overfitting and underfitting throughout, evaluating final models with performance broken down by subgroup where relevant
- **Explainability:** comparing blackbox and glassbox models, using XAI tools including GradCAM++ saliency maps and nearest neighbour visualisation


---

## Projects

### [Skin Lesion Classification - KNN & VGG16 Transfer Learning](skin_lesion_classification_knn_vgg16_transfer_learning.ipynb)
*May 2024*

Classifies 7 types of skin lesions from the HAM10000 dataset (~12,000 dermoscopy images). Fine-tuned a VGG16 network and compared it against a KNN baseline to evaluate the tradeoff between model complexity and performance. Class imbalance was a central challenge: the dataset is heavily skewed toward melanocytic nevi. Includes subgroup performance analysis by age, sex, and lesion localisation.

- Dataset: [HAM10000](https://challenge.isic-archive.com/data/#2018) (ISIC 2018 Challenge), © ViDIR Group, Medical University of Vienna ([doi:10.1038/sdata.2018.161](https://doi.org/10.1038/sdata.2018.161))
- Classes: melanoma, basal cell carcinoma, actinic keratoses, and 4 others
- Techniques: transfer learning, data augmentation, class weighting, subgroup evaluation
- Interpretability methods: GradCAM++ saliency maps (VGG16), nearest neighbour visualisation (KNN), glassbox vs blackbox comparison
- Ethical considerations: misclassification risks in a medical context, and whether performance holds equally across patient demographics

`transfer learning` `CNN` `VGG16` `KNN` `class imbalance` `medical imaging` `fairness evaluation` `XAI`

---

### [Diabetes Prediction - Neural Network](diabetes_prediction_neural_network.ipynb)
*March 2024*

Predicts diabetes from a health survey dataset (42,415 instances, 22 variables). The focus was systematic evaluation rather than picking a single model: tested 10 ANN architectures, 8 batch sizes, and 3 optimisers, with dropout and early stopping. Includes subgroup analysis by sex and cholesterol level to check whether the model performs consistently across groups.

- Grid search across architecture, batch size, and optimiser combinations
- Subgroup analysis to surface differential performance
- Interpretability methods: precision/recall breakdown by class and subgroup
- Ethical considerations: implications of false positives and false negatives in a health context, and whether the model performs consistently across demographic groups

`Keras` `ANN` `hyperparameter tuning` `grid search` `subgroup analysis` `healthcare`

---

### [Facial Age Classification - CNN on UTKFace](facial_age_classification_cnn_utkface.ipynb)
*March 2024*

Binary classification of face images as young (5–15) or old (50+) using a CNN trained on a filtered subset of UTKFace. The main focus is on how dataset construction decisions (filtering by ethnicity, balancing by gender) introduce or mitigate bias, and what that means for a deployed age detection system. Model performance was modest (75% on a small test set); the value of the notebook is in the reasoning around data choices rather than the results themselves.

- Dataset: UTKFace (filtered subset: 1,000 images, balanced by class and gender)
- Explicit analysis of gender distribution within age classes and its effect on what the model learns
- Ethical considerations: implications of automated age detection, and how dataset construction choices affect fairness
- Interpretability methods: GradCAM++ saliency maps showing which facial features drive predictions
- Deployed as a REST API using Docker and Azure

`CNN` `image classification` `dataset bias` `ethics` `Docker` `Azure`

---

### [Student Performance - Statistical Analysis](student_performance_statistical_analysis/)
*September–December 2023*

Statistical investigation into factors affecting secondary school grades in Portugal (maths and Portuguese, 2005–2006). Covers the pipeline from research design through to PCA, split across 9 modular notebooks. Each notebook covers a distinct method with assumption testing before applying it. The focus is on process rather than findings: it shows a methodical approach to statistics, including recognising when assumptions don't hold and thinking through what that means for the results.

| Notebook | Topic |
|----------|-------|
| [a1](student_performance_statistical_analysis/a1_analysis_design.ipynb) | Analysis design & research questions |
| [a2](student_performance_statistical_analysis/a2_data_description.ipynb) | Data description & summary statistics |
| [a3](student_performance_statistical_analysis/a3_ci_and_htm.ipynb) | Confidence intervals & hypothesis testing |
| [a4](student_performance_statistical_analysis/a4_assumption_testing.ipynb) | Assumption testing |
| [a5](student_performance_statistical_analysis/a5_relationship_testing.ipynb) | Relationship testing |
| [a6](student_performance_statistical_analysis/a6_linear_regression.ipynb) | Linear regression |
| [a7](student_performance_statistical_analysis/a7_anova.ipynb) | ANOVA |
| [a8](student_performance_statistical_analysis/a8_logistic_regression.ipynb) | Logistic regression |
| [a9](student_performance_statistical_analysis/a9_pca.ipynb) | PCA |

`scipy` `statsmodels` `regression` `ANOVA`

---

## Final Project - Investigating Bias Against Non-Native English Texts in AI Content Detectors
*September 2024*

I evaluated three commercial AI detection tools (Sapling, Originality.ai, Winston AI) across 1,592 essays from 10 Asian countries using the [ICNALE corpus](https://language.sakura.ne.jp/icnale/).

- No general bias found against non-native speakers in unedited essays
- Editing essays for grammar and spelling significantly increased misclassification rates, suggesting detectors rely on features of non-native writing that disappear when text is corrected
- Country-specific biases observed. Contrary to prior work, native English speakers were more likely to be misclassified as AI than non-natives
- Scope of project was quite limited with only one 200 word essay topic and one geographic region (Asia) 
- Findings reflect the state of AI detection tools in mid-2024 and should be read in that context

---

## Tools

Python · Jupyter · scikit-learn · Keras / TensorFlow · pandas · numpy · matplotlib · seaborn · scipy · statsmodels · Docker
