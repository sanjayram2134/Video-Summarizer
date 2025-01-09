# Video Summarizer AI Agent 🎥

**Video Summarizer AI Agent** is a multimodal AI-powered tool that provides detailed insights and context-based analysis of video content. This application is powered by Phidata's AI Agent framework and Google's Gemini 2.0 Flash Exp model, making it a robust solution for video summarization and query-based analysis.

## 🌟 Key Features

- **Upload and Process Videos:** Accepts video formats like `.mp4`, `.mov`, and `.avi` for analysis.
- **AI-Powered Summarization:** Leverages Gemini 2.0 Flash Exp for advanced video understanding.
- **User Query Support:** Accepts natural language queries to deliver targeted insights.
- **Supplementary Web Research:** Utilizes DuckDuckGo for additional context during analysis.
- **Seamless Integration:** Implements a user-friendly interface with Streamlit.

## 🚀 How It Works

### Video Upload
1. Users can upload videos directly through the app's interface.
2. Supported formats include `.mp4`, `.mov`, and `.avi`.

### Video Processing
1. Uploaded videos are temporarily stored and processed using Google's Generative AI API.
2. The app extracts meaningful content and context for analysis.

### Query-Based Analysis
1. Users can enter specific queries about the video.
2. The AI agent generates detailed responses using the video content and supplementary online research.

### Insights Delivery
1. Results are displayed in an easy-to-read format with actionable insights.

## 🛠️ Technologies Used

### Libraries and Frameworks
- **Streamlit:** For building the web-based user interface.
- **Phidata:** For agent creation and interaction.
- **Google Generative AI:** For video processing and summarization.
- **DuckDuckGo:** For supplementary web research.

### Languages
- **Python:** Backend scripting and integration.

## 🖥️ Installation and Setup

### Prerequisites
Ensure you have the following installed:
- **Python 3.8 or higher**
- **Pip** (Python package manager)

### Steps

#### Clone the Repository
`bash
git clone https://github.com/sanjayram2134/Video-Summarizer.git
cd Video-Summarizer`

### Setup environment
`python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate `

### Install Dependencies
`pip install -r requirements.txt
`

### Set your API_KEY
`GOOGLE_API_KEY=your_api_key_here
`

### Run the Application
`streamlit run summarizer.py
`

📫 Contact
For any questions or support, reach out:

Author: Sanjayram
GitHub: sanjayram2134
LinkedIn: Sanjayram's LinkedIn
