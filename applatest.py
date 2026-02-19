import streamlit as st

st.set_page_config(page_title="Travel Guide Assistant (RAG)", page_icon="🌍", layout="wide")

st.title("🌍 Travel Guide Assistant (RAG Based)")
st.write("Plan your trip using a simple Retrieval-Augmented Generation (RAG) approach.")

# ------------------ KNOWLEDGE BASE (RAG DATA) ------------------
travel_knowledge_base = {
    "kochi": {
        "places": ["Fort Kochi", "Marine Drive", "Mattancherry Palace", "Cherai Beach"],
        "foods": ["Appam & Stew", "Karimeen Fry", "Puttu & Kadala Curry", "Seafood"],
        "hotels": ["Budget Hotel", "Local Guest House", "Homestay"]
    },
    "bangalore": {
        "places": ["Lalbagh Botanical Garden", "Cubbon Park", "Bangalore Palace", "MG Road"],
        "foods": ["Masala Dosa", "Idli Vada", "Filter Coffee", "Biryani"],
        "hotels": ["Budget Hotel", "3-Star Hotel", "Hostel"]
    },
    "chennai": {
        "places": ["Marina Beach", "Kapaleeshwarar Temple", "Mahabalipuram", "Phoenix Mall"],
        "foods": ["Dosa", "Sambar", "Seafood", "Chettinad Cuisine"],
        "hotels": ["Budget Hotel", "Guest House", "3-Star Hotel"]
    }
}

# ------------------ USER INPUT ------------------
destination = st.text_input("📍 Enter Destination:")
days = st.number_input("📅 Number of Days:", min_value=1, max_value=10, value=3)
budget = st.number_input("💰 Total Budget (₹):", min_value=1000, step=500, value=5000)

# ------------------ RAG RETRIEVAL FUNCTION ------------------
def retrieve_data(city):
    city = city.lower()
    if city in travel_knowledge_base:
        return travel_knowledge_base[city]
    else:
        return {
            "places": ["Local attractions", "City center", "Popular parks"],
            "foods": ["Local cuisine", "Street food"],
            "hotels": ["Budget Hotel", "Guest House"]
        }

# ------------------ GENERATE ITINERARY ------------------
if st.button("Generate Itinerary"):

    data = retrieve_data(destination)

    st.subheader(f"✈️ Trip Plan for {destination.title()}")
    st.write(f"**Days:** {days}")
    st.write(f"**Budget:** ₹{budget}")

    st.subheader("📆 Daily Itinerary")
    for i in range(days):
        place = data["places"][i % len(data["places"])]
        st.write(f"**Day {i+1}:** Visit {place}")

    st.subheader("🏨 Hotel Suggestions")
    for hotel in data["hotels"]:
        st.write(f"- {hotel}")

    st.subheader("🍴 Food to Try")
    for food in data["foods"]:
        st.write(f"- {food}")

    st.subheader("📍 Places to Visit")
    for place in data["places"]:
        st.write(f"- {place}")

    st.subheader("💸 Budget Breakdown (Estimated)")
    hotel_budget = int(budget * 0.4)
    food_budget = int(budget * 0.3)
    travel_budget = int(budget * 0.3)

    st.write(f"🏨 Hotel: ₹{hotel_budget}")
    st.write(f"🍴 Food: ₹{food_budget}")
    st.write(f"🚗 Travel: ₹{travel_budget}")

    map_url = f"https://www.google.com/maps/search/{destination}"
    st.markdown(f"📍 [Open {destination.title()} on Google Maps]({map_url})")
