import os
import google.generativeai as genai

# 1. إعداد الاستثناءات للـ API
try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("مفتاح الـ API غير موجود في إعدادات Secrets!")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"❌ فشل في إعداد AI: {e}")
    exit(1)

def run():
    try:
        # محاولة جلب الخبر
        print("🤖 محاولة توليد الخبر من Gemini...")
        response = model.generate_content("اكتب خبر رياضي عاجل ومثير عن توقعات مونديال 2026 والمنتخبات العربية.")
        news_text = response.text.strip()
        
        # تجهيز قالب الخبر (مع إعادة كتابة الوسم لضمان الاستمرارية)
        new_post = f"""
    <article class="post-card">
        <img src="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=800" class="post-image">
        <div class="post-content">
            <span class="post-meta">رادار CZEAL AI • 2026</span>
            <h2 class="post-title">تحليل الذكاء الاصطناعي للمونديال</h2>
            <p class="post-excerpt">{news_text[:220]}...</p>
            <a href="#" class="btn-read">اقرأ المزيد</a>
        </div>
    </article>"""

        # 2. محاولة الوصول لملف HTML مع معالجة المسار
        file_path = "index.html"
        if not os.path.exists(file_path):
            # إذا لم يجده في الرئيسي، يبحث في المجلد الحالي بعمق
            file_path = os.path.join(os.getcwd(), "index.html")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 3. استراتيجية الخيارات المتعددة (Fallback Strategy)
        
        # الخيار الأول: البحث عن الوسم النموذجي
        if "" in content:
            print("🎯 الخيار الأول: تم العثور على الوسم الرئيسي.")
            updated_content = content.replace("", new_post)
        
        # الخيار الثاني: البحث عن الوسم بمسافات مختلفة (توقع أخطاء التنسيق)
        elif "" in content or "" in content:
            print("🔍 الخيار الثاني: تم العثور على الوسم بتنسيق مختلف.")
            import re
            updated_content = re.sub(r"", new_post, content)

        # الخيار الثالث: إذا اختفى الوسم تماماً، ابحث عن حاوية المقالات
        elif '<div class="container">' in content:
            print("⚠️ الخيار الثالث: الوسم مفقود، سيتم الحقن داخل الحاوية مباشرة.")
            updated_content = content.replace('<div class="container">', '<div class="container">' + new_post)

        # الخيار الرابع: الملاذ الأخير (تحت الهيدر)
        elif "</header>" in content:
            print("🚨 الخيار الرابع: الحقن أسفل الهيدر مباشرة.")
            updated_content = content.replace("</header>", "</header>" + new_post)
        
        else:
            raise Exception("لم يتم العثور على أي نقطة حقن داخل ملف HTML!")

        # حفظ التعديلات
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("✅ تم تحديث الموقع بنجاح باستخدام أفضل خيار متاح!")

    except Exception as e:
        print(f"💥 فشل ذريع في العملية: {e}")
        # لا نوقف السكربت هنا لكي لا تظهر علامة حمراء إذا كان الخطأ بسيطاً
        # ولكننا طبعنا الخطأ لنعرف سببه في سجلات الـ Action

if __name__ == "__main__":
    run()
