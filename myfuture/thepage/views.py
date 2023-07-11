from django.shortcuts import render
from random import choice
import random

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def index(request):

    segments={}
    segments ={
        'page2':'Si necesitas',
        'page3':'¿Por qué elegirme?',
        'page4': 'Conoce algunos de mis proyectos'
    }
    #Landing Page
    landing={}
    landing ={
        'header1': 'TE AYUDO A TRANSFORMAR',
        'header2': 'EN UN PROYECTO DIGITAL EXITOSO',
        'sub': 'Con un enfoque colaborativo, dedicación y compromiso alcanzaremos los resultados sobresalientes que necesitas.'
    }
    #banner1
    mission='Mi misión es brindarte un servicio integral, cercano y enfocado en los objetivos a alcanzar. Te ofrezco mi amplia experiencia combinada con mis habilidades técnicas. Te propongo que unamos nuestros esfuerzos en lograr resultados sorprendentes.'
    imgquote= 'thepage/img/quote.svg'
    portrait= 'thepage/img/pic.webp'


    #Page 2
    necesidades =[
        'Desarrollar tu mejor sitio web',
        'Crear o renovar tu tienda On-Line',
        'Desarrollar un sofware o aplicación',
        'Recopilar datos de internet',
        'O si tan sólo tienes una idea...',
    ]


    extended=[
        {'header': 'RESULTADOS SOBRESALIENTES',
        'imgdirec': 'thepage/img/topic1.jpg',
        'items': [
                '¿Estás buscando fortalecer tu presencia online y aumentar el engagement de tu audiencia?',
                'Como profesional del desarrollo web y marketing digital, mi enfoque está en construir una experiencia de usuario excepcional que conecte con tu audiencia y fomente la confianza. ',
                'Trabajemos juntos para lograr resultados sobresalientes.'
                ],
        'cta': 'Contactame',
        'link': 'contact'},

        {'header': 'DISEÑO, CREATIVIDAD Y CONVERSIÓN',
        'imgdirec': 'thepage/img/topic2.jpg',
        'items': [
                'Desarrollemos un sitio de e-commerce fuera de serie.',
                'Contarás con todas las herramientas necesarias para administrarlo fácilmente e incrementar tus ventas.',
                'Analicemos las problemáticas de tu tienda on-line y elaboremos un plan.',
                ],
               'cta': '¿Comenzamos?',
                'link':'contact' },

        {'header': 'SOLUCIONES UNICAS PARA TUS DESAFÍOS ÚNICOS',
        'imgdirec': 'thepage/img/topic3.jpg',
        'items': [
                'Construyamos algo increíble juntos.',
                'Como desarrollador, me especializo en brindar soluciones de calidad que se adaptan a las necesidades únicas de cada cliente. ',
                'Me enorgullece ofrecer un servicio al cliente excepcional, asegurándome de que cada proyecto sea entregado a tiempo y dentro del presupuesto acordado.'
                ],
               'cta': '¿Cómo puedo ayudarte?',
                'link':'contact'},

        {'header': 'INFORMACIÓN EN VALOR.',
            'imgdirec': 'thepage/img/topic4.jpg',
            'items': [
                '¿Necesitas recopilar y analizar datos clave para tu empresa de forma eficiente y precisa?',
                'Con más de 20 años de experiencia trabajando con información estratégica para importantes empresas, desarrollando soluciones innovadoras orientadas a la toma de decisiones.',
                'Transformemos juntos información en valor.'
                ],
           'cta': '¿Empezamos?',
            'link':'contact'},
        {'header': 'TODO COMIENZA POR UNA IDEA.',
            'imgdirec': 'thepage/img/topic5.jpg',
            'items': [
                'Pero lo que hagamos con ella es lo que marca la diferencia. Te acompañaré en el camino y juntos haremos que tu idea se convierta en realidad.',
                'Con más de 20 años de experiencia trabajando con información estratégica para importantes empresas, desarrollando soluciones innovadoras orientadas a la toma de decisiones.',
                'Transformemos juntos información en valor.'
                ],
           'cta': '¿Empezamos?',
            'link':'contact'},
    ]
    colors = ['#f72585ff', '#b5179eff', '#7209b7ff', '#560badff', '#480ca8ff', '#3a0ca3ff', '#3f37c9ff', '#4361eeff', '#4895efff', '#4cc9f0ff']
    page2=[]
    dic={}
    x=1
    for nec in necesidades:
        dic={
            'color1':choice(colors),
            'delay1':random.randint(1, 5)/10 + x/100,
            'width1': random.randint(8, 10) + x/100,
            'color2':choice(colors),
            'delay2':random.randint(1, 5)/10 + x/100,
            'width2': random.randint(4, 8) + x/100,
            'color3': choice(colors),
            'delay3':random.randint(1, 5)/10 + x/100,
            'width3': random.randint(4, 9) + x/1000,
            'necesidad': nec,
            'imgdirec': 'thepage/img/topic'+str(x)+'.jpg'
        }
        page2.append(dic)
        x = x + 1
    # Page3
    page3=[
        {'header': 'EXPERTISE',
            'subheader': 'EXPERTISE',
            'desc': ['Mis habilidades técnicas se potencian y complementan gracias a mi extensa trayectoria laboral en reconocidas empresas multinacionales.',
                    'Esto me permite identificar y desarrollar las mejores soluciones ante cada necesidad.'],
            'logos': [
                {'img':'thepage/img/tec1.png', 'alt': 'Brand Strategy'},
                {'img':'thepage/img/tec2.png', 'alt': 'Web Development'},
                {'img':'thepage/img/tec3.png', 'alt': 'Market Research'},
                {'img':'thepage/img/tec4.png', 'alt': 'Business Intelligence'},
                {'img': 'thepage/img/tec5.png', 'alt': 'Software Development'},
                {'img': 'thepage/img/tec6.png', 'alt': 'Digital Marketing'}
                ],
        'cta': 'Más info',
        'link':'about'},

        {'header': 'TEC',
            'subheader': 'COMPETENCIAS',
            'desc': ['Gracias al manejo avanzado de estas herramientas y a mi fuerte orientación al cliente, he logrado crecer y tener una carrera destacada en el mundo corporativo.',
                      'He desarrollado herramientas interactivas y fáciles de usar que simplifican la información compleja, adaptándola a las necesidades del usuario final y orientadas a la toma de decisiones informadas.',
                      'Mi enfoque siempre ha sido brindar soluciones personalizadas y de calidad al usuario final, creando herramientas eficientes, efectivas y amigables.'],
            'logos': [
            {'img':'thepage/img/comp1.png', 'alt': 'MS Excel'},
            {'img':'thepage/img/comp2.png', 'alt': 'Visual Basic For Excel'},
            {'img':'thepage/img/comp3.png', 'alt': 'Python'},
            {'img':'thepage/img/comp4.png', 'alt': 'Django'},
            {'img':'thepage/img/comp5.png', 'alt': 'Javascript'},
            {'img':'thepage/img/comp6.png', 'alt': 'Sass CSS'},
            {'img':'thepage/img/comp7.png', 'alt': 'HTML'},
            {'img':'thepage/img/comp8.png', 'alt': 'CSS'},
            {'img':'thepage/img/comp9.png', 'alt': 'Git'},
            {'img':'thepage/img/comp10.png', 'alt': 'SQL'},
            {'img':'thepage/img/comp11.webp', 'alt': 'Docker'},
            {'img':'thepage/img/comp12.png', 'alt': 'Kubernetes'}
            ],
            'cta': 'Ver Ejemplos',
        'link':'about#trayectoria'},


    {'header': 'TRA',
    'subheader': 'TRAYECTORIA',
    'desc': ['Cuento con más de 20 años de trayectoria ocupando puestos claves en importantes empresas multinacionales que me otorgan una ventaja significativa.',
              'Esta ventaja consiste en que puedo interpretar y adaptar mejor tus necesidades al proyecto y resultado final, contribuyendo al mismo desde mi experiencia.'
              'Estoy listo para aplicar toda mi experiencia a tu proyecto.'],
        'logos': [
            {'img':'thepage/img/tra1.png', 'alt': 'IBOPE'},
            {'img':'thepage/img/tra2.png', 'alt': 'Kantar Media'},
            {'img':'thepage/img/tra3.png', 'alt': 'Nielsen E-Ratings'},
            {'img':'thepage/img/tra4.png', 'alt': 'LAPTV Latin American Pay Televisión Services'},
            {'img':'thepage/img/tra5.png', 'alt': 'Fox International Channels'},
            {'img':'thepage/img/tra6.png', 'alt': 'TV Azteca Quintana Roo'},
            {'img':'thepage/img/tra7.png', 'alt': 'Fox Sports México'}
            ],
    'cta': 'Más info',
    'link':'about#trayectoria'},

    ]

    #Page4

    page4=[
            {'logo': 'thepage/img/nplogo.png',
            'logoalt': 'Nutri Peek Logo',
            'bkg': 'thepage/img/ejm1.jpg',
            'bkgalt': 'Nutri Peek Case Study',
            'desc': 'ALIMENTACIÓN 100% NATURAL PARA MASCOTAS',
            'link': 'nutripeek',
            'expertise': [
                'Desarrollo de Marca',
                'Desarrollo de Producto',
                'Estrategia de Marketing',
                'Diseño y Desarrollo Web',
                'Desarrollo de Software de gestión',
                'Creación de Contenido'
                ]},
        {'logo': 'thepage/img/calogo.png',
            'logoalt': 'Consorcio de Abogados Logo',
            'bkg': 'thepage/img/ejm2.jpg',
            'bkgalt': 'Consorcio de Abogados Case Study',
            'desc': 'ESTUDIO DE ABOGADOS DE CANCÚN',
            'link': 'consorciodeabogados',
            'expertise': [
                'Diseño y Desarrollo Web',
                'Creación de Contenido y Fotografía',
                'Estrategia de Marketing'
                ]},
            {'logo': 'thepage/img/fslogo.png',
            'logoalt': 'Fox Sports México Logo',
            'bkg': 'thepage/img/ejm3.jpg',
            'bkgalt': 'Fox Sports México Case Study',
            'desc': 'DISTRIBUIDOR DE CANALES DEPORTIVOS',
            'link': 'foxsports',
            'expertise': [
                'Business Intelligence Web App',
                'Business Intelligence Reports',
                'Recopilación de Datos de Internet (Web Scrapping / API) ',
                ]}
    ]

    context = {}
    context['anims']= anims(20)
    context['anims1']= anims(20)
    context['anims2']= anims(20)
    context['segments']= segments
    context['landing']= landing
    context['mission']= mission
    context['portrait']= portrait
    context['imgquote']= imgquote
    context['page2']= page2
    context['imgdirec']= 'thepage/img/topic'
    context['extended']= extended
    context['page3']= page3
    context['page4']= page4


    
    
    return render(request, 'thepage/index.html', context)

