// JS to handle background opacity on "Discover More" hover for each section
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.destination-section').forEach(section => {
        const btn = section.querySelector('.explore-btn');
        const bg = section.querySelector('.background-img');
        btn.addEventListener('mouseenter', () => {
            bg.style.opacity = 1;
        });
        btn.addEventListener('mouseleave', () => {
            bg.style.opacity = 0.5;
        });
        btn.addEventListener('focus', () => {
            bg.style.opacity = 1;
        });
        btn.addEventListener('blur', () => {
            bg.style.opacity = 0.5;
        });
    });
});