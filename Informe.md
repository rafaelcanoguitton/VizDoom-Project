# CS362 - Robótica 2020-02 (CCOMP10-1) - Laboratorio RL-03 - Implemetación y pruebas de VizDoom

## Integrantes

- Rafael Isaac Cano Guitton
- Jhorel Kevin Revilla Calderón

## Repositorio

- <https://github.com/rafaelcanoguitton/VizDoom-Project>

## Experimento Básico Cacodemon

<!-- descripción, ejecución, convergencia y resultados obtenidos -->

Este experimento consiste en tener un agente con comportamiento aleatorio, se presentan 3 acciones, moverse hacia la derecha, hacia la izquierda y disparar.  En este caso el agente por medio de la función `random.choice()`. Tenemos a un enemigo en pantalla, el cual es denominado como ***"Cacodemon"***, se mueve aleatoriamente pero generalmente se mantiene estático.

Este experimento corre hasta llegar a un estado terminal, el cual es cuando el cacodemon muere o se llega al timeout establecido por la función `game.setEpisodeTimeout()`, esta función recibe como parámetro el número de ticks que se desea que el juego corra, en este caso se estableción en 200 ticks.

Nuestro agente ganará 101 puntos por acabar con el enemigo, -5 al fallar un disparo y -1 punto por cada acción que se realice. Con esta configuración tenemos un setup que recompensa al agente por matar al enemigo y penaliza por fallar un disparo y por realizar una acción. El incentivo es hacia sólo realizar acciones que nos lleven a matar al enemigo y a no realizar un disparo fallido.

Cómo nuestro agente es un agente aleatorio realmente no se tiene ningún tipo de aprendizaje pero podemos medir algunos resultados del juego

<!-- cacodemon image -->
![cacodemon](media/Screenshot%20from%202022-12-01%2013-07-09.png)
## Experimento Básico Medikit Collecting

<!-- descripción, ejecución, convergencia y resultados obtenidos -->
## Configuración del Modelo de Deep Q-Learning

- ¿Cómo es el modelo utilizado: MDP, Modelo de premios y modelo Q-Learning?  

Se utiliza un modelo de Deep Q-Learning, donde el proceso de aprendizaje es similar a los juegos implementados del Atari 2600. El MDP se usa para poder escoger la mejor opción de acuerdo a los premios que se vayan ganando o perdiendo. Por ejemplo, en el primer experimento existen n estados, donde cada uno tiene tres acciones: moverse para la derecha, izquierda y disparar. Dependiendo de estas acciones suman o restan puntos, moverse a la izquierda o derecha, disminuye 1 punto, disparar y acertar suma 101 puntos, en caso contrario se resta 5 puntos.

- ¿Qué tipo de política es usada?  

Se emplea una política e-greedy con decaimiento lineal e. Por cada episodio, incrementa el porcentaje de cada acción dependiendo del puntaje obtenido. De esta forma, se puede deducir cuál es la mejor acción en cada estado.

- ¿Cómo se calculan y aproximan los valores Q?

La función Q se aproxima con una CNN que consta de dos capas convolucionales. A cada capa de convolución le sigue una capa de pooling máximo con pooling máximo de tamaño 2 y unidades lineales rectificadas para la activación. A continuación, hay una capa totalmente conectada con 800 unidades lineales rectificadas con fugas y una capa de salida con 8 unidades lineales correspondientes a las 8 combinaciones de las 3 acciones disponibles (izquierda, derecha y disparo). De acuerdo a los premios que va tomando cada acción, la tabla de valores Q es inicializada creando una matriz de n estados x la cantidad de acciones en cada experimento. Esta matriz inicia con todos los valores en 0, por lo que la probabilidad de que suceda una acción será la misma, en todos los casos. Después se escoge una acción al azar y se agrega el valor generado a la tabla Q[estado, acción].


- ¿Qué modelo de optimización se usa?  

Emplea un modelo de optimización con gradiente estocástica descendiente.
 
- ¿Existe estrategia de repetición de experiencias?

Sí, el personaje aparece siempre en la misma posición, por lo que hay muchas posibilidades de que se repitan comportamientos. Esto mejorar el comportamiento, con el objetivo de conseguir eliminar al enemigo en un tiempo menor y con mayor precisión.

- ¿Existen objetivos Q fijos?

Sí, en el caso del primer experimento es eliminar al enemigo y en el segundo experimento es los 2100 episodios.

  
  
## Experimento cambiando las condiciones del juego y parámetros de configuración del modelo Deep Q-Learning

<!-- descripción, ejecución, convergencia y resultados obtenidos -->
