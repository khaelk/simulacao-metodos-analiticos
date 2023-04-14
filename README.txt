## Como executar o simulador ##
Para executar o simulador é necessário primeiramente ajustar os parâmetros da simulação 
no arquivo de configuração "config.ini" conforme o seguinte modelo:
[configfile]    -> deve-se seguir este padrão no 'título'
initialTime: 2  -> tempo inicial em que chega o primeiro cliente
quantityNums: 10-> quantidade de números aleatórios
seed: 348       -> seed dos números aleatórios
arrivals: G     -> especifica o tipo da fila (G/M)
service: G      -> especifica o tipo da fila (G/M)
servers: 1      -> número de servidores atendendo os clientes
capacity: 3     -> capacidade da fila
arrivalTime: [1,2]-> intervalo de chegadas da fila
serviceTime: [3,6]-> intervalo de serviços da fila

Ajustados os parâmetros desejados, basta executar o arquivo 'run.exe' no mesmo diretório 
do arquivo de configuração, ou se preferir rodar por uma IDE deve executar o arquivo 'run.py'
em um terminal que o programa irá realizar a simulação com o que foi especificado.