// Funcionalidad básica para el formulario de contacto
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Aquí iría la lógica para enviar el formulario
            // Por ahora, solo mostraremos una alerta
            alert('¡Gracias por tu mensaje! Te contactaremos pronto.');
            contactForm.reset();
        });
    }
    
    // Efectos de animación para las tarjetas de servicios
    const serviceCards = document.querySelectorAll('.service-card, .feature');
    
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.3s ease';
        });
    });
    
    // Navegación responsive (podría expandirse)
    const menuToggle = document.createElement('button');
    menuToggle.innerHTML = '☰';
    menuToggle.classList.add('menu-toggle');
    
    const headerContent = document.querySelector('.header-content');
    const navigation = document.querySelector('.navigation');
    
    // Solo agregar el toggle menu en dispositivos móviles
    if (window.innerWidth <= 768) {
        headerContent.appendChild(menuToggle);
        
        menuToggle.addEventListener('click', function() {
            navigation.style.display = navigation.style.display === 'flex' ? 'none' : 'flex';
        });
    }
});