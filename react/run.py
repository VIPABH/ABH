import os
import sys
import asyncio

# ضمان قراءة الاستيراد من المسار الصحيح
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ABHS import *
import الحماية

async def main():
    print("⏳ جاري تشغيل بوت التفاعلات والـ 15 عميل...")
    await init_clients()
    
    # التأكد المباشر من بدء اتصال REACTBOT إن لم يكن متصلاً
    if 'REACTBOT' in globals() and REACTBOT:
        if not REACTBOT.is_connected():
            print("🔄 جاري ربط اتصال REACTBOT...")
            await REACTBOT.start()
            
    print("🚀 جميع الحسابات وبوت التفاعلات شغالين بنجاح!")

    try:
        # تشغيل الانتظار على REACTBOT
        if 'REACTBOT' in globals() and REACTBOT:
            await REACTBOT.run_until_disconnected()
        else:
            await asyncio.Event().wait()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("\n🛑 جاري إغلاق الجلسات بأمان...")
        
        # تجميع كافة العملاء المتاحين
        raw_clients = [c for c in [REACTBOT, mainABH, bot] + (ABHS if isinstance(ABHS, list) else []) if c]
        
        # إغلاق متتالي آمن يمنع كراش الـ Event Loop
        for client in raw_clients:
            try:
                if client and client.is_connected():
                    await client.disconnect()
            except Exception as e:
                print(f"تنبيه أثناء فصل جلسة: {e}")
                
        print("✅ تم الإغلاق بسلام.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 تم الإيقاف.")
