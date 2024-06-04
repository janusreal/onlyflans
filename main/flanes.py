from django.templatetags.static import static

flanes = [
    { 
     'id': 1,
     'titulo':'Flan borracho',
     'img': static('flan-borracho.jpeg'),
     'ingredientes': [
         '3/4 taza de azúcar', 
         '1 lata (12 oz) de leche condensada',
         '1 1/2 tazas de leche entera',
         '6 huevos',
         '1 1/2 cucharaditas de vainilla',
         '1/8 cucharadita de sal',
         '2 cucharadas de ron oscuro'
     ]
     },{ 
        'id': 2,
        'titulo':'Flan napolitano',
        'img': static('flan-napolitano-foto-principal.jpg'),
        'ingredientes': [
         '1 taza de azúcar (para el caramelo)',
         '1 lata (12 oz) de leche evaporada',
         '1 lata (14 oz) de leche condensada',
         '6 huevos',
         '1 cucharadita de esencia de vainilla'
     ]
     },
     { 
      'id': 3,
     'titulo':'Flan de queso y guayaba',
     'img': static('flan-de-queso-caramel-topped-cream-cheese-custard.jpg'),
     'ingredientes': [
         '1 lata (12oz) de leche evaporada',
         '1 lata (14 oz) de leche condensada',
         '2 tazas de néctar de guayaba o concentrado',
         '1 paquete (8 oz) queso crema',
         '1 de taza de azúcar',
         '5 huevos'
     ]
     },
     { 
      'id':4,
     'titulo':'Torta de Flan',
     'img': static('torta-de-flan.webp'),
     'ingredientes': [
         '1 Pizca Azúcar (para acaramelar la base del molde)',
         '1 Paquete Leche Condensada Nestlé (Para el flan)',
         '8 Unidades Yema De Huevo (Para el flan)',
         '325 cc Leche (Para el flan)',
         '1 Cucharadita Esencia De Vainilla (Para el flan)',
         '1 Caja Premezcla De Torta De Chocolate (Para la torta)'
     ]
     }
]