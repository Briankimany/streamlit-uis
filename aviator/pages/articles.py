import streamlit as st
import streamlit.components.v1 as components
import json

# Streamlit App Title
st.title("Article Title Placeholder Replacer")

# User input
user_input = st.text_input("Enter the article title:", placeholder="Type your article title here")

# Template where the placeholder 'ARTICLE_TITLE' will be replaced
template = '''Write an original, SEO-optimized article based on the article "ARTICLE_TITLE"" ,
should be informative, engaging, and offer actionable tips for readers aiming to enhance 
their financial freedom.

Requirements:
Structure:

Include headings and subheadings to organize content effectively.
Use bullet points to break down complex information for better readability.
Content:

Ensure the article is unique and plagiarism-free.
Incorporate relevant statistics, examples, and case studies to enhance credibility.
Use rich media suggestions (e.g., images or videos) to support the text.
Readability:

Aim for shorter sentences. Avoid having more than 20 words in a sentence; keep it under the recommended maximum of 25%.
Use simpler vocabulary to improve the Flesch reading ease score.
Try to make shorter sentences, using less difficult words to improve readability.
Use transition words throughout the article to enhance flow and coherence.
SEO Optimization:

Target keywords related to IT effectively to attract organic traffic.
Include internal links to relevant content and external links to authoritative sources.
Length:

Aim for approximately 1300 words, ensuring that the meta description is concise and under 160 characters.
By following these guidelines, create a compelling article that not only informs but also empowers readers to take actionable steps toward financial independence.

'''

# Button to generate the replaced code
if st.button("Generate Code"):
    if user_input:
        # Replace the placeholder with the user's input
        filled_template = template.replace("ARTICLE_TITLE", user_input)
        
        # Display the updated content in a code block
        st.code(filled_template, language="markdown")
        
        # Optionally provide a success message
        st.success("The placeholder has been replaced. You can copy the code above.")
        
        # Create a copy to clipboard button
        copy_button = f"""
        <button onclick="navigator.clipboard.writeText({json.dumps(filled_template)}); 
        document.getElementById('copy-success').style.display = 'block';" 
        style="
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        ">
        """

        # Render the button
        components.html(copy_button, height=60)

    else:
        st.warning("Please enter an article title before generating the code.")
