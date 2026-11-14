import streamlit as st

st.set_page_config(
    page_title="StudentSkill Hub | Project Showcase",
    page_icon=":material/school:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------- Styling ------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,500,0,0&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: #f6f7f5; color: #1d2b26; }
[data-testid="stSidebar"] { background: #173b32; }
[data-testid="stSidebar"] * { color: #f4f7f3 !important; }
.material-icon { font-family: 'Material Symbols Rounded'; font-weight: normal; font-style: normal; font-size: 1.55rem; line-height: 1; display: inline-block; font-feature-settings: 'liga'; -webkit-font-feature-settings: 'liga'; -webkit-font-smoothing: antialiased; }
.brand { display:flex; align-items:center; gap:.65rem; }
.brand .material-icon { font-size:1.8rem; color:#b9ddc9; }
.hero { background: linear-gradient(125deg,#173b32 0%,#245b4b 60%,#39735e 100%); padding: 2.4rem 2.6rem; border-radius: 22px; color: white; margin-bottom: 1.2rem; }
.hero h1 { color: white; font-family: Manrope,sans-serif; font-size: 2.7rem; line-height: 1.1; margin: .3rem 0 .8rem 0; }
.hero p { color: #e1eee7; font-size: 1.08rem; max-width: 850px; }
.eyebrow { color:#c5e3d3; text-transform:uppercase; letter-spacing:.15em; font-size:.75rem; font-weight:700; }
.section-tag { color:#39735e; font-weight:700; letter-spacing:.12em; text-transform:uppercase; font-size:.72rem; }
.card { background:white; border:1px solid #e4e9e4; border-radius:16px; padding:1.1rem 1.2rem; height:100%; min-height:145px; box-shadow:0 3px 12px rgba(20,50,40,.035); transition:transform .18s ease, box-shadow .18s ease, border-color .18s ease; }
.card:hover { transform:translateY(-3px); border-color:#b9d4c2; box-shadow:0 9px 22px rgba(20,50,40,.09); }
.card-icon { width:2.65rem; height:2.65rem; display:grid; place-items:center; border-radius:12px; color:#39735e; background:#edf4ef; margin-bottom:.8rem; }
.card h3 { color:#214c3e; font-family:Manrope,sans-serif; margin:.2rem 0 .45rem 0; font-size:1.06rem; }
.card p { color:#53645c; margin:0; font-size:.94rem; }
.step { background:white; border-left:4px solid #4b8b70; border-radius:10px; padding:.9rem 1rem; margin-bottom:.65rem; }
.step b { color:#214c3e; }
.note { background:#edf4ef; border:1px solid #d8e7dc; border-radius:12px; padding:1rem 1.1rem; color:#315a49; }
.warn { background:#fff7e8; border:1px solid #f0dfb8; border-radius:12px; padding:1rem 1.1rem; color:#74551d; }
.footer { color:#78857e; font-size:.82rem; border-top:1px solid #e2e8e2; padding-top:1rem; margin-top:2.5rem; }
div[data-testid="stMetric"] { background:white; border:1px solid #e4e9e4; padding:1rem; border-radius:14px; }
</style>
""", unsafe_allow_html=True)

PAGES = [
    "Home", "Problem & Proposed Idea", "Project Objectives", "Target Users & Roles",
    "Application Modules", "Student Workflow", "System Architecture", "Data Organisation",
    "Technology Stack", "Implementation Highlights", "Live Demonstration Plan",
    "Limitations & Future Improvements", "Conclusion & Sources"
]

def navigate_to(page_name):
    st.session_state["active_page"] = page_name


with st.sidebar:
    st.markdown('<div class="brand"><span class="material-icon" aria-hidden="true">school</span><strong>StudentSkill Hub</strong></div>', unsafe_allow_html=True)
    st.caption("PROJECT SHOWCASE WEBSITE")
    st.markdown("---")
    page_search = st.text_input("Find a section", placeholder="Try “skills” or “workflow”")
    if page_search:
        matching_pages = [name for name in PAGES if page_search.casefold() in name.casefold()]
        if matching_pages:
            st.caption("QUICK LINKS")
            for matching_page in matching_pages[:4]:
                st.button(
                    f"Open {matching_page}",
                    key=f"quick_page_{PAGES.index(matching_page)}",
                    on_click=navigate_to,
                    args=(matching_page,),
                )
        else:
            st.caption("No sections match that search.")
    page = st.radio("Explore the project", PAGES, key="active_page", label_visibility="visible")
    st.markdown("---")
    st.markdown("**SKILLS · SHARE · GROW**")
    st.caption("A desktop platform for showcasing skills, sharing talents and learning from peers.")


def header(kicker, title, subtitle=None):
    st.markdown(f'<div class="section-tag">{kicker}</div>', unsafe_allow_html=True)
    st.title(title)
    if subtitle:
        st.write(subtitle)


def card(title, body, icon="auto_awesome"):
    st.markdown(f'<div class="card"><div class="card-icon"><span class="material-icon" aria-hidden="true">{icon}</span></div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

if page == "Home":
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">PROJECT SHOWCASE · STUDENT COMMUNITY</div>
      <h1>StudentSkill Hub</h1>
      <p>A desktop platform for showcasing skills, sharing talents and learning from peers. It brings student profiles, skill discovery, peer requests and feedback together in one application.</p>
      <div style="margin-top:1.3rem;font-weight:700;letter-spacing:.16em;color:#d7eadf">SKILLS&nbsp;&nbsp; • &nbsp;&nbsp;SHARE&nbsp;&nbsp; • &nbsp;&nbsp;GROW</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### Discover what the project is about")
    st.write("StudentSkill Hub is designed to make the skills and experiences within a university community easier to discover. Students can introduce themselves, list their abilities, find peers with relevant skills and request support or collaboration.")
    a,b,c = st.columns(3)
    with a: card("Showcase", "Create a student profile and display skills, interests, portfolio items and achievements.", "account_box")
    with b: card("Connect", "Search for peers who have a particular skill or experience.", "search")
    with c: card("Collaborate", "Send and manage peer requests, then share feedback after collaboration.", "handshake")
    quick_a, quick_b = st.columns(2)
    with quick_a:
        st.button("Explore application modules", on_click=navigate_to, args=("Application Modules",))
    with quick_b:
        st.button("View the student workflow", on_click=navigate_to, args=("Student Workflow",))
    st.markdown("### Project at a glance")
    m1,m2,m3,m4 = st.columns(4)
    m1.metric("Application type", "Desktop")
    m2.metric("Main language", "Python")
    m3.metric("GUI framework", "Tkinter")
    m4.metric("Main user roles", "2")
    st.markdown('<div class="note"><b>Important:</b> StudentSkill Hub itself is a Python Tkinter desktop prototype. This Streamlit website is a separate information site created to explain the project and its idea.</div>', unsafe_allow_html=True)

elif page == "Problem & Proposed Idea":
    header("01 · BACKGROUND", "Problem Identification", "Why might a student skill-sharing platform be useful in a university community?")
    st.markdown("### The problem")
    points = [
        "Students have different academic, creative and practical skills that could benefit their peers.",
        "It may be difficult to discover who has a particular skill or experience within a campus community.",
        "Students need a simple way to present their abilities, connect with peers and request support.",
        "Without an organised platform, opportunities for peer learning and collaboration may be missed.",
    ]
    for i,p in enumerate(points,1):
        st.markdown(f'<div class="step"><b>{i:02d}</b> &nbsp; {p}</div>', unsafe_allow_html=True)
    st.markdown("### The proposed idea")
    st.write("StudentSkill Hub is a desktop application where university students can showcase skills and talents, discover peers, and request help from one another.")
    x,y,z,w = st.columns(4)
    with x: card("SHOWCASE", "Create a profile and list skills.", "account_box")
    with y: card("CONNECT", "Search for peers with relevant skills.", "link")
    with z: card("COLLABORATE", "Send and manage peer requests.", "handshake")
    with w: card("BUILD TRUST", "Share ratings and feedback.", "star")
    st.success("The goal is to make student-to-student knowledge sharing easier and more visible.")

elif page == "Project Objectives":
    header("02 · PURPOSE", "Project Objectives", "What the StudentSkill Hub application aims to provide.")
    objectives = [
        "Provide students with profiles to introduce themselves and their interests.",
        "Allow students to add, organise and display their skills and proficiency levels.",
        "Help users search and discover other students by skill.",
        "Support peer collaboration through requests, status tracking and feedback.",
        "Provide administrators with tools to manage accounts, moderate reports and view analytics.",
    ]
    for i,obj in enumerate(objectives,1):
        st.markdown(f'<div class="step"><b>Objective {i}</b><br>{obj}</div>', unsafe_allow_html=True)

elif page == "Target Users & Roles":
    header("03 · USERS", "Target Users and Roles", "The application provides different options depending on the signed-in user's role.")
    left,right = st.columns(2)
    with left:
        st.markdown("### :material/school: Student")
        for item in ["Register or sign in", "Manage personal profile", "Add skills and portfolio items", "Search for other students", "Send and track collaboration requests", "Give and receive feedback"]:
            st.markdown(f"- {item}")
    with right:
        st.markdown("### :material/admin_panel_settings: Administrator")
        for item in ["Access the administrator panel", "View the student directory", "Inspect and manage accounts", "Review reported content", "View campus activity analytics"]:
            st.markdown(f"- {item}")
    st.markdown('<div class="note">Role-based navigation means students and administrators see the screens and functions relevant to their responsibilities.</div>', unsafe_allow_html=True)

elif page == "Application Modules":
    header("04 · FEATURES", "Main Application Features", "The student and administrator areas are organised into the following modules.")
    modules = [
        ("Dashboard", "A starting point for student activity and key information.", "dashboard", "Student"),
        ("Profile", "Personal details, biography and student information.", "account_box", "Student"),
        ("Skills", "Add and manage skills, categories and proficiency.", "extension", "Student"),
        ("Search", "Discover students and skills using search and filters.", "manage_search", "Discovery"),
        ("Portfolio", "Present work, projects and achievements.", "folder_open", "Student"),
        ("Requests", "Accept, decline and track peer collaboration requests.", "mail", "Collaboration"),
        ("Feedback", "Submit ratings and written reviews after collaboration.", "star", "Collaboration"),
        ("Admin Panel", "Student directory, moderation and analytics.", "admin_panel_settings", "Administration"),
    ]
    categories = ["All", "Student", "Discovery", "Collaboration", "Administration"]
    filter_col, search_col = st.columns([1, 2])
    with filter_col:
        selected_category = st.selectbox("Filter by area", categories)
    with search_col:
        module_search = st.text_input("Search modules", placeholder="Search features by name or description")
    filtered_modules = [
        item for item in modules
        if (selected_category == "All" or item[3] == selected_category)
        and module_search.casefold() in f"{item[0]} {item[1]} {item[3]}".casefold()
    ]
    st.caption(f"Showing {len(filtered_modules)} of {len(modules)} modules")
    for start in range(0, len(filtered_modules), 2):
        c1,c2 = st.columns(2)
        for col, item in zip((c1,c2), filtered_modules[start:start+2]):
            with col: card(item[0],item[1],item[2])
    if not filtered_modules:
        st.info("No modules match those filters. Try another category or search term.")

elif page == "Student Workflow":
    header("05 · USER JOURNEY", "How a Student Uses the System", "A typical flow from signing in to providing feedback.")
    workflow = [
        ("Sign in", "Student accesses their account."),
        ("Build profile", "Add personal information and skills."),
        ("Find a peer", "Search for a student with a needed skill."),
        ("Send request", "Explain the support or collaboration needed."),
        ("Collaborate", "The recipient accepts or declines the request."),
        ("Give feedback", "Submit a rating and written review after completion."),
    ]
    for i,(title,desc) in enumerate(workflow,1):
        st.markdown(f'<div class="step"><span style="color:#4b8b70;font-weight:800">STEP {i}</span><br><b>{title}</b><br>{desc}</div>', unsafe_allow_html=True)
    st.caption("Workflow shown is based on the implemented student request and feedback screens.")

elif page == "System Architecture":
    header("06 · TECHNICAL DESIGN", "System Architecture", "The project separates the interface, application logic, data handling and supporting utilities.")
    layers = [
        ("USER INTERFACE", "Tkinter screens and reusable widgets", "Screens, forms and visual components"),
        ("APPLICATION LAYER", "Session handling, navigation and role-based screens", "Coordinates user interaction and application flow"),
        ("DATA LAYER", "DataStore using pandas DataFrames", "Provides data structures and data operations"),
        ("SUPPORTING MODULES", "Validation, helper functions, charts and analytics", "Reusable functions used across the application"),
    ]
    for i,(name,detail,extra) in enumerate(layers):
        st.markdown(f'<div class="step" style="text-align:center;border-left:0;border-top:4px solid #4b8b70"><b>{name}</b><br>{detail}<br><span style="color:#75847b;font-size:.88rem">{extra}</span></div>', unsafe_allow_html=True)
        if i != len(layers)-1: st.markdown("<div style='text-align:center;color:#4b8b70;font-size:1.2rem'>↓</div>", unsafe_allow_html=True)
    st.info("The project is divided into modules to keep screens, data operations and utilities organised.")

elif page == "Data Organisation":
    header("07 · DATA DESIGN", "Main Data Entities", "The project presentation identifies these logical data entities.")
    entities = [
        ("Students", "Student account and profile information."),
        ("Skills", "Skills linked to a student."),
        ("Achievements", "Student achievements."),
        ("Portfolio", "Portfolio items linked to a student."),
        ("Requests", "Peer requests: requester, recipient, skill and status."),
        ("Feedback", "Ratings and comments linked to a request."),
        ("Reports", "Reported student or portfolio content."),
    ]
    for i in range(0,len(entities),2):
        c1,c2 = st.columns(2)
        with c1: card(entities[i][0],entities[i][1],"database")
        if i+1 < len(entities):
            with c2: card(entities[i+1][0],entities[i+1][1],"database")
    st.markdown('<div class="warn"><b>Data-storage note:</b> These are logical tables described in the project materials. The current prototype stores data in memory using pandas DataFrames; the data is not yet persisted in a database.</div>', unsafe_allow_html=True)

elif page == "Technology Stack":
    header("08 · DEVELOPMENT STACK", "Technologies and Tools", "Tools identified in the group's project presentation and requirements.")
    tech = [
        ("Python", "Main programming language used to implement the application.", "code"),
        ("Tkinter", "Desktop graphical user interface, screens, forms and navigation.", "desktop_windows"),
        ("Pandas", "DataFrames used by the in-memory data store.", "table_chart"),
        ("NumPy", "Used for analytics data generation and calculations.", "calculate"),
        ("Matplotlib", "Used to create charts displayed in the admin analytics area.", "bar_chart"),
    ]
    for i in range(0,len(tech),2):
        c1,c2 = st.columns(2)
        with c1: card(tech[i][0],tech[i][1],tech[i][2])
        if i+1 < len(tech):
            with c2: card(tech[i+1][0],tech[i+1][1],tech[i+1][2])
    st.caption("Dependencies listed in requirements.txt: pandas, numpy and matplotlib. Tkinter ships with Python.")

elif page == "Implementation Highlights":
    header("09 · CODE STRUCTURE", "Implementation Highlights", "Key files and responsibilities in the project codebase.")
    items = [
        ("main.py", "Starts the Tkinter application."),
        ("app.py", "Manages the application window, signed-in user, navigation and role-based screens."),
        ("data/store.py", "Provides the DataStore and data operations using pandas DataFrames."),
        ("utils/validators.py", "Contains input-validation functions that return a result and message."),
        ("widgets/components.py and widgets/shell.py", "Organise reusable interface elements."),
        ("Administrator area", "Includes a student directory, content moderation and analytics charts."),
    ]
    for name,desc in items:
        st.markdown(f'<div class="step"><code>{name}</code><br>{desc}</div>', unsafe_allow_html=True)

elif page == "Live Demonstration Plan":
    header("10 · DEMONSTRATION", "What to Show Live", "Suggested sequence for demonstrating the implemented desktop application.")
    demos = [
        ("Login", "Sign in using a student account; show role-based navigation."),
        ("Profile and skills", "Open the profile and skills pages; demonstrate adding or editing information."),
        ("Search and portfolio", "Find a peer and view skills or portfolio items."),
        ("Requests", "Show an incoming request and its status actions."),
        ("Feedback", "Show the feedback form and rating interaction."),
        ("Admin", "Sign in as administrator; show directory, moderation and analytics."),
    ]
    for i,(name,desc) in enumerate(demos,1):
        st.markdown(f'<div class="step"><b>{i}. {name}</b><br>{desc}</div>', unsafe_allow_html=True)
    st.warning("Use screenshots captured from your own running application during the presentation if available. This information website does not replace the live desktop-app demonstration.")

elif page == "Limitations & Future Improvements":
    header("11 · CURRENT STATUS", "Limitations and Future Improvements", "The project presentation distinguishes the current prototype from planned next steps.")
    left,right = st.columns(2)
    with left:
        st.markdown("### Current limitations")
        for item in ["Data is stored in memory only.","Changes are lost when the program closes.","The application uses seeded/static sample data.","It is a desktop prototype rather than a deployed multi-user service."]:
            st.markdown(f"- {item}")
    with right:
        st.markdown("### Future improvements")
        for item in ["Connect a persistent database such as SQLite.","Add secure password hashing and stronger account security.","Support real multi-user access and deployment.","Improve testing, accessibility and user documentation."]:
            st.markdown(f"- {item}")
    st.markdown('<div class="note">The future improvements are proposed next steps; they should not be presented as features already completed in the current prototype.</div>', unsafe_allow_html=True)

elif page == "Conclusion & Sources":
    header("12 · WRAP-UP", "Making Student Skills Easier to Discover and Share", "StudentSkill Hub brings student profiles, skill discovery, peer requests and feedback into one desktop application.")
    st.markdown('<div class="hero"><div class="eyebrow">CONCLUSION</div><h1>Skills · Share · Grow</h1><p>StudentSkill Hub provides a foundation for a more connected and collaborative campus community.</p><div style="font-weight:700;margin-top:1rem">THANK YOU · QUESTIONS AND DISCUSSION</div></div>', unsafe_allow_html=True)
    st.markdown("### Project references and resources")
    st.markdown("- StudentSkill Hub project source code and README.md (group project materials).\n- Project requirements.txt: pandas, numpy and matplotlib.\n- [Python documentation](https://docs.python.org/3/)\n- [Tkinter documentation](https://docs.python.org/3/library/tkinter.html)\n- [Pandas documentation](https://pandas.pydata.org/docs/)\n- [NumPy documentation](https://numpy.org/doc/)\n- [Matplotlib documentation](https://matplotlib.org/stable/)")

st.markdown('<div class="footer">StudentSkill Hub · Project Information Website · Based on the group project presentation and supplied project materials.</div>', unsafe_allow_html=True)
