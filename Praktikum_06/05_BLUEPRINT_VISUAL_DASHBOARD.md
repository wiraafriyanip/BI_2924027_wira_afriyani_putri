# PRAKTIKUM 06 - PETA VISUAL FINAL

**Target:** M06_WIRA_AFRIYANI_PUTRI_2924027.pbix. Buat halaman bernama `Executive Overview`, Canvas 16:9.

| Area | Visual | Field/measure | Catatan format |
|---|---|---|---|
| Header, sisi kanan | Slicer 1 | Dim_Date[Year] | Dropdown |
| Header, sisi kanan | Slicer 2 | Dim_Branch[Branch_Name] | Dropdown |
| Header, sisi kanan | Slicer 3 | Fact_Sales[Channel] | Dropdown |
| Baris KPI 1 | Card | [_Measures][Total Sales] | Rp, satuan juta/miliar, 1 digit |
| Baris KPI 2 | Card | [_Measures][Gross Profit] | Rp, satuan sama dengan sales |
| Baris KPI 3 | Card | [_Measures][Profit Margin] | 0.0% |
| Baris KPI 4 | Card | [_Measures][Target Achievement %] | 0.0% |
| Tengah kiri (60%) | Line chart | Axis Dim_Date[Month_Year]; Y [Total Sales] | Sort Dim_Date[Month_Index] naik |
| Tengah kanan (40%) | Clustered bar | Axis Dim_Product[Category]; Y [Gross Profit] | Sort profit descending |
| Bawah (100%) | Matrix | Rows Dim_Branch[Branch_Name]; Values [Total Sales], [Gross Profit], [Profit Margin], [Target Achievement %] | Angka rapi dan tidak terpotong |

**Interaksi:** Edit interactions -> slicer Year / Branch / Channel memfilter visual yang relevan. Filter Branch memfilter target lewat relationship, sedangkan Channel hanya ada pada actual; pencapaian target berubah karena numerator berubah. Tooltip chart menampilkan nama bulan/kategori dan nilai tepat.

**Bukti:** screenshot relationship Model, dashboard tanpa filter, dashboard Year tunggal, dashboard Branch tunggal, dashboard Channel tunggal. Jangan ketik angka benchmark sebagai teks card.
