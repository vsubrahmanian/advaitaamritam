import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from the .env file
load_dotenv()

# Initialize the client. It automatically picks up GEMINI_API_KEY from your environment.
client = genai.Client()

# Test the setup with a basic call
interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
)
# Printing response for verification
print(interaction.output_text)

# ----------------
# SAMPLE OUTPUT
# ----------------
# At its core, **Artificial Intelligence (AI) does not work like a human brain**, even though it was originally inspired by it. Instead, AI works through a combination of **massive amounts of data, complex math (algorithms), and incredible computing power.**

# To understand how AI works, it helps to break it down into five main steps:

# ---

# ### 1. Data (The Fuel)
# AI cannot learn without data. Just as a child needs to see hundreds of pictures of dogs to understand what a dog is, an AI needs massive amounts of data to learn a task. 
# * If you want an AI to translate languages, it reads billions of translated sentences.
# * If you want an AI to drive a car, it analyzes millions of hours of driving footage.

# ### 2. Algorithms (The Recipe)
# Algorithms are step-by-step sets of instructions and mathematical formulas that tell the computer how to process the data. Think of it as a recipe. The data is the ingredients, and the algorithm is the method for baking the cake.

# ### 3. Machine Learning (Learning from Experience)
# In the past, programmers had to write strict rules for computers (e.g., *“If the user types X, respond with Y”*). Modern AI uses **Machine Learning**, which changes the approach:
# * Instead of programming rules, programmers give the computer data and let the computer **find the rules itself**.
# * **Example:** Instead of telling the AI what a cat looks like (pointy ears, whiskers), you show it 10,000 photos of cats. The AI figures out the common patterns on its own.

# ### 4. Neural Networks and Deep Learning (The Engine)
# Most modern AI (like ChatGPT, facial recognition, or self-driving cars) uses **Deep Learning**, which relies on **Artificial Neural Networks**.
# * These are layered networks of mathematical "neurons" loosely inspired by the human brain.
# * **How it works in layers:** If you show a neural network a picture of a face:
#   * The **first layer** might just detect light and dark pixels.
#   * The **second layer** detects lines and edges.
#   * The **third layer** detects shapes (like a nose or an eye).
#   * The **final layer** puts it all together and says, *"That's Sarah."*

# ### 5. Training (Trial and Error)
# An AI isn't smart right out of the box; it has to be **trained**. 
# * The AI makes a guess about something (e.g., *"Is this email spam or not?"*).
# * If it’s wrong, the system receives a "penalty" and adjusts its internal math settings (called **weights**) to get it right next time.
# * This process happens **billions of times** at lightning speed until the AI's accuracy is very high.

# ---

# ### Summary: What is AI actually doing?
# At the end of the day, current AI is essentially an **advanced prediction machine**. 

# When you ask ChatGPT a question, it isn't "thinking" or "feeling." It is using probability to calculate **the most likely next word** in a sentence, based on all the text it was trained on. 

# * **Data** goes in $\rightarrow$ **Math/Patterns** are found $\rightarrow$ **Predictions** come out.