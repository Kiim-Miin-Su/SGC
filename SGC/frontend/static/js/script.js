
let currentIndex = 0;

function slideAds() {
    const slides = document.querySelector('.ad-slider .slides');
    const totalSlides = slides.children.length;

    currentIndex = (currentIndex + 1) % totalSlides;
    slides.style.transform = `translateX(-${currentIndex * 100}%)`;
}

setInterval(slideAds, 4000); // 4초마다 슬라이드 전환

