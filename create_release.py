import os
import zipfile
import shutil

def main():
    print("=== สร้างไฟล์ Release สำหรับ GMCM Thai Description Injector ===")
    
    # กำหนดไฟล์ที่ต้องการเอาเข้า zip
    files_to_include = [
        "inject_manifest_descriptions.command",
        "README.md",
        "LICENSE"
    ]
    
    # เช็คว่าไฟล์ที่จำเป็นมีอยู่ครบไหม
    for f in files_to_include:
        if not os.path.exists(f):
            print(f"❌ ไม่พบไฟล์ที่จำเป็น: {f}")
            print("กรุณารันสคริปต์นี้ในโฟลเดอร์ stardew-gmcm-thai-injector")
            return

    # ถามเวอร์ชัน
    version = input("กรุณากรอกเวอร์ชัน (ตัวอย่าง: 1.0.0): ").strip()
    if not version:
        print("❌ เวอร์ชันไม่ถูกต้อง ยกเลิกการทำ Release")
        return

    # สร้างโฟลเดอร์ releases ถ้ายังไม่มี
    release_dir = "releases"
    if not os.path.exists(release_dir):
        os.makedirs(release_dir)
        
    zip_filename = f"StardewGMCMThaiInjector-v{version}.zip"
    zip_path = os.path.join(release_dir, zip_filename)
    
    print(f"\nกำลังสร้างไฟล์ {zip_filename} ...")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for f in files_to_include:
            zipf.write(f)
            print(f"  ✓ เพิ่มไฟล์: {f}")
            
    print(f"\n✅ สร้างไฟล์ Release สำเร็จ! ถูกบันทึกไว้ที่: {zip_path}")

if __name__ == "__main__":
    main()
