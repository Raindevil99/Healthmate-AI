import streamlit as st
from conditions_db import conditions_db
from api_fallback import search_condition  # mock fallback

st.set_page_config(page_title="HealthMate AI", page_icon="💊", layout="centered")

st.markdown("<h1 style='text-align: center; color: teal;'>💊 HealthMate AI</h1>", unsafe_allow_html=True)
st.write("### AI-powered symptom checker with medicine guidance, humor, and positivity.")

symptom_input = st.text_input("Enter your symptoms:")

if st.button("Diagnose Me 🚀"):
    symptom_key = symptom_input.lower().strip()

    if symptom_key in conditions_db:
        # Local DB result
        data = conditions_db[symptom_key]
        st.success(f"### {data['description']}")

        st.subheader("💊 Medicines")
        for med in data["medicines"]:
            st.write(f"- **{med['name']}**: {med['use']} — _{med['duration']}_")

        st.markdown("#### 🛒 Buy Medicines:")
        for link in data["links"]:
            st.markdown(f"- [{link['name']}]({link['url']})")

        st.subheader("🏠 Home Remedy")
        st.info(data["home_remedy"])

        st.subheader("😂 Humor Boost")
        st.write(data["humor"])

        st.subheader("🌟 Positivity Boost")
        st.write(data["positivity"])

        st.warning(f"**Disclaimer:** {data['disclaimer']}")

    else:
        # Fallback: mock API
        st.warning("Not found in local database. Using simulated API for hackathon demo...")
        api_result = search_condition(symptom_key)  # this returns mock data for now

        if api_result:
            st.success(f"### {api_result['condition']}")
            st.write(api_result["description"])

            st.subheader("💊 Medicines")
            for med in api_result["medicines"]:
                st.write(f"- **[{med['name']}]({med['link']})** — _{med['duration']}_")

            st.subheader("🏠 Home Remedy")
            st.info(api_result["home_remedy"])

            st.subheader("😂 Humor Boost")
            st.write(api_result["humor"])

            st.subheader("🌟 Positivity Boost")
            st.write(api_result["positivity"])

            st.markdown(
                "<p style='color: gold; font-style: italic;'>"
                "(This is a simulated API for the hackathon. Built to integrate with real medical APIs like Infermedica once approved.)"
                "</p>",
                unsafe_allow_html=True
            )
            st.markdown("[Consult a doctor on Practo](https://www.practo.com)")
        else:
            st.error("No results found in local or simulated API. Please consult a doctor.")
            st.markdown("[Consult a doctor on Practo](https://www.practo.com)")
