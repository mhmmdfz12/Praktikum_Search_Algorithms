# Praktikum_Search_Algorithms

#Deskripsi

Repository ini berisi implementasi berbagai algoritma pencarian dalam Pyhton. Algoritma pencarian ini digunakan untuk menemukan jalur atau solusi dalam suatu ruang pencarian. Dalam proyek ini, kami mengimplementasikan berbagai algoritma pencarian, baik yang tidak berinformasi (uninformed search) 
maupun yang berinfomasi (informed search).

#Penjelasan Algoritma

Uninformed Search (Tidak Berinformasi)
1. Depth First Search (DFS) - Algoritma yang menelusuri simpul secara mendalam sebelum kembali dan 
   menjelajahi jalur lain.
2. Breadth First Search (BFS) - Algoritma yang menelusuri simpul secara mendatar, dengan 
   mengeksplorasi semua tetangga sebelum melanjutkan ke level berikutnya.
3. Uniform Cost Search (UCS) - Algoritma yang menggunakan antrian prioritas untuk mengeksplorasi 
   jalur dengan biaya paling rendah terlebih dahulu.

Informed Search (Berinformasi)

1. Greedy Best-First Search - Algoritma yang memilih simpul berdasarkan nilai heuristiknya, tanpa 
   mempertimbangkan biaya yang sudah dikeluarkan.
2. A* Tree Search** - Algoritma yang menggunakan kombinasi biaya langkah (g) dan heuristik (h) 
   untuk mencari jalur optimal dalam struktur pohon.
3. A* Graph Search** - Mirip dengan A* Tree Search tetapi menghindari eksplorasi ulang simpul yang sudah dikunjungi.

#Cara Menjalankan di Google Colab
1. Clone repository ini ke Google Colab atau komputer lokal
2. Jalankan script yang diinginkan dengan Python
3. Jika menggunakan Google Colab, unggah file terlebih dahulu dan jalankan
