import streamlit as st

st.title("💻 Programming Language Picker")

st.write("Select your favorite programming language and discover where it is commonly used.")

languages = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "Go",
    "Rust",
    "Kotlin",
    "Swift"
]
info = {
    "Python": "Great for Data Science, AI, Automation, and Web Development.",
    "Java": "Popular for Enterprise Applications and Android Development.",
    "C": "Widely used in Operating Systems and Embedded Systems.",
    "C++": "Used in Game Development and High-Performance Applications.",
    "JavaScript": "The language of the Web.",
    "Go": "Designed for Cloud Computing and Backend Services.",
    "Rust": "Known for Memory Safety and High Performance.",
    "Kotlin": "Modern language for Android Development.",
    "Swift": "Used for iOS and macOS App Development."
}
selected = st.selectbox("Choose a Programming Language",languages)
st.success(f"You selected **{selected}**")

st.info(info[selected])

rating = st.slider("How much do you like this language?",1,10,1)

st.write(f"⭐ Your Rating: **{rating}/100**")

if st.button("Submit"):
    st.balloons()
    st.success(f"Thanks! You rated {selected} {rating}/100.")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
