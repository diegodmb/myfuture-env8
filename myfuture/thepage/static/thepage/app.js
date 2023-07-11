

const typed = new Typed('.typed', {
strings: ['TU IDEA', 'TU PLAN','TU VISIÓN','TU SUEÑO', 'TU FUTURO'],
	typeSpeed: 80, // Velocidad en mlisegundos para poner una letra,
	startDelay: 300, // Tiempo de retraso en iniciar la animacion. Aplica tambien cuando termina y vuelve a iniciar,
	backSpeed: 80, // Velocidad en milisegundos para borrrar una letra,
	smartBackspace: false, // Eliminar solamente las palabras que sean nuevas en una cadena de texto.
	shuffle: false, // Alterar el orden en el que escribe las palabras.
	backDelay: 2000, // Tiempo de espera despues de que termina de escribir una palabra.
	loop: true, // Repetir el array de strings
	loopCount: false, // Cantidad de veces a repetir el array.  false = infinite
	showCursor: true, // Mostrar cursor palpitanto
	cursorChar: '|', // Caracter para el cursor
	contentType: 'html', // 'html' o 'null' para texto sin formato
});



var hero = document.getElementById('hero')
var pos = hero.getBoundingClientRect()

//Scrolling Landing

window.addEventListener('scroll', () => {
  var value = window.scrollY;
  //promo.style.top =  60 + value / 3 * 0.2 + 'vh';
  hero.style.opacity = 1 - value * 0.002;
});

//Click sobre topic

function mostrarExten(event) {
  let extendId = this.dataset.imagen.slice(-1);
  let ext = document.getElementById("ext"+extendId);
  ext.style.display= "grid";
}

// Hover sobre Topics

function mostrarImagen(event) {
    let imagenId = this.dataset.imagen;
    let imagen = document.getElementById(imagenId);
  
    if(event.type === 'mouseover') {
      imagen.style.display = "block";
    } else {
      imagen.style.display = "none" 
    }
  }
  
  let textos = document.querySelectorAll("[data-imagen]");
  textos.forEach(texto => {
      texto.addEventListener("mouseover", mostrarImagen);
      texto.addEventListener("mouseout", mostrarImagen);
      texto.addEventListener("click", mostrarExten);
  });

  function moverImagen(event) {
    let imagenId = "topicdecor" + this.id.slice(-1); // obtiene el número del id del contenedor para obtener el id de la imagen correspondiente
    let imagen = document.getElementById(imagenId);
    //let ymove = (event.pageY - this.getBoundingClientRect().top) * 0.0009;
    //let ymove = event.clientY * 0.003;
    //let xmove = event.pageX * 0.003;
    //let height = window.innerHeight;
    //let width = window.innerWidth;
    imagen.style.transform = "translateX(-30px)";
    let x = event.clientX / 15;
    let y = event.clientY / 15 + 30;
  

    imagen.style.transform = "translate("+ x + "px, " + y + "px)"; // actualiza la posición x de la imagen en función de la posición del mouse
     
  }
  
  let contenedores = document.querySelectorAll("[id^='topic']"); // selecciona todos los contenedores cuyo id comienza con "topic"
  contenedores.forEach(contenedor => {
    contenedor.addEventListener("mousemove", moverImagen);
    contenedor.addEventListener("click", mostrarExten);
  });

// Interrumpe la acción en los Tag A Topic para permitir la ejecucción de otra funcion
let topics = document.querySelectorAll("a.nec");

  topics.forEach(topic => {
    topic.addEventListener("click", function(event) {
      event.preventDefault();
    });
  });


  //Cierra Extended Topic

for (let i = 1; i <= 8; i++) {
  const image = document.getElementById(`close${i}`);
  image.addEventListener("click", function() {
    console.log(i)
    document.getElementById(`ext${i}`).style.display = "none";
  });
}