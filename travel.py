from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    timeout=150,
    max_tokens=5000,
    temperature=0.7
)

print("............. AI Travel Planner .............")
print("Answer these questions properly for better results.\n")


days = int(input("Enter number of days including journey: "))
place = input("Enter the main location you want to travel: ")
cash = input("Enter total budget in Rupees: ")
people = int(input("Enter Total No of people: "))
preference = list(input("Your budget will be mostly allocated on which things: "))


prompt = ChatPromptTemplate.from_messages([
    ("system","""
    You are an expert AI in travel planning.
    Create practical, family-friendly trip plans.
    Keep recommendations realistic and budget-aware.
    """),
    ("human","""
    Create a {days}-day travel plan for {destination} starting from Kolkata.
    Total Budget: ₹{budget} for {count}people including travelling from kolkata (use flight fare of "Median" value) and allocate most of the budget in {pref}.
    Give:
    1. Day-wise itinerary
    2. Food suggestions
    3. Budget split
    4. Travel tips
    5. Best time to visit
    6. Recommended top 3 hotels
    """),
])

final_prompt = prompt.invoke({
    "days": days,
    "destination": place,
    "budget": cash,
    "count": people,
    "pref": preference
})


trip_plan = llm.invoke(final_prompt)


print("\n............. Your Travel Plan .............\n")
print(trip_plan.text)