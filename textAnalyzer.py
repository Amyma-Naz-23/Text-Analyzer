import streamlit as st
import re

def count_vowels(text):
    return len(re.findall(r'[aeiouAEIOU]', text))

def count_consonants(text):
    return len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text))

def main():
    st.set_page_config(page_title="Text Analyzer", layout="wide")
    st.title("📊 Enhanced Text Analyzer")
    st.markdown("---")
    
    # User Input Section
    st.header("📝 Enter Text")
    text = st.text_area("Enter your paragraph:", "", height=150)
    
    if text.strip():
        # Creating Layout Columns
        col1, col2 = st.columns(2)
        
        # Word and Character Count
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        
        # Vowel and Consonant Count
        vowel_count = count_vowels(text)
        consonant_count = count_consonants(text)
        
        # Sentence Count
        sentence_count = len(re.split(r'[.!?]', text)) - 1
        
        # Search and Replace
        with st.expander("🔍 Search & Replace"):
            search_word = st.text_input("Enter word to search:").strip()
            replace_word = st.text_input("Enter word to replace with:")
            modified_text = re.sub(rf'\b{re.escape(search_word)}\b', replace_word, text, flags=re.IGNORECASE) if search_word else text
        
        # Uppercase, Lowercase, Title Case, and Reverse Text
        uppercase_text = text.upper()
        lowercase_text = text.lower()
        titlecase_text = text.title()
        reversed_text = text[::-1]
        
        # Operators Usage
        contains_python = "Python" in text
        avg_word_length = char_count / word_count if word_count > 0 else 0
        
        # Display Results in Columns
        with col1:
            st.subheader("📌 Analysis Results")
            st.write(f"**Total Words:** {word_count}")
            st.write(f"**Total Characters:** {char_count}")
            st.write(f"**Vowel Count:** {vowel_count}")
            st.write(f"**Consonant Count:** {consonant_count}")
            st.write(f"**Sentence Count:** {sentence_count}")
            st.write(f"**Contains 'Python'?:** {'✅ Yes' if contains_python else '❌ No'}")
            st.write(f"**Average Word Length:** {avg_word_length:.2f}")
        
        with col2:
            st.subheader("🔄 Modified Text (After Replacement)")
            st.success(modified_text)
        
        # Display Text Transformations in Expanders
        with st.expander("🔠 Case Conversions & Reverse Text"):
            st.write("**Uppercase:**", uppercase_text)
            st.write("**Lowercase:**", lowercase_text)
            st.write("**Title Case:**", titlecase_text)
            st.write("**Reversed Text:**", reversed_text)
        
    else:
        st.warning("⚠️ Please enter some text to analyze.")

if __name__ == "__main__":
    main() 