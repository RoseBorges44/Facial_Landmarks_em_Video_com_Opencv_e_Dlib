# Detecção de Pontos de Referência Facial em Vídeo com Opencv e Dlib

Neste projeto, foi desenvolvido um sistema de Reconhecimento Facial.
O software emprega abordagens provenientes da área de Visão Computacional e Aprendizado de Máquina, com o propósito de reconhecer e rastrear pontos característicos no rosto humano, tais como os olhos, nariz e boca, em um fluxo contínuo de vídeo em tempo real.

<p align="center">
  <img src="https://github.com/RoseBorges44/Facial_Landmarksl_em_Video_com_Opencv_e_Dlib/blob/ff47ca5f9b3be25f6b6538ec9183875db8b7d593/Video_Deteccao_Facial%20(1).gif" alt="Demonstração em GIF">
</p>


# Estrutura do Projeto
A estrutura do projeto é a seguinte:

── *main.py* <p>
── *requirements.txt* <p>
── *shape_predictor_68_face_landmarks.dat*<p>

# Descrição dos arquivos:

*main.py*:  script Python principal que contém a lógica do detector facial.<p>
*requirements.txt*:  arquivo que lista as dependências necessárias para executar o programa.<p>
*shape_predictor_68_face_landmarks.dat*:  arquivo de dados usado pelo detector de marcos faciais do dlib - *link para baixar* https://bit.ly/3q8F4x3

# Pré-requisitos
Para executar este projeto, você precisa ter o Python instalado em seu sistema. As dependências do projeto são listadas no arquivo *requirements.txt* e podem ser instaladas com o seguinte comando:

*pip install -r requirements.txt*

# Detalhes do Projeto
Esse programa identifica os pontos de referência facial no rosto de um indivíduo em um vídeo contínuo. O processo é executado através das fases a seguir:
- Captação do fluxo de vídeo em tempo real através da webcam.
- Detecção de rostos na imagem utilizando o detector de rostos do dlib.
- Detecção dos marcos faciais usando o preditor de marcos faciais do dlib.
- Mostra o vídeo com o quadro com os pontos faciais e retângulo.

 O software emprega o detector de pontos de referência facial fornecido pela biblioteca dlib para estabelecer a localização dos olhos, nariz e boca da pessoa.

