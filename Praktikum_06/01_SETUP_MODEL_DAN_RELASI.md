# SETUP MODEL UNTUK PRAKTIKUM 06 DAN 07

File kerja: Salin M05 PBIX ke M06 sebelum melakukan perubahan. Pertahankan M05 untuk bukti definisi laba Praktikum 05.

## Import dalam satu Navigator
Di Home > Transform data > New Source > Excel Workbook, pilih Dataset_Praktikum_BI_Raw.xlsx dan centang sekaligus:
- Dim_Product_Raw -> ubah nama query menjadi Dim_Product.
- Dim_Customer_Raw -> bila header masih Column1 dst., Home > Use First Row as Headers; rename Dim_Customer.
- Fact_Target -> gunakan nama Fact_Target; Month_Start tipe Date, Month_Key whole number, target numeric.
- Fact_Operations (opsional untuk KPI operasional, tetapi tidak perlu untuk visual wajib M06).

Dim_Product[Category] memiliki variasi kapitalisasi dari file raw. Sebelum digunakan pada grafik, pilih Transform > Format > Trim dan Capitalize Each Word (Title Case) untuk membersihkan kategori. Jangan menyatukan label kategori tanpa memeriksa maknanya.

## Dimensi tanggal
Klik Modeling > New table, masukkan isi `02_NEW_TABLE_Dim_Date.dax` tanpa komentar baris pertama. Tabel ini ber-grain satu tanggal kalender. Urutkan Dim_Date[Month_Year] dengan Dim_Date[Month_Index].

## Relationship (Model view, arah filter Single dari dimensi ke fact)
| From (one) | To (many) | Cardinality / active |
|---|---|---|
| Dim_Date[Date] | Fact_Sales[Transaction_Date_Clean] | 1:* active |
| Dim_Date[Date] | Fact_Target[Month_Start] | 1:* active (baris target berada pada hari pertama bulan) |
| Dim_Branch[Branch_ID] | Fact_Sales[Branch_ID] | 1:* active |
| Dim_Branch[Branch_ID] | Fact_Target[Branch_ID] | 1:* active |
| Dim_Product[Product_ID] | Fact_Sales[Product_ID] | 1:* active |
| Dim_Customer[Customer_ID] | Fact_Sales[Customer_ID] | 1:* active, jika sudah unik dan model menerima blank di fact |

Jangan menghubungkan Fact_Target langsung ke Fact_Sales; grain berbeda. Jangan menghubungkan Fact_Operations langsung ke Fact_Sales (bulanan-cabang vs transaksi). Jangan ubah Dim_Branch asli dengan B099 tanpa bukti; transaksi B099 tetap ada dalam Fact_Sales. Pada slicer Branch yang memilih cabang resmi, B099 tidak termasuk secara wajar.

## Uji sebelum dashboard
- Total Sales tanpa filter: sekitar Rp 1.435.310.614,12.
- M06 Gross Profit dari SUM(Profit): sekitar Rp 457,64 juta.
- M06 Profit Margin: sekitar 31,9%.
- Target Achievement: sekitar 13,1%.
- Slicer Year dan Branch harus memfilter penjualan dan target secara selaras.
- Slicer Channel memfilter aktual tetapi tidak punya atribut di Fact_Target; jelaskan konteks target pada dashboard.

Jika Power BI menolak relationship karena duplikasi dimensi, periksa key & tipe data sebelum membuat relationship.
