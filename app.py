import streamlit as st

# Used for Streamlit deployment
from swarm import Swarm, Agent

# For local deployment, use the following importations instead
'''
from swarm.swarm.core import Swarm
from swarm.swarm.types import Agent
'''

from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file if available
load_dotenv()

# Function to set OpenAI API key dynamically in the session state
def set_openai_api_key():
    api_key_input = st.text_input("Enter your OpenAI API Key", type="password")
    if api_key_input:
        os.environ['OPENAI_API_KEY'] = api_key_input
        st.success("OpenAI API Key set successfully!")
    else:
        st.warning("Please enter your OpenAI API Key to continue.")


# Initialize the Swarm client
def initialize_swarm_client():
    return Swarm()

# Define the scraping function
def scrape_website(url):
    """Scrapes the content of the website."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()  # Return the text content from the HTML
    except requests.exceptions.RequestException as e:
        return f"Error during scraping: {str(e)}"

# Scraper Agent
scraper_agent = Agent(
    name="Scraper Agent",
    instructions="You are an agent that scrapes content from websites.",
    functions=[scrape_website]  # The agent can use the scrape_website function
)

# Define the analysis function
def analyze_content(content):
    """Analyzes the scraped content for key points."""
    summary = f"Summary of content: {content[:200]}..."  # A simple placeholder summarization
    return summary

# Research Agent
research_agent = Agent(
    name="Research Agent",
    instructions="You are an agent that analyzes content and extracts key insights.",
    functions=[analyze_content]  # The agent can use the analyze_content function
)

# Define the writing function
def write_summary(context_variables):
    """Writes a summary based on the analysis."""
    analysis = context_variables.get('analysis', '')
    summary = f"Here's a detailed report based on the research: {analysis}"
    return summary

# Writer Agent
writer_agent = Agent(
    name="Writer Agent",
    instructions="You are an agent that writes summaries of research.",
    functions=[write_summary]  # The agent can use the write_summary function
)

# Orchestrate the workflow
def orchestrate_workflow(client, url):
    # Step 1: Scrape the website
    scrape_result = client.run(
        agent=scraper_agent,
        messages=[{"role": "user", "content": f"Scrape the following website: {url}"}]
    )
    scraped_content = scrape_result.messages[-1]["content"]

    # Check for any error during scraping
    if "Error during scraping" in scraped_content:
        return scraped_content

    # Step 2: Analyze the scraped content
    research_result = client.run(
        agent=research_agent,
        messages=[{"role": "user", "content": f"Analyze the following content: {scraped_content}"}]
    )
    analysis_summary = research_result.messages[-1]["content"]

    # Step 3: Write the summary based on the analysis
    writer_result = client.run(
        agent=writer_agent,
        messages=[{"role": "user", "content": f"Write a summary based on this analysis: {analysis_summary}"}],
        context_variables={"analysis": analysis_summary}  # Pass the analysis to the writer agent
    )

    final_summary = writer_result.messages[-1]["content"]
    return final_summary

# Streamlit App UI
st.title("🔍 OpenAI SWARM Web Scraping and Content Analysis with Multi-Agent System")
st.caption("This app scrapes a website, analyzes the content, and generates a summary using a multi-agent system built on OpenAI's Swarm framework.")

# Input for OpenAI API Key
st.subheader("OpenAI API Key Setup")
set_openai_api_key()

# Initialize Swarm client only after API key is set
if 'OPENAI_API_KEY' in os.environ and os.environ['OPENAI_API_KEY']:
    # Initialize the Swarm client after API key is entered
    client = initialize_swarm_client()

    # Input field for the website URL
    url = st.text_input("Enter the URL of the website you want to scrape", placeholder="https://example.com")

    # Run Workflow button
    if st.button("Run Workflow"):
        if url:
            with st.spinner("Running the multi-agent workflow..."):
                final_report = orchestrate_workflow(client, url)
            st.success("Workflow complete!")
            st.write("### Final Report:")
            st.write(final_report)
        else:
            st.error("Please enter a valid URL.")
else:
    st.warning("Please set your OpenAI API Key to proceed.")

# Footer with credits
st.write("---")
st.write("**Developed by Jad Tounsi El Azzoiani**")
st.write("[GitHub Repo](https://github.com/jadouse5) | [LinkedIn](https://www.linkedin.com/in/jad-tounsi-el-azzoiani-87499a21a/)")
