from controllers.controller import *

routes ={

"index_route":"/","indexcontroller":IndexController.as_view("index"),
"quemsomos_route":"/quemsomos","quemsomos_controller":LinkQuemSomosController.as_view("quemsomos"),
"contato_route":"/contato","contato_controller":LinkContatoController.as_view("contato"),
"envio_route":"/envio","envio_controller":EnvioController.as_view("envio"),

}