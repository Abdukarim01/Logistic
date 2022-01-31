/* ONLOAD ANIMATIONS */
window.onload  = function(){
  let cursors = document.querySelectorAll(".cursor");
  
  cursors.forEach(function(e){

  let cursor_top = Math.floor(Math.random() * (5000 - 50 + 1) + 50);
  let cursor_left = Math.floor(Math.random() * (95 - 5 + 1) + 5);
  let cursor_rotate = Math.floor(Math.random() * 360);
  e.style = `width:50px; 
              position:absolute;
              z-index:-1 !important;
              margin-top:${cursor_top}px;
               left:${cursor_left}%;
               transform:rotate(${cursor_rotate}deg);`;


  
  let animMove = Math.floor(Math.random() * (100 - 50 + 1) + 50)
  e.animate([
  // keyframes
   {transform:'translateY(0px) translateX(0px)' },
   {transform:`translateY(-${animMove+10}px) translateX(-${animMove+5}px) rotate(${animMove+2}deg)`},
   {transform:`translateY(-${animMove+20}px) translateX(-${animMove+10}px) rotate(${animMove+4}deg)` },
   {transform:`translateY(-${animMove+30}px) translateX(-${animMove+15}px) rotate(${animMove+6}deg)` },
   {transform:`translateY(-${animMove+40}px) translateX(-${animMove+20}px) rotate(${animMove+8}deg)` }
], {
  // timing options
  duration: 5000,
  iterations: Infinity,

})
  });
  document.querySelector(".sc1_text1").querySelector("h1").style = "transition: ease 2s; opacity:1;transform:translateX(0%);"
  setTimeout(()=>{
    document.querySelector(".sc1_text2").querySelector('p').style = "transform: translateX(0%); opacity:1; transition: ease 2s;"
  },500)
  setTimeout(()=>{
    document.querySelector(".sc1_clip_btn ").querySelector('button').style = "transform: translateX(0%); opacity:1; transition: ease 2s;"
  },1000)
  }

/* HEADER NAVBAR CONTROL */
let num = 0;
function controlMenu(){

    num++
function mediaNavbar(x) {
    var growDiv = document.querySelector('.sc2_navbar_menu');
    var wrapper = growDiv.querySelector('ul');
  if (x.matches) { 
          if(num >= 2){num = 0}
          if(num == 0){growDiv.style.height = "0px";
                       growDiv.style = "border-bottom:none;";
                       document.body.style = "position:inherit;";
                       document.querySelector(".navbar_control").querySelector("i").classList = "fa fa-bars"
                       setTimeout(()=>{
                        document.querySelector(".curtain").style = "display:none;"
                      },400)       
                      }
          if(num == 1){growDiv.style.height = wrapper.clientHeight + "px";
                       growDiv.style.borderBottom = "1px solid #ffc000";
                       document.querySelector(".curtain").style = "display:block;";
                       document.body.style = "position:fixed;";
                       document.querySelector(".navbar_control").querySelector("i").classList = "fa fa-times"
                      }
  }else {
    growDiv.style = ""
    num = 0
    document.querySelector(".curtain").style = "display:none;"
  }
}

var x = window.matchMedia("(max-width: 992px)")
mediaNavbar(x)
x.addListener(mediaNavbar) 

}



/* CAROUSELS */
 var main_sc2_swipper = new Swiper(".main_sc2_swipper", {
    slidesPerView: "auto",
    spaceBetween: 1,
    loop:false,
    grabCursor: true,
    // centeredSlides: true,
    // autoplay: {
    // delay: 2500,
    // disableOnInteraction: false,
    // },
    pagination: {
    el: ".swiper-pagination",
    clickable: true,  
    },
    });

function mediaslide(y) {
  if (y.matches) {
    document.querySelector(".sc4_carts_swipper").classList = "swiper sc4_carts_swipper"
    document.querySelector(".for_swiper-wrapper").classList = "swiper-wrapper for_swiper-wrapper"
    let slide = document.querySelectorAll(".for_swiper-slide");
    slide.forEach(function(e){
      e.classList = "swiper-slide for_swiper-slide"
    })
    var main_sc4_swipper = new Swiper(".sc4_carts_swipper", {
    slidesPerView: "auto",
    spaceBetween: 1,
    loop:false,
    grabCursor: true,
    // centeredSlides: true,
    // autoplay: {
    // delay: 2500,
    // disableOnInteraction: false,
    // },
    pagination: {
    el: ".swiper-pagination",
    clickable: true,  
    },
    });
  } 

  else {
    document.querySelector(".sc4_carts_swipper").classList = "sc4_carts_swipper"
    document.querySelector(".for_swiper-wrapper").classList = "for_swiper-wrapper"
    let slide = document.querySelectorAll(".for_swiper-slide");
    slide.forEach(function(e){
      e.classList = "for_swiper-slide"
    })
  }
}

var y = window.matchMedia("(max-width: 768px)")
mediaslide(y)
y.addListener(mediaslide) 

var main_sc5_swipper = new Swiper(".sc5_swiper", {
    slidesPerView: "auto",
    spaceBetween: 1,
    loop:false,
    grabCursor: true,
    // centeredSlides: true,
    // autoplay: {
    // delay: 2500,
    // disableOnInteraction: false,
    // },
    pagination: {
    el: ".swiper-pagination",
    clickable: true,  
    },
    });
 


