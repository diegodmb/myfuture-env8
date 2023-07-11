const sections = document.querySelectorAll('.dwork');
sections.forEach((section) => {
  const container = section.querySelector('.content');
  const tags = Array.from(section.querySelector('.hiden').querySelectorAll('p')).map((tag) => tag.innerText);
  const tagCloud = TagCloud(container, tags, {
    // Configuración del TagCloud
    radius: 220,
    maxSpeed: 'fast',
    initSpeed: 'fast',
    direction: 135,
    keep: true
  });
});

