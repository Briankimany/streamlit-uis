import streamlit as st

# Predefined recipient and email content
recipient_email = "briangatu4@gmail.com"
subject = "Opposition to BT Maize"
body = """
Dear Sir/Madam,

Re: Opposition to the Proposed Release and Placement of BT Maize Varieties

I am writing to express my strong opposition to the proposed release and placement of BT maize varieties on the market. 

[You can add more points here.]

Thank you for considering this important issue.

Yours sincerely,
[Your Name]
[Your Contact Information]
"""

# Define replacement strings
newline_replacement = '%0A'
space_replacement = '%20'
left_bracket_replacement = '%5B'
right_bracket_replacement = '%5D'

# Generate the mailto link
mailto_link = "mailto:" + recipient_email + "?subject=" + subject.replace(" ", space_replacement) + "&body=" + body.replace(" ", space_replacement).replace("\n", newline_replacement).replace("[", left_bracket_replacement).replace("]", right_bracket_replacement)

# Streamlit UI
st.title("Send Your Opposition to BT Maize")
st.write("Click the button below to open your email app and send your feedback:")
st.markdown("[ Send Email](" + mailto_link + ")", unsafe_allow_html=True)