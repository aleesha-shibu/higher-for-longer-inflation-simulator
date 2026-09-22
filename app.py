import streamlit as st
import pandas as pd
import random
import plotly.graph_objects as go


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Higher-for-Longer Debt & Inflation Simulator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# COLOUR PALETTE
# =========================================================

EMERALD = "#16A085"
DARK_EMERALD = "#0E6655"
LIGHT_MINT = "#DFF5EF"
SLATE = "#1E293B"
SLATE_GRAY = "#64748B"
LIGHT_BACKGROUND = "#F8FAFC"
BORDER = "#E2E8F0"
WHITE = "#FFFFFF"
TEAL = "#2A9D8F"


# =========================================================
# =========================================================
# CUSTOM STYLING
# =========================================================

st.markdown(
    """
    <style>

    /* MAIN PAGE */
    .main {
        background-color: #F8FAFC;
        padding-top: 1.5rem;
    }

    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #F1F5F9;
        border-right: 1px solid #CBD5E1;
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #0F172A !important;
    }

    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span {
        color: #0F172A;
    }

    /* SIDEBAR INPUTS */
    [data-testid="stSidebar"] input {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] [data-baseweb="input"] {
        background-color: #FFFFFF !important;
    }

    /* TITLES */
    .eyebrow {
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 1.8px;
        text-transform: uppercase;
        color: #047857;
        margin-bottom: 0.3rem;
    }

    .hero-title {
        font-size: 2.7rem;
        font-weight: 750;
        color: #0F172A;
        margin-bottom: 0.3rem;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }

    .section-title {
        font-size: 1.45rem;
        font-weight: 700;
        color: #0F172A;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
    }

    /* METRIC CARDS */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-left: 4px solid #047857;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.05);
    }

    [data-testid="stMetricLabel"] {
        color: #475569 !important;
    }

    [data-testid="stMetricValue"] {
        color: #0F172A !important;
    }

    /* INFORMATION CARD */
    .info-card {
        padding: 1rem 1.2rem;
        border-radius: 10px;
        border: 1px solid #A7DCCF;
        background-color: #ECFDF5;
        color: #0F172A;
        margin-bottom: 1rem;
    }

    .info-card strong {
        color: #065F46;
    }

    /* BUTTON */
    div.stButton > button {
        background-color: #047857;
        color: #FFFFFF !important;
        border: 1px solid #047857;
        border-radius: 8px;
        font-weight: 650;
        padding: 0.55rem 1rem;
    }

    div.stButton > button:hover {
        background-color: #065F46;
        border-color: #065F46;
        color: #FFFFFF !important;
    }

    /* GENERAL TEXT */
    .stMarkdown,
    .stText,
    p {
        color: #0F172A;
    }

    /* CAPTIONS */
    .stCaption,
    [data-testid="stCaptionContainer"] {
        color: #475569 !important;
    }

    /* DATAFRAME */
    [data-testid="stDataFrame"] {
        border: 1px solid #CBD5E1;
        border-radius: 8px;
    }

    /* DIVIDER */
    hr {
        border-color: #CBD5E1;
    }

    /* FOOTER */
    .footer {
        text-align: center;
        color: #64748B;
        font-size: 0.8rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #CBD5E1;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# ECONOMIC ASSUMPTIONS
# =========================================================

starting_inflation = 0.0348
target_inflation = 0.04
max_inflation = 0.06

debt_interest = 0.12
savings_return = 0.05


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("## Simulation Inputs")

st.sidebar.caption(
    "Enter your starting financial position and simulation period."
)

st.sidebar.markdown("---")

debt = st.sidebar.number_input(
    "Current Debt (₹)",
    min_value=0.0,
    value=500000.0,
    step=10000.0,
    help="Enter your current outstanding debt."
)

savings = st.sidebar.number_input(
    "Current Savings (₹)",
    min_value=0.0,
    value=300000.0,
    step=10000.0,
    help="Enter your current savings or financial reserves."
)

years = st.sidebar.number_input(
    "Simulation Period (Years)",
    min_value=1,
    max_value=50,
    value=10,
    step=1,
    help="Choose how many years you want to simulate."
)

st.sidebar.markdown("---")

run_simulation = st.sidebar.button(
    "▶  Run Simulation",
    use_container_width=True,
    type="primary"
)

st.sidebar.markdown("---")

st.sidebar.markdown("### Economic Assumptions")

st.sidebar.caption(
    f"Starting inflation: **{starting_inflation:.2%}**"
)

st.sidebar.caption(
    f"Target inflation: **{target_inflation:.2%}**"
)

st.sidebar.caption(
    f"Debt interest rate: **{debt_interest:.2%}**"
)

st.sidebar.caption(
    f"Savings return: **{savings_return:.2%}**"
)


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="eyebrow">FINANCIAL SIMULATION MODEL</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">'
    'Higher-for-Longer Debt & Inflation Simulator'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Explore how debt, savings and inflation may evolve over time '
    'under a higher-for-longer interest-rate environment.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# ASSUMPTION CARDS
# =========================================================

assumption_col1, assumption_col2, assumption_col3 = st.columns(3)

with assumption_col1:
    st.metric(
        "Starting Inflation",
        f"{starting_inflation:.2%}"
    )

with assumption_col2:
    st.metric(
        "Target Inflation",
        f"{target_inflation:.2%}"
    )

with assumption_col3:
    st.metric(
        "Debt Interest Rate",
        f"{debt_interest:.2%}"
    )

st.divider()


# =========================================================
# SIMULATION FUNCTION
# =========================================================

def run_financial_simulation(debt, savings, years):

    current_debt = debt
    current_savings = savings

    inflation = starting_inflation
    inflation_factor = 1

    results = []

    for year in range(1, years + 1):

        # Grow debt and savings
        current_debt *= (1 + debt_interest)
        current_savings *= (1 + savings_return)

        # Random yearly inflation fluctuation
        inflation += random.uniform(-0.003, 0.003)

        # Gradually move inflation toward target
        inflation += (target_inflation - inflation) * 0.15

        # Keep inflation within assumed range
        inflation = max(
            0.02,
            min(inflation, max_inflation)
        )

        # Cumulative inflation
        inflation_factor *= (1 + inflation)

        # Inflation-adjusted values
        real_savings = current_savings / inflation_factor
        real_debt = current_debt / inflation_factor
        real_networth = real_savings - real_debt

        # Nominal net worth
        nominal_networth = current_savings - current_debt

        results.append({
            "Year": year,
            "Debt": current_debt,
            "Savings": current_savings,
            "Inflation": inflation * 100,
            "Real Savings": real_savings,
            "Nominal Net Worth": nominal_networth,
            "Real Net Worth": real_networth
        })

    return pd.DataFrame(results)


# =========================================================
# BEFORE SIMULATION
# =========================================================

if not run_simulation:

    st.markdown(
        f"""
        <div class="info-card">
        <strong>Ready to simulate?</strong><br>
        Enter your debt, savings and simulation period in the sidebar,
        then click <strong>Run Simulation</strong> to generate the
        financial projections.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">How the Model Works</div>',
        unsafe_allow_html=True
    )

    info_col1, info_col2, info_col3 = st.columns(3)

    with info_col1:
        st.markdown("### 01 · Debt Growth")
        st.write(
            "Debt compounds annually using the assumed "
            "12% higher-for-longer interest rate."
        )

    with info_col2:
        st.markdown("### 02 · Savings Growth")
        st.write(
            "Savings grow annually using the assumed "
            "5% savings return."
        )

    with info_col3:
        st.markdown("### 03 · Inflation Impact")
        st.write(
            "Inflation fluctuates each year and gradually "
            "moves toward the assumed 4% target."
        )

    st.divider()

    st.markdown(
        '<div class="section-title">Economic Assumptions</div>',
        unsafe_allow_html=True
    )

    assumption_table = pd.DataFrame({
        "Assumption": [
            "Starting Inflation",
            "Target Inflation",
            "Maximum Inflation",
            "Debt Interest Rate",
            "Savings Return"
        ],
        "Value": [
            "3.48%",
            "4.00%",
            "6.00%",
            "12.00%",
            "5.00%"
        ],
        "Purpose": [
            "Initial inflation level",
            "Long-run inflation target",
            "Upper simulation limit",
            "Annual debt growth",
            "Annual savings growth"
        ]
    })

    st.dataframe(
        assumption_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="footer">'
        'Educational financial simulation · Not financial advice'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# SIMULATION RESULTS
# =========================================================

else:

    df = run_financial_simulation(
        debt,
        savings,
        years
    )

    final = df.iloc[-1]

    # =====================================================
    # RESULTS HEADER
    # =====================================================

    st.markdown(
        '<div class="section-title">Simulation Results</div>',
        unsafe_allow_html=True
    )

    st.caption(
        f"Projection based on ₹{debt:,.0f} starting debt, "
        f"₹{savings:,.0f} starting savings and a "
        f"{years}-year simulation period."
    )

    # =====================================================
    # KPI CARDS
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Final Debt",
            f"₹{final['Debt']:,.0f}"
        )

    with col2:
        st.metric(
            "Final Savings",
            f"₹{final['Savings']:,.0f}"
        )

    with col3:
        st.metric(
            "Final Inflation",
            f"{final['Inflation']:.2f}%"
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "Real Savings Value",
            f"₹{final['Real Savings']:,.0f}"
        )

    with col5:
        st.metric(
            "Nominal Net Worth",
            f"₹{final['Nominal Net Worth']:,.0f}"
        )

    with col6:
        st.metric(
            "Real Net Worth",
            f"₹{final['Real Net Worth']:,.0f}"
        )

    st.divider()

    # =====================================================
    # INTERPRETATION
    # =====================================================

    st.markdown(
        '<div class="section-title">What the Simulation Shows</div>',
        unsafe_allow_html=True
    )

    interpretation_col1, interpretation_col2 = st.columns(2)

    with interpretation_col1:

        debt_growth = final["Debt"] - debt

        st.markdown("### Debt Position")

        st.write(
            f"Starting debt of **₹{debt:,.0f}** grows to "
            f"approximately **₹{final['Debt']:,.0f}** "
            f"over {years} years under the assumed "
            f"{debt_interest:.0%} annual interest rate."
        )

        st.caption(
            f"Total nominal debt increase: ₹{debt_growth:,.0f}"
        )

    with interpretation_col2:

        savings_growth = final["Savings"] - savings

        st.markdown("### Savings Position")

        st.write(
            f"Starting savings of **₹{savings:,.0f}** grows to "
            f"approximately **₹{final['Savings']:,.0f}** "
            f"under the assumed {savings_return:.0%} annual return."
        )

        st.caption(
            f"Total nominal savings increase: ₹{savings_growth:,.0f}"
        )

    st.divider()


    # =====================================================
    # CHARTS
    # =====================================================

    st.markdown(
        '<div class="section-title">Financial Trends</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # DEBT VS SAVINGS
    # -----------------------------------------------------

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        st.markdown("### Debt vs Savings")

        fig_debt_savings = go.Figure()

        fig_debt_savings.add_trace(
            go.Scatter(
                x=df["Year"],
                y=df["Debt"],
                mode="lines+markers",
                name="Debt",
                line=dict(
                    color=SLATE,
                    width=3
                ),
                marker=dict(
                    color=SLATE,
                    size=7
                )
            )
        )

        fig_debt_savings.add_trace(
            go.Scatter(
                x=df["Year"],
                y=df["Savings"],
                mode="lines+markers",
                name="Savings",
                line=dict(
                    color=EMERALD,
                    width=3
                ),
                marker=dict(
                    color=EMERALD,
                    size=7
                )
            )
        )

        fig_debt_savings.update_layout(
            height=400,
            plot_bgcolor=WHITE,
            paper_bgcolor=WHITE,
            font=dict(
                color=SLATE
            ),
            xaxis=dict(
                title="Year",
                gridcolor=BORDER
            ),
            yaxis=dict(
                title="Amount (₹)",
                gridcolor=BORDER,
                tickprefix="₹"
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(
                l=20,
                r=20,
                t=30,
                b=20
            )
        )

        st.plotly_chart(
            fig_debt_savings,
            use_container_width=True
        )


    # -----------------------------------------------------
    # INFLATION
    # -----------------------------------------------------

    with chart_col2:

        st.markdown("### Inflation Trend")

        fig_inflation = go.Figure()

        fig_inflation.add_trace(
            go.Scatter(
                x=df["Year"],
                y=df["Inflation"],
                mode="lines+markers",
                name="Inflation",
                line=dict(
                    color=EMERALD,
                    width=3
                ),
                marker=dict(
                    color=EMERALD,
                    size=7
                )
            )
        )

        fig_inflation.add_hline(
            y=target_inflation * 100,
            line_dash="dash",
            line_color=DARK_EMERALD,
            annotation_text="Target: 4%"
        )

        fig_inflation.update_layout(
            height=400,
            plot_bgcolor=WHITE,
            paper_bgcolor=WHITE,
            font=dict(
                color=SLATE
            ),
            xaxis=dict(
                title="Year",
                gridcolor=BORDER
            ),
            yaxis=dict(
                title="Inflation (%)",
                gridcolor=BORDER,
                ticksuffix="%"
            ),
            showlegend=False,
            margin=dict(
                l=20,
                r=20,
                t=30,
                b=20
            )
        )

        st.plotly_chart(
            fig_inflation,
            use_container_width=True
        )


    # -----------------------------------------------------
    # NET WORTH
    # -----------------------------------------------------

    st.markdown("### Net Worth Over Time")

    fig_networth = go.Figure()

    fig_networth.add_trace(
        go.Scatter(
            x=df["Year"],
            y=df["Nominal Net Worth"],
            mode="lines+markers",
            name="Nominal Net Worth",
            line=dict(
                color=TEAL,
                width=3
            ),
            marker=dict(
                color=TEAL,
                size=7
            )
        )
    )

    fig_networth.add_trace(
        go.Scatter(
            x=df["Year"],
            y=df["Real Net Worth"],
            mode="lines+markers",
            name="Real Net Worth",
            line=dict(
                color=DARK_EMERALD,
                width=3
            ),
            marker=dict(
                color=DARK_EMERALD,
                size=7
            )
        )
    )

    fig_networth.update_layout(
        height=430,
        plot_bgcolor=WHITE,
        paper_bgcolor=WHITE,
        font=dict(
            color=SLATE
        ),
        xaxis=dict(
            title="Year",
            gridcolor=BORDER
        ),
        yaxis=dict(
            title="Net Worth (₹)",
            gridcolor=BORDER,
            tickprefix="₹"
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
    )

    st.plotly_chart(
        fig_networth,
        use_container_width=True
    )

    st.divider()


    # =====================================================
    # YEARLY DATA
    # =====================================================

    st.markdown(
        '<div class="section-title">Year-by-Year Simulation</div>',
        unsafe_allow_html=True
    )

    display_df = df.copy()

    display_df["Debt"] = display_df["Debt"].map(
        lambda x: f"₹{x:,.2f}"
    )

    display_df["Savings"] = display_df["Savings"].map(
        lambda x: f"₹{x:,.2f}"
    )

    display_df["Inflation"] = display_df["Inflation"].map(
        lambda x: f"{x:.2f}%"
    )

    display_df["Real Savings"] = display_df["Real Savings"].map(
        lambda x: f"₹{x:,.2f}"
    )

    display_df["Nominal Net Worth"] = display_df[
        "Nominal Net Worth"
    ].map(
        lambda x: f"₹{x:,.2f}"
    )

    display_df["Real Net Worth"] = display_df[
        "Real Net Worth"
    ].map(
        lambda x: f"₹{x:,.2f}"
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


    # =====================================================
    # METHODOLOGY
    # =====================================================

    with st.expander("View Simulation Methodology"):

        st.write(
            """
            The model projects debt and savings over the selected
            simulation period.

            **Debt:** grows annually using the assumed debt interest rate.

            **Savings:** grows annually using the assumed savings return.

            **Inflation:** changes randomly each year within a controlled
            range and gradually moves toward the target inflation rate.

            **Real values:** nominal values are adjusted using cumulative
            inflation to illustrate the effect of changing purchasing power.

            Because annual inflation includes a random component,
            repeated simulations can produce slightly different results.
            """
        )

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown(
        '<div class="footer">'
        'Higher-for-Longer Debt & Inflation Simulator · '
        'Educational financial simulation · Not financial advice'
        '</div>',
        unsafe_allow_html=True
    )