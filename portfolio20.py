import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import base64
import os

# Page Config
st.set_page_config(page_title="Zaid Ahamed", layout="wide")

# Helper to embed image
def get_img_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def render_skill_badges(skills):
    badges = ""
    for skill in skills.split(","):
        skill = skill.strip()
        badges += f'<span style="color:black;background-color:#eee;border-radius:10px;padding:5px 10px;margin:3px;display:inline-block;font-size:12px;">{skill}</span>'
    return badges

def render_skill_icons(skills):
    badges = ""
    for skill in skills.split(","):
        skill = skill.strip().lower().replace(" ", "_")
        icon_path = f"Skills/{skill}.png"
        if os.path.exists(icon_path):
            badges += f'<img src="data:image/png;base64,{get_img_base64(icon_path)}" title="{skill}" style="height:100px; margin:10px;">'
        else:
            badges += f'<span style="background:#eee;padding:4px 10px;border-radius:12px;margin:3px;font-size:13px;">{skill}</span>'
    return badges



# def display_certificate(image_path, name, platform, date):
#     cert_img = Image.open(image_path)
#     with st.container():
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             st.image(cert_img.resize((400, 300)))
#         with col2:
#             st.markdown(f"<h5 style='margin-bottom:5px;'>{name}</h5>", unsafe_allow_html=True)
#             st.write(f"**Platform:** {platform}")
#             st.write(f"**Date:** {date}")
#             st.markdown("---")

