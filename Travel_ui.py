import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    timeout=150,
    max_tokens=5000,
    temperature=0.7
)


st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")

st.title("✈️ AI Travel Planner")
st.write("Plan your perfect trip from Kolkata with AI assistance")

# ---------------- UI ---------------- #

col1, col2 = st.columns(2)

with col1:
    days = st.slider("📅 Number of Days", 1, 15, 5)
    people = st.slider("👨‍👩‍👧‍👦 Number of People", 1, 10, 2)

with col2:
    place = st.text_input("📍 Destination", placeholder="e.g., Goa, Manali")
    cash = st.number_input("💰 Total Budget (₹)", min_value=1000, step=1000)


st.subheader("🎯 Budget Preference")

preferences = st.multiselect(
    "Where should most of your budget go?",
    ["Food", "Luxury Stay", "Budget Stay", "Adventure", "Shopping", "Sightseeing"],
)


priority_level = st.slider("How strongly should we prioritize this?", 1, 10, 7)


pref_text = f"{preferences} with priority level {priority_level}"

# ---------------- Prompt ---------------- #

prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are an expert AI in travel planning.
    Create practical, family-friendly trip plans.
    Keep recommendations realistic and budget-aware.
    """),
    ("human", """
    Create a {days}-day travel plan for {destination} starting from Kolkata.

    Total Budget: ₹{budget} for {count} people.
    Include travel cost from Kolkata using median flight fare.

    Allocate most of the budget towards: {pref}

    Provide:
    1. Day-wise itinerary
    2. Food suggestions
    3. Budget split
    4. Travel tips
    5. Best time to visit
    6. Top 3 hotel recommendations
    """),
])



if st.button("✨ Generate Travel Plan"):
    if not place or cash == 0:
        st.warning("Please fill all fields properly.")
    else:
        with st.spinner("Planning your trip... ✈️"):
            final_prompt = prompt.invoke({
                "days": days,
                "destination": place,
                "budget": cash,
                "count": people,
                "pref": pref_text
            })

            response = llm.invoke(final_prompt)

        st.success("Your Travel Plan is Ready!")

        st.markdown("## 🧳 Travel Plan")
        st.write(response.text)