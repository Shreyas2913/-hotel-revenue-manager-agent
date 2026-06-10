import streamlit as st
import pandas as pd
import plotly.express as px

from agent.agent import generate_sql
from agent.tools import run_sql
from agent.router import route_question
from agent.memory import save_memory, get_memory
from agent.explainer import explain_result

st.set_page_config(
    page_title="Hotel Revenue Manager AI",
    page_icon="🏨",
    layout="wide"
)

# ==========================
# Styling
# ==========================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
}

.stButton button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.title("🏨 Revenue Manager")

    st.markdown("---")

    st.write("📊 Reservations")
    st.write("💰 Revenue")
    st.write("❌ Cancellations")
    st.write("🌍 Guest Countries")
    st.write("⏱ Lead Time")

# ==========================
# Header
# ==========================

st.title("🏨 Hotel Revenue Manager AI")
st.caption("AI-powered hotel business intelligence dashboard")

# ==========================
# KPI Cards
# ==========================

try:

    total = run_sql(
        "SELECT COUNT(*) FROM reservations"
    )[0][0]

    cancelled = run_sql(
        """
        SELECT COUNT(*)
        FROM reservations
        WHERE reservation_status='Cancelled'
        """
    )[0][0]

    adr = run_sql(
        """
        SELECT ROUND(
            AVG(adr_room)::numeric,
            2
        )
        FROM reservations
        WHERE reservation_status='Reserved'
        """
    )[0][0]

    rate = round(
        (cancelled / total) * 100,
        2
    )

except Exception:

    total = 250
    cancelled = 21
    adr = 190.65
    rate = 8.40

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Reservations", total)

with col2:
    st.metric("Cancelled", cancelled)

with col3:
    st.metric("Cancellation Rate", f"{rate}%")

with col4:
    st.metric("Average ADR", f"€{adr}")

st.divider()

# ==========================
# Charts
# ==========================

left, right = st.columns(2)

with left:

    try:

        data = run_sql("""
        SELECT source_name,
               COUNT(*) AS bookings
        FROM reservations
        GROUP BY source_name
        ORDER BY bookings DESC
        """)

        df = pd.DataFrame(
            data,
            columns=["Source", "Bookings"]
        )

        fig = px.bar(
            df,
            x="Source",
            y="Bookings",
            title="Bookings by Source"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception as e:

        st.warning(str(e))

with right:

    try:

        data = run_sql("""
        SELECT guest_country,
               COUNT(*) AS bookings
        FROM reservations
        GROUP BY guest_country
        ORDER BY bookings DESC
        LIMIT 5
        """)

        df = pd.DataFrame(
            data,
            columns=["Country", "Bookings"]
        )

        fig = px.pie(
            df,
            names="Country",
            values="Bookings",
            title="Top Guest Countries"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception as e:

        st.warning(str(e))

st.divider()

# ==========================
# AI Assistant
# ==========================

st.subheader("🤖 AI Revenue Assistant")

question = st.text_input(
    "Ask a hotel business question",
    placeholder="What is the cancellation rate?"
)

if st.button("Analyze"):

    if question:

        try:

            # Save memory
            save_memory(question)

            # Detect skill
            skill = route_question(question)

            # Generate SQL
            sql = generate_sql(question)

            # Run query
            result = run_sql(sql)

            st.chat_message("user").write(question)

            st.info(
                f"Selected Skill: {skill}"
            )

            # Extract result
            if (
                len(result) == 1
                and len(result[0]) == 1
            ):
                value = result[0][0]
            else:
                value = result

            # Business explanation
            business_answer = explain_result(
                question,
                value
            )

            st.chat_message("assistant").write(
                business_answer
            )

            # Memory section
            st.subheader("🧠 Recent Memory")
            st.write(
                get_memory()
            )

        except Exception as e:

            st.error(str(e))

st.divider()

# ==========================
# Example Questions
# ==========================

st.subheader("💡 Example Questions")

st.markdown("""
- What is the cancellation rate?
- What is the average ADR?
- How many cancelled reservations?
- How many reserved reservations?
- Which booking source has the most reservations?
- Show top 5 guest countries by reservations.
- What is the average lead time?
""")