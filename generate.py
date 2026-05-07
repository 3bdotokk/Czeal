import os
import google.generativeai as genai

# إعداد Gemini
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error configuring AI: {e}")

def get_ai_content():
    prompt = "اكتب خبراً رياضياً مثيراً جداً عن مونديال 2046 لموقع Czeal.com. ضع العنوان في سطر والمحتوى في سطر آخر. في النهاية أضف كلمة KEYWORD: متبوعة بكلمة إنجليزية واحدة مثل soccer."
    response = model.generate_content(prompt)
    return response.text

def update_html(raw_text):
    # استخراج النص والكلمة المفتاحية
    if "KEYWORD:" in raw_text:
        main_text, keyword = raw_text.split("KEYWORD:")
        keyword = keyword.strip()
    else:
        main_text, keyword = raw_text, "football"

    lines = [line for line in main_text.strip().split('\n') if line.strip()]
    title = lines[0] if lines else "تحديث مونديالي جديد"
    body = lines[1] if len(lines) > 1 else title

    # رابط صورة عشوائي بناء على الكلمة
    img_url = f"https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=800&auto=format&fit=crop&sig={keyword}"

    new_post = f"""
    <article class="post-card">
        <img src="{img_url}" class="post-image" alt="Czeal AI News">
        <div class="post-content">
            <span class="post-meta">تحليل CZEAL AI • نشط</span>
            <h2 class="post-title">{title}</h2>
            <p class="post-excerpt">{body[:150]}...</p>
            <a href="#" class="btn-read">اقرأ المزيد</a>
        </div>
    </article>
    """

    # البحث عن ملف index.html في المجلد الحالي
    file_path = "index.html"
    if not os.path.exists(file_path):
        raise FileNotFoundError("لم يتم العثور على ملف index.html!")

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    if "" in html:
        updated_html = html.replace("", new_post)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_html)
        print("✅ تم تحديث الموقع بنجاح!")
    else:
        print("❌ لم يتم العثور على وسم في ملف index.html")

if __name__ == "__main__":
    text = get_ai_content()
    update_html(text)
