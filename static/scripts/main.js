window.onload = function () {
  let year = document.getElementById("year");
  if (year) {
    year.textContent = new Date().getFullYear();
  }

  setTimeout(function () {
    let alert = document.querySelector(".alert"); // Select the alert element
    if (alert) {
      alert.classList.remove("show"); // Remove the 'show' class to hide the alert
      alert.classList.add("fade"); // Add the 'fade' class to apply fading effect
    }
  }, 3000); // 5 seconds delay
};
