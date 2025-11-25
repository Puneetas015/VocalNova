import streamlit as st
import pandas as pd
import numpy as np
import time

# --- Configuration ---
st.set_page_config(
    page_title="Voice Bot Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Mock Data Generation ---
@st.cache_data
def load_data():
    """Generates mock data for demonstration."""
    
    # 1. Query Data
    query_data = {
        'Query Type': ['Account Balance', 'Order Status', 'FAQ/General', 'Agent Handover', 'Technical Issue'],
        'Count': [180, 120, 350, 45, 25]
    }
    df_queries = pd.DataFrame(query_data)
    
    # 2. Performance Data (Response Times)
    latency = np.random.normal(loc=1.2, scale=0.3, size=7) # Avg 1.2s, Std Dev 0.3s
    date_range = pd.date_range(end=pd.Timestamp.now().date(), periods=7)
    df_performance = pd.DataFrame({
        'Date': date_range,
        'Avg Response Time (s)': latency.round(2)
    })
    
    # 3. Error Rate
    total_interactions = df_queries['Count'].sum()
    error_count = 35 # Mock 35 errors (e.g., NLU failure, STT error)
    error_rate = (error_count / total_interactions) * 100
    
    return df_queries, df_performance, error_rate, total_interactions

df_queries, df_performance, error_rate, total_interactions = load_data()


# --- Dashboard Layout ---

st.title("🗣️ Intelligent Voice Bot Performance Dashboard")
st.markdown("---")

## 📈 Key Performance Indicators (KPIs)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total User Interactions", value=f"{total_interactions:,}")
    st.subheader("Query Volume Distribution")
    st.bar_chart(df_queries.set_index('Query Type'))

with col2:
    st.metric(label="Overall Error Rate", value=f"{error_rate:.1f}%")
    st.subheader("Average Response Times (Last 7 Days)")
    st.line_chart(df_performance.set_index('Date'))
    

with col3:
    avg_latency = df_performance['Avg Response Time (s)'].mean()
    st.metric(label="Average Latency", value=f"{avg_latency:.2f} s", delta="Stable")
    
    # Display the purpose of tracking metrics
    st.markdown("""
        ### Metrics for Improvement 
        Tracking these metrics helps identify bottlenecks and areas for NLU refinement:
        * **Query Volume:** Highlights the most common customer needs.
        * **Response Time:** Ensures fast service; high latency indicates API or network issues.
        * **Error Rate:** Pinpoints NLU/STT failures needing model retraining.
    """)

st.markdown("---")
st.caption(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")