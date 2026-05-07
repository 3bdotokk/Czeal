import os
import google.generativeai as genai

def run():
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("❌ Error: API Key not found in environment!")
            return

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("🤖 Asking Gemini for news...")
        response = model.generate_content("اكتب خبر رياضي قصير جدا لموقع Czeal.com عن مونديال 2046.")
        news_text = response.text
        
        # قالب المقال
        new_post = f"""
        <article class="post-card">
            <img src="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=800" class="post-image">
            <div class="post-content">
                <span class="post-meta">تحديث آلي • Czeal AI</span>
                <h2 class="post-title">خبر مونديالي جديد</h2>
                <p class="post-excerpt">{news_text[:150]}...</p>
                <a href="#" class="btn-read">اقرأ المزيد</a>
            </div>
        </article>
        """

        if not os.path.exists("index.html"):
            print("❌ Error: index.html not found!")
            return

        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        if "" in html:
            updated_html = html.replace("", new_post)
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(updated_html)
            print("✅ Success! Site updated.")
        else:
            print("❌ Error: Tag not found in index.html")

    except Exception as e:
        print(f"💥 Critical Error: {e}")

if __name__ == "__main__":
    run()
