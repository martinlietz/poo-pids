class monitor:
    def __init__(self):
        pass

    _resolucao_maxima_horizontal ->int
    _resolucao_maxima_vertical->int
    _resolucao_horizontal_atual->int
    _resolucao_vertical_atual->int
    _volume->int # que pode receber de 0 a 100
    _ligado->bool

    def aumentaVolume(self):
        #  possibilita aumentar o volume em incrementos de 5
        _volume = 100 if (_volume + 5 > 100) else _volume + 5
    
    def diminuiVolume(self):
        # possibilita aumentar o volume em incrementos de 5
        _volume = 0 if (_volume - 5 < 0) else _volume - 5
    
    def liga(self, log):
        # liga o monitor
        _ligado =  True
    def desliga(self, log):
        # desliga o monitor
        _ligado =  False
    def alteraResolucao(self, horizontal, vertical):
        # muda a resolução atual, não pode ser superior à resolução máxima horizontal ou vertical
        _resolucao_horizontal_atual = _resolucao_maxima_horizontal if horizontal > _resolucao_maxima_horizontal else horizontal
        _resolucao_vertical_atual = _resolucao_maxima_vertical if vertical > _resolucao_maxima_vertical else vertical