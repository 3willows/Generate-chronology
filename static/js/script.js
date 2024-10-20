document.addEventListener('DOMContentLoaded', function() {
  const mobilePopup = document.getElementById('mobile-popup');
  const closeBtn = mobilePopup.querySelector('.close');

  // Check if the device is a mobile device
  if (window.matchMedia("(max-width: 768px)").matches) {
      mobilePopup.style.display = 'block';
  }

  closeBtn.addEventListener('click', function() {
      mobilePopup.style.display = 'none';
  });

  window.addEventListener('click', function(event) {
      if (event.target === mobilePopup) {
          mobilePopup.style.display = 'none';
      }
  });
});