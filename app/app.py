import streamlit as st
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

st.title('A/B Testing Calculator')
st.write('Comapare control vs treatment performance')

st.header('User Input')

control_users=st.number_input("Control - Total Users",min_value=1,max_value=25000)
control_conversions=st.number_input("Control - Conversions",min_value=0,max_value=500)

treatment_users=st.number_input("Treatment - Total Users",min_value=1,max_value=25000)
treatment_conversions=st.number_input("Treatment - Conversions",min_value=0,max_value=500)


p1=control_conversions/control_users
p2=treatment_conversions/treatment_users

lift=p2-p1

conversions=[control_conversions,treatment_conversions]
n=(control_users,treatment_users)

ztest,pval=proportions_ztest(conversions,n,alternative='smaller')

se=np.sqrt((p1*(1-p1))/control_users + (p2*(1-p2))/treatment_users)

me=1.96*se

lb=(p2-p1) - me
ub=(p2-p1) + me

st.header("Results")

st.write(f"Control Conversion Rate: {p1:.4f}")
st.write(f"Treatment Conversion Rate: {p2:.4f}")
st.write(f"Lift: {lift:.4f}")

st.write(f"P-value: {pval:.5f}")
st.write(f"Confidence Interval: ({lb:.4f}, {ub:.4f})")


if pval < 0.05:
    st.success("Treatment performs better (statistically significant)")
else:
    st.warning("No strong evidence that treatment is better")