def display_certificate_grid(certificates):
    for row in range(0, len(certificates), 3):
        cols = st.columns(3)
        for i in range(3):
            if row + i < len(certificates):
                cert = certificates[row + i]
                with cols[i]:
                    st.markdown(
                        f"""
                        <div style='border: 2px solid #ccc; padding: 15px; border-radius: 12px; background-color: #DFE2DF; margin: 10px'>
                            <img src='data:image/png;base64,{get_img_base64(cert['image'])}' style='width:100%; height:320px; object-fit: contain; border-radius: 8px;'/>
                            <h5 style='margin-top:10px; margin-bottom:5px; color: #303630;'>{cert['name']}</h5>
                            <div style='display: flex; justify-content: space-between; align-items: center; margin-top: 5px;'>
                                <p style='margin: 0; font-size: 16px; color: #434C43;'>{cert['platform']}</p>
                                <p style='margin: 0; font-size: 16px; color: #434C43;'>{cert['date']}</p>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


# def display_project(image_path, title, description, skills, github_link):
#     with st.expander(title):
#         col1, col2 = st.columns([1, 2])
#         with col1:
#             image = Image.open(image_path)
#             st.image(image.resize((450, 300)), use_container_width=False)
#         with col2:
#             st.write(description)
#             st.markdown(render_skill_badges(skills), unsafe_allow_html=True)
#             st.markdown(f"[🔗 GitHub Repo]({github_link})")



def display_project(image_path, title, description, skills, github_link):
    with st.expander(title):
        col1, col2 = st.columns([1, 2])
        with col1:
            image = Image.open(image_path)
            st.image(image.resize((450, 300)), use_container_width=False)
        with col2:
            st.markdown(description)
            st.markdown(render_skill_badges(skills), unsafe_allow_html=True)
            st.markdown(f"[🔗 GitHub Repo]({github_link})")



# Top Navigation Bar
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Projects", "Contact"],
    icons=["house", "person", "folder", "envelope"],
    orientation="horizontal",
)

# Home
if selected == "Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        image = Image.open("PP4.png")
        st.image(image.resize((400, 400)), use_container_width=False)
    with col2:
        st.title("Zaid Ahamed")
        st.subheader("Data Engineer | Data Analyst")
        st.write("Passionate about delivering data-driven solutions for real-world problems.")

        st.markdown(f"""
        <style>
        .icon-container {{
            display: flex;
            align-items: center;
            gap: 20px;
            margin-top: 15px;
        }}
        .icon-container img {{
            width: 32px;
            height: 32px;
        }}
        </style>
        <div class="icon-container">
            <a href="https://www.linkedin.com/in/zaidahamed055/" target="_blank" title="LinkedIn">
                <img src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4nICAnaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkJz48c3ZnIGhlaWdodD0iMTAwJSIgc3R5bGU9ImZpbGwtcnVsZTpldmVub2RkO2NsaXAtcnVsZTpldmVub2RkO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2UtbWl0ZXJsaW1pdDoyOyIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgd2lkdGg9IjEwMCUiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6c2VyaWY9Imh0dHA6Ly93d3cuc2VyaWYuY29tLyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxnIGlkPSJnNTg5MSI+PHBhdGggZD0iTTUxMiw2NGMwLC0zNS4zMjMgLTI4LjY3NywtNjQgLTY0LC02NGwtMzg0LDBjLTM1LjMyMywwIC02NCwyOC42NzcgLTY0LDY0bDAsMzg0YzAsMzUuMzIzIDI4LjY3Nyw2NCA2NCw2NGwzODQsMGMzNS4zMjMsMCA2NCwtMjguNjc3IDY0LC02NGwwLC0zODRaIiBpZD0iYmFja2dyb3VuZCIgc3R5bGU9ImZpbGw6IzI4NjdiMjsiLz48ZyBpZD0ic2hhcGVzIj48cmVjdCBoZWlnaHQ9IjI1Ny45NjIiIGlkPSJyZWN0MTEiIHN0eWxlPSJmaWxsOiNmZmY7IiB3aWR0aD0iODUuNzYiIHg9IjYxLjA1MyIgeT0iMTc4LjY2NyIvPjxwYXRoIGQ9Ik0xMDQuNTEyLDU0LjI4Yy0yOS4zNDEsMCAtNDguNTEyLDE5LjI5IC00OC41MTIsNDQuNTczYzAsMjQuNzUyIDE4LjU4OCw0NC41NzQgNDcuMzc3LDQ0LjU3NGwwLjU1NCwwYzI5LjkwMywwIDQ4LjUxNiwtMTkuODIyIDQ4LjUxNiwtNDQuNTc0Yy0wLjU1NSwtMjUuMjgzIC0xOC42MTEsLTQ0LjU3MyAtNDcuOTM1LC00NC41NzNaIiBpZD0icGF0aDEzLTAiIHN0eWxlPSJmaWxsOiNmZmY7ZmlsbC1ydWxlOm5vbnplcm87Ii8+PHBhdGggZD0iTTM1Ny4yNzgsMTcyLjYwMWMtNDUuNDksMCAtNjUuODY2LDI1LjAxNyAtNzcuMjc2LDQyLjU4OWwwLC0zNi41MjNsLTg1LjczOCwwYzEuMTM3LDI0LjE5NyAwLDI1Ny45NjEgMCwyNTcuOTYxbDg1LjczNywwbDAsLTE0NC4wNjRjMCwtNy43MTEgMC41NTQsLTE1LjQyIDIuODI3LC0yMC45MzFjNi4xODgsLTE1LjQgMjAuMzA1LC0zMS4zNTIgNDMuOTkzLC0zMS4zNTJjMzEuMDEyLDAgNDMuNDM2LDIzLjY2NCA0My40MzYsNTguMzI3bDAsMTM4LjAybDg1Ljc0MSwwbDAsLTE0Ny45M2MwLC03OS4yMzcgLTQyLjMwNSwtMTE2LjA5NyAtOTguNzIsLTExNi4wOTdaIiBpZD0icGF0aDE1IiBzdHlsZT0iZmlsbDojZmZmO2ZpbGwtcnVsZTpub256ZXJvOyIvPjwvZz48L2c+PC9zdmc+" alt="LinkedIn">
            </a>
            <a href="https://github.com/zaid638" target="_blank" title="GitHub">
                <img src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4nICAnaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkJz48c3ZnIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDEyOCAxMjgiIGlkPSJTb2NpYWxfSWNvbnMiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDEyOCAxMjgiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxnIGlkPSJfeDMxX19zdHJva2UiPjxnIGlkPSJHaXRodWJfMV8iPjxyZWN0IGNsaXAtcnVsZT0iZXZlbm9kZCIgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBoZWlnaHQ9IjEyOCIgd2lkdGg9IjEyOCIvPjxwYXRoIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTYzLjk5NiwxLjMzM0MyOC42NTYsMS4zMzMsMCwzMC4wOTksMCw2NS41OTEgICAgYzAsMjguMzg0LDE4LjMzNiw1Mi40NjcsNDMuNzcyLDYwLjk2NWMzLjIsMC41OSw0LjM2OC0xLjM5NCw0LjM2OC0zLjA5NmMwLTEuNTI2LTAuMDU2LTUuNTY2LTAuMDg4LTEwLjkyNyAgICBjLTE3LjgwNCwzLjg4My0yMS41Ni04LjYxNC0yMS41Ni04LjYxNGMtMi45MDgtNy40MjEtNy4xMDQtOS4zOTctNy4xMDQtOS4zOTdjLTUuODEyLTMuOTg4LDAuNDQtMy45MDcsMC40NC0zLjkwNyAgICBjNi40MiwwLjQ1NCw5LjgsNi42MjIsOS44LDYuNjIyYzUuNzEyLDkuODE5LDE0Ljk4LDYuOTg0LDE4LjYyOCw1LjMzN2MwLjU4LTQuMTUyLDIuMjM2LTYuOTg0LDQuMDY0LTguNTkgICAgYy0xNC4yMTItMS42MjItMjkuMTUyLTcuMTMyLTI5LjE1Mi0zMS43NTNjMC03LjAxNiwyLjQ5Mi0xMi43NSw2LjU4OC0xNy4yNDRjLTAuNjYtMS42MjYtMi44NTYtOC4xNTYsMC42MjQtMTcuMDAzICAgIGMwLDAsNS4zNzYtMS43MjcsMTcuNiw2LjU4NmM1LjEwOC0xLjQyNiwxMC41OC0yLjEzNiwxNi4wMjQtMi4xNjVjNS40MzYsMC4wMjgsMTAuOTEyLDAuNzM5LDE2LjAyNCwyLjE2NSAgICBjMTIuMjE2LTguMzEzLDE3LjU4LTYuNTg2LDE3LjU4LTYuNTg2YzMuNDkyLDguODQ3LDEuMjk2LDE1LjM3NywwLjYzNiwxNy4wMDNjNC4xMDQsNC40OTQsNi41OCwxMC4yMjgsNi41OCwxNy4yNDQgICAgYzAsMjQuNjgxLTE0Ljk2NCwzMC4xMTUtMjkuMjIsMzEuNzA1YzIuMjk2LDEuOTg0LDQuMzQ0LDUuOTAzLDQuMzQ0LDExLjg5OWMwLDguNTktMC4wOCwxNS41MTctMC4wOCwxNy42MjYgICAgYzAsMS43MTksMS4xNTIsMy43MTksNC40LDMuMDg4QzEwOS42OCwxMTguMDM0LDEyOCw5My45NjcsMTI4LDY1LjU5MUMxMjgsMzAuMDk5LDk5LjM0NCwxLjMzMyw2My45OTYsMS4zMzMiIGZpbGw9IiMzRTc1QzMiIGZpbGwtcnVsZT0iZXZlbm9kZCIgaWQ9IkdpdGh1YiIvPjwvZz48L2c+PC9zdmc+" alt="GitHub">
            </a>
        </div>
        """, unsafe_allow_html=True)
    

# About
elif selected == "About":
    st.header("About Me")
    tabs = st.tabs(["About Me", "Skills", "Experience", "Education", "Certifications"])

    with tabs[0]:
        st.subheader("Who I Am")
        st.markdown("""
        <div style='text-align: justify; font-size: 18px;'>
        
        <br>
        I am a <strong>Data Engineer</strong> and <strong>Data Analytics Expert</strong> with hands-on experience in modern data tools. I specialize in building data pipelines, designing data models, performing data cleaning and transformation, and crafting insightful dashboards that empower businesses to make data-driven decisions.

        <br><br>
        ✅ <strong>Data Engineering Expertise</strong><br>
        <ul>
        <li>Designing and implementing ETL/ELT pipelines using Python and SQL.</li>
        <li>Experience with orchestration tools like <strong>Apache Airflow</strong>.</li>
        <li>Building scalable data solutions using <strong>PySpark</strong>, <strong>Snowflake</strong>, <strong>PostgreSQL</strong>, and cloud services like <strong>AWS</strong>.</li>
        </ul>

        <br><br>                    
        ✅ <strong>Analytics & Business Intelligence</strong><br>
        <ul>
        <li>Proficient in creating interactive dashboards with <strong>Power BI</strong> and <strong>Excel</strong>.</li>
        <li>Uncovering actionable insights to drive business growth and operational efficiency.</li>
        <li>Expertise in data cleaning, transformation, and visualization.</li>
        </ul>

        <br><br>
        ✅ <strong>Real-World Project Experience</strong><br>
        <ul>
        <li>Developed and maintained an ETL pipeline for a <strong>Google Earth Engine</strong> data project, storing time-series data in <strong>PostgreSQL</strong> for analytics.</li>
        <li>Designed an end-to-end ETL pipeline with metadata and validation for a marketing agency.</li>
        <li>Built a <strong>Job Analysis Dashboard</strong> using data scraped from job boards — automated the ETL process, analyzed job trends, and visualized key metrics in Power BI.</li>
        <li>Created analytics solutions for a luxury hotel chain, helping them regain market share through KPI dashboards and actionable insights.</li>
        </ul>

        <br>
        🌟 <em>Clear and effective communication from project start to finish.</em><br>
        🌟 <em>Solutions tailored to your business challenges.</em><br>
        🌟 <em>On-time delivery and commitment to excellence.</em>

        <br><br>
        💬 <strong>Let’s connect to discuss how I can bring my expertise to your team!</strong>

        </div>
        """, unsafe_allow_html=True)

    with tabs[1]:
        # st.subheader("Technical Skills")
        # st.markdown("""
        # - **Languages**: Python, SQL
        # - **Data Engineering**: Apache Airflow, ETL, PostgreSQL, Google Earth Engine, APIs
        # - **Data Analysis**: Pandas, NumPy, Matplotlib, Power BI, Tableau
        # - **Cloud & Tools**: AWS S3, Docker, Streamlit, Git, Linux
        # - **Web**: Web Scraping (BeautifulSoup), HTML, CSS
        # """)
        st.markdown(render_skill_icons("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17"), unsafe_allow_html=True)



    with tabs[2]:
        st.subheader("Experience")
        st.write("**Data Engineering Intern (Oct 2022 - Present)**")
        st.write("NCAI (National Center for Artificial Intelligence)")
        st.markdown("""   
          - Developed solutions for extracting and storing large satellite image datasets, ensuring efficient data handling.
          - Created robust, production-ready ETL pipelines to efficiently extract satellite image data from Google Earth Engine, transforming and loading it into PostgreSQL for analysis and reporting.
        """)

    with tabs[3]:
        st.subheader("Education")
        st.write("B.E. in Computer Systems Engineering — Final Year")
        st.write("NED University of Engineering and Technology, Karachi, Pakistan")

    with tabs[4]:
        st.subheader("Certifications")
        # display_certificate("Portfolio/cert_data_engineer.png", "Associate Data Engineer", "DataCamp", "2024")
        # display_certificate("Portfolio/cert_aws.png", "AWS Cloud Practitioner (CLF-C02)", "DataCamp", "2024")
        # display_certificate("Portfolio\Certifications\Google Advanced Data Analytics.jpg", "Advanced Data Analytics Specialization", "Google", "2024")
        # display_certificate("Portfolio/cert_ibm_analytics.png", "Data Analytics Specialization", "IBM", "2023")
        certificate_list = [
            {"image": "Certifications/AWS_Cloud_Practitioner.png", "name": "AWS Cloud Practitioner (CLF-C02)", "platform": "DataCamp", "date": "2025"},
            {"image": "Certifications/Data_Engineer_in_Python.png", "name": "Data Engineer in Python", "platform": "DataCamp", "date": "2025"},
            {"image": "Certifications/Associate_Data_Engineer.png", "name": "ASSOCIATE DATA ENGINEER", "platform": "DataCamp", "date": "2024"},
            {"image": "Certifications/Associate_Data_Engineer_in_SQL.png", "name": " Associate Data Engineer in SQL", "platform": "DataCamp", "date": "2024"},
            {"image": "Certifications/Google_Advanced_Data_Analytics.png", "name": "Advanced Data Analytics Specialization", "platform": "Coursera", "date": "2024"},
            {"image": "Certifications/IBM_Data_Analyst.png", "name": "Advanced Data Analytics Specialization", "platform": "Coursera", "date": "2023"}
        ]
        display_certificate_grid(certificate_list)


# Projects
elif selected == "Projects":
    st.header("Projects")
    tabs = st.tabs(["Data Engineering", "Data Analysis"])

    with tabs[0]:
        display_project("projects/GEE_ETL_Diagram.png", "Satellite Image Data Extraction Project", 
                        """
                        - Created robust, production-ready ETL pipelines to efficiently extract satellite image data from Google Earth Engine.
                        - Transformed and loaded data into PostgreSQL for analysis and reporting.
                        - Built with error handling, scalable, and automation support.
                        - Developed Webapp using Streamlit for Visualize the NDVI data.
                        """, "Python, SQL, PostgreSQL, ETL, Google Earth Engine, Streamlit", "https://github.com/zaid638/GEE-Data-Extraction")
        display_project("projects/Job_Analysis_ETL_Diagram.png", "Job Analysis Project",
                        """
                        - Developed an ETL pipeline using Python and created an interactive dashboard with PowerBI to analyze job postings.  
                        - Identified trends and insights in job requirements, skills, education levels, and experience to inform job seekers and recruiters.
                        """, "Python, Pandas, BeautifulSoupWeb, Power BI, Excel, Web Scraping", "https://github.com/zaid638/Job-Analysis-Project")
        display_project("projects/Marketing_ETL_Diagram.png", "Marketing ETL Pipeline Project", 
                        """
                        - Developed a Python-based ETL pipeline to process customer data from Excel, leveraged pandas for efficient data manipulation. 
                        - Demonstrated proficient database integration by loading US customer records to MySQL and UK/India customer records to PostgreSQL. 
                        - Generated comprehensive metadata in JSON format for enhanced data governance and traceability.
                        """, "Python, SQL, Excel, MySQL, PostgreSQL", "https://github.com/zaid638/Marketing-ETL-Pipeline")
        display_project("projects/Retail_ETL_Diagram.png", "Retail Data Pipeline Project", 
                        """
                        - Developed a data pipeline for analyzing supply and demand patterns, particularly around holidays. 
                        - Conducted preliminary data analysis to extract initial insights.
                        """, "Python, SQL, Excel, PostgreSQL", "https://github.com/zaid638/Data-Camp-Projects/tree/main")
        display_project("projects/17.png", "Cleaning an Orders Dataset with PySpark Project", 
                        """
                        - In this project, I work with an e-commerce company and use PySpark for data processing, to clean an orders dataset. 
                        - A peer Machine Learning team has requested me to clean the data containing the information about orders made last year. They are planning to further use this cleaned data to build a demand forecasting model. To achieve this, they have shared their requirements regarding the desired output format.
                        """, "Python, PySpark", "https://github.com/zaid638/Data-Camp-Projects")

    with tabs[1]:
        display_project("projects/Dashboard1.png", "Job Analysis Project", 
                        """
                        - Created an ETL pipeline using Python to clean and transform job posting data, then built a dashboard using Power BI to analyze trends in job requirements and skills. 
                        - Demonstrated ability to turn raw data into actionable insights for understanding market dynamics.
                        """, "Python, Pandas, Web Scraping, PowerBI, Excel", "https://github.com/zaid638/Job-Analysis-Project")
        display_project("projects/Dashboard2.png", "AtliQ Grands Hotel Dashboard", 
                        """
                        - A BI Dashboard created for a luxury hotel chain to analyze the Data and give required insights and recommendations.
                        """, "Python,  Excel, Power BI, DAX, Data Visualization", "https://github.com/zaid638/Analysis-of-AtliQ-Grands-Hospitality-Domain")
        # display_project("Portfolio/projects/Dashboard3.png", "Technology Trend Analysis", " Analyzed real-world datasets, created visualizations & interactive dashboards, and presented reports on data analysis findings. The findings of this analysis offer valuable insights into the trends shaping the technological landscape in programming language, databases, platforms, web frameworks sectors.", "Python, SQL, Tableau, Excel", "https://github.com/zaid638/IBM-Capstone-Project")
        # display_project("Portfolio/projects/GEE_ETL_Diagram.png", "Cricket Analysis", "Prepared banking campaign data by handling nulls, deduplication, and column normalization.", "Data Cleaning, Pandas, Excel", "https://github.com/zaid638/BankMarketingCleaning")
        # display_project("Portfolio/projects/GEE_ETL_Diagram.png", "Fire Emergency Analysis", "Prepared banking campaign data by handling nulls, deduplication, and column normalization.", "Data Cleaning, Pandas, Excel", "https://github.com/zaid638/BankMarketingCleaning")



# Contact
elif selected == "Contact":
    st.write("---")
    st.header("Contact Me")
    contact_form = """
    <form action="https://formsubmit.co/ebd04fde33f077150535abf5f99d5909" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 8px; margin-bottom: 10px;"><br>
        <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 8px; margin-bottom: 10px;"><br>
        <textarea name="message" placeholder="Your message" rows="5" required style="width: 100%; padding: 8px; margin-bottom: 10px;"></textarea><br>
        <button type="submit" style="padding: 10px 20px; background-color: #1a3355; color: white; border: none;">Send</button>
        <input type="hidden" name="_next" value="https://zaid-ahamed.streamlit.app/">
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    st.write("Or email me directly at 📧 zaidahamed638@gmail.com")


# ---- STYLING ----
st.markdown("""
<style>
    input, textarea {
        width: 100%;
        padding: 0.5em;
        margin: 0.5em 0;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    button {
        padding: 0.7em;
        border: none;
        border-radius: 5px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


