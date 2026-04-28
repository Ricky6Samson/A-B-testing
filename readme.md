# 📊 A/B Testing Project (Python + Streamlit)

## 📌 Overview
This project is an end-to-end **A/B testing analysis tool** that compares Control vs Treatment groups to evaluate whether a change improves conversion rates. It combines statistical analysis with an interactive Streamlit app.

---

## 🎯 Problem Statement
Determine whether a new product version (Treatment) leads to a **statistically significant improvement in conversion rate** compared to the existing version (Control).

---

## 🧠 Approach

- Calculated **conversion rates** for both groups  
- Performed **two-proportion Z-test** to test significance  
- Built **95% confidence interval** using standard error and Z = 1.96  
- Interpreted results for business decision-making  

---

## 📈 Key Results

- Control Conversion Rate: ~11.8%  
- Treatment Conversion Rate: ~13.1%  
- Lift: ~1.28%  
- Result: **Statistically Significant (p < 0.05)**  
- Confidence Interval: [0.70%, 1.86%]  

👉 Conclusion: Treatment improves conversion rate and can be considered for rollout.

---

## 🌐 Streamlit App

An interactive app was built to:
- Input experiment data  
- Compute conversion rates, p-value, and confidence interval  
- Provide instant statistical decision  

Run:
```bash
streamlit run app/streamlit_app.py

## 🛠️ Tech Stack
- Python  
- NumPy  
- Pandas  
- Statsmodels  
- Streamlit  

---

## 💡 Key Learnings
- A/B testing and hypothesis testing in real-world scenarios  
- Interpreting p-values and confidence intervals  
- Translating statistical results into business decisions  
- Building simple data applications using Streamlit  