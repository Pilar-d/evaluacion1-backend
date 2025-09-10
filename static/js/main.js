
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            alert('¡Gracias por tu mensaje! Te contactaremos pronto.');
            contactForm.reset();
        });
    }
    
    const serviceCards = document.querySelectorAll('.service-card, .feature');
    
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.3s ease';
        });
    });
    
    const menuToggle = document.createElement('button');
    menuToggle.innerHTML = '☰';
    menuToggle.classList.add('menu-toggle');
    
    const headerContent = document.querySelector('.header-content');
    const navigation = document.querySelector('.navigation');
    

    if (window.innerWidth <= 768) {
        headerContent.appendChild(menuToggle);
        
        menuToggle.addEventListener('click', function() {
            navigation.style.display = navigation.style.display === 'flex' ? 'none' : 'flex';
        });
    }
});