import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def run():
    try:
        # طلب الخبر
        response = model.generate_content("اكتب خبر رياضي مثير وقصير عن مونديال 2026 والمنتخبات العربية.")
        news_text = response.text.strip()
        
        new_post = f"""
    <article class="post-card">
        <img src="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=800" class="post-image">
        <div class="post-content">
            <span class="post-meta">توقعات AI • مونديال 2026</span>
            <h2 class="post-title">تحليل عاجل من CZEAL</h2>
            <p class="post-excerpt">{news_text[:200]}...</p>
        </div>
    </article>"""

        # قراءة الملف
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()

        # الاستبدال (استخدمنا وسم مبسط جداً لضمان النجاح)
        if "" in content:
            updated = content.replace("", new_post)
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(updated)
            print("✅ Success!")
        else:
            print("❌ Tag not found!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
