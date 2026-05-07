import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def get_ai_content():
    prompt = "اكتب خبراً رياضياً قصيراً جداً عن مونديال 2046 لموقع Czeal.com. ضع العنوان في سطر والمحتوى في سطر آخر. في النهاية أضف كلمة KEYWORD: متبوعة بكلمة إنجليزية مثل soccer."
    response = model.generate_content(prompt)
    return response.text

def update_html(raw_text):
    try:
        main_text, keyword = raw_text.split("KEYWORD:")
        keyword = keyword.strip()
    except:
        main_text, keyword = raw_text, "football"

    lines = main_text.strip().split('\n')
    title = lines[0]
    body = lines[1] if len(lines) > 1 else lines[0]

    img_url = f"https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=800&auto=format&fit=crop&sig={keyword}"

    new_post = f"""
    <article class="post-card">
        <img src="{img_url}" class="post-image">
        <div class="post-content">
            <span class="post-meta">تحديث آلي • 2046</span>
            <h2 class="post-title">{title}</h2>
            <p class="post-excerpt">{body[:120]}...</p>
            <a href="#" class="btn-read">اقرأ المزيد</a>
        </div>
    </article>
    """

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    updated_html = html.replace("", new_post)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated_html)

if __name__ == "__main__":
    text = get_ai_content()
    update_html(text)
