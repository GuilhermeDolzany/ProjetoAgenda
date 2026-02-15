Descrição do projeto

Este projeto é uma agenda de contatos simples feita em Python que roda no terminal. A ideia é oferecer um jeito direto de cadastrar, consultar, editar e excluir contatos sem precisar de interface gráfica ou banco de dados complexo. Os dados ficam armazenados em um arquivo CSV local, o que facilita tanto a persistência das informações quanto a exportação e importação para outros sistemas.

A estrutura é baseada em um dicionário em memória que representa a agenda durante a execução. Sempre que algo é alterado, o sistema salva automaticamente no arquivo database.csv, garantindo que nada se perca ao fechar o programa. O menu interativo guia o usuário pelas opções disponíveis, tornando o uso intuitivo mesmo para quem não tem muita familiaridade com programação.

Além disso, o código foi organizado em funções separadas para cada responsabilidade, o que facilita manutenção, testes e futuras melhorias.

README.md
Agenda de Contatos em Python

Autor: GuilhermeDolzany (Dolzany_)

Sobre

Aplicação de linha de comando para gerenciamento de contatos. Permite adicionar, buscar, editar, excluir, importar e exportar contatos usando arquivos CSV como armazenamento.

Os dados são carregados automaticamente ao iniciar e salvos sempre que há alterações.

Requisitos

Python 3.8 ou superior

Nenhuma biblioteca externa é necessária (usa apenas bibliotecas padrão: os e csv)

Como executar

Salve o código em um arquivo, por exemplo:

agenda.py


Execute no terminal:

python agenda.py

Funcionalidades

Menu principal:

1 - Mostrar todos
2 - Buscar
3 - Incluir
4 - Editar
5 - Excluir
6 - Exportar CSV
7 - Importar CSV
0 - Sair


Mostrar todos
Exibe todos os contatos cadastrados.

Buscar
Mostra os dados completos de um contato pelo nome.

Incluir
Adiciona um novo contato à agenda.

Editar
Atualiza telefone, email e endereço de um contato existente.

Excluir
Remove um contato permanentemente.

Exportar CSV
Salva todos os contatos em um arquivo escolhido.

Importar CSV
Importa contatos de um arquivo CSV compatível.

Estrutura do arquivo CSV

O sistema espera arquivos com este formato:

Nome,Telefone,Email,Endereco
João,11999999999,joao@email.com,Rua A
Maria,11888888888,maria@email.com,Rua B

Armazenamento automático

O programa cria e atualiza automaticamente o arquivo:

database.csv


Esse arquivo funciona como banco de dados local.

Possíveis melhorias futuras

Interface gráfica

Busca parcial por nome

Validação de telefone e email

Suporte a múltiplos arquivos de agenda

Sistema de autenticação de usuário
