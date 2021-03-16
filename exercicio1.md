# Classe Monitor

Crie uma classe monitor que satisfaça as seguintes condições:

atributos:
- resolucao_maxima_horizontal: inteiro
- resolucao_maxima_vertical: inteiro
- resolucao_horizontal_atual: inteiro
- resolucao_vertical_atual: inteiro
- volume: inteiro que pode receber de 0 a 100
- ligado: booleano/lógico

métodos:
- aumentaVolume: possibilita aumentar o volume em incrementos de 5
- diminuiVolume: possibilita aumentar o volume em incrementos de 5
- liga: liga o monitor
- desliga: desliga o monitor
- alteraResolucao: muda a resolução atual, não pode ser superior à resolução máxima horizontal ou vertical
