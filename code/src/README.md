# Gen AI-Powered Data Profiling Solution

This project provides an AI-powered solution for data profiling and validation based on regulatory instructions. It uses OpenAI's GPT API and freely available Python libraries to extract rules, validate data, and suggest remediation actions.

---

## Features
1. **Extract and Refine Rules**: Extract validation rules from regulatory instructions using GPT.
2. **Generate Profiling Rules**: Automatically define profiling rules for data integrity checks.
3. **Data Validation**: Validate datasets against extracted and predefined rules.
4. **Remediation Suggestions**: Suggest automated remediation actions for flagged data issues.

---

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or later
- pip (Python package manager)
- OpenAI API key

---

## Setup Instructions

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/ewfx/gaidp-team-orion.git
   cd data-profiling-solution


2.Create a Virtual Environment (Optional)
It's recommended to use a virtual environment:

python -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts\activate # For Windows

3.Install Dependencies
Install all required Python libraries using:
pandas
openai

4.Set Up OpenAI API Key
Replace YOUR_API_KEY in the script with your actual OpenAI API key. Alternatively, set it as an environment variable:

export OPENAI_API_KEY='your_api_key' # For Linux/Mac
set OPENAI_API_KEY='your_api_key' # For Windows

5.Run the Script
Execute the main script:

python GenAI_DP.py
