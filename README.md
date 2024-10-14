# 🔍 OpenAI SWARM Web Scraping Streamlit Web App and Content Analysis with Multi-Agent System

This project implements a multi-agent system that performs web scraping, content analysis, and summary generation using OpenAI's **Swarm framework**. The system automates the extraction and processing of information from websites, making it ideal for applications like content aggregation, market analysis, and research automation.

---

## Table of Contents
1. [Author](#author)
2. [Introduction](#introduction)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Running the Project](#running-the-project)
6. [Credits](#credits)
7. [Conclusion](#conclusion)
8. [License](#license)

---

## Author
This project was developed by **Jad Tounsi El Azzoiani**, a passionate machine learning and artificial intelligence enthusiast focused on efficient computing, AI-based web scraping, and automation. My goal is to explore cutting-edge AI technologies and contribute to the open-source community by sharing knowledge and innovative solutions.

- **GitHub**: [Jad Tounsi El Azzoiani](https://github.com/jadouse5)
- **LinkedIn**: [Jad Tounsi El Azzoiani](https://www.linkedin.com/in/jad-tounsi-el-azzoiani-87499a21a/)

---

## Introduction
This project demonstrates the implementation of a **multi-agent system** capable of performing web scraping, analyzing the scraped data, and generating summaries. Built using **OpenAI's Swarm framework**, the system can automatically scrape data from websites, process it, and generate concise reports. The workflow is ideal for use cases where real-time content extraction and analysis are critical, such as:
- **Content aggregation**
- **Market research**
- **Data analysis for research automation**

---

## Prerequisites
Before running the project, ensure you have the following dependencies installed:

- Python 3.10+
- **Streamlit** - for building the interactive web app.
- **OpenAI API Key** - required for accessing the Swarm framework.
- **BeautifulSoup** - for web scraping.
- **Requests** - for handling HTTP requests.
- **dotenv** - for managing environment variables.

These tools are essential for running the multi-agent system and performing web scraping and analysis.

---

## Installation

### Step 1: Install Python
Make sure **Python 3.10+** is installed. You can download it from the official [Python website](https://www.python.org/downloads/).

### Step 2: Set Up a Virtual Environment
To isolate project dependencies, it's a good practice to create a virtual environment. Follow these steps:

1. Open a terminal and navigate to your project directory.
2. Create a virtual environment named `myenv`:

   ```bash
   python -m venv myenv
   ```

3. Activate the virtual environment:

   - **On macOS/Linux**:
   
     ```bash
     source myenv/bin/activate
     ```
   
   - **On Windows**:
   
     ```bash
     myenv\Scripts\activate
     ```

### Step 3: Install Jupyter (Optional)
If you want to run or develop the project using Jupyter notebooks, install JupyterLab within the virtual environment:

```bash
pip install jupyterlab
```

### Step 4: Install the Required Python Packages
Once your virtual environment is active, install the necessary dependencies for the project:

```bash
pip install streamlit beautifulsoup4 requests python-dotenv
pip install git+https://github.com/openai/swarm.git
```

### Step 5: Set Up the OpenAI API Key
1. In the project directory, create a `.env` file to store environment variables.
2. Add the following line to the `.env` file, replacing `your-api-key-here` with your actual OpenAI API key:

```ini
OPENAI_API_KEY=your-api-key-here
```

---

## Running the Project

Once you have set up the environment and installed the required packages, follow these steps to run the project:

1. **Activate the virtual environment**:
   
   - **On macOS/Linux**:
   
     ```bash
     source myenv/bin/activate
     ```

   - **On Windows**:
   
     ```bash
     myenv\Scripts\activate
     ```

2. **Run the Streamlit app**:
   
   Start the Streamlit app by running:

   ```bash
   streamlit run app.py
   ```

3. **Access the app in your browser**:

   Once the app is running, go to the local URL provided by Streamlit (typically `http://localhost:8501`).

4. **Run the workflow**:

   - Enter the URL of the website you want to scrape in the input field.
   - Click the **Run Workflow** button to start the scraping and analysis process.
   - View the generated summary directly in the browser once the workflow completes.

---

### Deactivating the Virtual Environment
When you’re done working on the project, deactivate the virtual environment by running:

```bash
deactivate
```

### Key Updates:
- **Virtual Environment Setup**: Instructions for creating and activating a virtual environment (`myenv`) are added to ensure clean package management.
- **Deactivation**: Included a section on how to deactivate the environment after use.

This should help ensure the project runs in a controlled environment without conflicts with other Python installations or packages. Let me know if you need any further improvements!

## Credits
This project makes use of OpenAI’s **Swarm framework** for multi-agent orchestration. You can learn more about Swarm on GitHub:

- **Swarm GitHub Repository**: [OpenAI Swarm](https://github.com/openai/swarm)

---

## Conclusion
This project illustrates the power of multi-agent systems in automating web scraping and content analysis tasks. By leveraging **OpenAI’s Swarm framework**, we created a highly efficient, flexible system capable of extracting valuable insights from websites. The project is a stepping stone towards more complex AI-driven systems for automating data extraction and analysis.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact
Feel free to reach out for collaboration or to discuss this project further:

- **GitHub**: [Jad Tounsi El Azzoiani](https://github.com/jadouse5)
- **LinkedIn**: [Jad Tounsi El Azzoiani](https://www.linkedin.com/in/jad-tounsi-el-azzoiani-87499a21a/)

---