def about(request):
    landing={}
    landing ={
        'header1': 'VERSATILIDAD Y COMPROMISO',
        'sub': ['Me llamo Diego Alvarez, soy desarrollador Full Stack, Diseñador Web y un experto en MS Excel.',
                'Tengo una muy amplia trayectoria en importantes empresas multinaciones, ocupando puestos claves para toda latinoamérica. Ahora te ofrezco toda mi experiencia y habilidades enfocado a tu proyecto.']
    }

    yo={
        'img': 'thepage/img/pic.webp',
        'imgalt': 'Yo, desarrollador',
        'imgquote': 'thepage/img/quote.svg',
        'quotealt': 'Quote',
        'quote': 'Como desarrollador Full-Stack, puedo ofrecerte soluciones completas, desde el diseño y programación de la interfaz visual (lo que se ve) hasta los aspectos técnicos detrás de escena que permite que todo funcione sin problemas (lo que no se ve).',
        'quote1': 'Mi amplia trayectoria corporativa me coloca un paso adelante de otros servicio similares.'

    }

    trabajo={
        'header': 'Los pilares fundamentales de mi proceso de trabajo',
        'items': [
        {'tit': 'INTEGRIDAD Y COMPROMISO', 'img': 'thepage/img/integridad.jpg','ext': 'Construir relaciones sólidas basadas en la confianza y el respeto mutuo es más que un objetivo, es un valor fundamental. Creo que la transparencia y la honestidad son la base de cualquier relación duradera y significativa. Y lo sé por experiencia propia.'},
        {'tit': 'ESCUCHAR Y ENTENDER','img': 'thepage/img/entender.jpg', 'ext': 'Comprender en profundidad las necesidades de mis clientes para elaborar el mejor plan de acción y las mejores soluciones específicas.'},
        {'tit': 'ESCALABLE Y SOSTENIBLE','img': 'thepage/img/escalable.jpg', 'ext': 'Soluciones que funcionen y sean sostenibles y escalables en el futuro desde el primer día'},
        {'tit': 'COMUNICACIÓN Y PARTICIPACIÓN','img': 'thepage/img/comunicacion.jpg','ext': 'Proceso de comunicación fluido, metódico y constante para asegurarnos en todo momento el estar en la misma página.'},
        {'tit': 'CALIDAD Y SEGURIDAD', 'img': 'thepage/img/seguridad.jpg','ext': 'Pruebas exhaustivas y rigurosas previo a las entregas, garantizando de esta forma, el cumplimientos de requisitos y su estabilidad.'},
        {'tit': 'SOPORTE Y MANTENIMIENTO', 'img': 'thepage/img/soporte.jpg','ext': 'Proporcionar un servicio cercano y en pos de abordar las dificultades de forma temprana y lograr un funcionamiento pleno.'},
        ]
    }

    empresas= ['Desarrollador Independiente',
                'TV Azteca Quintana Roo',
                'Fox International Channels',
                'LAPTV',
                'Kantar Media', 
                'IBOPE Argentina']

    contacto={ 'linkedin': 'Linkedin',
                'link': 'https://www.linkedin.com/in/diegoh73/',
                'cv': 'Mi CV',
                'pdf': 'thepage/img/CV Diego Alvarez 2023 Esp.pdf ' 

            }
    
    trayectoria= [
                    {'empresa': 'DHA-Dev',
                    'logo': 'thepage/img/traf.png',
                    'sitio': 'https://dha-dev.com',
                    'periodo': 'Mar2020 - Presente',
                    'cargo': 'Desarrollador Full-Stack',
                    'logros': ['Desarrollo reportes interactivos de Business Intelligence para Fox Sports.',
                                'Creé una aplicación Web para agrupar, jerarquizar y analizar audiencias y tendencias en Twitter (En desarrollo)',
                               'Lideré la estrategia de marca y productos para Nutri Peek.',
                               'Desarrollé la aplicación web para gestión, administración y ventas Nutripeek.Diseñé y desarrollé su sitio web',
                               'Diseñé y desarrollé un WebScrapper para analizar la compentencia de Fox Sports.',
                               'Diseñé y desarrollé el sitio web para dos estudios de abogados en Cancún.',
                               'Analicé el mercado publicitario Latinoamericano para Fox, generando información de gran valor para la compañía al consolidar grandes bases de datos de proveedores locales de los principales países.']
                    },
                    {'empresa': 'TV Azteca QRoo',
                     'logo': 'thepage/img/tra6.png',
                    'sitio': 'https://www.aztecaquintanaroo.com/',
                    'periodo': 'Sep-2018 - Mar-2020',
                    'cargo': 'Inteligencia Comercial',
                    'logros': ['Fui responsable de las cuentas y prospectos más importantes de la televisora. Empresas como Hertz, Best Day, Grupo Xcaret, Aeromar y Grand Coral, entre otros.',
                               'Contribuí a captar clientes gracias a la incorporación de estudios y análisis de datos, mejorando la eficiencia de inversión del cliente.',
                               'Optimicé las estrategias publicitarias y de comunicación para los clientes en todas las plataformas publicitarias.',
                               'Como resultado de mi trabajo, en solo un año, tuve a mi cargo el presupuesto de ventas más importante de la televisora (40%), superando mi presupuesto anual en más del 50%.']
                    },
                    {'empresa': 'Fox (Ahora Star+)',
                     'logo': 'thepage/img/tra5.png',
                    'sitio': 'https://www.starplus.com/es-mx/',
                    'periodo': 'May-2010 - Abr-2018',
                    'cargo': 'Director de Estrategia de Producto',
                    'logros': ['Gestioné la información de mercado de BI para diferentes áreas de la empresa, incluyendo contenido, ventas publicitarias, marketing, digital, prensa/RRPP y alta gerencia.',
                               'También fui responsable de los estudios de mercado Ad-Hoc, cuantitativos y cualitativos para toda la región.',
                               'Logré una mayor sinergia entre los distintos equipos de trabajo y su vinculación con la alta gerencia.',
                               'Logré un mayor compromiso y valoración de la información orientada a la toma de decisiones'
                               'Implementé análisis de eficiencia de presupuesto de programación, lo que generó ahorros valuados en millones de dólares.',
                               'Logré mejorar significativamente la calidad y los tiempos de entrega de los reportes.']
                    },
                    {'empresa': 'LAPTV (Ahora Star+)',
                     'logo': 'thepage/img/tra4.png',
                    'sitio': 'https://www.starplus.com/es-mx/',
                    'periodo': 'Jul-2004 - Jun-2010',
                    'cargo': 'Gerente Investigación de Mercado',
                    'logros': ['Definí y realicé estudios de mercado cuantitativos y cualitativos para toda la región, lo que me permitió contribuir en la profesionalización y respaldo de decisiones comerciales, marketing y producto basadas en análisis de información.',
                               'Participé activamente en el relanzamiento y actualización de las marcas de la compañía (Movie City, Cinecanal y The Film Zone).',
                               'Me destaqué brindando soporte a las áreas de venta publicitaria de toda la región.',
                               'Logré un mayor compromiso y valoración de la información orientada a la toma de decisiones',
                               'Por mi contribución, fui promovido a la gerencia de Investigación de Mercado para toda la región desde Argentina, posición históricamente localizada en Atlanta, EE.UU.']
                    },
                    {'empresa': 'Kantar Media',
                     'logo': 'thepage/img/tra3.png',
                    'sitio': 'https://www.kantar.com/latin-america',
                    'periodo': 'Jun-2003 - Jul-2004',
                    'cargo': 'Jefe de Produccción',
                    'logros': ['Estuve a cargo de la producción del estudio Target Group Index (TGI) para Argentina, supervisando tareas desde el diseño del cuestionario, la producción y hasta la presentación, ventas y capacitación a clientes.',
                               'Junto con mi equipo, logramos cumplir por primera vez los cronogramas previstos y los plazos pactados con los clientes con el mejor estándar de calidad de su historia.']
                    },
                    {'empresa': 'IBOPE Argentina',
                     'logo': 'thepage/img/tra3.png',
                    'sitio': 'https://www.kantaribopemedia.com.ar/',
                    'periodo': 'Nov-1992 - Jun-2003',
                    'cargo': 'Jefe de Proyectos',
                    'logros': ['Realicé una consultoria de capacitación en Guatemala orientada a las oficinas locales y a los canales de TV Abierta, fortaleciendo la relación entre ambas partes y desarrollando herramientas para la oficina local.',
                               'En el rol de Jefe Comercial de Nielsen eRatings logré que los principales jugadores del mercado de Internet contrataran nuestro estudio por sobre la competencia.',
                               'Como Líder de Proyecto adapté e introduje al mercado argentino los más avanzados softwares de análisis de audiencia y planificación publicitaria de la compañía Markdata',
                               'Me convertí en referente en cuestiones de medición de audiencias y uso de herramientas para el mercado argentino, dando apoyo a la empresa en cada nuevo proyecto y desafío.']
                    }]
    
    tools=[
        {'tool':'Django',
        'tablist': ['Resumen', 'Ventajas', 'Django y Yo', '¿Por qué Django?'],
        'img': 'thepage/img/django.jpg',
        'atributos': ['Confiable', 'Seguro', 'Rápido', 'Escalable', 'Flexible'],
        'cta': '¿Quieres saber más?',
        'tabs': [
                {'header': 'DJANGO EN ACCIÓN',
                 'desc': ['Utilizo Django como framework para el desarrollo de sitios web y aplicaciones. Me apasiona trabajar con esta tecnología porque permite una rápida creación de prototipos y una fácil escalabilidad.',
                          ]},
                {'header': 'UNA OPCIÓN SUPERADORA',
                 'desc': ['Django es un framework confiable y de alto rendimiento que ofrece una gran cantidad de herramientas para el desarrollo web.',
                          'Entre sus beneficios se encuentran la seguridad, escalabilidad y flexibilidad. Además, con Django es posible crear aplicaciones rápidamente y con una sintaxis clara y concisa.',
                        ]},
                {'header': 'EXPERTO EN DJANGO',
                 'desc': ['Como especialista en Django, tengo experiencia en el desarrollo de aplicaciones y sitios web de alta calidad.',
                        'Me apasiona ayudar a mis clientes a convertir sus ideas en proyectos web exitosos y escalables.',
                        'Me comprometo a ofrecerte soluciones innovadoras y de alta calidad en tu proyecto.'
                        ]},
                {'header': 'CONTROL TOTAL',
                 'desc': ['Django es una excelente opción para aquellos que buscan un sitio web personalizado, seguro y escalable.',
                          'A diferencia de Wordpress y otros CMS, Django ofrece un control total sobre la estructura y el diseño del sitio web, lo que permite crear una experiencia única para los usuarios.',
                        ]},

        ]
        },
        {'tool':'Javascript',
        'tablist': ['Resumen', 'La Estuctura', 'El Diseño', 'La Interactividad', 'Avanzado'],
        'img': 'thepage/img/javascript.jpg',
        'tabs': [
                {'header': 'JAVASCRIPT / HTML / CSS',
                 'desc': ['Javascript, HTML y CSS son tres lenguajes de programación fundamentales para cualquier desarrollador web.'
                          'Cada uno tiene su propia función y juntos permiten la creación de sitios web dinámicos e interactivos.',
                          'Cuento con más de 5 años experiencia programando con estos lenguajes y se aplica tanto para el desarrollo de sitios web, como de aplicaciones web.'
                          ]},
              {'header': 'HTML, EL ESQUELETO',
                 'desc': ['HTML, abreviatura de Hypertext Markup Language, es el lenguaje utilizado para crear la estructura de una página web.',
                           'Permite definir el contenido y la jerarquía de los elementos, como encabezados, párrafos, imágenes y enlaces.'
                        ]},
                {'header': 'CSS, EL ESTILO Y EL DISEÑO',
                 'desc': [ 'CSS, abreviatura de Cascading Style Sheets, es el lenguaje utilizado para dar estilo y diseño a una página web.',
                           'Permite definir cómo se ven los elementos en una página, incluyendo colores, fuentes, tamaños y posicionamiento.',
                        ]},
                {'header': 'JAVASCRIPT, LE DA VIDA',
                 'desc': ['Javascript es un lenguaje de programación de alto nivel que se utiliza para crear interactividad en las páginas web.',
                           'Permite crear efectos dinámicos, como animaciones y transiciones, y también permite la creación de aplicaciones web complejas'
                           'El dominio de Javascript es esencial en el desarrollado web paraq crear experiencias interactivas y enriquecedoras para los usuarios.'
                        ]},
                {'header': 'EL POTENCIAL',
                 'desc': ['Si lo que necesitas es un sitio web de calidad o una aplicación web para tu negocio, es fundamental contar con un desarrollador que domine estos lenguajes',
                          'HTML, CSS y Javascript permitirán que tu sitio web sea dinámico, efectivo y atractivo para tus visitantes, lo que puede marcar la diferencia en el éxito de tu proyecto.',
                          'Si inviertes en un desarrollador web profesional y experimentado, tendrás la tranquilidad de saber que tu sitio web está en buenas manos y que se utilizarán las mejores prácticas para su creación y desarrollo. '
                        ]},

        ]
        },
        {'tool':'Excel',
        'tablist': ['Resumen', 'Ventajas', 'Business Intelligence', 'Automatización', 'Excel+'],
        'img': 'thepage/img/excel.jpg',
        'tabs': [
                {'header': '"EXCEL GURU"',
                 'desc': ['Puedo hacer cosas extraordinarias con esta herramienta. He trabajado con ella por más de 20 años.',
                          'Mi experiencia me ha permitido dominar una amplia gama de habilidades, desde el análisis de datos hasta la creación de informes complejos, detallados pero al mismo tiempo de rápida interpretación.',
                          'Si necesitas un experto en Excel, ¡No dudes en contactarme!'
                          ]},
                {'header': 'HERRAMIENTA CLAVE',
                 'desc': ['Excel es una herramienta fundamental en el mundo de los negocios y la industria en general. ',
                          'He sabido aprovechar sus capacidades para organizar y analizar grandes cantidades de datosy destacarme por ese trabajo en importantes organizaciones.. ',
                          'Con Excel, he simplificado el manejo de datos complejos mediante tablas dinámicas, con la creación de Dashboard intuitivos y he respaldado la toma de decisiones informadas basadas en la gestión de información corporativa y de mercado.'
                        ]},
                {'header': 'EXPERTO EN BI',
                 'desc': ['A lo largo de mi carrera, Excel a jugado un papel preponderante, sobre todo en lo referente al análisis orientado a Business Intelligence e Investigación de Mercado.',
                           'Domino todas las funciones avanzadas y los distintos métodos de búsquedas, filtros y fórmulas, así como también las tablas dinámicas y el manejo de grandes bases de datos.',
                           #'Esto me permite analizar gran cantidad de información y presentarla de manera clara, concisa y acorde a las necesidades estratégicas',
                           'Puedo identificar tendencias y patrones en los datos, lo que me ayuda a anticipar posibles oportunidades y escenarios para respaldar la toma de decisiones informadas.'
                          ]},
                {'header': 'PROGRAMACIÓN EN EXCEL',
                 'desc': ['El dominio de Macros y Programación en Excel con VBA me otorga una gran ventaja ya que me permite automatizar tareas repetitivas, sistematizar y agilizar procesos, personalizando el funcionamiento de Excel según las necesidades específicas.',
                           'Esto se traduce en una mejora en la eficiencia, precisión y productividad de las tareas; ahorro de tiempo y recursos para tu negocio.',
                           'Además, puedo utilizar mis habilidades en Excel y VBA para crear soluciones personalizadas y automatizadas a tus necesidades'
                        ]},
                {'header': 'UN PLUS POCO HABITUAL',
                 'desc': ['Excel'
                        ]},

        ],
        }
    ]
    etools= [{'header': 'WEB SCRAPPING / API',
              'img': 'thepage/img/api.jpg',
              'imgalt': 'Web Scrapping Image',
            'desc': ['Tengo experiencia en la extracción de datos de diferentes sitios web mediante API (Aplication Programming Interfaces) y/o empleando técnicas de Web Scrapping.',
                    'Este tipo de técnicas son muy utilizadas en una gama muy amplia de industrias para obtener datos clave, entre las que se destacan el sector turístico, financiero, inmobiliario, medios de comunicación, sector de la salud, etc.',
                        ],
            'cta': 'Más Información'
            },
            {'header': 'DEVOPS',
              'img': 'thepage/img/devops.jpg',
              'imgalt': 'Devops Image',
            'desc': ['Como profesional en DevOps, puedo implementar soluciones de gestión de contenedores y orquestación utilizando herramientas como Kubernetes y Docker.',
                    'También soy hábil en el uso de plataformas en la nube como Heroku y AWS para garantizar una implementación eficiente y escalable de aplicaciones y sitios web.'
                    'Mi conocimiento en estas tecnologías me permite ofrecer soluciones robustas y fiables para cualquier proyecto de desarrollo web.'
                        ],
            'cta': 'Más Información'
            },
            {'header': 'FOTOGRAFIA, EDICIÓN Y DISEÑO',
              'img': 'thepage/img/foto.jpg',
              'imgalt': 'Fotografía Image',
            'desc': ['Tengo experiencia en la extracción de datos de diferentes sitios web utilizando consultas mediante API (Aplication Programming Interfaces) y/o empleando técnicas de Web Scrapping.',
                     'De esta manera, puedo alimentar bases de datos y a partir de ellas analizar y visualizar la información para identificar patrones y tendencias que puedan ser útiles para la toma de decisiones.',
                     'Este tipo de técnicas son muy utilizadas en una gama muy amplia de industrias, entre las que se destacan el sectot turístico, financiero, inmobiliario, medios de comunicación, sector de la salud, etc.',
                     'En resumen, cualquier industria que requiera acceso a datos de diferentes fuentes puede beneficiarse de las API y el web scraping para automatizar la recopilación de información y mejorar la toma de decisiones basada en datos.'
                        ],
            'cta': 'Más Información'
            }
        ]
    context = {}
    context['tanims1']= anims(3)
    context['tanims2']= anims(1)
    context['tanims3']= anims(4)
    context['tanims4']= anims(4)
    context['tanims5']= anims(4)
    context['banims1']= anims(2)
    context['banims2']= anims(3)
    context['banims3']= anims(2)
    context['banims4']= anims(1)
    context['banims5']= anims(4)


    context['landing']= landing
    context['yo']= yo
    context['trabajo']= trabajo
    context['empresas']= empresas
    context['trayectoria']= trayectoria
    context['tools']= tools
    context['etools']= etools
    context['contacto']= contacto
    

    return render(request, 'thepage/about.html', context)

