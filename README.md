## Video Summarizer AI Agent

🎥 Video Summarizer AI Agent is a multimodal AI-powered tool that provides detailed insights and context-based analysis of video content. This application is powered by Phidata's AI Agent framework and Google's Gemini 2.0 Flash Exp model, making it a robust solution for video summarization and query-based analysis.

🌟 Key Features

Upload and Process Videos: Accepts video formats like .mp4, .mov, and .avi for analysis.

AI-Powered Summarization: Leverages Gemini 2.0 Flash Exp for advanced video understanding.

User Query Support: Accepts natural language queries to deliver targeted insights.

Supplementary Web Research: Utilizes DuckDuckGo for additional context during analysis.

Seamless Integration: Implements a user-friendly interface with Streamlit.

🚀 How It Works

Video Upload

Users can upload videos directly through the app's interface.

Supported formats include .mp4, .mov, and .avi.

Video Processing

Uploaded videos are temporarily stored and processed using Google's Generative AI API.

The app extracts meaningful content and context for analysis.

Query-Based Analysis

Users can enter specific queries about the video.

The AI agent generates detailed responses using the video content and supplementary online research.

Insights Delivery

Results are displayed in an easy-to-read format with actionable insights.

🛠️ Technologies Used

Libraries and Frameworks

Streamlit: For building the web-based user interface.

Phidata: For agent creation and interaction.

Google Generative AI: For video processing and summarization.

DuckDuckGo: For supplementary web research.

Languages

Python: Backend scripting and integration.

🖥️ Installation and Setup

Prerequisites

Ensure you have the following installed:

Python 3.8 or higher

Pip (Python package manager)

Steps

Clone the Repository
"""
git clone https://github.com/sanjayram2134/Video-Summarizer.git
cd Video-Summarizer
"""

Set Up Virtual Environment
"""
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
"""
Install Dependencies
"""
pip install -r requirements.txt
"""
Set Up API Keys

Create a .env file in the project root.

Add your Google API key:
"""
GOOGLE_API_KEY=your_api_key_here
"""
Run the Application
"""
streamlit run summarizer.py
"""
Access the App

Open your browser and navigate to http://localhost:8501.

📊 Example Use Case

Upload a video file (example_video.mp4).

Enter a query, such as:

"What is the main theme of the video?"

"Summarize the key events in the video."

Click on Analyze Video.

Review the AI-generated insights and context-rich summary.

🤝 Contributions

Contributions are welcome! If you have ideas to improve the project, feel free to open an issue or submit a pull request.

📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

📫 Contact

For any questions or support, reach out:

Author: Sanjayram

GitHub: sanjayram2134

LinkedIn: Sanjayram's LinkedIn

🙌 Acknowledgements

Special thanks to Phidata and Google for providing the tools and models that made this project possible.
