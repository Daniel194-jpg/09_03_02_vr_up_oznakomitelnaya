const images = [
    'images/image1.jpg',
    'images/image2.jpg',
    'images/image3.jpg',
    'images/image4.jpg',
    'images/image5.jpg'
];

let currentIndex = 0;

const sliderImage = document.getElementById('slider-image');
const caption = document.getElementById('caption');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

function updateSlider() {
    sliderImage.src = images[currentIndex];
    caption.textContent = `Image ${currentIndex + 1} of ${images.length}`;
}

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex === 0) ? images.length - 1 : currentIndex - 1;
    updateSlider();
});

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
    updateSlider();
});

// Initial update
updateSlider();