// Carousel ======================================


const slides=document.querySelectorAll(".slide");
const slider=document.querySelector(".slider");
let c=0;
let i=0;
slides.forEach((slide,index)=>{
   i=index
})
function slideshow(){
  slides.forEach((slide)=>{
    slider.style.transform=`translateX(-${c * 100}%)`
  })
}
function prev(){
  if(c<=0){
    c=i
  }
  else{c--}
  slideshow()
}
function next(){
  if(c>=i){
    c=0
  }
  else{c++}
  slideshow()
}


// STARSSS ================================

const rates=document.querySelectorAll(".rate");
rates.forEach((rate,index)=>{
  rate.addEventListener('click',(e)=>{
    let x= index;
    rates.forEach((rate,t)=>{
      if(x>=t){
        rate.style.color="rgb(239, 68, 68)"
      }
      else{
        rate.style.color="rgb(75 85 99)"
      }
      
   })
})
})

const disc = ('{{product.mrp}}' - '{{product.sale_price}}')/'{{product.mrp}}'*100;
console.log(disc)
document.getElementById('discount').innerHTML=disc.toFixed(2)+"%";


// Adding cart items  ---------
// ================================================================
// ================================================================


if (localStorage.getItem('thistle_cart') == null) {
    var thistle_cart = {};
} else {
    thistle_cart = JSON.parse(localStorage.getItem('thistle_cart'));
    
    console.log(thistle_cart);
    updateCart(thistle_cart);
}



// ==========================If the add to cart button is clicked, add/increment the item ====================
$('.cart').click(function() {
    console.log('clicked');
    var idstr = document.getElementById('prid').value;
    console.log(idstr);
    console.log(thistle_cart);




    if (thistle_cart[idstr] != undefined) {
        qty = thistle_cart[idstr][0]+1;


    } else {
        qty = 1;

        name = document.getElementById('name').innerHTML;
        price = document.getElementById('price').innerHTML;
        mrp = document.getElementById('mrp').innerHTML;
        img = document.getElementById('img').value;
        thistle_cart[idstr] = [qty,name,parseInt(price),parseInt(mrp),img,idstr.slice(2)];
    }
    updateCart(thistle_cart);
});


function updateCart(thistle_cart) {
    var sum = 0;
    for (var item in thistle_cart) {

            sum = sum+thistle_cart[item][0];

        }
    var idstr = document.getElementById('prid').value;
    if (thistle_cart[idstr] !== undefined){
    if (thistle_cart[idstr][0]!==0){
                console.log(item)
            document.getElementById('atc').innerHTML = "<div class='mt-5  cart'><button id='minus' class=' minus font-bold text-white bg-indigo-500 border-0 pb-1 px-2 focus:outline-none hover:bg-indigo-600 mt-5 rounded'>-</button> <span id='val' class=' font-bold p-3 mx-2 border text-center w-8'>" + thistle_cart[idstr][0] + "</span> <button id='plus' class='plus font-bold text-white bg-indigo-500 border-0 pb-1 px-2 focus:outline-none hover:bg-indigo-600 mt-5 rounded'   > + </button> </div>";
            }
            else {
                delete thistle_cart[item];


            }
}



    localStorage.setItem('thistle_cart', JSON.stringify(thistle_cart));
   // document.getElementById('cart').innerHTML = sum;

    console.log(thistle_cart);
}


// If plus or minus button is clicked, change the cart as well as the display value==================
// =======================
// ========================


$('.divpr').on("click", "button.minus", function() {
    var idstr = document.getElementById('prid').value;
    console.log(thistle_cart)
    thistle_cart[idstr][0] = thistle_cart[idstr][0] - 1;
    thistle_cart[idstr][0] = Math.max(0, thistle_cart[idstr][0]);
    document.getElementById('val').innerHTML = thistle_cart[idstr][0];
    updateCart(thistle_cart);
});
$('.divpr').on("click", "button.plus", function() {
    var idstr = document.getElementById('prid').value;

    if (thistle_cart[idstr]!=undefined){
      thistle_cart[idstr][0] = thistle_cart[idstr][0] + 1;
    document.getElementById('val').innerHTML = thistle_cart[idstr][0];
    }
    else{
        qty = 1;
        name = document.getElementById('name').innerHTML;
        price = document.getElementById('price').innerHTML;
        mrp = document.getElementById('mrp').innerHTML;
        img = document.getElementById('img').value;
        thistle_cart[idstr] = [qty,name,parseInt(price),parseInt(mrp),img,idstr.slice(2)];
    }
    updateCart(thistle_cart);
});