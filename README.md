# 🚀 AI Marketing Campaign Generator

Generate complete marketing campaigns in seconds using AI. Input your brand details, target audience, and campaign goals — get ad copy, social posts, email sequences, and creative concepts.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)
![OpenAI](exithttps://img.shields.io/badge/OpenAI-GPT--4-green)
## Features

- 🎯 **Multi-Channel Campaigns** — Instagram, LinkedIn, Email, Google Ads, and more
- ✍️ **Multiple Ad Variations** — Get 3 copy options per channel
- 🎨 **Creative Concepts** — Visual direction for designers
- 📅 **Content Calendar** — Week-long posting schedule
- 🏷️ **Hashtags & Keywords** — SEO and social optimization
- ⬇️ **Export** — Download campaigns as Markdown

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/campaign-generator.git
cd campaign-generator
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Project Structure

```
campaign-generator/
├── app.py                 # Streamlit UI
├── src/
│   └── generator.py       # Core LLM logic
├── requirements.txt
├── .env.example
└── README.md
```

## Usage

1. Enter your brand name and product description
2. Describe your target audience (demographics, pain points, interests)
3. Select your campaign goal (launch, awareness, conversions, etc.)
4. Choose marketing channels
5. Pick a tone/voice
6. Click "Generate Campaign"
7. Download the results!

## Example Output

The generator creates:

- **Campaign Strategy** — Theme, core message, value propositions
- **Ad Copy** — 3 variations per channel with headlines, body, CTAs
- **Hashtags & Keywords** — For social and SEO
- **Creative Concepts** — Visual direction descriptions
- **Content Calendar** — 1-week posting schedule

## Tech Stack

- **Python 3.9+**
- **Streamlit** — UI framework
- **OpenAI GPT-4o-mini** — LLM for generation
- **Pydantic** — Data validation

## Future Enhancements

- [ ] Claude API support
- [ ] Image generation with DALL-E
- [ ] Brand guidelines upload (RAG)
- [ ] Campaign history & saving
- [ ] A/B copy testing suggestions
- [ ] Competitor analysis

## License

MIT

---

Built by [Your Name](https://github.com/yourusername)
