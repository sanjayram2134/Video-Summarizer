import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai

import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
import os

# Page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Multimodal AI Agent- Video Summarizer",
    page_icon="🎥",
    layout="wide"
)

# Load environment variables
load_dotenv()

class VideoSummarizerApp:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
        self.agent = self.initialize_agent()
        self.video_path = None
        self.processed_video = None

    @staticmethod
    @st.cache_resource
    def initialize_agent():
        return Agent(
            name="Video AI Summarizer",
            model=Gemini(id="gemini-2.0-flash-exp"),
            tools=[DuckDuckGo()],
            markdown=True,
        )

    def upload_video(self, video_file):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
            temp_video.write(video_file.read())
            self.video_path = temp_video.name
        return self.video_path

    def process_video(self):
        try:
            self.processed_video = upload_file(self.video_path)
            while self.processed_video.state.name == "PROCESSING":
                time.sleep(1)
                self.processed_video = get_file(self.processed_video.name)
            return self.processed_video
        except Exception as error:
            raise RuntimeError(f"Error processing video: {error}")

    def analyze_video(self, user_query):
        if not user_query:
            raise ValueError("User query is required for analysis.")
        try:
            analysis_prompt = (
                f"""
                Analyze the uploaded video for content and context.
                Respond to the following query using video insights and supplementary web research:
                {user_query}

                Provide a detailed, user-friendly, and actionable response.
                """
            )
            response = self.agent.run(analysis_prompt, videos=[self.processed_video])
            return response.content
        except Exception as error:
            raise RuntimeError(f"Error analyzing video: {error}")
        finally:
            if self.video_path:
                Path(self.video_path).unlink(missing_ok=True)

    @staticmethod
    def customize_text_area_height():
        st.markdown(
            """
            <style>
            .stTextArea textarea {
                height: 100px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    def run(self):
        # st.set_page_config(
        #     page_title="Multimodal AI Agent - Video Summarizer",
        #     page_icon="🎥",
        #     layout="wide"
        # )

        st.title("Phidata Video AI Summarizer Agent 🎥🎤🖬")
        st.header("Powered by Gemini 2.0 Flash Exp")

        video_file = st.file_uploader(
            "Upload a video file", type=['mp4', 'mov', 'avi'], help="Upload a video for AI analysis"
        )

        if video_file:
            self.video_path = self.upload_video(video_file)
            st.video(self.video_path, format="video/mp4", start_time=0)

            user_query = st.text_area(
                "What insights are you seeking from the video?",
                placeholder="Ask anything about the video content. The AI agent will analyze and gather additional context if needed.",
                help="Provide specific questions or insights you want from the video."
            )

            if st.button("🔍 Analyze Video", key="analyze_video_button"):
                if not user_query:
                    st.warning("Please enter a question or insight to analyze the video.")
                else:
                    try:
                        with st.spinner("Processing video and gathering insights..."):
                            self.process_video()
                            result = self.analyze_video(user_query)
                        st.subheader("Analysis Result")
                        st.markdown(result)
                    except Exception as error:
                        st.error(f"An error occurred during analysis: {error}")
        else:
            st.info("Upload a video file to begin analysis.")

        self.customize_text_area_height()

# Run the app
if __name__ == "__main__":
    app = VideoSummarizerApp()
    app.run()
