if (localStorage.getItem('thistle_cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('thistle_cart'));
}
console.log(cart);
var sum = 0;
var totalPrice = 0;
var totalMrp = 0;
if ($.isEmptyObject(cart)) {
    //if object is empty
    mystr = `<p>Your cart is empty, please add some items to your cart before checking out!</p>`
    $('#items').append(mystr);
} else {
    for (item in cart) {
        let qty = cart[item][0];
        let name = cart[item][1];
        let price = cart[item][2];
        let mrp = cart[item][3]
        let img = cart[item][4];
        let prod_id = cart[item][5];
        sum = sum + qty;
        totalPrice = totalPrice + qty*price
        totalMrp = totalMrp + qty*  mrp
        if (qty!==0){
       // $('#items').append(`<div class='card-body'><div class='d-flex justify-content-between'><div class='d-flex flex-row align-items-center'><div><a href="/products/${prod_id}"><img src='${img}'class='img-fluid rounded-3' alt='Shopping item' style='width: 65px;''></a></div><div class=''><h5 class='mx-2 '>${name}</h5></div></div><div class='d-flex flex-row '><div class="mt-3" style='width: 120%; color:rgb(75, 74, 74); text-align: right;'><h6 class='fw-normal mb-1'>Qty:${qty}</h6><h5 class='mb-0'>&#8377 ${price*qty}</h5></div></div></div></div>`);
        }
      }

}
// document.getElementById('cart').innerHTML = sum;
// document.getElementById('totalPrice').innerHTML = totalPrice;
$('#items_json').val(JSON.stringify(cart));
