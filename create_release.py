import os
import zipfile
import subprocess

def run_cmd(cmd):
    print(f"Executing: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ Error: {res.stderr}")
        return False
    return True

def main():
    print("=== สร้างไฟล์ Release สำหรับ GMCM Thai Description Injector ===")
    
    files_to_include = [
        "inject_manifest_descriptions.command",
        "README.md",
        "LICENSE"
    ]
    
    for f in files_to_include:
        if not os.path.exists(f):
            print(f"❌ ไม่พบไฟล์ที่จำเป็น: {f}")
            return

    version = input("กรุณากรอกเวอร์ชัน (ตัวอย่าง: 1.0.0): ").strip()
    if not version:
        print("❌ เวอร์ชันไม่ถูกต้อง")
        return

    release_dir = "releases"
    if not os.path.exists(release_dir):
        os.makedirs(release_dir)
        
    zip_filename = f"StardewGMCMThaiInjector-v{version}.zip"
    zip_path = os.path.join(release_dir, zip_filename)
    
    print(f"\nกำลังสร้างไฟล์ {zip_filename} ...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for f in files_to_include:
            zipf.write(f)
            
    print(f"✅ สร้างไฟล์ Release สำเร็จ: {zip_path}")
    
    tag_name = f"v{version}"
    title = f"GMCM Thai Description Injector {tag_name}"
    notes = f"แพตช์แปลภาษาไทยสำหรับเมนู GMCM เวอร์ชัน {version}"
    
    print(f"\n🚀 กำลังอัปโหลด Release ขึ้น GitHub ({tag_name})...")
    
    if not run_cmd(['git', 'tag', tag_name]): return
    if not run_cmd(['git', 'push', 'origin', tag_name]): return
    
    gh_cmd = [
        'gh', 'release', 'create', tag_name, zip_path,
        '--title', title,
        '--notes', notes
    ]
    if run_cmd(gh_cmd):
        print(f"\n🎉 อัปโหลด Release {tag_name} ขึ้น GitHub สำเร็จแล้ว!")

if __name__ == "__main__":
    main()
