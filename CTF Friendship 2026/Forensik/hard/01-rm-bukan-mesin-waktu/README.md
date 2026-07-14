# rm Bukan Mesin Waktu

**Kategori:** Disk Forensics / File Carving  
**Kesulitan:** Hard  
**Artifact:** `employee\\\\\\\_backup.img`

Seorang pegawai menjalankan `rm`, membersihkan history, dan yakin catatan
incident-nya lenyap. Tim hanya memperoleh image filesystem ext4.

Pulihkan catatan yang dihapus dan temukan flag.

**Hint:** `rm` membuang referensi, tetapi belum tentu langsung menghapus isi
blok datanya.



flag : FS26{menghapusmu\_tidak\_semudah\_rm\_rf\_di\_ext4}

