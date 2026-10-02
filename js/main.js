
document.addEventListener("DOMContentLoaded", () => {
  // Mobile nav toggle
  const toggle = document.querySelector(".menu-toggle");
  const navLeft = document.querySelector(".nav-left");
  if (toggle && navLeft) {
    toggle.addEventListener("click", (e) => {
      e.stopPropagation();
      navLeft.classList.toggle("mobile-open");
    });
  }

  // Dropdown toggle functionality (click/touch support)
  const dropdowns = document.querySelectorAll(".dropdown");
  dropdowns.forEach(dropdown => {
    const toggleBtn = dropdown.querySelector(".dropdown-toggle");
    if (toggleBtn) {
      toggleBtn.addEventListener("click", (e) => {
        if (window.innerWidth <= 960) {
          e.preventDefault();
          dropdown.classList.toggle("is-open");
        }
      });
    }
  });

  // Close dropdown or mobile menu when clicking outside
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".site-header")) {
      dropdowns.forEach(d => d.classList.remove("is-open"));
      if (navLeft) navLeft.classList.remove("mobile-open");
    }
  });

  // Automatic active menu highlighting based on current page URL
  const pathParts = window.location.pathname.split("/");
  let currentPath = pathParts[pathParts.length - 1];
  if (!currentPath || currentPath === "") {
    currentPath = "index.html";
  }

  const navLinks = document.querySelectorAll(".nav a, .dropdown-panel a");
  navLinks.forEach(link => {
    const href = link.getAttribute("href");
    if (href === currentPath) {
      link.classList.add("active");
      
      const parentDropdown = link.closest(".dropdown");
      if (parentDropdown) {
        const toggleBtn = parentDropdown.querySelector(".dropdown-toggle");
        if (toggleBtn) {
          toggleBtn.classList.add("active");
        }
      }
    }
  });

  // Discovery list flash notification
  document.querySelectorAll("[data-discover]").forEach(btn => {
    btn.addEventListener("click", () => {
      const name = btn.dataset.discover;
      const flash = document.querySelector(".flash");
      if (flash) {
        flash.textContent = `${name} added to your discovery list`;
        flash.style.display = "block";
        setTimeout(() => flash.style.display = "none", 2200);
      }
    });
  });

  // Form submit demo flash notification
  document.querySelectorAll("form[data-demo]").forEach(form => {
    form.addEventListener("submit", e => {
      e.preventDefault();
      const flash = document.querySelector(".flash");
      if (flash) {
        flash.textContent = "Thank you — your message has been received.";
        flash.style.display = "block";
        setTimeout(() => flash.style.display = "none", 2500);
      }
      form.reset();
    });
  });

  // Ingredient exploration
  const ingredientButtons = document.querySelectorAll("[data-ingredient]");
  const ingredientTitle = document.querySelector("#ingredient-title");
  const ingredientText = document.querySelector("#ingredient-text");
  const ingredientImg = document.querySelector("#ingredient-img");
  const ingredientData = {
    olive: ["Olive", "Explore regions, makers, harvest stories and small-batch olive products.", "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=1000&q=85"],
    sesame: ["Sesame", "Discover traditional pressing, regional character and pantry applications.", "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=1000&q=85"],
    cacao: ["Cacao", "Trace cacao from origin and fermentation through makers and finished treats.", "https://images.unsplash.com/photo-1511381939415-e44015466834?auto=format&fit=crop&w=1000&q=85"],
    saffron: ["Saffron", "Follow the spice from harvest to carefully selected artisan products.", "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=1000&q=85"]
  };

  ingredientButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.ingredient;
      if (ingredientData[key]) {
        if (ingredientTitle) ingredientTitle.textContent = ingredientData[key][0];
        if (ingredientText) ingredientText.textContent = ingredientData[key][1];
        if (ingredientImg) {
          ingredientImg.style.opacity = "0.3";
          setTimeout(() => {
            ingredientImg.src = ingredientData[key][2];
            ingredientImg.alt = `Artisan ${ingredientData[key][0]}`;
            ingredientImg.style.opacity = "1";
          }, 150);
        }
        ingredientButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
      }
    });
  });
  // FAQ Accordion toggle
  document.querySelectorAll(".faq-question").forEach(q => {
    q.addEventListener("click", () => {
      const item = q.closest(".faq-item");
      if (item) item.classList.toggle("open");
    });
  });

  // Harvest Radar Tab switcher
  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const flash = document.querySelector(".flash");
      if (flash) {
        flash.textContent = `Showing harvest data for ${btn.textContent}`;
        flash.style.display = "block";
        setTimeout(() => flash.style.display = "none", 2000);
      }
    });
  });
});


