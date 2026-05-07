import os
import google.generativeai as genai

# إعداد Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def get_content():
    prompt = """اكتب خبراً رياضياً قصيراً جداً عن كأس العالم 2046 لموقع Czeal.com. 
    اجعل العنوان مثيراً والمحتوى دقيقاً. 
    بعد النص، أضف كلمة KEYWORD: متبوعة بكلمة إنجليزية واحدة تصف الموضوع (مثل: stadium, trophy, football)."""
    response = model.generate_content(prompt)
    return response.text

def update_html(text):
    # استخراج الكلمة المفتاحية للصورة
    parts = text.split("KEYWORD:")
    news_content = parts[0].strip()
    keyword = parts[1].strip() if len(parts) > 1 else "football"
    
    # رابط صورة عشوائي من Unsplash بناءً على الكلمة المفتاحية
    img_url = f"https://source.unsplash.com/featured/600x400?{keyword}"
    
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    # تنسيق المقال الجديد كبطاقة Post Card
    new_post = f"""
    <article class="post-card">
        <img src="{img_url}" class="post-image" alt="World Cup">
        <div class="post-content">
            <span class="post-meta">تحليل آلي • تحديث اليوم</span>
            <h2 class="post-title">{news_content.splitlines()[0]}</h2>
            <p class="post-excerpt">{news_content.splitlines()[1] if len(news_content.splitlines()) > 1 else news_content}...</p>
            <a href="#" class="btn-read">اقرأ التفاصيل</a>
        </div>
    </article>
    """
    
    # وضع المقال في المكان الصحيح
    updated_html = html.replace("", f"\n{new_post}")
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated_html)

if __name__ == "__main__":
    content = get_content()
    update_html(content)
