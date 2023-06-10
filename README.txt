## Como executar o simulador ##
Para executar o simulador é necessário primeiramente ajustar os parâmetros da simulação em tandem
no arquivo de configuração "config.ini" conforme o seguinte modelo:
[configfile]    -> deve-se seguir este padrão no 'título'
initialTime: [["q1", 1]]-> tempo inicial em que chega o primeiro cliente em cada fila que chegam clientes de fora do sistema
quantityNums: 10-> quantidade de números aleatórios
seed: 348       -> seed dos números aleatórios

Lista de queues da rede de filas cada item da lista deve ter os seguintes atributos na seguinte ordem:
["nomeFila", numeroServidores, capacidade, temposChegada, temposSaida, [arrayNetworking]]
Para o atributo arrayNetworking temos que para cada item dele:
["nomeFilaDestino", probabilidadeEvento(probabilidade deve ser valor de 0 a 1 e fechar 1 dentro do arrayNetworking)]
obs: caso o "nomeFilaDestino" seja "s" isso indicará uma saída do sistema.

Ex:
queuesList: [["q1", 1, inf, [1, 4], [1, 1.5], [["q2", 0.8], ["q3", 0.2]]], ["q2", 3, 5, -1, [5, 10], [["q1", 0.3], ["q2", 0.5], ["s", 0.2]]], ["q3", 2, 8, -1, [10, 20], [["q2", 0.7], ["s", 0.3]]]]

Ajustados os parâmetros desejados, basta executar o arquivo 'run.exe' no mesmo diretório 
do arquivo de configuração, ou se preferir rodar por uma IDE deve executar o arquivo 'run.py'
em um terminal que o programa irá realizar a simulação com o que foi especificado.