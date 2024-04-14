import streamlit as st

def main():
    st.title('Streamlit App : Add Title here')
    st.write('Here is an example of ...Add Description here:')

    # Embed the Hugging Face chatbot using an iframe
    chatbot_url = "https://hf.co/chat/assistant/661b432f5693cfc26defd2c3"
    st.markdown(f'<iframe src="{chatbot_url}" width="700" height="500"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
