def analisis_review_aplikasi(reviews):
    if not reviews:
        return None
    
    # Menghitung rating terendah, rating tertinggi, dan rata-rata rating
    rating_terendah = min(reviews)
    rating_tertinggi = max(reviews)
    rata_rata_rating = sum(reviews) / len(reviews)
    
    # Mengembalikan hasil
    return [rating_terendah, rating_tertinggi, round(rata_rata_rating, 1)]

# Contoh penggunaan dengan input pertama
data_review_1 = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0]
output_1 = analisis_review_aplikasi(data_review_1)
print("Input:", data_review_1)
print("Output:", output_1)

# Contoh penggunaan dengan input kedua
data_review_2 = [5, 4, 2.5, 5, 3.6, 1.1, 3.6, 4, 4.2, 1.5]
output_2 = analisis_review_aplikasi(data_review_2)
print("Input:", data_review_2)
print("Output:", output_2)
