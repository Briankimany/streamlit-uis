import streamlit as st

# Predefined recipient and email content
recipient_email = "btmaize@biosafetykenya.go.ke"
subject = "Opposition to BT Maize"
body = """
Dear Sir/Madam,

Re: Opposition to the Proposed Release and Placement of BT Maize Varieties on the Market

I am writing to express my strong concerns regarding the proposal to release and place BT maize varieties on the Kenyan market. 
While I acknowledge the potential benefits of agricultural biotechnology, I firmly believe that the risks and implications associated with BT maize require careful and thorough consideration before any such approval is granted.

• Loss of traditional crop diversity: 
   Kenya has a rich agricultural heritage, with many traditional crops that are well-suited to the local climate and soil conditions. 
   The introduction of GMOs could lead to the loss of these traditional varieties, as farmers may be encouraged to adopt GMOs instead. This could result in a loss of genetic diversity, making crops more vulnerable to disease and pests.

• Dependence on foreign corporations:
   Many GMOs are developed and patented by foreign corporations, which could lead to a loss of control over Kenya's food system. 
   If Kenyan farmers become dependent on GMOs, they may be forced to purchase seeds and other inputs from these corporations, rather than being able to save and exchange seeds as they have traditionally done.

• Uncertainty about long-term health effects: 
  While the scientific consensus is that GMOs are safe to eat, some people may still be concerned about the potential long-term health effects of consuming GMOs. 
  There is limited research on the health effects of GMOs, and some people may prefer to err on the side of caution and stick to traditional foods.

• Risk of contamination of traditional crops: 
  GMOs can cross-breed with traditional crops, potentially altering their genetic makeup. 
  This could result in the loss of traditional crop varieties, as well as the introduction of unwanted traits into non-GMO crops.

• Cultural and spiritual significance of traditional foods: 
  For many Kenyans, traditional foods are not just a source of nutrition, but also an important part of their cultural and spiritual heritage. 
  The introduction of GMOs could be seen as a threat to these traditional practices and ways of life, and some people may prefer to stick with the foods that have been passed down to them through generations.

Thank you for considering my views on this critical matter. I trust that the NBA will prioritize the health, environment, and socio-economic well-being of the people of Kenya in its decision-making process.

Yours faithfully,
[Your Contact Information]
"""

# Define replacement strings
newline_replacement = '%0A'
space_replacement = '%20'
left_bracket_replacement = '%5B'
right_bracket_replacement = '%5D'

# Generate the mailto link


st.title("Send Your Opposition to BT Maize")


NAME = st.text_input("Your Name:  ")
if NAME:
    body = body.replace("[Your Contact Information]",  NAME)

    if st.button("Submit"):
        st.text_area("Edit the email body", value=body, height=300)
      
        mailto_link = "mailto:" + recipient_email + "?subject=" + subject.replace(" ", space_replacement) + "&body=" + body.replace(" ", space_replacement).replace("\n", newline_replacement).replace("[", left_bracket_replacement).replace("]", right_bracket_replacement)

        st.link_button("Send ", mailto_link )
        st.write("Click the button below to open your email app and send your feedback:")
        st.markdown("[ Send Email](" + mailto_link + ")", unsafe_allow_html=True)