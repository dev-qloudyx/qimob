
  function sidebar() {
      return {
          isMobile: window.matchMedia("(max-width: 640px)").matches,
          sidebarOpen: false,
          sidebarProductMenuOpen: false,
          content: document.getElementById('content'),
  
          updateIsMobile() {
              this.isMobile = window.matchMedia("(max-width: 640px)").matches;
              this.updateContentMargin(); // Add this line
          },
  
          updateContentMargin() {
              if (this.sidebarOpen && !this.isMobile) {
                  this.content.style.marginLeft = '220px';
              } else if (!this.sidebarOpen && !this.isMobile) {
                  this.content.style.marginLeft = '60px';
              } 
              else {
                  // Add a condition for when it's mobile
                  this.content.style.marginLeft = '0px'; // or whatever value you prefer when it's mobile
              }
          },
  
          toggleSidebar() {
              this.sidebarOpen = !this.sidebarOpen;
              this.updateContentMargin(); // Call this instead of updateIsMobile
          },
  
          toggleSidebarProductMenu() {
              this.sidebarProductMenuOpen = !this.sidebarProductMenuOpen;
              window.localStorage.setItem('sidebarProductMenuOpen', this.sidebarProductMenuOpen ? 'open' : 'close');
          },
  
          checkSidebarProductMenu() {
              const storedState = window.localStorage.getItem('sidebarProductMenuOpen');
              if (storedState) {
                  this.sidebarProductMenuOpen = storedState === 'open';
              }
          },
  
          init() {
              window.addEventListener('resize', this.updateIsMobile.bind(this));
              this.checkSidebarProductMenu();
          }
      }
  }
  
  window.addEventListener('DOMContentLoaded', (event) => {
      sidebar().init();
  });
  