def services(request):
    landing ={
        'header1': 'MI EXPERIENCIA ES EL ',
        'span': 'PLUS',
        'sub': ['Mis paquetes de servicio están diseñadas a la medida de tu presupuesto.',
        'Te ofrezco un servicio distinto, te ofrezco agregar valor a tu proyecto digital único. Mi experiencia es el plus',
        ]
    }

    pluses=[{
        'tit': 'FLEXIBLE',
        'subtit':'Adaptado a las necesidades cambiantes',
        'desc':[
                 'Te brindo la flexibilidad necesaria para ajustar y personalizar el desarrollo y evolución de tu proyecto en cuanto a tareas y tiempos.'
                 ]
    },
        {'tit': 'POR SUSCRIPCIÓN',
        'subtit':'Forjando una relación a largo plazo',
        'desc': [
            'A través de un modelo de suscripción, puedes iniciar un desarrollo completo, escalable y de primer nivel sin una inversión inicial elevada.',
            'Y por supuesto, soporte técnico y actualizaciones continuas.'
            ]
        },
        {'tit': 'AMPLIO',
         'subtit':'Aportando Valor',
        'desc': [
            'Desde el diseño y desarrollo web, la automatización de procesos con MS Excel, marketing e investigación de mercado. Sistemas de pago, gestión de usuarios y funciones personalizadas.',
            ]
        },
        {'tit': 'EXTERNO',
         'subtit':'Un Recurso Independiente de tu lado',
        'desc': [
            'Como desarrollador externo, te ofrezco la ventaja de contribuir con una visión fresca, capacitada y experimentada sustentada por mi trayectoria y conocimientos.',
            ]
        },
    ]

    segments={}
    segments ={
        'page2':'Te ofrezco los siguientes servicios',
    }

  #Page 2
    necesidades =[
        'DESARROLLO WEB',
        'DESARROLLO DE SOFTWARE',
        'AUTOMATIZAR PROCESOS',
        'RECOPILAR Y ANALIZAR INFORMACIÓN',
        'UN POCO DE TODO...',
    ]


    extended=[
        {'header': 'TE PROPONGO DIFERENCIARTE',
        'imgdirec': 'thepage/img/topic1.jpg',
        'items': [
                'A través de una sesión estratégica y personalizada, exploremos juntos tus metas y objetivos.',
                'Transformemos tu visión en una experiencia online auténtica y diferente a todo, reflejando fielmente tu visión y aportemos valor a tu propuesta.',
                'Con una comunicación constante y fluida, encontraremos las claves que te hacen único y las plasmaremos al proyecto.',
                'Trabajemos juntos para lograr resultados sobresalientes.'
                ],
        'cta': 'Contactame',
        'link': 'contact'},

        {'header': 'INFINITAS POSIBILIDADES',
        'imgdirec': 'thepage/img/nutriapp.jpg',
        'items': [
                'A través de una sesión estratégica analizaremos las necesidades y problemáticas de tu negocio.',
                'Elaboremos un plan de trabajo que nos lleve a una solución que sea a tu exacta medida.',
                'Identifiquemos las formas de ahorrar tiempos y recursos, mejorando procesos y gestiones administrativas',
                'Detectemos todas aquellas tareas repetitivas que te quitan tiempo, provocan errores y te aburren e implementemos una automatización de procesos',
                'Diseñemos juntos los dashboards que ayudarán a monitorear la operación y que obtengas la información que necesitas, cuando la necesitas.',
                'Implementemos las herramienta mediante un proceso de mejora constante.'
                'Te aseguro que añadiremos valor a tu negocio y lo llevaremos un paso adelante.'
                ],
               'cta': '¿Comenzamos?',
                'link':'contact' },

        {'header': 'INFORMACIÓN EN VALOR.',
            'imgdirec': 'thepage/img/foxtwitter.jpg',
            'items': [
                '¿Necesitas recopilar y analizar datos clave para tu empresa de forma eficiente y precisa?',
                'Con más de 20 años de experiencia trabajando con información estratégica para importantes empresas, desarrollando soluciones innovadoras orientadas a la toma de decisiones.',
                'Transformemos juntos información en valor.'
                ],
           'cta': '¿Empezamos?',
            'link':'contact'},
        {'header': 'TODO COMIENZA POR UNA IDEA.',
            'imgdirec': 'thepage/img/topic5.jpg',
            'items': [
                'Pero lo que hagamos con ella es lo que marca la diferencia. Te acompañaré en el camino y juntos haremos que tu idea se convierta en realidad.',
                'Con más de 20 años de experiencia trabajando con información estratégica para importantes empresas, desarrollando soluciones innovadoras orientadas a la toma de decisiones.',
                'Transformemos juntos información en valor.'
                ],
           'cta': '¿Empezamos?',
            'link':'contact'},
    ]
    colors = ['#f72585ff', '#b5179eff', '#7209b7ff', '#560badff', '#480ca8ff', '#3a0ca3ff', '#3f37c9ff', '#4361eeff', '#4895efff', '#4cc9f0ff']
    page2=[]
    dic={}
    x=1
    for nec in necesidades:
        dic={
            'color1':choice(colors),
            'delay1':random.randint(1, 5)/10 + x/100,
            'width1': random.randint(8, 10) + x/100,
            'color2':choice(colors),
            'delay2':random.randint(1, 5)/10 + x/100,
            'width2': random.randint(4, 8) + x/100,
            'color3': choice(colors),
            'delay3':random.randint(1, 5)/10 + x/100,
            'width3': random.randint(4, 9) + x/1000,
            'necesidad': nec,
            'imgdirec': 'thepage/img/serv'+str(x)+'.jpg'
        }
        page2.append(dic)
        x = x + 1

    context = {}
    context['tanims1']= anims(3)
    context['tanims2']= anims(2)    
    context['tanims3']= anims(4)
    context['tanims4']= anims(4)
    context['tanims5']= anims(4)
    context['banims1']= anims(3)
    context['banims2']= anims(2)
    context['banims3']= anims(4)
    context['banims4']= anims(1)
    context['banims5']= anims(2)
    context['landing']=landing
    context['pluses']=pluses
    context['segments']=segments
    context['page2']=page2
    context['extended']=extended

    return render(request, 'thepage/services.html', context)

