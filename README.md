# 🌍 EcoBuddy - AI Learning Buddy

An intelligent AI-powered learning companion that helps students understand Climate Change through interactive explanations, real-life examples, quizzes, and Q&A using Google Gemini API and Streamlit.

## ✨ Features

- **🎓 Explain Concepts** - Get detailed, easy-to-understand explanations of climate-related topics
- **🌏 Real-Life Examples** - Learn through practical, relatable scenarios from around the world
- **📝 Quiz Generator** - Test your knowledge with AI-generated multiple-choice questions
- **❓ Ask Anything** - Get answers to any climate-related questions
- **📖 Learning History** - Track your learning journey with session history
- **📥 Download Responses** - Save your learning materials for offline access
- **🎨 Beautiful UI** - Clean, intuitive interface with modern design

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google API Key (free from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mummadianila/AI-Learning-Buddy.git
   cd AI-Learning-Buddy
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google API Key**
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key
   - Create `.streamlit/secrets.toml` in your project directory:
     ```toml
     GOOGLE_API_KEY = "your-api-key-here"
     ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`

## 📚 How to Use

1. **Enter a Climate Topic** - Type any climate-related topic you want to learn about
2. **Choose an Activity**:
   - **Explain Concept** - Get a detailed explanation
   - **Real-Life Example** - See practical examples
   - **Quiz** - Take a 5-question quiz
   - **Ask Anything** - Ask climate-related questions
3. **Click Generate** - Wait for AI to generate content
4. **Download** - Save your response for later

## 📂 Project Structure

```
AI-Learning-Buddy/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── secrets.toml      # API keys (create this file)
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables
Create `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your-google-generativeai-api-key"
```

### Streamlit Configuration (Optional)
Create `.streamlit/config.toml` for additional customization:
```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
```

## 🌱 Climate Topics Examples

- Greenhouse Effect
- Carbon Footprint
- Renewable Energy
- Deforestation
- Ocean Acidification
- Melting Glaciers
- Extreme Weather
- Sustainable Development
- Carbon Dioxide (CO2)
- Climate Action

## 🤖 AI Model

- **Model**: Google Gemini Pro
- **API**: Google Generative AI
- **Rate Limits**: Depends on your Google API quota

## 📝 Example Queries

### Explain Concept
"Explain the greenhouse effect"

### Real-Life Example
"Show examples of renewable energy"

### Quiz
"Quiz me on climate change"

### Ask Anything
"What is carbon sequestration and how does it help?"

## 🛠️ Troubleshooting

### API Key Error
- Verify your API key is correct in `.streamlit/secrets.toml`
- Check that you have quota remaining on Google AI Studio
- Ensure the file is in the correct directory

### ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Connection Issues
- Check your internet connection
- Verify Google API is accessible from your region
- Check if you've exceeded API rate limits

## 🚀 Deployment

### Deploy on Streamlit Cloud
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy and add secrets in the deployment settings

### Deploy on Other Platforms
- **Heroku**: Add `Procfile` with `web: streamlit run app.py`
- **Docker**: Create `Dockerfile` for containerization
- **AWS/Google Cloud**: Use respective deployment services

## 📜 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Check existing documentation
- Review troubleshooting section

## 🌍 Learn More

- [Google Gemini API Documentation](https://ai.google.dev/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Climate Change Resources](https://climate.nasa.gov/)

---

**🌱 Made with ❤️ for climate education**
