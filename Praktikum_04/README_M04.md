# Praktikum 04: penyelesaian dan tindak lanjut

Status saat M04 diunggah: PBIX berisi Fact_Sales, Dim_Branch, audit_Fact_Sales_Branch, audit_Branch_Unmatched, dan stg_Fact_Sales_Raw. Empat unmatched B099 telah diidentifikasi dan diberi status Exclude from branch analysis pada Fact_Sales, bukan dihapus.

Bukti terverifikasi via screenshot: 4 transaksi (T0005749, T0006010, T0009222, T0015021), total Revenue B099 Rp362.760,93.

Penyempurnaan dokumentasi pengumpulan: masukkan screenshot M04_Left_Outer_Merge.png dan M04_Audit_B099.png ke folder Praktikum_04 saat diunggah ke GitHub. Foto ini tidak disertakan dalam paket jika pengguna menyimpannya hanya di laptop.

**Keputusan:** B099 dikecualikan dari pemeringkatan cabang sambil tetap dihitung dalam total perusahaan; tindak lanjut ialah verifikasi kode dari pengelola master cabang.
