## PORT 
5000 -> products : JS express
5001 -> cart : PHP lumen
5002 -> users : Python flask
5003 -> reviews : Python flask 
5004 -> main : Python flask

## ExpressJS
- npm init -y
- npm install express
- node app.js


## Lumen
- Run `composer create-project --prefer-dist laravel/lumen app_cart`
- Buka file routes/web.php dan tambahkan rute-rute yang diperlukan untuk API 

> // Route untuk mendapatkan semua produk[space][space]
Route::get('/cart', 'CartController@index');[space][space]

> // Route untuk mendapatkan detail produk berdasarkan ID[space][space]
Route::get('/cart/quantity/{id}', 'CartController@show');

- Buat file CartController.php di `app/Http/Controllers`

- update kodenya 

- jalankan server `php -S localhost:5001 -t public`