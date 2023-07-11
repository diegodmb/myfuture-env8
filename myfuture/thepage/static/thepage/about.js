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


const myTags = [
    'JavaScript', 'Sass', 'CSS', 'HTML', 'SEO / SEM', 'Web Design', 'DevOps', 'Docker', 'Kubernetes',
    'React', 'Market Research', 'API', 'Google Analytics', 'UI/UX Design',
    'Python', 'Git', 'Software Development', 'Web Scrapper',
    'Django', 'MS Excel', 'VBA for Excel', 'Business Intelligence',
    'MySQL', 'Web Design', 'Brand Strategy', 'Figma', 'Photoshop', 'BI Dashboards'
];

var tagCloud = TagCloud('.content', myTags,{

    // radius in px
    radius: 300,
  
    // animation speed
    // slow, normal, fast
    maxSpeed: 'fast',
    initSpeed: 'fast',
  
    // 0 = top
    // 90 = left
    // 135 = right-bottom
    direction: 135,
  
    // interact with cursor move on mouse out
    keep: true
  
  }); 

  document.addEventListener('DOMContentLoaded', () => {
    //TRAYECTORIA
    // Obtener todos los elementos de tab y contenido
    const tabs = document.querySelectorAll('.tab');
    const tabContents = document.querySelectorAll('.tab-content');
  
    // Manejar clics en los tabs
    tabs.forEach((tab) => {
      tab.addEventListener('click', (e) => {
        e.preventDefault();
  
        // Desactivar el tab activo actual
        const activeTab = document.querySelector('.tab.active');
        if (activeTab) {
          activeTab.classList.remove('active');
        }
  
        const activeTabContent = document.querySelector('.tab-content.active');
        if (activeTabContent) {
          activeTabContent.classList.remove('active');
        }
  
        // Activar el nuevo tab
        const selectedTab = e.target.getAttribute('href');
        const selectedTabContent = document.getElementById(selectedTab);
        tab.classList.add('active');
        if (selectedTabContent) {
          selectedTabContent.classList.add('active');
        }
      });
    });




});

var ttabs = document.querySelectorAll('.ttab'); // Cambia '.ttab' por el selector correcto de tus tabs

ttabs.forEach(function(tab) {
  tab.addEventListener('mousedown', function(e) {
    // Realiza la acción deseada con el tab clicado, por ejemplo:
    console.log(e.target); // Muestra el elemento clicado en la consola

    // Luego, puedes continuar con el código para manejar los tabs como lo deseas
    // Aquí puedes agregar la lógica para activar/desactivar tabs, etc.
  });
});



function handleTabClicks(tool) {
  var ttabs = document.querySelectorAll('.tt' + tool);
  var ttabContents = document.querySelectorAll('.tc' + tool);
  

  ttabs.forEach((tab) => {
    tab.addEventListener('click', (e) => {
      console.log(tab)
      // Desactivar el tab activo actual dentro del conjunto de pestañas y contenido específico
      var activeTab = document.querySelector('.ttab.active[data-tab^="' + tool + '"]');


      if (activeTab) {
        activeTab.classList.toggle('active');
      }
      var activeTabContent = document.getElementById(activeTab.getAttribute('data-tab'));
      if (activeTabContent) {
        activeTabContent.classList.remove('active');
      }

      // Activar el nuevo tab dentro del conjunto de pestañas y contenido específico
      var selectedTab = e.target.getAttribute('data-tab');
      var selectedTabContent = document.getElementById(selectedTab);
      tab.classList.add('active');
      if (selectedTabContent) {
        selectedTabContent.classList.add('active');
      }
    });
  });
}

