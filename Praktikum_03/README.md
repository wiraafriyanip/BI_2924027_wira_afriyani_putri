# Praktikum 03 — Kecerdasan Bisnis

**Materi:** Data Cleaning, Analisis Tren Penjualan, dan Regresi Linier menggunakan Power BI.

**Nama:** Wira Afriyani Putri  
**NIM:** 2924027

## Tujuan Praktikum

Melakukan pembersihan data transaksi SumbarMart 360 menggunakan Power Query, memvisualisasikan tren total penjualan bulanan, dan menganalisis kecenderungan penjualan menggunakan regresi linier melalui fungsi DAX LINESTX.

## Tahapan Praktikum

1. Membuat staging data dan query Fact_Sales.
2. Menghapus 22 baris dengan Transaction_ID duplikat.
3. Menstandardisasi kategori Channel menjadi Toko, Online, dan WhatsApp.
4. Membersihkan format tanggal, harga produk, dan persentase diskon.
5. Mempertahankan 282 nilai null pada Satisfaction_Score.
6. Membuat visualisasi tren penjualan selama 32 bulan.
7. Melakukan regresi linier menggunakan LINESTX.

## Hasil Praktikum

- Jumlah transaksi setelah cleaning: 15.712 baris.
- Periode analisis: Januari 2024 – Agustus 2026.
- Slope regresi: Rp190.527,50 per bulan.
- Intercept: Rp41.709.752,88.
- Koefisien determinasi (R²): sekitar 0,048146.

Hasil analisis menunjukkan kecenderungan tren penjualan yang meningkat, tetapi hubungan linier antara waktu dan total penjualan masih lemah.

## Berkas Hasil

- File Power BI (.pbix)
- Laporan analisis (.pdf)
- Screenshot visualisasi tren penjualan dan hasil regresi.
