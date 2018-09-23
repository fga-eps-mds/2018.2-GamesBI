---
title: Documento de arquitetura
author: Bruno
layout: post
categories: DEV
---

## Histórico de Revisões

|Data|Versão|Descrição|Autor|
| --- | --- | --- | --- |
|28/08/2018|0.1|Criação da estrutura do documento|Ingrid Soares|
|28/08/2018|0.1|Adição de tópicos|Bruno Rodrigues Santos|
|29/08/2018|0.1|Adição de arquitetura MVT|Alan Lima|
|29/08/2018|0.1|Adição de Arquitetura de Microserviços|Alan Lima|
|29/08/2018|0.2|Atualizações e Correções|Bruno Rodrigues Santos|
|03/09/2018|1.0|Atualização da visão geral e adição dos MER|Bruno Rodrigues Santos|
|10/09/2018|1.1|Adição do diagrama de pacotes|Bruno Rodrigues Santos|
|21/09/2018|1.2|Atualização dos Microserviços e camadas|Marco Antônio Lima|
|23/09/2018|1.2|Definição do padrão de arquitetura REST|Alan Lima|

# Documento de Arquitetura

Sumário
----------------

* 1 . [Introdução](#1-introdução)
    * 1.1. [Finalidade](#11-finalidade)
    * 1.2. [Escopo](#12-escopo)
    * 1.3. [Definições, acrônimos e abreviações](#13-definições-acrônimos-e-abreviações)
    * 1.4. [Referências](#14-referências)
    * 1.5. [Visão Geral](#15-visão-geral)

* 2 . [Representação da Arquitetura](#2-representação-da-arquitetura)
   * 2.1. [Representação do padrão de Arquitetura REST](#21-padrão-de-arquitetura-rest)
   * 2.2. [Representação da Arquitetura de Microserviços](#22-arquitetura-de-microserviços)   
   * 2.3. [Representação da Arquitetura do REACT](#23-padrão-de-arquitetura-do-react)  


* 3 . [Metas e Restrições da Arquitetura](#3-metas-e-restrições-da-arquitetura)

* 4 . [Arquitetura dos Serviços e visão de Implementação](#4-arquitetura-dos-serviços-e-visão-de-implementação)
   * 4.1. [Visão Geral](#41-visão-geral)
   * 4.2. [Microserviços e Camadas](#42-microserviços-e-camadas)
   * 4.3. [Diagrama de pacotes](#43-diagrama-de-pacotes)

* 5 . [Visão de Dados](#5-visão-de-dados)


## 1. Introdução

----

### 1.1 Finalidade

Este documento mostra uma visão geral sobre a arquitetura e ferramentas utilizadas no projeto GamesBI.

### 1.2 Escopo

Neste documento serão retratados os modelos arquiteturais implementados, descrição e utilização de frameworks
que compõe o projeto GamesBI, plataforma de business intelligence com temática de jogos digitais. Exploramos
de maneira detalhada o funcionamento e a visão arquitetural do projeto.

### 1.3 Definições, acrônimos e abreviações

- MVT - Model, View, Template
- MVC - Model, View, Controller
- ORM - Object Relational Mapper
- DRM - Document Relational Mapper

### 1.4 Referências

### 1.5 Visão Geral

O presente documento faz o detalhamento e descrição de características da arquitetura escolhidas pela equipe.
Estaremos descrevento o padrão arquitetural MVT, arquitetura de Microserviços e APIs Rest

## 2. Representação da Arquitetura

----

A arquitetura do projeto possuirá ambientes diferentes: API's REST, por debaixo do framework Django, assim como o ambiente WEB de interação com usuário, feito em react. Juntando todos os ambientes e coordenando-os, formamos assim uma arquitetura de Microserviços.

### 2.1 Padrão de Arquitetura REST

O termo foi definido no ano 2000, na tese de doutorado de Roy Fielding e é a sigla para Representational State Transfer: é um design de arquitetura construído para servir aplicações em rede.

Conceitualmente falando, o modelo REST (REpresentational State Transfer) representa nada mais que uma possibilidade para a criação de web services, cujas principais diferenças em relação ao modelo tradicional (SOAP) estão na utilização semântica dos métodos HTTP (GET, POST, PUT e DELETE), na leveza dos pacotes de dados transmitidos na rede e na simplicidade, fazendo desnecessária a criação de camadas intermediárias (Ex.: Envelope SOAP) para encapsular os dados.

<p align="middle"><img src="https://i.imgur.com/QtD42Z2.png" ></p>

---

#### Características de uma requisição REST:

* O método HTTP é utilizado para determinar a operação a ser realizada em um determinado recurso. Em geral, utiliza-se o GET para recuperar, POST para criar, PUT para alterar e DELETE para apagar;
* O recurso, por sua vez, é indicado na URL da requisição;
Parâmetros podem ser passados na própria URL e/ou no corpo na requisição;
* Os tipos de dados utilizados na requisição e na resposta devem ser acordados entre o servidor e o(s) cliente(s). JSON e XML estão entre os tipos mais utilizados.

---

#### REST x RESTful:

Existe uma certa confusão quanto aos termos REST e RESTful. Entretanto, ambos representam os mesmo princípios. A diferença é apenas gramatical. Em outras palavras, sistemas que utilizam os princípios REST são chamados de RESTful.

* REST: conjunto de princípios de arquitetura
* RESTful: capacidade de determinado sistema aplicar os princípios de REST.

#### Aplicação

Tendo em vista estes conceitos, podemos mencionar a maneira pela qual são aplicados no GamesBI. Que se baseia em sua arquitetura de microserviços, de forma com que cada serviço se define como uma API RESTful que trabalha com JSON como dados de resposta.

* <b>IGDB Service</b>: Realiza requisições GET para a API do IGDB e armazena os dados necessários.
* <b>Youtube Service</b>: Realiza requisições GET para o microserviço da IGDB e API do Youtube e armazena os dados necessários.
* <b>Steam Service</b>: Realiza requisições GET para o microserviço da IGDB e API da Steam e armazena os dados necessários.
* <b>Twich Service</b>: Realiza requisições GET para o microserviço da IGDB e API da Twich e armazena os dados necessários.

Por fim, todos estes dados são centralizados e tratados no CrossData para que posteriormente possam ser disponibilizados para o Front End da GamesBI.

---

<!-- * Model

 O framework Django facilita na interface com o banco de dados. Cada classe da modelo se compara a uma tabela do banco de dados, e as instâncias destas classes, representam os registros destas tabelas. Para adicionar valores ao banco, basta definí-los nas respectivas variáveis. Esta camada contém qualquer coisa e tudo sobre os dados: como acessá-lo , como validá-lo , quais comportamentos que tem e as relações entre os dados. Para o mapeamento dos dados, não será necessário utilizar códigos em SQL para garantir a persistência dos dados no banco.

---

* View

A camada View é responsável pela implementação das regras de apresentação e negócio do nosso sistema. É nela onde iremos nos comunicar com a Model e a Template, cadastrando e tratando as informações recebidas. Retornando para o usuário uma resposta em JSON, ou erros encontrados. Esta é equivalente a Controller na arquitetura MVC

---

* Detalhes arquiteturais

As resoluções de urls, responsabilidade dada as controllers no MVC, é feita pela própria estrutura do framework

O Django oferece um sistema ORM com o banco de dados que permite ao desenvolvedor não se preocupar com querys explicitamente escritas. Com a intrudução do Banco de dados Não-Relacional MongoDB, o ORM é substituído pelo DRM, por conta das características exclusivas do banco. -->

### 2.2 Arquitetura de Microserviços

 arquitetura orientada a micro serviços foi adotada para este projeto devido a suas vantagens em relação a estrutura monolítica, dentre elas estão:
* Disponibilização de novos processos ou serviços sem impacto nos processos e serviços existentes.
* Alterações em processos e serviços sem a necessidade de parada de todo o sistema.
* Otimização da utilização da infraestrutura de nuvem.
* Redução da complexidade de manutenção.

### 2.3 Padrão de arquitetura do REACT

## 3. Metas e Restrições da Arquitetura

----

### 3.1 Metas
A Arquitetura desse projeto tem como principal objetivo o desacoplamento do sistemas em diferentes microserviços, trazendo máxima independência possível, favorecendo o entendimento sobre o objetivo de cada microserviço, a manutenibilidade e evolução. O sistema deve proporcionar facilidade para os usuários poderem aferir os dados, além de facilitar a análise dos mesmos.

### 3.2 Restrições da Arquitetura
- O projeto possui as seguintes restrições:
- Framework Django 2.1 com Python 3.7
- Padrão MVT
- API's REST

## 4. Arquitetura dos Serviços e visão de Implementação

----

### 4.1 Visão Geral

<p align="middle"><img src="https://i.imgur.com/faDwAzt.jpg"></p>

### 4.2 Microserviços e camadas

A arquitetura e sua versão atual está particionada em:

* 1 - Front-End

  Esta fronteira é responsável por resgatar as estatísticas geradas pelo microserviço Metabase e
  apresentar para o usuário final.

* 2 - Metabase

  Fronteira responsavel por receber os dados do Cross Data. Assim, gerando gráficos e estatísticas que serão apresentados no Front-End.  

* 3 - Cross Data

  Fronteira responsável por receber os dados das API's externas e persisti-los no banco de dados. Para posteriormente fornecer esses dados para o Metabase.

* 4 - IGDB Data

  Fronteira responsável pela listagem dos jogos mais populares, será responsável por repassar para os outros microserviços quais jogos deveráo ser recuperados em suas respectivas fontes de dados.

* 5 - Steam Data

  Fronteira responsável pela busca de dados na API da SteamSpy. Receberá os parâmetros de busca e buscará por eles na API.

* 6 - Twitch Data

  Fronteira responsável pela busca de dados na API da Twitch. Receberá os parâmetros de busca e buscará por eles na respectiva API.

* 7 - Youtube Data

  Fronteira responsavel pela busca de dados na API do Youtube. Receberá os parâmetros de busca e buscará por eles na respectiva API.

APIs Externas:
  Diferentes fontes de dados acerca de jogos digitais
  * SteamSpy
  * Twitch API
  * IGDB API
  * Youtube API

### 4.3 Diagrama de pacotes

<p align="middle"><img src="https://i.imgur.com/6ncZkMh.jpg"></p>

* Acima é demonstrada a implementação geral dos pacotes de cada microserviço, onde o "<X>" será substituído pelo nome dos respectivos microserviços.

Dentro de Aplicações Django, os pacotes são representados pelos apps.

* IMPORTDATA
O app importdata é responsável pela comunicação com as API's e fontes de dados externas. Tendo como tarefa a importação dos dados, tratamento e persistência no banco de dados

* API
O app API é responsável pela disponibilização dos dados persistidos no banco de dados para os outros microserviços através de endpoints específicos, também podendo ser usado por qualquer outra aplicação que deseja acessar os dados.

## 5 Visão de dados

----

  5.1 IGDB Data

  <p align="middle"><img src="https://i.imgur.com/xzeykEY.jpg"></p>

  5.2 Steam Data

  <p align="middle"><img src="https://i.imgur.com/um3A0Kw.jpg"></p>

  5.3 Twitch Data

  <p align="middle"><img src="https://i.imgur.com/2duWVJ7.jpeg"></p>

  5.4 Cross Data

  <p align="middle"><img src="https://i.imgur.com/C1IriEs.jpg"></p>
