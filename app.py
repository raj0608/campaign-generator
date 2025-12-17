"""
Campaign Generator - Streamlit UI
"""
import streamlit as st
import os
from dotenv import load_dotenv
from src.generator import CampaignGenerator, CampaignInput

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Campaign Generator",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .output-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🚀 AI Marketing Campaign Generator")
st.markdown("*Generate complete marketing campaigns in seconds*")
st.divider()

# Sidebar for API key (if not in .env)
with st.sidebar:
    st.header("⚙️ Settings")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        api_key = st.text_input("Enter Gemini API Key", type="password")
        if api_key:
            st.success("API key set!")
    else:
        st.success("API key loaded from .env")

    st.divider()
    st.markdown("### How to use")
    st.markdown("""
    1. Fill in your brand details
    2. Define your target audience
    3. Select channels & tone
    4. Click Generate!
    """)

# Main form
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Brand & Product")

    brand_name = st.text_input(
        "Brand Name",
        placeholder="e.g., BrewMate"
    )

    product_description = st.text_area(
        "Product/Service Description",
        placeholder="What are you selling? What makes it unique?",
        height=100
    )

    st.subheader("🎯 Target Audience")

    target_audience = st.text_area(
        "Describe your ideal customer",
        placeholder="Demographics, pain points, interests, behaviors...",
        height=100
    )

with col2:
    st.subheader("📢 Campaign Details")

    campaign_goal = st.selectbox(
        "Campaign Goal",
        [
            "Product Launch",
            "Brand Awareness",
            "Lead Generation",
            "Sales/Conversions",
            "Event Promotion",
            "Customer Retention"
        ]
    )

    channels = st.multiselect(
        "Marketing Channels",
        ["Instagram", "Facebook", "LinkedIn", "Twitter/X", "Email", "Google Ads", "TikTok"],
        default=["Instagram", "Email"]
    )

    tone = st.select_slider(
        "Tone/Voice",
        options=[
            "Formal & Professional",
            "Professional but Friendly",
            "Casual & Conversational",
            "Playful & Witty",
            "Bold & Edgy"
        ],
        value="Professional but Friendly"
    )

    additional_context = st.text_area(
        "Additional Context (Optional)",
        placeholder="Any specific requirements, existing taglines, competitor info, etc.",
        height=80
    )

st.divider()

# Generate button
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])

with col_btn2:
    generate_clicked = st.button(
        "🎨 Generate Campaign",
        type="primary",
        use_container_width=True
    )

# Validation and generation
if generate_clicked:
    # Validate inputs
    if not api_key:
        st.error("Please enter your Gemini API key in the sidebar.")
    elif not brand_name:
        st.error("Please enter a brand name.")
    elif not product_description:
        st.error("Please describe your product/service.")
    elif not target_audience:
        st.error("Please describe your target audience.")
    elif not channels:
        st.error("Please select at least one marketing channel.")
    else:
        # Create input object
        campaign_input = CampaignInput(
            brand_name=brand_name,
            product_description=product_description,
            target_audience=target_audience,
            campaign_goal=campaign_goal,
            channels=channels,
            tone=tone,
            additional_context=additional_context if additional_context else None
        )

        # Generate with loading spinner
        with st.spinner("🧠 Crafting your campaign... This takes about 30 seconds."):
            try:
                generator = CampaignGenerator(api_key=api_key)
                result = generator.generate(campaign_input)

                # Store in session state
                st.session_state.generated_campaign = result
                st.session_state.campaign_input = campaign_input

            except Exception as e:
                st.error(f"Error generating campaign: {str(e)}")

# Display results
if "generated_campaign" in st.session_state:
    st.divider()
    st.subheader("✨ Your Generated Campaign")

    # Campaign output
    st.markdown(st.session_state.generated_campaign)

    # Download button
    st.divider()
    col_dl1, col_dl2, col_dl3 = st.columns([1, 1, 1])

    with col_dl2:
        st.download_button(
            label="📥 Download as Markdown",
            data=st.session_state.generated_campaign,
            file_name=f"{st.session_state.campaign_input.brand_name}_campaign.md",
            mime="text/markdown",
            use_container_width=True
        )

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center; color: gray;'>Built with ❤️ using Streamlit & Gemini</div>",
    unsafe_allow_html=True
)
