---
title: Camada Física -  APS 5 - DTMF - Encoder e recepção
authors: Frederico Curti e Guilherme Graicer
date: Setembro - 2017
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



