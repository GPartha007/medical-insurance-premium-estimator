### 🗂️ Project name:
Medical Insurance Premium Estimator

### 📋 Project type: 
Public

### 🛡️ Client name:
XYZ Medical Insurance Corporation

---

### 🎯 Problem statement:
Help __XYZ Medical Insurance__ in automate the quoting process by calculating the yearly medical cover cost for new customers based on their health profile.

Client asked to develop a __regression model__ to predict individual medical costs billed by health insurance. Here we will analyse factors like _age_, _BMI_, _smoking status_, and _region_ to determine their impact on __charges__.

### ⚙️ Problem type: 
Regression

---

### 📜 Features:
* __age:__ Age of primary beneficiary.
* __sex:__ Insurance contractor gender(male/female)
* __bmi:__ __Body mass index__, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (__kg/m^2__) using the ratio of height to weight, ideally __18.5__ to __24.9__.
* __children:__ Number of children covered by health insurance / Number of dependents.
* __smoker:__ Indicator, if you smoke(yes/no).
* __region:__ The beneficiary's residential area in the US, northeast, southeast, southwest, northwest.

### 💡 Target variable:
* __charges:__ Individual medical costs billed by health insurance

---

### 🧐 Internal model metrics (Data Science / Model Performance)

These metrics help the analytics team evaluate model quality.

- __Out-of-Bag Score:__ 0.804
- __Mean Absolute Error:__ 2784.35
- __Mean Absolute Percentage Error:__ 41%
- __Mean Squared Error:__ 26343303.974
- __R-squared:__ 0.827
- __Adj. R-squared:__ 0.824

### Out-of-Bag Score = 0.804
The model can explain approximately __80.4%__ of unseen observations during training. Indicates stable performance without requiring a separate validation dataset. Gives confidence that the model will behave similarly for new applicants.

### R² = 0.827
__82.7%__ of premium variation is explained by Age, BMI, and Smoker status. This means the selected factors are strong predictors of insurance cost. Age, BMI and smoking status should remain key underwriting variables.
Business can justify premium differentiation based on these factors.

### Adjusted R² = 0.824
Very close to __R²__. The model is not artificially inflating performance because of unnecessary features. Current feature set is efficient. Additional variables should only be added if they bring significant predictive value.

### MAE(Mean Absolute Error) = ₹2,784.35
On average, predicted premium differs from actual premium by __₹2,784__.
Suppose average premium is __₹15,000__. Then,

__Error:__ ₹2,784 / ₹15,000 ≈ __18.5%__

This means many customers may receive quotes within a few thousand rupees of the actual premium.

__Decision Supported__<br>
If Premium Range is __₹50,000__ - __₹100,000__. Error is relatively small. Model can be used directly.

If Premium Range is __₹5,000__ – __₹15,000__. Error is substantial. Human review may still be required.


### MAPE(Mean Absolute Percentage Error) = 41%
Predictions are off by __41%__ on average. This is the most concerning metric.

__For example:__<br>
Actual Premium = ₹10,000

Predicted Premium may be:
- ₹5,900
- ₹14,100

A large difference for customers.

__Decision Supported__
- Avoid fully automated premium pricing.
- Use model as a decision-support tool.
- Improve feature engineering before production rollout.

__Business Risk__

- __Underpricing Risk__<br>
  Actual Premium = ₹20,000<br>
  Predicted = ₹12,000<br>
  _Company loses revenue._

- __Overpricing Risk__<br>
  Actual Premium = ₹20,000<br>
  Predicted = ₹28,000<br>
  _Customer may move to competitors._


### MSE(Mean Square Error) = 26,343,303.97
Some customers experience very large prediction errors. Because __MSE__ squares errors, it highlights extreme misses.

Likely causes:
- Very high-risk smokers
- Customers with extremely high BMI
- Outlier premium values

__Decision Supported__
- Create separate models for high-risk groups.
- Introduce risk segmentation.

__Example:__
- Low-risk customers
- Medium-risk customers
- High-risk customers

This often improves pricing accuracy.

---

### 🛠️ Business oriented metrics (Executive / Insurance Perspective):
These are the metrics executives care about.

### Premium Prediction Accuracy

__Derived from:__<br>
MAPE = 41%

__Insight__<br>
Approximate prediction accuracy:<br>
100 − 41 = 59%

__Business Interpretation__<br>
Current pricing accuracy is around __59%__.

__Decision__

Suitable for:
- Initial quote generation
- Customer self-service portals

Not ideal for:
- Final premium determination
- Regulatory reporting


### Revenue Leakage Risk

__Derived from:__ MAE and MAPE

__Insight__<br>
Underestimated premiums create revenue loss.

__Business Impact__<br>
Example:<br>
10,000 policies × ₹2,784 average error<br>
Potential pricing exposure:<br>
__≈ ₹27.8 million__

__Decision__<br>
Monitor underprediction rates carefully.


### Customer Retention Risk

__Derived from:__ MAPE

__Insight__<br>
Overestimated premiums may discourage purchases.

__Business Impact__
- Customers compare insurance providers.
- An inflated quote can directly reduce conversion.

__Decision__<br>
Use confidence intervals around predictions.

__Example:__<br>
Predicted Premium: __₹18,000 ± ₹2,500__<br>
instead of a single value.

---

## Executive Summary
__Strengths__

✅ Model explains __~83%__ of premium variability.

✅ Generalizes well __(OOB = 0.804)__.

✅ Features are meaningful and not overfitting.

✅ Suitable for __quote estimation__ and __underwriting support__.

__Concerns__

⚠️ Average percentage error is __41%__.

⚠️ Some customers experience ___large prediction errors___.

⚠️ Financial risk exists from underpricing and overpricing.

⚠️ Not yet reliable enough for __fully automated premium determination__.

---

The most important business takeaway is that the model has strong explanatory power __(R² ≈ 83%)__ but relatively high pricing error __(MAPE ≈ 41%)__. It is valuable as a ___decision-support___ and ___quote-generation___ tool, but additional features (e.g., region, gender, medical history, dependents, occupation, coverage type) would likely be needed before using it as the sole engine for premium pricing.

---

### 💻 End Product Layout: 
A web platform where a user enters their age, BMI, and habits, and the system outputs an estimated annual premium in dollars (e.g., "$4,250 / year").

### 🧩 Full-stack framework: 
Streamlit

### 🔗 Deployed app link:
[https://medical-insurance-premium-estimator-app.onrender.com/](https://medical-insurance-premium-estimator-app.onrender.com/)

---

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/GPartha007/medical-insurance-premium-estimator.git
cd medical-insurance-premium-estimator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment - Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Developed by

Partha Sarathi Guha
<br>
Data Science & Analytics Enthusiast | Python Developer

### Connect With Me

* [LinkedIn](https://www.linkedin.com/in/partha-sarathi-guha-08b2a921b/)
* [GitHub](https://github.com/GPartha007)
* [Portfolio Website](https://parthaguha-dev.onrender.com/)
