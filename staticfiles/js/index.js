function randomValues() {
  anime({
    targets: '.cursor',
    translateX: function() {
      return -anime.random(0, 500);
    },
     translateY: function() {
      return -anime.random(0, 800);
    },
    easing: 'easeInOutQuad',
    duration: 750,
    complete: randomValues,
  
  });
}
randomValues()

var acc = document.querySelectorAll(".swiper_carts");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}

window.onload = ()=>{

  let pulses = document.querySelectorAll(".pulse_container");
  let cursors = document.querySelectorAll(".cursor");
  cursors.forEach(function(e,index){
  let cursor_top = Math.floor(Math.random() * (700 - 110 + 1) + 110 )
  let cursor_left = Math.floor(Math.random() * (90 - 5 + 1) + 5 )
  let cursor_rotate = Math.floor(Math.random() * (360 - 10 + 1) + 10 )
    e.style = `position:absolute; top:${cursor_top}%; margin-left:${cursor_left}%; transition:ease 0.4s;`;
   
  })
  document.querySelector(".sc1_text1").querySelector("h1").style = "transition: ease 2s; opacity:1;transform:translateX(0%);"
  setTimeout(()=>{
    document.querySelector(".sc1_text2").querySelector('p').style = "transform: translateX(0%); opacity:1; transition: ease 2s;"
  },500)
  setTimeout(()=>{
    document.querySelector(".sc1_clip_btn ").querySelector('button').style = "transform: translateX(0%); opacity:1; transition: ease 2s;"
  },1000)
}
window.addEventListener('scroll', function() {
 /* ANIM1 */
 var element = document.querySelector('.section_items1 ').querySelector(".servis_text_block");
  var position = element.getBoundingClientRect();
  if(position.top < window.innerHeight - 250) {
    element.style = "transform:translateX(0%); opacity: 1; transition: ease 1.5s;"
  }else{
    element.style = "transform:translateX(-50%); opacity: 0; transition: all 1.5s;"
  }

  var element2 = document.querySelector('.section_items1 ').querySelector(".servis_image_block");
  var position2 = element.getBoundingClientRect();
  if(position2.top < window.innerHeight - 450) {
    element2.style = "transform:translateX(0%); opacity: 1; transition: ease 1.5s;"
  }else{
    element2.style = "transform:translateX(50%); opacity: 0; transition: all 1.5s;"
  }
 /*ENDANIM1*/

/* ANIM2*/
 var element3 = document.querySelector('.section_items2 ').querySelector(".servis_text_block");
  var position3 = element3.getBoundingClientRect();
  if(position3.top < window.innerHeight - 350) {
    element3.style = "transform:translateX(0%); opacity: 1; transition: ease 1.5s;"
  }else{
    element3.style = "transform:translateX(50%); opacity: 0; transition: all 1.5s;"
  }

  var element4 = document.querySelector('.section_items2').querySelector(".servis_image_block");
  var position4 = element4.getBoundingClientRect();
  if(position4.top < window.innerHeight - 250) {
    element4.style = "transform:translateX(0%); opacity: 1; transition: ease 1.5s;"
  }else{
    element4.style = "transform:translateX(-50%); opacity: 0; transition: all 1.5s;"
  }
/*ENDANIM2*/

/* ANIM3 */
let scroll = Math.floor(window.scrollY);
if(scroll <= 650){
  document.querySelector(".sc1_text1").querySelector("h1").style = "transition: ease 2s; opacity:1;transform:translateX(0%);"
  setTimeout(()=>{
    document.querySelector(".sc1_text2").querySelector('p').style = "transform: translateX(0%); opacity:1; transition: ease 2s;"
  },500)
  setTimeout(()=>{
    document.querySelector(".sc1_clip_btn ").querySelector('button').style = "transform: translateX(0%); opacity:1; transition: ease 2s;"
  },1000)
}else{
  document.querySelector(".sc1_text2").querySelector('p').style = "transform: translateX(-20%); opacity:0; transition: ease 0.5s;"
  document.querySelector(".sc1_clip_btn ").querySelector('button').style = "transform: translateX(-80%);opacity: 0;transition: ease 0.5s;"
  document.querySelector(".sc1_text1").querySelector("h1").style = "transition: ease 0.5s; opacity:0;transform:translateX(-40%);"
  
}

/* ENDANIM3 */

/* ANIM4 */
let cards = document.querySelectorAll(".for_swiper-slide");
cards.forEach((e,index)=>{
  let csrdposition = e.getBoundingClientRect();
  if(csrdposition.top < window.innerHeight - 150){
    e.style = "transform: translateX(0%); opacity: 1;transition: ease 1.5s"
  }
})
/* ENDANIM4 */

});

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
    autoplay: {
    delay: 2500,
    disableOnInteraction: false,
    },
    pagination: {
    el: ".swiper-pagination",
    clickable: true,  
    },
    });


var main_sc5_swipper = new Swiper(".new_section_swiper1", {
    slidesPerView: "auto",
    spaceBetween: 1,
    centeredSlides: true,
    loop:false,
    grabCursor: true,
    autoplay: {
    delay: 2000,
    disableOnInteraction: false,
    },
    
    });

var main_sc5_swipper = new Swiper(".new_section_swiper2", {
    slidesPerView: "auto",
    spaceBetween: 1,
    loop:false,
    grabCursor: true,
    autoplay: {
    delay: 3500,
    disableOnInteraction: false,
    },
    
    });


let element = document.querySelectorAll(".client_comment");
element.forEach((e)=>{
  e.addEventListener('click', function(){
        var panel = this;
          if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
            panel.style.transform = null;
          } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
            panel.style.transform = 'skew(-9deg)'
          }
  })  
})
