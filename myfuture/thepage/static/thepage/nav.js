var prevScrollPos = window.pageYOffset;
window.onscroll = function() {

    var currentScrollPos = window.pageYOffset;
    if (prevScrollPos > currentScrollPos){
        document.getElementById('nav').style.top = '0';
    }
    else{
        document.getElementById('nav').style.top = '-100px';
    }
prevScrollPos = currentScrollPos;
}




const navSlide = () => {
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".burger-menu");
    const snav = document.querySelector(".burger-sub-menu");
    const navLinks = document.querySelectorAll(".burger-sub-menu a");
    //toggle Nav
    burger.addEventListener("click", () => {
        console.log("Click")
        nav.classList.toggle("burger-active");
        snav.classList.toggle("sub-burger-active");

        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            }
            else {
                link.style.animation = `navlinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            }
        });
        burger.classList.toggle('toggle');

        //Check if sub-burger-active class is present
        if (snav.classList.contains('sub-burger-active')) {
            snav.style.animation = "subburger 0.5s cubic-bezier(0.645,0.045,0.355,1)"; // Animación normal
        } else {
            snav.style.animation = "subburger-reverse 0.5s cubic-bezier(0.645,0.045,0.355,1)"; // Animación en reversa
        }
    });
}

navSlide();







