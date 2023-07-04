import streamlit as st
import snowflake.snowpark import Session

st.title('Streamlit to Snowflake')

# established snowflake connection
@st.cache_resource
def create_session():
  return Session.builder.configs(st.secrets.snowflake).create()

session = create_session()
st.success("Connected to Snowflake!")
