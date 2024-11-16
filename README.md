# What If? - Decision Making Support Tool

## Overview
**What If?** is an interactive web application designed to help you make better decisions by comparing two important scenarios. By analyzing both options, the app provides a detailed, hypothetical vision of how your life or day might change depending on which option you choose. It considers both short-term and long-term effects, emotional and practical aspects, and the overall impact on your well-being and personal fulfillment.

## Features
- **Scenario Comparison**: Enter two different scenarios you are considering, and the app will analyze both to help you understand their possible consequences.
- **Interactive Analysis**: Get a detailed, balanced analysis of your scenarios, including advantages and disadvantages.
- **User-Friendly Interface**: Simple and intuitive UI with a clean layout and real-time feedback.
- **Customizable Appearance**: The app comes with a custom background and the ability to display a logo to personalize your experience.

## How It Works
1. **Enter Your Scenarios**: Describe two scenarios in the provided text boxes. These could be life-changing decisions, career moves, or anything you'd like to analyze.
2. **Send for Analysis**: Once both scenarios are filled out, click the "Send" button to start the analysis. The app will send the input to the backend, where a powerful AI model processes your data.
3. **Get Your Analysis**: The app will generate an analysis based on your scenarios, comparing them in terms of emotional, practical, and long-term impacts.
4. **Visual Comparison**: After the analysis is complete, the app will present the two scenarios side by side with a vertical line separating them for easy comparison.

## Technologies Used
- **Google Gemini API**: For generating content and analyzing the scenarios.

## Installation

To run this app locally, you need to have Python 3.x installed. Then, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/what-if.git
   ```

2. **Install Dependencies:**
Create a virtual environment and install the required libraries:

```bash
   cd what-if
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

   ```

3. **Set Up Your Google Gemini API Key:**
You'll need to set up your Google API key for Gemini. Replace the placeholder in the code with your actual API key:

```bash
   GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"

   ```

4. **Run the App:**

```bash
   streamlit run app.py

   ```

This will open the app in your browser at http://localhost:8501.

## Usage
- Enter your two scenarios in the text boxes provided.
- Click "Send" to submit your scenarios for analysis.
- View the analysis, with each scenario displayed side by side.
