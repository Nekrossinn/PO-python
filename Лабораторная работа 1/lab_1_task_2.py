# TODO Найдите количество книг, которое можно разместить на дискете

disc_space = 1.44 * 1024 * 1024
book_space = 4 * 25 * 50 * 100
book_amount = disc_space//book_space
print("Количество книг, помещающихся на дискету:", book_amount)