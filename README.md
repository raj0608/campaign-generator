# 🚀 AI Marketing Campaign Generator

Generate complete marketing campaigns in seconds using AI. Input your brand details, target audience, and campaign goals — get ad copy, social posts, email sequences, and creative concepts.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)
![Gemini](https://img.shields.io/badge/Google-Gemini_2.0-orange)

## ✨ Features

- 🎯 **Multi-Channel Campaigns** — Instagram, LinkedIn, Email, Google Ads, TikTok, and more
- ✍️ **Multiple Ad Variations** — Get 3 copy options per channel
- 🎨 **Creative Concepts** — Visual direction for designers
- 📅 **Content Calendar** — Week-long posting schedule
- 🏷️ **Hashtags & Keywords** — SEO and social optimization
- ⬇️ **Export** — Download campaigns as Markdown

## 🚀 Quick Start

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

Get your free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

```bash
cp .env.example .env
# Edit .env and add your Gemini API key
```

Your `.env` file should look like:
```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📁 Project Structure

```
campaign-generator/
├── app.py                 # Streamlit UI
├── src/
│   ├── __init__.py
│   └── generator.py       # Core LLM logic
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🎮 Usage

1. Enter your brand name and product description
2. Describe your target audience (demographics, pain points, interests)
3. Select your campaign goal (launch, awareness, conversions, etc.)
4. Choose marketing channels
5. Pick a tone/voice
6. Click "Generate Campaign"
7. Download the results!

## 📋 Example Output

The generator creates:

- **Campaign Strategy** — Theme, core message, value propositions
- **Ad Copy** — 3 variations per channel with headlines, body, CTAs
- **Hashtags & Keywords** — For social and SEO
- **Creative Concepts** — Visual direction descriptions
- **Content Calendar** — 1-week posting schedule

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** — UI framework
- **Google Gemini 2.0 Flash** — LLM for generation
- **Pydantic** — Data validation

## 🔮 Future Enhancements

- [ ] OpenAI GPT-4 support
- [ ] Claude API support
- [ ] Image generation with DALL-E / Imagen
- [ ] Brand guidelines upload (RAG)
- [ ] Campaign history & saving
- [ ] A/B copy testing suggestions
- [ ] Competitor analysis via web search

## 📝 License

MIT

---

Built by [Rohan](https://github.com/raj0608)