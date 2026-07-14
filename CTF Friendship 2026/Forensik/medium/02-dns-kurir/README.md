# DNS Kurir

**Kategori:** Network Forensics / DNS Exfiltration  
**Kesulitan:** Medium  
**Artifact:** `office\\\\\\\_traffic.pcap`

SOC melihat workstation `10.26.0.42` mengirim query DNS aneh ke resolver
internal. Paket datang tidak sesuai urutan.

Rekonstruksi pesan yang dikirim dan temukan flag.

**Hint:** Label pertama adalah nomor urut; label kedua bukan teks biasa.



flag : FS26{dns\_exfil\_kurir\_paket\_nyasar\_ga\_pake\_maps}

