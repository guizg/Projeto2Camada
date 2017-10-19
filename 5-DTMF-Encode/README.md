---
title: Camada Física -  APS 5 - DTMF - Encoder e recepção
authors: Frederico Curti e Guilherme Graicer
date: Setembro - 2017
---

# Descrever a modulação/ demodulação

## Modulação

Antes de modular, o sinal foi filtrado por um Passa-Baixa com cut-off de 3000 Hz (frequencia maxima da voz humana)
Para modular os sinais bastou multiplicá-loa por portadoras.

## Demodulação

Para demodular, bastou multiplicar o sinal recebido pela portadora original e aplicar novamente o filtro Passa-Baixa com o mesmo cut-off.

# Descrever as frequências das portadoras utilizadas e as bandas ocupadas

Utilizamos 7000 e 14000 Hz, pois o nosso sinal original foi filtrado para ocupar até 3000Hz e quando modulado a banda dobra (ocupando 6000Hz, com o centro na frequencia escolhida para a portadora). Portanto, um vai ocupar de 4000 a 10000 Hz e o outro de 11000 a 17000 Hz.

# Transmissão

## Mensagens, no tempo

![bleh](msgRecebidas.png)

## Fourier das mensagens

![bleh](fSinal.png)

## Fourier das mensagens filtradas

![bleh](fFiltrados.png)

## Fourier das portadoras

![bleh](fPortadoras.png)

## Fourier dos sinais modulados

![bleh](fModulados.png)

## Fourier da soma deles

![bleh](fSomado.png)

# Recepção

## Sinal recebido, no tempo

![sinalRecebido](sinalRecebido.png)

## Fourier do sinal recebido

![fRecebido](fRecebido.png)

## Mensagens recuperadas, no tempo antes do filtro

![msgRecebidasSemFiltro](msgRecebidasSemFiltro.png)

## Fourier das mensagens recuperadas, antes do filtro

![fRecebidaSemFiltro](fRecebidaSemFiltro.png)

## Mensagens recuperadas, no tempo

![msgRecebidas](msgRecebidas.png)

## Fourier das mensagens recuperadas 

![fRecebida](fRecebida.png)

# Áudio transmitido vs recebido

Muito pouco ruído, o áudio recebido ficou bem parecido com o transmitido.

---
# Descrever a geração de tons

A biblioteca numpy é usada para fazer as curvas senoides de cada frequencia que compoem o tom e então elas são somadas, formando a curva final. 

# Gráficos de cada tom (com a descrição de suas frequências)

## Encoder

![encoder1](imgs/encoder/encoder-1.png)

Tom do 1 gerado. Senoide da frequência 697 Hz somada com a senoide da 1209 Hz

![encoder1](imgs/encoder/encoder-2.png)

Tom do 2 gerado. Senoide da frequência 697 Hz somada com a senoide da 1336 Hz

![encoder1](imgs/encoder/encoder-3.png)

Tom do 3 gerado. Senoide da frequência 697 Hz somada com a senoide da 1477 Hz

![encoder1](imgs/encoder/encoder-a.png)

Tom do A gerado. Senoide da frequência 697 Hz somada com a senoide da 1633 Hz

![encoder1](imgs/encoder/encoder-4.png)

Tom do 4 gerado. Senoide da frequência 770 Hz somada com a senoide da 1209 Hz

![encoder1](imgs/encoder/encoder-5.png)

Tom do 5 gerado. Senoide da frequência 770 Hz somada com a senoide da 1336 Hz

![encoder1](imgs/encoder/encoder-6.png)

Tom do 6 gerado. Senoide da frequência 770 Hz somada com a senoide da 1477 Hz

![encoder1](imgs/encoder/encoder-b.png)

Tom do B gerado. Senoide da frequência 770 Hz somada com a senoide da 1633 Hz

![encoder1](imgs/encoder/encoder-7.png)

Tom do 7 gerado. Senoide da frequência 852 Hz somada com a senoide da 1209 Hz

![encoder1](imgs/encoder/encoder-8.png)

Tom do 8 gerado. Senoide da frequência 852 Hz somada com a senoide da 1336 Hz

![encoder1](imgs/encoder/encoder-9.png)

Tom do 9 gerado. Senoide da frequência 852 Hz somada com a senoide da 1477 Hz

![encoder1](imgs/encoder/encoder-c.png)

Tom do C gerado. Senoide da frequência 852 Hz somada com a senoide da 1633 Hz

