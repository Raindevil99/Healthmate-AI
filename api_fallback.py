def search_condition(symptoms):
    # Simulated fallback response for hackathon demo
    return {
        "condition": "Simulated Condition (Demo) – Real API Not Approved Yet",
        "description": (
            f"Based on symptoms '{symptoms}', this is a simulated API response. "
            "The real medical API integration (e.g., Infermedica) is not yet approved."
        ),
        "medicines": [
            {
                "name": "Example Medicine A",
                "link": "https://www.netmeds.com/",
                "duration": "Every 6 hours as needed"
            },
            {
                "name": "Example Medicine B",
                "link": "https://pharmeasy.in/",
                "duration": "Once daily"
            }
        ],
        "home_remedy": "Drink warm fluids, rest well, and eat light meals. (Demo Data)",
        "humor": "Your immune system just entered beast mode. 💪 (Demo Data)",
        "positivity": "Your body is fighting back strong — keep supporting it! 🌟 (Demo Data)",
        "disclaimer": (
            "⚠️ This is demo data for hackathon purposes only. "
            "Do not self-medicate. Always consult a licensed doctor."
        )
    }
