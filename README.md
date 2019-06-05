# CG-2019.2
### Descrição
Repositório para desenvolvimento de algoritmos de identificação de placas de trânsito em imagens. Este projeto é parte avaliativa da disciplina de Computação Gráfica de Ciência da Computação - UFPA.

### Alunos:
- Lucas Gabriel de Souza -201604940039

## Instalação

### Clone do projeto:
`$ git clone https://github.com/souzaluuk/CG-2019.2`

Caso queira utilizar o `virtualenv` para isolar sua biblioeteca da utilizada no projeto:

```bash
$ sudo pip3 install virtualenv
$ virtualenv CG-2019.2
$ source CG-2019.2/bin/activate
```

Feito isso, pode-se instalar as bibliotecas necessárias:

```bash
$ pip3 install numpy matplotlib opencv-python==3.4.2.17 opencv-contrib-python==3.4.2.17
```

Execute o [main.py](main.py) para o teste:

`$ python3 main.py`