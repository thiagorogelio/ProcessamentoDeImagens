# HUE em HSV

* **HSV** é a abreviatura para o sistema de cores formadas pelas componentes **hue (matiz)**, **saturation (saturação)** e **value (valor)**. O HSV também é conhecido como HSB (hue, saturation e brightness — matiz, saturação e brilho, respectivamente). Esse sistema de cores define o espaço de cor conforme descrito abaixo, utilizando seus três parâmetros:

* **Matiz (tonalidade)**: Verifica o tipo de cor, abrangendo todas as cores do espectro, desde o vermelho até o violeta, mais o magenta. Atinge valores de 0 a 360, mas para algumas aplicações, esse valor é normalizado de 0 a 100%.
* **Saturação**: Também chamado de "pureza". Quanto menor esse valor, mais com tom de cinza aparecerá a imagem. Quanto maior o valor, mais "pura" é a imagem. Atinge valores de 0 a 100%.
* **Valor (brilho)**: Define o brilho da cor. Atinge valores de 0 a 100%.

Esse sistema foi inventado no ano de 1974, por Alvy Ray Smith. É caracterizada por ser uma transformação não-linear do sistema de cores RGB. Outros sistemas de cores relacionados incluem o HSL (L de luminosity ou luminosidade) e o HSI (I de intensity ou intensidade). [Wikipedia]

Este trabalho consiste em gerar a roda de cores em sistema de representação HSV.

![alt tag](https://github.com/thiagorogelio/ProcessamentoDeImagens/HUEinHSV/ColorWheel.jpg)

Este trabalho foi desenvolvido utilizando a linguagem [Python 2.7.9](https://www.python.org/) e as bibliotecas [Numpy](http://www.numpy.org/) e [OpenCV](http://opencv.org/)


