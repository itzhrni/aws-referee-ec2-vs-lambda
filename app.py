import streamlit  as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="AWS Referee | EC2 vs Lambda",
    page_icon="⚖️",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    /* Main Background and Text */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Custom Card Styling */
    .compute-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #ff9900;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        min-height: 300px;
    }
    
    .ec2-card { border-left: 5px solid #FF9900; }
    .lambda-card { border-left: 5px solid #E7157B; }

    /* Decision Banner */
    .verdict-banner {
        background-color: #232f3e;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #ff9900;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        padding: 0.5rem 2rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ec7211;
        border: none;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------- Header ----------
st.markdown(
    """
    <div style="text-align:center; padding-bottom: 20px;">
        <h1 style="color: #232f3e; font-size: 3rem;">⚖️ AWS Referee</h1>
        <p style="color: #545b64; font-size: 1.2rem;">
            The objective judge for <b>Compute</b> decisions. 
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Sidebar / Inputs ----------
with st.sidebar:
    st.header("⚙️ Workload Profile")
    st.info("Adjust the sliders and toggles to define your requirements.")
    
    cost = st.select_slider(
        "💰 Cost Priority",
        options=["Low (Save $$$)", "Medium", "High (Performance First)"],
        value="Medium"
    )

    traffic = st.selectbox(
        "📈 Traffic Pattern",
        ["Steady & Predictable", "Spiky / Event-driven", "Experimental/Dev"]
    )

    ops = st.radio(
        "🛠️ Management Capacity",
        ["I want full control (High Ops)", "I want zero-management (Low Ops)"]
    )

    latency = st.toggle("⚡ Critical Sub-100ms Latency Required", value=False)
    
    st.divider()
    analyze_btn = st.button("⚖️ Run Referee Analysis", use_container_width=True)

# ---------- Main Layout ----------
if not analyze_btn:
    # Default State - Welcome Screen
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg", width=150)
        st.markdown("""
        ### Welcome to the Referee Room.
        Use the sidebar to input your workload characteristics. 
        The Referee will weigh the trade-offs between **EC2 (Infrastructure as a Service)** 
        and **Lambda (Function as a Service)**.
        """)
else:
    # ---------- Analysis State ----------
    
    # 1. Comparison Cards
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
            <div class="compute-card ec2-card">
                <h2 style="color:#232f3e;">🖥️ AWS EC2</h2>
                <p style="color:gray;">Virtual Servers in the Cloud</p>
                <hr>
                <b>Best for:</b>
                <ul>
                    <li>Long-running processes</li>
                    <li>Legacy applications</li>
                    <li>Predictable high-traffic</li>
                </ul>
                <b>The "Cost":</b> Continuous hourly billing regardless of usage.
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="compute-card lambda-card">
                <h2 style="color:#232f3e;">⚡ AWS Lambda</h2>
                <p style="color:gray;">Serverless Code Execution</p>
                <hr>
                <b>Best for:</b>
                <ul>
                    <li>Event-driven logic</li>
                    <li>Intermittent tasks</li>
                    <li>Rapid scaling</li>
                </ul>
                <b>The "Cost":</b> Potential cold starts and execution limits.
            </div>
            """, unsafe_allow_html=True)

    # 2. Logic & Recommendation
    st.divider()
    
    # Simple logic engine
    recommendation = ""
    reasoning = ""
    icon = ""

    if latency or (traffic == "Steady & Predictable" and cost == "High (Performance First)"):
        recommendation = "AWS EC2 (Elastic Compute Cloud)"
        icon = "🖥️"
        reasoning = "Because you require <b>consistent performance</b> or have <b>predictable traffic</b>, the overhead of Lambda cold starts or per-request pricing would be a disadvantage."
    elif ops == "I want zero-management (Low Ops)" or traffic == "Spiky / Event-driven":
        recommendation = "AWS Lambda (Serverless)"
        icon = "⚡"
        reasoning = "Since you prefer <b>low operational overhead</b> and have <b>unpredictable traffic</b>, Lambda's 'scale-to-zero' and pay-per-use model is the most efficient choice."
    else:
        recommendation = "Hybrid / ECS Fargate"
        icon = "☁️"
        reasoning = "Your needs sit in the middle. Consider <b>Fargate</b> for a serverless experience with container-level control."
   
    st.markdown(
        "<p style='text-align:center; color:#555;'>"
        "<b>Key trade-off:</b> Control & predictability vs operational simplicity & elasticity."
        "</p>",
        unsafe_allow_html=True
        )


    # 3. The Verdict Display
    st.markdown(f"""
        <div class="verdict-banner">
            <h2 style="color: #ff9900;">THE VERDICT (Based on Your Constraints)</h2>
            <h1 style="color: white; margin: 10px 0;">{icon} {recommendation}</h1>
            <p style="font-size: 1.1rem; max-width: 800px; margin: 0 auto;">
                {reasoning}
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 4. Deep Dive Tabs
    st.write("### 🔍 Trade-off Deep Dive")
    tab1, tab2, tab3 = st.tabs(["💰 Pricing Model", "🚀 Scalability", "🛠️ Maintenance"])
    
    with tab1:
        st.write("**EC2:** You pay for the instance size per second. Best for high utilization (>60%).")
        st.write("**Lambda:** You pay for execution time (ms) and request count. Best for low or bursty utilization.")
        
    with tab2:
        st.write("**EC2:** Scaling takes minutes (Auto Scaling Groups). Handles massive sustained throughput easily.")
        st.write("**Lambda:** Scaling is near-instant (milliseconds). Limited by regional concurrency quotas.")
        
    with tab3:
        st.write("**EC2:** You are the admin. You patch the OS, update runtimes, and manage security.")
        st.write("**Lambda:** AWS manages the underlying OS. You only care about your code.")

# ---------- Footer ----------
st.markdown(
    """
    <div style="text-align:center; padding: 50px 0; color: #879196; font-size: 0.8rem;">
        <hr>
        AWS Referee | Trade-off reasoning generated with Kiro AI | Educational Demo
    </div>
    """,
    unsafe_allow_html=True
)
