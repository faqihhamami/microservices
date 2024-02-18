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
<blockquote>
// Route untuk mendapatkan semua produk
Route::get('/cart', 'CartController@index');

// Route untuk mendapatkan detail produk berdasarkan ID
Route::get('/cart/quantity/{id}', 'CartController@show');
</blockquote>

- Buat file CartController.php di `app/Http/Controllers`

- update kodenya 

- jalankan server `php -S localhost:5001 -t public`