def portfolio(request):
    landing={}
    landing ={
        'header1': 'EXPERIENCIAS DIGITALES',
        'sub': ['Aquí te presento algunos de mis proyectos realizados como desarrollador independiente.',
        'Proyectos que combinan diseño y desarrollo web. Aplicaciones web. Recolección, análisis de datos con web scrapping y API, gestión de bases de datos, proyectos de Business Intelligence y mis trabajos en fotografía',
        ]
    }

    workindex=[{'img': 'thepage/img/nutripeek.jpg',
              'imgalt': 'Nutri Peek',
              'tit': 'NUTRI PEEK',
              'id': 'nutripeek'
            },
            {'img': 'thepage/img/foxsports.jpg',
              'imgalt': 'Fox Sports',
              'tit': 'FOX SPORTS',
              'id': 'foxsports'
              
            },
            {'img': 'thepage/img/consorcio.jpg',
              'imgalt': 'Consorcio de Abogados',
              'tit': 'CONSORCIO DE ABOGADOS',
              'id': 'consorciodeabogados'
            },
            {'img': 'thepage/img/fotografia.jpg',
              'imgalt': 'Fotografía',
              'tit': 'FOTOGRAFÍA',
              'id': 'fotografia'
            }
    ]

    context = {}
    context['tanims1']= anims(3)
    context['tanims2']= anims(1)    
    context['tanims3']= anims(4)
    context['tanims4']= anims(4)
    #context['tanims5']= anims(4)
    #context['banims1']= anims(2)
    #context['banims2']= anims(3)
    context['banims3']= anims(4)
    #context['banims4']= anims(1)
    context['banims5']= anims(2)
    context['landing']=landing
    context['workindex']=workindex

    return render(request, 'thepage/portfolio.html', context)