![encoder1](imgs/encoder/encoder-0.png)

Tom do 0 gerado. Senoide da frequência 941 Hz somada com a senoide da 1336 Hz

![encoder1](imgs/encoder/encoder-#.png)

Tom do # gerado. Senoide da frequência 941 Hz somada com a senoide da 1477 Hz

![encoder1](imgs/encoder/encoder-d.png)

Tom do D gerado. Senoide da frequência 941 Hz somada com a senoide da 1633 Hz

## Decoder

![decoder](imgs/decoder/decoder1.png)

Tom do 1 recebido. Senoide da frequência 697 Hz somada com a senoide da 1209 Hz com ruídos

![decoder](imgs/decoder/decoder2.png)

Tom do 2 recebido. Senoide da frequência 697 Hz somada com a senoide da 1336 Hz com ruídos

![decoder](imgs/decoder/decoder3.png)

Tom do 3 recebido. Senoide da frequência 697 Hz somada com a senoide da 1477 Hz com ruídos

![decoder](imgs/decoder/decoderA.png)

Tom do A recebido. Senoide da frequência 697 Hz somada com a senoide da 1633 Hz com ruídos

![decoder](imgs/decoder/decoder4.png)

Tom do 4 recebido. Senoide da frequência 770 Hz somada com a senoide da 1209 Hz com ruídos

![decoder](imgs/decoder/decoder5.png)

Tom do 5 recebido. Senoide da frequência 770 Hz somada com a senoide da 1336 Hz com ruídos


![decoder](imgs/decoder/decoder6.png)

Tom do 6 recebido. Senoide da frequência 770 Hz somada com a senoide da 1477 Hz com ruídos


![decoder](imgs/decoder/decoderB.png)

Tom do B recebido. Senoide da frequência 770 Hz somada com a senoide da 1633 Hz com ruídos

![decoder](imgs/decoder/decoder7.png)

Tom do 7 recebido. Senoide da frequência 852 Hz somada com a senoide da 1209 Hz com ruídos

![decoder](imgs/decoder/decoder8.png)

Tom do 8 recebido. Senoide da frequência 852 Hz somada com a senoide da 1336 Hz com ruídos


![decoder](imgs/decoder/decoder9.png)

Tom do 9 recebido. Senoide da frequência 852 Hz somada com a senoide da 1477 Hz com ruídos


![decoder](imgs/decoder/decoderC.png)

Tom do C recebido. Senoide da frequência 852 Hz somada com a senoide da 1633 Hz com ruídos


![decoder](imgs/decoder/decoder0.png)

Tom do 0 recebido. Senoide da frequência 941 Hz somada com a senoide da 1336 Hz com ruídos


![decoder](imgs/decoder/decoder#.png)

Tom do # recebido. Senoide da frequência 941 Hz somada com a senoide da 1477 Hz com ruídos


![decoder](imgs/decoder/decoderD.png)

Tom do D recebido. Senoide da frequência 941 Hz somada com a senoide da 1633 Hz com ruídos

---
# Entrega APS 6 - Decodificação

- ## Fourier do sinal *transmitido* / Fourier do sinal *recuperado*
### Tom 1
![decoder](imgs/encoder2/encoder1.png)
![decoder](imgs/decoder2/1.png)
### Tom 2
![decoder](imgs/encoder2/encoder2.png)
![decoder](imgs/decoder2/2.png)
### Tom 3
![decoder](imgs/encoder2/encoder3.png)
![decoder](imgs/decoder2/3.png)
### Tom A
![decoder](imgs/encoder2/encoderA.png)
![decoder](imgs/decoder2/A.png)
### Tom 4
![decoder](imgs/encoder2/encoder4.png)
![decoder](imgs/decoder2/4.png)
### Tom 5
![decoder](imgs/encoder2/encoder5.png)
![decoder](imgs/decoder2/5.png)
### Tom 6
![decoder](imgs/encoder2/encoder6.png)
![decoder](imgs/decoder2/6.png)
### Tom B
![decoder](imgs/encoder2/encoderb.png)
![decoder](imgs/decoder2/b.png)
### Tom 7
![decoder](imgs/encoder2/encoder7.png)
![decoder](imgs/decoder2/7.png)
### Tom 8
![decoder](imgs/encoder2/encoder8.png)
![decoder](imgs/decoder2/8.png)
### Tom 9
![decoder](imgs/encoder2/encoder9.png)
![decoder](imgs/decoder2/9.png)
### Tom C
![decoder](imgs/encoder2/encoderc.png)
![decoder](imgs/decoder2/c.png)
### Tom *
![decoder](imgs/encoder2/encoderEstrelinha.png)
![decoder](imgs/decoder2/*.png)
### Tom 0
![decoder](imgs/encoder2/encoder0.png)
![decoder](imgs/decoder2/0.png)
### Tom \#
![decoder](imgs/encoder2/encoderhashtag.png)
![decoder](imgs/decoder2/hashtag.png)
### Tom D
![decoder](imgs/encoder2/encoderD.png)
![decoder](imgs/decoder2/D.png)

## Frequências recebidas e a enviadas de cada tom (divergências)
Ao tocar o tom 1, reconhecemos as frequencias
> 692 Hz <br>
> 1204.5 Hz <br>
> 1245.5 Hz

~ +- 8.7Hz erro

Ao tocar o tom 2, reconhecemos as frequencias
> 691.0 Hz <br>
> 701.8 Hz <br>
> 716.75 Hz <br>
> 1308.5 Hz <br>
> 1334.6 Hz <br>
> 1348.0 Hz <br>

+- 0.3Hz erro

Ao tocar o tom 3, reconhecemos as frequencias
> 652.0 Hz <br>
> 692.5 Hz <br>
> 700.0 Hz <br>
> 1460.0 Hz <br>
> 1499.6 Hz <br>

+- 8.4Hz erro

- <b> Com isso, concluímos que existiu aproximadamente um erro de ±6Hz na captação
do sinal, sendo que isso é influenciado pelo threshold definido, que varia para cada microfone.
No exemplo, o threshold foi de > 30db</b>


## Tempos utilizados (geração e recepção dos sinais)
    Nos nossos testes, usamos amostras de 1 segundo, pois se mostrou suficiente para a demonstração
    e identificação dos tons, que foi o mesmo da geração

---
title: Camada Física -  APS 5 - DTMF - Encoder e recepção
author: Rafael Corsi - rafael.corsi@insper.edu.br 
date: Setembro - 2017
---

![DTMF](doc/sistema.png)

*Entrega : Até o começo da aula do dia 21/9*

# Novas Duplas

Favor preencher o form com informações das novas duplas :

**Um novo repositório deve ser criado !!!**
 - https://goo.gl/forms/hE9Aow318dYQtO5u1

# APS 5 : DTMF - Encoder e recepção.

Implementar a codificação dos números 0,1,..9 em código DTMF, transmitir o sinal pelo falante de um computador e fazer o recebimento do áudio em outro computador. Não é necessário implementar a decodificação.

- [Lista aula 9 ](https://github.com/Insper/Camada-Fisica-Computacao/blob/master/2-Aulas/9-DTMF/9-Lista-DTMF.pdf)

## Dicas

Algumas dicas de implementação podem ser lidas em : 
 
- [Dicas](https://github.com/Insper/Camada-Fisica-Computacao/blob/master/3-Projetos/5-DTMF-Encode/5-DTMF-Dicas-Encoder.md)

# Requisitos

Requisitos de projeto :

1. encoderDTMF.py
    - Geração dos tons
        - Gerar os tons DTMF para cada um dos símbolos (0,1,..9)
        - Para cada símbolo plotar os sinais gerados (no tempo)

1. decoderDTMF.py
    - Recepção de áudio
        - Deve receber um áudio pelo microfone
        - A cada 1 segundo plotar o sinal recebido pelo microfone.
    - Tons
        - Receber cada um dos tons (1 segundo) e salvar os sinais para uso futuro.
    
1. Documentação
    - Descrever a geração dos tons
    - Descrever as frequências que compõem cada tom
    - Plotar e comentar os gráficos de cada tom com o do gerado e recebido.
    
## Itens extras

1. Interface gráfica para transmitir os tons
1. Exibir a transformada de Fourier dos sinais (transmitido e recuperado)

## Validação

- Gerar os tons e validar com um aplicativo no celular.
- Reproduzir o sinal salvo dos tons.

## Rubricas

| Nota máxima | Descritivo                                                |
|-------------|-----------------------------------------------------------|
| A           | - Entregue no prazo                                       |
|             | - Implementado extras                                     |
| B           | - Entregue no prazo                                       |
|             | - Implementado requisitos necessários                     |
| C           | - Entregue fora do prazo                                  |
|             | - Implementando requisitos necessários                    |
| D           | - Nem todos os requisitos necessários foram implementados |
| I           | - Não entregue                                            |



