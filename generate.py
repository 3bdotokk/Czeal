import os
import google.generativeai as genai

# إعداد Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def run():
    try:
        # التوجيه الذكي لجذب الزوار لمونديال 2026
        prompt = """
        اكتب خبراً رياضياً تحليلياً عاجلاً ومثيراً عن استعدادات وتوقعات المنتخبات لمونديال 2026.
        ركز على المنتخبات العربية (مثل المغرب، السعودية، مصر، أو السودان) وفرص تألقها.
        اجعل العنوان صادماً وجذاباً جداً.
        في النهاية أضف كلمة KEYWORD: متبوعة بكلمة إنجليزية مثل stadium أو football.
        """
        response = model.generate_content(prompt)
        news_text = response.text.strip()
        
        # استخراج العنوان والمحتوى والكلمة المفتاحية
        try:
            main_text, keyword = news_text.split("KEYWORD:")
            keyword = keyword.strip()
        except:
            main_text, keyword = news_text, "soccer"

        lines = [line for line in main_text.strip().split('\n') if line.strip()]
        title = lines[0]
        body = " ".join(lines[1:]) if len(lines) > 1 else main_text

        # قالب الخبر الجديد بنظام الأتمتة
        new_post = f"""
    <article class="post-card">
        <img src="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=800&sig={keyword}" class="post-image">
        <div class="post-content">
            <span class="post-meta">تحليل ذكي • مونديال 2026</span>
            <h2 class="post-title">{title}</h2>
            <p class="post-excerpt">{body[:180]}...</p>
            <a href="#" class="btn-read">اقرأ التحليل الكامل</a>
        </div>
    </article>"""

        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        if "" in html:
            updated_html = html.replace("", new_post)
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(updated_html)
            print("✅ تم تحديث الموقع بنجاح!")
        else:
            print("❌ لم يتم العثور على الوسم ARTICLES_START")

    except Exception as e:
        print(f"💥 خطأ: {e}")

if __name__ == "__main__":
    run()
