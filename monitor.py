class monitor:
    def __init__(self):
        pass

    _resolucao_maxima_horizontal:int = 0
    _resolucao_maxima_vertical:int = 0
    _resolucao_horizontal_atual:int = 0
    _resolucao_vertical_atual:int = 0
    _volume:int = 0 # que pode receber de 0 a 100
    _ligado:bool = False

    def aumentaVolume(self):
        #  possibilita aumentar o volume em incrementos de 5
        self._volume = 100 if (self._volume + 5 > 100) else self._volume + 5
    
    def diminuiVolume(self):
        # possibilita aumentar o volume em incrementos de 5
        self._volume = 0 if (self._volume - 5 < 0) else self._volume - 5
    
    def liga(self, log):
        # liga o monitor
        self._ligado =  True
    def desliga(self, log):
        # desliga o monitor
        self._ligado =  False
    def alteraResolucao(self, horizontal: int, vertical: int):
        # muda a resolução atual, não pode ser superior à resolução máxima horizontal ou vertical
        self._resolucao_horizontal_atual = self._resolucao_maxima_horizontal if horizontal > self._resolucao_maxima_horizontal else horizontal
        self._resolucao_vertical_atual = self._resolucao_maxima_vertical if vertical > self._resolucao_maxima_vertical else vertical

if __name__ == "__main__":
    n = monitor()
    n.aumentaVolume()