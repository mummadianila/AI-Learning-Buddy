import streamlit as st
import google.generativeai as genai
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="EcoBuddy - AI Learning Buddy",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .activity-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .response-box {
        background: #f0f8ff;
        padding: 1.5rem;
        border-left: 4px solid #667eea;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize API
def init_api():
    try:
        api_key = st.secrets.get("GOOGLE_API_KEY")
        if not api_key:
            st.error("❌ GOOGLE_API_KEY not found in secrets. Please configure it in .streamlit/secrets.toml")
            st.stop()
        genai.configure(api_key=api_key)
        return genai.GenerativeModel("gemini-pro")
    except Exception as e:
        st.error(f"❌ Failed to initialize API: {str(e)}")
        st.stop()

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "model" not in st.session_state:
    st.session_state.model = init_api()

# Header
st.markdown("""
    <div class="main-header">
    <h1>🌍 EcoBuddy - AI Learning Buddy</h1>
    <p>Learn Climate Change with AI-powered explanations, examples, and quizzes</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📚 About EcoBuddy")
    st.write("""
    EcoBuddy helps you understand Climate Change through:
    - **Concept Explanations** - Simple breakdowns of complex topics
    - **Real-Life Examples** - Practical scenarios from our world
    - **Quiz Generator** - Test your knowledge
    - **Ask Anything** - Get answers to your climate questions
    """)
    
    st.divider()
    
    # Learning History
    if st.session_state.chat_history:
        st.header("📖 Learning History")
        if st.button("🗑️ Clear History"):
            st.session_state.chat_history = []
            st.rerun()
        
        for i, item in enumerate(reversed(st.session_state.chat_history[-5:]), 1):
            with st.expander(f"{i}. {item['topic']} ({item['activity']})"):
                st.markdown(item['response'])
                st.caption(f"📅 {item['timestamp']}")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input(
        "📚 Enter a Climate Change topic",
        placeholder="e.g., Greenhouse Effect, Carbon Footprint, Renewable Energy...",
        help="Type any climate-related topic you want to learn about"
    )

with col2:
    activity = st.selectbox(
        "Choose Activity",
        ["Explain Concept", "Real-Life Example", "Quiz", "Ask Anything"],
        help="Select how you want to learn about this topic"
    )

st.divider()

# Generate content
if st.button("✨ Generate", use_container_width=True, type="primary"):
    if not topic.strip():
        st.warning("⚠️ Please enter a climate topic first!")
    else:
        # Define prompts based on activity
        prompts = {
            "Explain Concept": f"""Explain '{topic}' in the context of Climate Change in simple, easy-to-understand terms suitable for students. 
            Include:
            - A clear definition
            - Why it matters for climate change
            - Key points to remember
            Keep it concise but informative (around 300-400 words).""",
            
            "Real-Life Example": f"""Provide 2-3 relatable, real-life examples of '{topic}' related to Climate Change. 
            Make each example:
            - Easy to understand
            - From different regions or industries
            - Practical and concrete
            Include the impact and solutions where relevant.""",
            
            "Quiz": f"""Create 5 multiple-choice quiz questions about '{topic}' related to Climate Change.
            Format each as:
            Q1: [question]
            A) [option]
            B) [option]
            C) [option]
            D) [option]
            Correct Answer: [letter]
            Explanation: [why this is correct]""",
            
            "Ask Anything": f"""Answer the following question about Climate Change: '{topic}'
            Provide a comprehensive, well-researched answer that is:
            - Accurate and evidence-based
            - Easy to understand
            - Includes relevant facts and figures
            - Suggests actions if applicable"""
        }
        
        with st.spinner("🔄 Generating content using Gemini AI..."):
            try:
                prompt = prompts[activity]
                response = st.session_state.model.generate_content(prompt)
                
                # Store in session state
                st.session_state.chat_history.append({
                    "topic": topic,
                    "activity": activity,
                    "response": response.text,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                
                # Display response
                st.success(f"✅ {activity} for '{topic}'")
                st.markdown(f"""
                    <div class="response-box">
                    {response.text}
                    </div>
                """, unsafe_allow_html=True)
                
                # Add download button
                st.download_button(
                    label="📥 Download Response",
                    data=response.text,
                    file_name=f"{topic}_{activity}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"❌ Error generating content: {str(e)}")
                st.info("💡 Tip: Make sure your GOOGLE_API_KEY is valid and you have API credits.")

# Footer
st.divider()
st.markdown("""
    <div style="text-align: center; color: #888; font-size: 0.9rem; padding: 2rem 0;">
    <p>🌱 EcoBuddy - Learning about Climate Change for a better future</p>
    <p>Powered by Google Gemini AI | Built with Streamlit</p>
    </div>
""", unsafe_allow_html=True)
