---
## _Página de registro civil utilizando Django_
---
Este repositorio contiene la idea propuesta para el diseño de una página de citas utilizando Django.
Esta idea consiste de una página de citas del registro civil, para la obtención de una respectiva cédula, donde se le solicita al usuario registrarse (tener una cuenta) para poder solicitar una cita. Si dicho usuario ya posee una cuenta en la plataforma, puede ingresar utilizando sus datos respectivamente.
El usuario puede solicitar una cita para una fecha propuesta, a demás de otras funcionalidades.

---
## Autores del proyecto
---
* `Jeaustin Sirias Chacón; carné B66861`
* `Juan Felipe Cortes Rentería; carné B52250`

---
## Instrucciones para el uso del proyecto
---
Este proyecto contiene un `makefile` para simplificar su manejo. Inicie clonando el presente repositorio en el directorio deseado de su ordenador, digitando la siguiente instrucción en su ventana de comandos:

```
$ git clone https://github.com/JeaustinSirias/EIE_Django_project.git
```
Una vez realizada la operación anterior puede elegir entre inicializar el proyecto directamente desde su ordenador o construir un contenedor utilizado su `Dockerfile`. Digite las iguientes instrucciones para inicializar el proyecto de forma local:
```
$ make require
$ make run
```
O bien, digite el siguiente comando, si desea construir una imagen de Docker e inicializar un contenedor:
```
$ make container
```
---
Observaciones
---
El proyecto cuenta con un usuario administrativo por defecto con los siguientes credenciales:
* nombre de usuario **admin**
* Contraseña: **admin**
