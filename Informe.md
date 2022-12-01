# CS362 - Robótica 2020-02 (CCOMP10-1) - Laboratorio RL-03 - Implemetación y pruebas de VizDoom

## Integrantes

- Rafael Isaac Cano Guitton
- Jhorel Kevin Revilla Calderón

## Repositorio

- <https://github.com/rafaelcanoguitton/VizDoom-Project>

## Experimento Básico Cacodemon

<!-- descripción, ejecución, convergencia y resultados obtenidos -->
## Experimento Básico Medikit Collecting

<!-- descripción, ejecución, convergencia y resultados obtenidos -->
## Configuración del Modelo de Deep Q-Learning

- ¿Cómo es el modelo utilizado: MDP, Modelo de premios y modelo Q-Learning?
Se utiliza un modelo de Deep Q-Learning, donde el proceso de aprendizaje es similar a los juegos implementados del Atari 2600. El MDP se usa para poder escoger la mejor opción de acuerdo a los premios que se vayan ganando o perdiendo. Por ejemplo, en el primer experimento existen n estados, donde cada uno tiene tres acciones: moverse para la derecha, izquierda y disparar. Dependiendo de estas acciones suman o restan puntos, moverse a la izquierda o derecha, disminuye 1 punto, disparar y acertar suma 101 puntos, en caso contrario se resta 5 puntos.

- ¿Qué tipo de política es usada?
Se emplea una política e-greedy con decaimiento lineal e. Por cada episodio, incrementa el porcentaje de cada acción dependiendo del puntaje obtenido. De esta forma, se puede deducir cuál es la mejor acción en cada estado.

- ¿Cómo se calculan y aproximan los valores Q?
  
- ¿Qué modelo de optimización se usa?
  Emplea un modelo de optimización con gradiente estocástica descendiente.
- ¿Existe estraegia de repetición de experiencias?
  
- ¿Existen objetivos Q fijos?
  
  
## Experimento cambiando las condiciones del juego y parámetros de configuración del modelo Deep Q-Learning

<!-- descripción, ejecución, convergencia y resultados obtenidos -->