def profile(request, profile):
    dworks=[{'id':'nutripeek',
             'nombre':'NUTRI PEEK',
             'desc':'Nutri Peek es una empresa dedicada a la elaboración de alimento natural para mascotas',
             'decordesc': 'thepage/img/nutridesc.jpg',
             'sitio': 'nutripeek.com.mx',
             'visitas': '4.7K',
             'quote': ['Involucrado en el proyecto desde su concepción, jugué un rol clave en su etapa de desarrollo de producto, aportando toda mi experiencia a ello.',
                       'Tuve la responsabilidad de desarrollar su página web y el software administrativo y de gestión de la empresa, abarcando gran parte de la operación.',
                       'Por supuesto que elegí Django porque brinda un entorno robusto, flexible y seguro que garantiza un desarrollo ágil, escalable y de calidad, que proporciona una solución confiable y eficiente.',
                       'A pocos meses de iniciar la operación y por las característica únicas otorgadas al producto logramos fidelizar una base importante de clientes de consumo regular y nuevos clientes continuaban llegabando semana a semana.'
                       ],
             'tags':['Estrategia de Marketing', 'Desarrollo de producto', 'Diseño de Logo', 'Software Development', 'Web Design', 'Web Development', 'Estrategia de contenido', 'Social Media','Diseño Gráfico', 'Fotografía', 'Edición Fotográfica', 'Photoshop', 'Figma', 'Django', 'Python', 'Facebook Ads'],
            'items': [{'img': 'thepage/img/nutriestrategia.jpg',
                       'imgalt': 'Estrategia de Producto',
                       'desc': 'Estrategia de Producto',
                       'ext': ['A partir de un importante trabajo de investigación previa, logramos introducir un producto innovador al mercado de mascotas',
                               'La competencia son marcas ya establecidas, cuyas principales fortalezas son la facilidad y el precio, pero con una fuerte contra, no contribuyen a una buena salud y son productos ultraprocesado y antinaturales.'
                               'Además identificamos otras debilidades en la percepción de estas marcas y es la lejaniaIdentificamos otras debilidades en estas marcas']
                    },
                    {'img': 'thepage/img/nutriprod.jpg',
                       'imgalt': 'Cercanía de marca',
                       'desc': 'Una marca cercana, un producto único',
                       'ext': ['Por lo tanto, centramos el desarrollo del producto hacia  gran calidad, de fácil preparación, ofreciendo un servicio personalizado y cercano.',
                               'Junto con una estrategia '
                               'Se logró fidelizar a una importante base de clientes y el producto fue recomendado por veterinarios.',
                               'Esto fue la base que permitió el desarrollo de un software integral para la gestión de la operación el cuál encontrarán descripto en esta misma página.']
                    },
                    { 'img':'thepage/img/nutrilogo.jpg',
                        'desc':'Diseño de logotipo', 
                        'ext':['La forma octogonal del logo representa la forma de las hamburguesas para mascotas.',
                                'Esta forma se integra a la clásica huellita que identifican inequívocamente a los producto para mascotas',
                                'Se desarrollaron varias versiones en las que se combinan distintos colores como forma de adaptarse a diferentes tonalidades de fondo'],
                    },
                      {'img':'thepage/img/nutripage.jpg',
                        'desc': 'Desarrollo de página web', 
                       'ext':['Diseño, Desarrollo y Contenidos para la página',
                              'Nuestro objetivo de comunicación era la importancia de brindar la mejor alimentación para nuestras mascotas',
                              'El foco estuvo puesto en destacar la importancia para la salud y la felicidad de las mascotas de brindarles la mejor alimentación, y que la mismo tiempo, sea muy facil de servir.',
                              ]
                       },
                      {'desc': 'Contenidos Nutri Peek Blog',
                        'ext':['Con un fuerte foco en la estrategia SEO y como resultado de la investigación previa, desarrollamos la estrategia de contenido del blog de nutri peek enfocado en las temáticas más solicitadas por nuestro target cuando se trata de alimentación saludable para mascotas',
                               'Temáticas como alimentación saludable para mascotas, los riesgos del alimento seco y también con espacio para la diversión, con perfiles de las razas de mascota preferidas por los mexicanos.'],
                        'img':'thepage/img/nutriblog.jpg'},
                      {'desc': 'Software de Gestión', 
                       'ext':['El software de gestión integral para nutri peek, abarcay relaciona todo el proceso de operación del emprendimiento:',
                              'Comenzando desde la gestión de proveedores, las materias primas y sus precios, el inventario de producto en todas sus recetas, incluyendo el empaque y etiquetado, los costos y gastos de la operación.',
                              'Por el lado comercial, la herramienta permitia gestionar clientes, conocer sus hábitos de compra, gestionar los pedidos, organizar el calendario de entregas, la facturación, incluyendo la forma de pago y el seguimiento de los cobros pendientes.'],
                        'img':'thepage/img/nutrigral.jpg'},
                        {'desc': 'Software de Gestión: Bases de Datos', 
                       'ext':['El software mantenía, relacionaba y alimentaba distintas bases de datos en SQL',
                              'Categoría de gastos, Proveedores, Gastos, Productos, Clientes y sus mascotas, pedidos y detalle de pedido son las bases de datos relacionales administradas por la aplicación'],
                        'img':'thepage/img/nutridb.jpg'},
                        {'desc': 'Software de Gestión: Dashboards', 
                       'ext':['A partir de la información colectada y almacenada en las bases de datos durante la operación de Nutri Peek y aprovechando mi experiencia en Business Intelligence se desarrollaron distintos reportes con el objetivo de optimizar la operación',
                              'Destaco los reportes gastos y ventas, variaciones de gastos y ventas vs mes anterior y vs mismo período del mes anterior. Evolución de ventas, agrupadas de forma anual, trimestral, mensual y semanalmente. Ranking de clientes, frecuencia de compra y programación de clientes frecuentes. Cronograma y agenda de entrega de pedidos, entre otros.'],
                        'img':'thepage/img/nutriapp.jpg'},
                        {'desc': 'Diseño Gráfico, Fotografía y Edición', 
                       'ext':['Me encargué del diseño y edición del arte y las fotografías utilizadas en el emprendimiento.',
                              'Packaging, etiquetas, artes promocionales y redes sociales'],
                        'img':'thepage/img/nutriartes.jpg'}, 
                        ]},

                        {'id':'foxsports',
                        'nombre':'FOX SPORTS',
                        'desc':'Fox Sports México es el canal líder en deportes de la TV Méxicana. Transmite las principales propiedades deportivas como La Liga MX, Fórmula 1, UFC, NFL, entre otras. Es adempas un referente periodiodístico de los deportes a partir de sus emblemáticas producciones originales como La Última Palabra, Central Fox y Fox Sports Radioproduce programas deportivos de gran repercusión.',
                        'sitio': 'foxsports.com.mx',
                        'visitas': '5.5M',
                        'quote': ['Me encanta el trabajo que realizo para Fox Sports, combino mi pasión por los deportes con mi experiencia en análisis avanzado de datos, investigación de mercado y estrategia de contenido.',
                                'Con acceso a una fuente infinita de información que se actualiza diariamente, proveniente tanto de fuentes interna como externas, cuyos resultados se emplean en respaldar la toma de decisiones estratégicas y potenciar resultados futuros en cuestiones audiencia, acciones promocionales, estrategia de contenido y ventas publicitarias.',
                                'La gestión de grandes volúmenes de datos es un gran desafío que requiere el dominio de herramientas como Excel avanzado con Macros y Tablas dinámicas, así como Python y Django para web scraping y consultas a API on line.',
                                'Trabajo en consolidar el liderazgo del grupo en términos de audiencia y ventas publicitarias en un mercado muy dinámico y competitivo.'
                                ],
                        'tags':['Business Intelligence', 'Estrategia de Contenido', 'Excel Avanzado', 'Tablas Dinámicas', 'Visual Basic for Excel', 'Macros', 'Django & Python', 'API | Web Scrapping', 'Bases de Datos', 'Data Analysis', 'TV Ratings', 'IBOPE', 'Ad Spent'],
                        'items': [{'img': 'thepage/img/foxintro.jpg',
                                'imgalt': 'Introducción a la medición de audiencia',
                                'desc': 'Un Rol Clave en los Medios',
                                'ext': ['En la industria de la TV y los medios de comunicación en general, los ratings representan un elemento fundamental en la rutina diaria de trabajo.',
                                        'Las mediciones de audiencia televisiva producen grandes volúmenes de información que requieren de un trabajo meticuloso de análisis, elaboración y presentación de datos por parte de los analistas que trabajan con ella.',
                                        'El análisis de esta información se torna clave para desarrollar la estrategia de contenido, para analizar en detalle a los competidores y por sobre todas las cosas, juega un papel trascendental en la distribución de la pauta publicitaria.',
                                        ]
                                },
                                {'img': 'thepage/img/foxgral.jpg',
                                'imgalt': 'Business Intelligence para Fox Sports',
                                'desc': 'Business Intelligence',
                                'ext': ['Los informes de Business Intelligence para Fox Sports cubren las necesidades de información para las áreas de Programación, Ventas, Distribución, Adquisiciones, Marketing, Prensa y Relaciones Públicas y la Alta Gerencia.',
                                        'A abarcan desde el desempeño diario del contenido, tendencias, resultados mensuales, trimestrales, semestrales, anuales, resultados y oportunidades de ventas, proyecciones, objetivos y proyectos especiales. Todo comparado vs competidores',
                                        'Los reportes deben ser sintéticos, completos, interactivos, de fácil interpretación y presentados de forma profesional.',
                                        ]
                                },
                                {'img': 'thepage/img/foxauto.jpg',
                                'imgalt': 'Imagen que muestra Hoja de Excel con botones que representan la Sistematización de Reportes',
                                'desc': 'Sistematización de Reportes',
                                'ext': ['Para poder lograrlo es necesario por una lado alimentar, categorizar, relacionar y analizar bases de datos de gran tamaño e implementar sistemas que automaticen la generación de los principales reportes rutinarios y deben estar adaptados para poder responder de forma ágil a requerimientos frecuentes y especiales.',
                                        'Para ello me valgo principalmente de mis conocimientos avanzados en Excel, Macros avanzadas desarrolladas con Visual Basic, tablas dinámicas, dominio extenso de funciones. Además, me valgo de Web Scrapping y Consultas a API para obtener información on-line',
                                    ]
                                },
                                { 'img':'thepage/img/foxdb.jpg',
                                    'imgalt': 'Imagen que representa la gestión de bases de datos',
                                    'desc':'Gestión de Bases de Datos', 
                                    'ext':['Base de datos de audiencia por contenido en canales propios y competidores, con audiencia en diferentes targets de audiencia donde incorporo categorizaciones propias que potencian el análisis, por ejemplo: tipo de contenido, categoría de deporte o género de programa, liga, equipo, tipo de emisión, costo de la propiedad.',
                                           'Base de datos de inversión publicitaria en México, donde también incorporo categorizaciones personalizadas con el objetivo de potenciar el análisis, detectar oportunidades y obtener ventajas competitivas a partir de información exclusiva.',
                                           'Base de datos de programación futura de competidores mediante el desarrollo de una aplicación que colecta la información on-line y que otorga una ventaja competitiva al permitirnos accionar gracias a esta información.'
                                        ],
                                },
                                {'img':'thepage/img/foxtwitter.jpg',
                                    'imgalt': 'Aplicación para analizar Twitter Deportes',
                                    'desc': 'Twitter for Sports', 
                                'ext':['Desarrollé una aplicación on-line con Django que releva en tiempo real los tweets de las principales cuentas de Twitter vinculadas al deporte y sus resultados (Likes, Comments, Retweets, Quotes), mediante consultas a la API de Twitter.',
                                        'La información se agrupa en distintas categorías personalizables, para poder consolidar, jerarquizar y perfilar en distintas temporalidades y de esta forma, conocer de forma rápida y completa, las tendencias de la red social más importante para los medios de comunicación.',
                                        'La aplicación está diseñada para poder crear distintos "Universos", por ejemplo, periódicos, partidos políticos, personalidades de la cultura, por citar algunos casos.'
                                        ]
                                },
                                {'img':'thepage/img/foxads.jpg',
                                    'imgalt': 'Reportes en Excel para analizar el mercado publicitario',
                                    'desc': 'Ventas Publicitarias', 
                                'ext':['A partir de la base de datos de inversión publicitaria para el mercado de México, desarrollé una herramienta fundamental para el equipo de ventas que aporta un valor agregado a la información de ventas.',
                                        'Además de visualizar los principales KPI y compararlos contra el desempeño del grupo, es posible identificar las marcas que están lanzando campañas para poder contactarlas y ofrecerles espacios en el grupo.',
                                        'De la misma manera, es posible visualizar a simple vista, cuales anunciantes invierten en los canales competidores y no invierten en Fox Sports o que invierten menos, entre muchas otras características diferenciales y únicas.',
                                        'Esta herramienta está diseñada para ser interpretada de forma sencilla y a simple vista y para lograrlo aprovecho las características avanzadas de excel, como funciones, macros, tablas dinámicas, etc.'
                                        ]
                                },
                            ]},
                            {'id':'consorciodeabogados',
                        'nombre':'CONSORCIO DE ABOGADOS',
                    'desc':'Consorcio de Abogados es un jóven estudio de abogados de Quintana Roo especializado en Derecho Familiar y Derecho Civil. Han llevado adelante con éxito casos de divorcio, pensiones alimenticias y conflictos laborales entre otros.',
                    'decordesc': 'thepage/img/nutridesc.jpg',
                    'sitio': 'consorciodeabogados.com.mx',
                    'visitas': '1.1K',
                    'quote': ['Me convocaron inicialmente para el diseño y desarrollo de su sitio web, pero la relación se fue extendiendo hacia el asesoramiento en la estrategia de contenido de su página web y su blog, una sesión fotográfica con las abogadas asociadas, desarrollando también es su estrategia anual de marketing y marketing digital.',
                              'Extraigo de esta experiencia la sinergia que logramos entre la experiencia de ambas partes en pos de alcanzar un resultado muy satisfactorio y con la promesa de volver a colaborar en un futuro próximo.'
                            ],
                    'tags':['Estrategia de Marketing', 'Diseño de Logo', 'Web Design', 'Web Development', 'Estrategia de contenido','Diseño Gráfico', 'Fotografía', 'Edición Fotográfica', 'Photoshop', 'Figma', 'HTML/CSS'],
                    'items': [{'img': 'thepage/img/consorcioweb.jpg',
                            'imgalt': 'Imágenes de mi desarrollo web para Consorcio de Abogados',
                            'desc': 'Investigación preliminar a fondo',
                            'ext': ['Conocer en profundidad la cultura del Estudio fue mi objetivo inicial. Sus atributos diferenciales, su forma de trabajar, las metas para el sitio web y público objetivo. Respondí a sus dudas y coordinamos los siguientes pasos.',
                                    'Realicé una investigación exhaustiva sobre sitos web de estudios de abogados en Derecho Familiar y Laboral con mejor posicionamiento en Google, clasificándolos por categorías (locales, mexicanos e internacionales) e identificando patrones comunes en su diseño y contenido. Aquí apliqué toda mi experiencia en investigación de mercado.',
                                    'Identifiqué fortalezas, puntos en común en diseño y contenido, consultas habituales y obtuve la inspiración creativa necesaria para realizar tres propuestas de diseño.'],
                            },
                            {'img': 'thepage/img/consorcioweb2.jpg',
                            'imgalt': 'Imágenes de mi desarrollo web para Consorcio de Abogados',
                            'desc': 'Dedicación, compromiso y seriedad',
                            'ext': ['El desarrollo del sitio web, su estrategia de contenido y sus keywords estuvieron centrados en los tres atributos principales que Consorcio de Abogados ofrece a sus clientes y en como se relacionan estos con las necesidades de sus potenciales clientes.',
                                    'Paleta de colores amigables, texto claro y cercano y un contenido pensado para ayudar a los visitantes a orientarlos en sus necesidades puntuales.']
                            },
                            { 'img':'thepage/img/consorciofoto.jpg',
                                'desc':'Sesión Fotográfica', 
                                'ext':['Una imagen es una poderosa herramienta para generar confianza y cercanía.',
                                        'Ayuda a humanizar, mostrando personas auténticas y capturando emociones genuinas que transmiten empatía y conexión.',
                                        'Es por este motivo que realizamos una sesión fotográfica para generar el contenido visual del sitio y buscando capturar estos atributos escenciales.'],
                            },
                            {'img':'thepage/img/consorciologo.jpg',
                                'desc': 'Adaptación de Logo', 
                            'ext':['Recibí su logo en formato PNG en muy baja calidad. No era posible usar este logo para el desarrollo web y prácticamente hacia ningun otro uso ',
                                    'Por este motivo volví a diseñar el logo en formato SVG, utilizando la herramienta de diseño FIGMA.',
                                    'A partir de ahora, el logo de Consorcio de Abogados permite una adaptación perfecta a cualquier tipo de uso y tamaño sin pérdida de calidad.'
                                    ]
                            },
                            {'img':'thepage/img/consorcioplan.jpg',
                                'desc': 'Plan Integral de Marketing',
                                'ext':['La elección y contratación de un Estudio de Abogados para representación o asesoramiento es una decisión crucial que abarca diversos aspectos tanto dentro como fuera del ámbito digital. ',
                                    'Con base en una investigación preliminar exhaustiva, he desarrollado un completo plan integral de marketing con eje central en su página web, el desarrollo de redes sociales y la implementación de estrategias de marketing y relaciones públicas en el mundo real.',
                                    'Este plan integral de marketing fue presentado a Consorcio de Abogados como una propuesta y fue aprobado para su implementación durante el año 2022.'],
                                },
                                ]},
                        {'id':'fotografia',
                        'nombre':'FOTOGRAFÍA',
                    'desc':'Realizo fotografía artística desde hace más de 10 años. Cuando alguno de mis clientes lo requiere, realizo fotografía comercial y publicitaria. Utilizo Photoshop como herramienta de Edición fotográfica.',
                    'decordesc': 'thepage/img/nutridesc.jpg',
                    'sitio': 'flickr.com/people/diegoh73/',
                    'visitas': '360K',
                    'quote': ['Mi pasión por la fotografía comenzó hace más de 10 años y desde ese momento, mi cámara reflex me acompaña a todos mis viajes y a muchas de mis salidas.',
                              'He tomado cursos de fotografía, edición fotográfica y visión y composición fotográfica dictado por un reconocido fotógrafo argentino llamado Luis René Morilla.',
                              'He realizado sesiones fotográficas para Nutri Peek, Consorcio de Abogados y para mostrar el trabajo terminado del nuevo edificio de Amerimed en Plaza de las Américas.'

                            ],
                    'tags':['Fotografía Publicitaria', 'Edición Fotográfica', 'Fotografía Comercial', 'Fotografía Artística','Photoshop', 'Figma'],
                    'items': [{'img': 'thepage/img/consorcioweb.jpg',
                            'imgalt': 'Imágenes de mi desarrollo web para Consorcio de Abogados',
                            'desc': 'Investigación preliminar a fondo',
                            'ext': ['Conocer en profundidad la cultura del Estudio fue mi objetivo inicial. Sus atributos diferenciales, su forma de trabajar, las metas para el sitio web y público objetivo. Respondí a sus dudas y coordinamos los siguientes pasos.',
                                    'Realicé una investigación exhaustiva sobre sitos web de estudios de abogados en Derecho Familiar y Laboral con mejor posicionamiento en Google, clasificándolos por categorías (locales, mexicanos e internacionales) e identificando patrones comunes en su diseño y contenido. Aquí apliqué toda mi experiencia en investigación de mercado.',
                                    'Identifiqué fortalezas, puntos en común en diseño y contenido, consultas habituales y obtuve la inspiración creativa necesaria para realizar tres propuestas de diseño.'],
                            },
                            {'img': 'thepage/img/consorcioweb2.jpg',
                            'imgalt': 'Imágenes de mi desarrollo web para Consorcio de Abogados',
                            'desc': 'Dedicación, compromiso y seriedad',
                            'ext': ['El desarrollo del sitio web, su estrategia de contenido y sus keywords estuvieron centrados en los tres atributos principales que Consorcio de Abogados ofrece a sus clientes y en como se relacionan estos con las necesidades de sus potenciales clientes.',
                                    'Paleta de colores amigables, texto claro y cercano y un contenido pensado para ayudar a los visitantes a orientarlos en sus necesidades puntuales.']
                            },
                            { 'img':'thepage/img/consorciofoto.jpg',
                                'desc':'Sesión Fotográfica', 
                                'ext':['Una imagen es una poderosa herramienta para generar confianza y cercanía.',
                                        'Ayuda a humanizar, mostrando personas auténticas y capturando emociones genuinas que transmiten empatía y conexión.',
                                        'Es por este motivo que realizamos una sesión fotográfica para generar el contenido visual del sitio y buscando capturar estos atributos escenciales.'],
                            },
                            {'img':'thepage/img/consorciologo.jpg',
                                'desc': 'Adaptación de Logo', 
                            'ext':['Recibí su logo en formato PNG en muy baja calidad. No era posible usar este logo para el desarrollo web y prácticamente hacia ningun otro uso ',
                                    'Por este motivo volví a diseñar el logo en formato SVG, utilizando la herramienta de diseño FIGMA.',
                                    'A partir de ahora, el logo de Consorcio de Abogados permite una adaptación perfecta a cualquier tipo de uso y tamaño sin pérdida de calidad.'
                                    ]
                            },
                            {'img':'thepage/img/consorcioplan.jpg',
                                'desc': 'Plan Integral de Marketing',
                                'ext':['La elección y contratación de un Estudio de Abogados para representación o asesoramiento es una decisión crucial que abarca diversos aspectos tanto dentro como fuera del ámbito digital. ',
                                    'Con base en una investigación preliminar exhaustiva, he desarrollado un completo plan integral de marketing con eje central en su página web, el desarrollo de redes sociales y la implementación de estrategias de marketing y relaciones públicas en el mundo real.',
                                    'Este plan integral de marketing fue presentado a Consorcio de Abogados como una propuesta y fue aprobado para su implementación durante el año 2022.'],
                                },
                                ]},
                            ]
    work=filtrar_lista(dworks, profile)

    context = {}
    context['work']=work
    return render(request, 'thepage/profile.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message = f'From: {name}\nEmail: {email}\n\n{message}'
            send_mail(
                subject,
                message,
                email,
                ['your_email@example.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    context={}
    context['tanims1']= anims(3)
    context['tanims3']= anims(4)
    context['banims1']= anims(2)
    context['banims2']= anims(3)

    context['form']= form

    return render(request, 'thepage/contact.html', context)


def anims(n):
    
    colors = ['#f72585ff', '#b5179eff', '#7209b7ff', '#560badff', '#480ca8ff', '#3a0ca3ff', '#3f37c9ff', '#4361eeff', '#4895efff', '#4cc9f0ff']
    
    anims=[]
    for x in range(n):
        dic={}
        dic={
            'color':choice(colors),
            'delay':random.randint(1, 5)/10 + x/100,
            'width': random.randint(2, 4) + x/100,
            'height': random.randint(2, 6)
        }
        anims.append(dic)
        dic={}
    return(anims)

def filtrar_lista(lista, variable):
    for item in lista:
        if item['id'] == variable:
            return item
    return None
