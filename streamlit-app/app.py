import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="Medical Insurance Premium Estimator",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern cards and big price
st.markdown("""
<style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #6b7280;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        text-align: center;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .metric-label {
        font-size: 0.875rem;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #111827;
    }
    .price-container {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        padding: 2rem 2rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 20px 25px -5px rgba(37, 99, 235, 0.3);
    }
    .price-label {
        color: #bfdbfe;
        font-size: 1.125rem;
        margin-bottom: 0.5rem;
    }
    .price-value {
        color: white;
        font-size: 4rem;
        font-weight: 800;
        line-height: 1;
    }
    .smoker-yes { color: #dc2626 !important; }
    .smoker-no { color: #16a34a !important; }
</style>
""", unsafe_allow_html=True)

# Sidebar inputs
with st.sidebar:
    st.header("👤 Your Details")
    st.write("Adjust to see instant estimate")
    
    age = st.number_input(
        "**Age**",
        min_value=18,
        max_value=100,
        value=18,
        step=1,
        help="Enter your age in years: 18 to 100"
    )
    
    bmi = st.number_input(
        "**BMI**",
        min_value=10.0,
        max_value=50.0,
        value=22.0,
        step=0.1,
        format="%.1f",
        help="Body Mass Index"
    )
    
    smoker = st.radio(
        "**Smoker?**",
        options=["No", "Yes"],
        horizontal=True,
        help="Do you currently smoke?"
    )
    
    st.markdown("---")
    st.caption("**Note:** This is a demo estimator for educational purposes")


# Main content
st.markdown('<h1 class="main-title">Medical Insurance Premium Estimator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Get an instant estimate based on your health profile</p>', unsafe_allow_html=True)

# Display inputs in cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Age</div>
        <div class="metric-value">{age} yrs</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">BMI</div>
        <div class="metric-value">{bmi:.1f} kg/m²</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    smoker_class = "smoker-yes" if smoker == "Yes" else "smoker-no"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Smoker</div>
        <div class="metric-value {smoker_class}">{smoker}</div>
    </div>
    """, unsafe_allow_html=True)



def calculate_estimate_premium(age, bmi, smoker):
    filename = "../models/pipeline_random_forest.pkl"
    load_model = pkl.load(open(filename, 'rb'))

    print(f"Age: {age}")

    input_data = pd.DataFrame(
        data = [[age, bmi, smoker.lower()]], 
        columns = ['age', 'bmi', 'smoker']
    )

    y_pred = load_model.predict(input_data)

    return y_pred

premium = calculate_estimate_premium(age, bmi, smoker)

# Big price display
st.markdown(f"""
<div class="price-container">
    <div class="price-label">Estimated Annual Premium</div>
    <div class="price-value">~ ${np.round(premium[0], 3):,}</div>
</div>
""", unsafe_allow_html=True)

# Additional insights
# st.html("<br>")
# st.markdown("### What affects your premium?")
# c1, c2, c3 = st.columns(3)
# with c1:
#     st.info(f"**Age factor:** ${age * 220:,}")
# with c2:
#     bmi_extra = max(0, int((bmi - 21) * 180))
#     st.info(f"**BMI factor:** ${bmi_extra:,}")
# with c3:
#     if smoker == "Yes":
#         smoker_extra = 15000
#         st.error(f"**Smoking surcharge:** ${smoker_extra:,}")
#     else:
#         st.success(f"**Non-smoker discount applied**")