import os
import streamlit as st
from dotenv import load_dotenv
import streamlit_authenticator as stauth # pip install streamlit-authenticator
from streamlit_authenticator.utilities import LoginError
import yaml
from yaml.loader import SafeLoader
from process_files import process_files_tab
from explore_data import explore_data_tab
from instructions import instructions_tab

# Load environment variables
load_dotenv()

# Set the page layout to wide
st.set_page_config(layout="wide")
# Construct the absolute path to the config file
config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')

# Loading config file
with open(config_path, 'r', encoding= 'utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)
# Creating a login widget
try:
    authenticator.login()
except LoginError as e:
    st.error(e)

if st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
elif st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    def initialize_session_state():
        env_vars = {
            'system_prompt': "SYSTEM_PROMPT",
            'schema': "OUTPUT_SCHEMA",
            'blob_conn_str': "BLOB_CONN_STR",
            'container_name': "CONTAINER_NAME",
            'cosmos_url': "COSMOS_URL",
            'cosmos_key': "COSMOS_KEY",
            'cosmos_db_name': "COSMOS_DB_NAME",
            'cosmos_documents_container_name': "COSMOS_DOCUMENTS_CONTAINER_NAME",
            'cosmos_config_container_name': "COSMOS_CONFIG_CONTAINER_NAME"
        }
        for var, env in env_vars.items():
            if var not in st.session_state:
                st.session_state[var] = os.getenv(env)

    # Initialize the session state variables
    initialize_session_state()


    # Tabs navigation
    title = st.header("ARGUS: Automated Retrieval and GPT Understanding System")
    tabs = st.tabs(["🧠 Process Files", "🔎 Explore Data", "🖥️ Instructions"])

    # Render the tabs
    with tabs[0]:
        process_files_tab()
    with tabs[1]:
        explore_data_tab()
    with tabs[2]:
        instructions_tab()
