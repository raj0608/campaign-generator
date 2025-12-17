"""
Campaign Generator - Core LLM logic (Gemini version)
"""
import google.generativeai as genai
from pydantic import BaseModel
from typing import Optional


class CampaignInput(BaseModel):
    """User inputs for campaign generation"""
    brand_name: str
    product_description: str
    target_audience: str
    campaign_goal: str
    channels: list[str]
    tone: str
    additional_context: Optional[str] = None


class CampaignGenerator:
    """Generates marketing campaigns using Gemini"""

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def _build_prompt(self, inputs: CampaignInput) -> str:
        """Construct the campaign generation prompt"""

        channels_str = ", ".join(inputs.channels)

        prompt = f"""You are an expert marketing strategist and copywriter. 
Create a comprehensive marketing campaign based on the following brief:

## BRAND & PRODUCT
- **Brand Name:** {inputs.brand_name}
- **Product/Service:** {inputs.product_description}

## TARGET AUDIENCE
{inputs.target_audience}

## CAMPAIGN DETAILS
- **Goal:** {inputs.campaign_goal}
- **Channels:** {channels_str}
- **Tone/Voice:** {inputs.tone}

{f"## ADDITIONAL CONTEXT" + chr(10) + inputs.additional_context if inputs.additional_context else ""}

---

## YOUR TASK

Generate a complete marketing campaign with the following sections:

### 1. CAMPAIGN STRATEGY
- Campaign name/theme (something catchy)
- Core message (1-2 sentences)
- Key value propositions (3 bullet points)

### 2. AD COPY
For each channel ({channels_str}), provide:
- 3 different ad copy variations
- Each should have: Headline, Body, Call-to-Action
- Respect platform character limits and best practices

### 3. HASHTAGS & KEYWORDS
- 10 relevant hashtags for social media
- 5 target keywords for search/SEO

### 4. CREATIVE CONCEPTS
- Describe 3 visual/image concepts a designer could create
- Include mood, style, key elements to feature

### 5. CONTENT CALENDAR
- Suggest a 1-week posting schedule
- Include which content goes on which channel and when

Be specific, creative, and tailor everything to resonate with the target audience.
Use the specified tone consistently throughout all copy.
"""
        return prompt

    def generate(self, inputs: CampaignInput) -> str:
        """Generate the marketing campaign"""

        prompt = self._build_prompt(inputs)
        
        # Add system context to the prompt
        full_prompt = """You are a world-class marketing strategist who creates compelling, 
conversion-focused campaigns. You write copy that connects emotionally with audiences while driving action.

""" + prompt

        response = self.model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.8,
                max_output_tokens=3000,
            )
        )

        return response.text
