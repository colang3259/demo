from gtts import gTTS
import os

# The text you want to convert to speech
text = """
ntroduction
Welcome to [Exciting Math]!

Today, we will explore how mathematics plays a crucial role in artificial intelligence (AI). AI is transforming the way we live and work, and mathematics is the foundation of AI algorithms and models.

Part 1: Basic Machine Learning Algorithms
Linear Regression

Introduction: Linear regression is a basic machine learning algorithm for predicting continuous values.
Formula: 
𝑦
=
𝑚
𝑥
+
𝑏
y=mx+b
Example: Predicting house prices based on area.
K-Nearest Neighbors (KNN)

Introduction: KNN is used to classify data points based on neighboring points.
Example: Classifying flower types based on features like petal length and width.
Deep Learning with Neural Networks

Introduction: Neural networks are complex models capable of learning from large and abstract data.
Example: Image recognition and natural language processing.
Part 2: Real-World Applications of AI
Medical Diagnosis

Introduction: AI can help diagnose diseases based on medical images and patient data.
Example: Detecting cancer from X-ray images.
 

Introduction: AI models predict market trends and optimize investment portfolios.
Example: Automated trading systems.
Natural Language Processing (NLP)

Introduction: AI can understand and respond to human natural language.
Example: Virtual assistants like Siri and Google Assistant.
Part 3: Conclusion
Mathematics is the key to unlocking the potential of artificial intelligence. Understanding these algorithms and models will help us maximize the benefits of AI in our daily lives.

Don't forget to like and subscribe to not miss the upcoming videos!

Call-to-Action
If you want to learn more about each algorithm, leave a comment and we will make detailed videos on each topic.

Happy learning and see you in the next video!
!
"""

# Language in which you want to convert
language = 'en'

# Creating the gTTS object
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named "output.mp3"
speech.save("output.mp3")

# Playing the converted file
os.system("start output.mp3")  # On Windows
# os.system("afplay output.mp3")  # On macOS
# os.system("mpg321 output.mp3")  # On Linux
