<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Response;

class CartController extends Controller
{
    // Dummy data for cart
    private $cart_items = [
        ["user_id" => 1, "product_id" => 1, "quantity" => 2],
        ["user_id" => 1, "product_id" => 2, "quantity" => 1],
        ["user_id" => 2, "product_id" => 1, "quantity" => 1]
    ];

    // Route to get cart items
    public function getCart()
    {
        return response()->json($this->cart_items);
    }

    // Route to get total quantity of a product in the cart
    public function getTotalQuantity($product_id)
    {
        $total_quantity = array_reduce($this->cart_items, function ($carry, $item) use ($product_id) {
            if ($item['product_id'] == $product_id) {
                $carry += $item['quantity'];
            }
            return $carry;
        }, 0);

        return response()->json(['product_id' => $product_id, 'total_quantity' => $total_quantity]);
    }
}
