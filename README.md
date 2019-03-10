# WebScraper

WebScraper es un programa para buscar información en páginas web. La búsqueda se realiza directamente a partir del html de la página.

## Author
* Toni Pacheco Fernández toni.pafe@gmail.com

## Usage
```bash
python3 webscraper.py
```
## Requirements
```bash
pip3 install -r requirements.txt  
```
beautifulsoup4==4.7.1  
bs4==0.0.1  
coverage==4.5.2  
lxml==4.3.1  
parameterized==0.7.0  
soupsieve==1.8  

## License
[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)


## Documentation

### Clase url.Url
Se trata de una clase de tipo contenedor de datos. Su función es encapsular la url sobre la que se va a realizar la búsqueda. Se encarga también de comprobar que la url tiene un formato correcto.
La url www.example.com/ no es aceptada, pero si la url https://www.example.com/ o la url https://example.com/

##### Url(url : str)
Recibe una cadena de caracteres como argumento.


### Clase seeker.Seeker
La clase Seeker es la encargada de realizar la búsqueda propiamente dicha. Se ha decidido encapsular la búsqueda en una clase separada del cliente, dado que esta es la parte del código más propensa el cambiar. Cada vez que se quiera realizar una nueva búsqueda, el código que la realiza deberá ser reescrito para atender los nuevos requisitos de información. De esta forma sólo será necesario generar un nuevo componente de tipo seeker.ISeeker para contar con una nueva búsqueda, sin necesidad de tocar otras partes del código que son comunes a todas las búsquedas.

##### seek(tree)
Todo componente de tipo Seeker debe implementar el método seek.
Este método recibe como parámetro la estructura de datos generada partir del html de la página en la que se quiere realizar la búsqueda.


### Clase ConsoleMessenger
ConsoleMessenger es una clase del tipo messenger.IMessenger.
Esta clase es la encargada de encapsular el envío de información. De esta forma se garantiza que el modo cómo se envía la información está totalmente desacoplado da la búsqueda. Así cambiar el modo de envío es tan simple como inyectar una nueva dependencia al cliente.

##### send(messege : str, destination=sys.stdout)
Todo componente de tipo IMessenger debe implementar el método send.
La clase ConsoleMessenger por defecto envía la información a través de la salida estándar.

### Clase Downloader
Esta clase se encarga de aislar la dependencia de la librería [urllib](https://docs.python.org/3.7/library/urllib.html).

###### tools.Downloader.download(url : Url)
Este es un método estático que abre la conexión, descarga el html y finalmente cierra la conexión.


### Clase HTMLParser
Esta clase se encarga de aislar la dependencia de la librería [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

##### tools.HTMLParser.parse(html)
Este es un método estático que recibe el html y lo convierte en una estructura anidada.


### Clase Client
La clase client.Client actúa como controlador de la búsqueda.

##### Client(url : Url, seeker : ISeeker, out=ConsoleMessenger)
El constructor recibe tres parámetros. El primero de tipo Url que contiene la url sobre la que se realizará la búsqueda. El segundo es un parámetro de tipo ISeeker, que es el encargado de realizar la búsqueda. Y el tercero es el componente encargado de enviar la información (por defecto recibe un ConsoleMessenger, de modo que la información se envía a través de la salida estándar).

El Cliente se sirve además de los métodos de las clases tools.Downloader y tools.HTMLParser para descargar y *parsear* el html de la página.


# Configurador automático de busquedas
Esta funcionalidad se compone de tres elementos:
* El primero es un componente de tipo ISeeker. La idea principal de este componente es que realiza la búsqueda que compone un SearchBuilder.
* El componente SearchBuilder se encarga de componer la búsqueda a partir de unas estructuras de datos que un *parser* se encarga de capturar de un archivo `*.data`.
* El componente SearchParser se encarga de *parsear* los datos necesarios para componer la búsqueda.

Cave destacar que esta funcionalidad es solo un prototipo. De modo que no es todo lo eficiente, fiable y robusta que cabria esperar. Además solo unos pocos tipos de búsqueda están soportados.

## Usage
```bash
python3 webscraper.py <filename>.data
```

## Archivo de configuración
Se trata de un archivo `*.data`. El formato de archivo se describe a continuación:
+ La primera línea corresponde a la url de la página en la que se desea buscar. Cave destacar que el formato de la url debe ser https://www.example.com/ o https://example.com/, no acepta urls del tipo www.example.com/.

+ La segunda línea viene marcada con la palabra `container=`. En esta se pasan los valores que identifican el *container* html en el que se quiere buscar.

+ La tercera línea va marcada con la palabra `subcontainer=`. Aquí se puede indicar una ubicación que estuviera anidada en el primer container. Esta línea es opcional (puede omitirse).

+ Las lineas sucesivas, marcadas con la palabra `item=` están reservadas para la localización de todas aquellas informaciones que se quieran recopilar de el html.

#### Archivo ejemplo:

##### Template del archivo
```bash
https://www.example.com/
container = tag, class
subcontainer = tag, class
item = tag, class > atribute
item = tag, class > text
item = tag, class | tag, class > text
item = tag, class | tag, class | ...
```
***
##### Ejemplo de como generar el archivo:
###### html de ejemplo
```
<ul class='goodlist_1'>
  <li>
    <span>Title Item 1</span>
    <div class='priceitem'>
      <span class='price' oriprice='10.00'> </span>
    </div>
    <div class='priceitem'>
      <span class='price_old' oriprice='12.00'> </span>
    </div>
    <span>Title Item 2</span>
    <div class='priceitem'>
      <span class='price' oriprice='5.00'> </span>
    </div>
    <div class='priceitem'>
      <span class='price_old' oriprice='8.50'> </span>
    </div>
  </li>
</ul>
```
El archivo para obtener la información referente a los *items* de este html sería el que se muestra a continuación.
- El elemento `,` separa `tag` de `class`.
- El elemento `|` separa los diferentes elementos anidados.
- El elemento `>` indica el atributo que se quiere seleccionar.
- El elemento `¬` significa vacío.
- La palabra `text` indica que se quiere seleccionar el contenido de tipo texto de un *tag*.
- Cualquier línea del archivo que empiece por `*` será ignorada.
###### archivo `.data` de ejemplo
```
https://www.banggood.com/Flashdeals.html
container=ul, goodlist_1
subcontainer = li, ¬
item = span, title > text
item = div, priceitem | span, price > oriprice
item = div, priceitem | span, price_old > oriprice
```
En la carpeta `WebScraper/examples` pueden encontrarse algunos ejemplos de este tipo de archivos.
***
