AI Travel Planner (LangChain + Gemini)

Overview:
This is a simple command-line AI travel planner built using LangChain and Google Gemini (via ChatGoogleGenerativeAI). The program generates a personalized, budget-aware travel itinerary based on user input.

Features:

* Generates day-wise travel itinerary
* Suggests food options
* Provides budget breakdown
* Recommends hotels
* Includes travel tips and best time to visit
* Tailored for trips starting from Kolkata

Requirements:

* Python 3.8+
* Google Generative AI API key

Dependencies:
Install required libraries using:
pip install langchain langchain-google-genai python-dotenv

Setup:

1. Clone the repository
2. Create a `.env` file in the root directory
3. Add your API key:
   GOOGLE_API_KEY=your_api_key_here

Usage:
Run the script:
python main.py

Then enter:

* Number of days
* Destination
* Total budget (in INR)
* Number of people
* Budget preference (e.g., food, travel, luxury)

Example Input:
Days: 5
Destination: Goa
Budget: 30000
People: 2
Preference: food

Output:

* Day-wise itinerary
* Food recommendations
* Budget allocation
* Travel tips
* Best time to visit
* Top 3 hotels

Notes:

* Flight cost is assumed based on a median estimate
* Input preference is taken as characters (can be improved to structured input)
* Output quality depends on prompt design and API response

-------------------------------------------------------------------------------

Author:
Prithwiraj Biswas

License:
For educational use 
Give proper credit to the Owner for personal use