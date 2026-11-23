# PRAKTIKUM 11 — KELOMPOK 04
## Kecerdasan Bisnis | Sample Superstore

Paket ini berisi PBIX, laporan, analisis, reproduksi Random Forest, workbook sumber, screenshot, serta audit kesesuaian dokumen. Revisi ini menyelaraskan isi laporan dengan metadata PBIX dan bukti yang benar-benar tersedia.

## Struktur paket
- `00_PETUNJUK/` — README status, checklist, audit status, dan daftar revisi.
- `01_PBIX/` — PBIX P11 yang diterima; tidak diubah dalam revisi dokumentasi.
- `02_LAPORAN_UTAMA/` — laporan kelompok P11 DOCX/PDF yang diselaraskan.
- `03_AI_INSIGHT_AUDIT/` — tiga audit AI dalam format 9 unsur sesuai panduan.
- `04_VALIDASI_MODEL_DAN_FILTER/` — laporan grain, inventaris 12 tabel, relationship, dan validasi filter.
- `05_ANALISIS_WAHYU/` — analisis deskriptif/prediktif dan Random Forest Wahyu.
- `06_MINICASE/` — mini-case 3 halaman.
- `07_REPRODUKSI_RANDOM_FOREST/` — script yang diperbaiki, workbook hasil, log, dan paket reproduksi.
- `08_DATA_DAN_REFERENSI/` — workbook model, Data Dictionary, dataset sumber, serta sheet audit P11 tambahan.
- `09_BUKTI_P11/` — screenshot yang disertakan dari versi kerja M10/M11 dan crop visual.
- `10_KONTRIBUSI/` — template Contribution Log untuk dilengkapi anggota.

## Ringkasan temuan
- Dataset sumber: 10.194 order line, 5.111 Order ID unik, 296 pesanan retur; Return Rate historis keseluruhan 5,79%.
- Metadata PBIX paket: 3 halaman dan 12 tabel.
- Screenshot Manage Relationships: 10 relationship, 7 Active, 3 Inactive.
- Satu relationship Active menghubungkan Fact_OrderCategory ke Fact_OrderSummary (fact-to-fact); tiga relationship Inactive melibatkan People.
- Anomaly Detection pada metadata masih menggunakan Orders[Order Date] harian; panduan meminta Month Start bulanan.
- Decomposition Tree pada metadata memakai Total Profit → Region → Category → Sub-Category.
- Key Influencers pada metadata memakai target Returned = Yes, Explain by Region dan Discount Band.
- Halaman Return Rate Perbandingan mencampur field Orders dan Fact_OrderSummary; visual Category perlu memakai Fact_OrderCategory dengan DISTINCTCOUNT Order ID.

## Catatan provenance
Tidak semua screenshot berasal dari PBIX final yang sama. Screenshot marker anomaly dan Decomposition Tree full-screen berasal dari jendela kerja M10; screenshot sensitivity dan filter East berasal dari jendela kerja M11; crop Key Influencers dan relationship tidak menampilkan judul jendela. Laporan membedakan screenshot pendukung dari metadata PBIX paket. Jangan menyebut seluruh screenshot sebagai bukti final satu file.

## Random Forest
Script reproduksi diperbaiki dan berhasil dijalankan kembali. Train = 7.345 baris, test = 2.849 baris. Model A (Sales + Discount): MAE 25,172; RMSE 103,651; R² 0,772. Model B (Sales): MAE 48,083; RMSE 190,354; R² 0,231. Log reproduksi tersedia pada folder 07.

## Pekerjaan yang belum selesai
Paket ini lengkap secara dokumentasi, tetapi **belum 100% tervalidasi secara fungsional**. PBIX harus di-refresh dan diuji di Power BI Desktop; anomaly axis perlu diubah menjadi bulanan; interaksi Decomposition Tree dan Key Influencers harus dicocokkan dengan matrix; visual Return Rate harus diperbaiki; relationship fact-to-fact perlu dievaluasi; screenshot final perlu diambil ulang; Contribution Log harus dilengkapi anggota.

## Referensi yang digunakan
- Panduan Praktikum 11 Kecerdasan Bisnis dengan Power BI (Oktober 2026).
- Project Charter Praktikum 09 Kelompok 04 versi 3 (3 November 2026).
- Data Inventory Superstore Kelompok 04 versi 3 (3 November 2026).
- Rencana KPI, Timeline, dan Decision Log Kelompok 04 versi 3.
- Dataset Sample Superstore dan workbook model Kelompok 04.

Catatan: dokumen referensi M09 dan Panduan Praktikum 11 tidak terdapat sebagai file asli di ZIP sumber yang diunggah; judulnya dicantumkan di sini karena digunakan sebagai acuan dan tercantum pada daftar pustaka laporan.

## Update berkas terbaru
PBIX `p11 final(1).pbix` memiliki SHA-256 identik dengan PBIX di paket sebelumnya, sehingga konten PBIX belum berubah. Screenshot terbaru menambahkan percobaan Anomaly Order Month pada file kerja dua halaman, tetapi metadata PBIX paket tiga halaman masih memakai Order Date harian. Screenshot relationship final memperlihatkan 7 Active dan 3 Inactive (nama file “8Aktif” tidak akurat). Screenshot Return Rate M10 menunjukkan rate sekitar 5,8% yang sama untuk seluruh Category dan Segment; hal ini harus diperiksa sebagai masalah filter propagation atau definisi measure. Semua screenshot terbaru disimpan pada `09_BUKTI_P11/`.
