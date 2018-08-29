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

# Documento de Arquitetura

Sumário
----------------

* 1 . [Introdução](#1-introdução)
    * 1.1. [Finalidade](#11-finalidade)
    * 1.2. [Escopo](#12-escopo)
    * 1.3. [Definições, acrônimos e abreviações](#13-Definições,-acrônimos-e-abreviações)
    * 1.4. [Referências](#14-referências)
    * 1.5. [Visão Geral](#15-Visão-Geral)

* 2 . [Representação da Arquitetura](#2-Representação-da-Arquitetura)
   * 2.1. [Representação do padrão de Arquitetura MVT](#21-Padrão-de-Arquitetura-MVT)
   * 2.2. [Representação da Arquitetura de Microserviços](#22-Arquitetura-de-Microserviços)   

* 3 . [Metas e Restrições da Arquitetura](#3-Metas-e-Restrições-da-Arquitetura)

* 4 . [Visão de Casos de Uso](#4-Visão-de-Casos-de-Uso)
   * 4.1. [Atores](#41-atores)
   * 4.2. [Realizações de Casos de Uso](#42-Realizações-de-Casos-de-Uso)

* 5 . [Visão de Processos](5-Visão-de-Procesos)

* 6 . [Visão de Implementação](#6-Visão-de-Implementação)
	 * 6.1. [Visão Geral](#61-Visão-Geral)
   * 6.2. [Diagrama de Pacotes](#62-Diagrama-de-Pacotes)
   * 6.3. [Pacotes de Design Significativos do Ponto de Vista da Arquitetura](#63-Pacotes-de-Design-Significativos-do-Ponto-de-Vista-da-Arquitetura)

* 7 . [Arquitetura dos Serviços e visão de Implementação](#7-Arquitetura-dos-Serviços-e-visão-de-Implementação)
   * 7.1. [Visão Geral](#71-Micro-Serviços-e-Camadas)
   * 7.1. [Microserviços e Camadas](#72-Visão-Geral)

* 8 . [Visão de Dados](#8-visao)


## 1. Introdução

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

A arquitetura do projeto possuirá ambientes diferentes: API's REST, por debaixo do framework MVT Django, assim como o ambiente WEB de interação com usuário. Juntando todos os ambientes e coordenando-os, formamos assim uma arquitetura de Microserviços.

### 2.1 Padrão de Arquitetura MVT

Os padrões de arquitetura expressam formas de organizar a estrura do sistema e ajudam a lidar com a complexidade do software. O padrão utilizado neste projeto é o MVT, que por sua vez se assemelha bastante ao conhecido MVC. Tanto que, de acordo com o Django Book, o Django segue o padrão MVC suficientemente para ser considerado um framework MVC.

<p align="middle"><img src="https://i.imgur.com/hYYq7q4.png" ></p>

* Model
---
As Models do MVC e do MVT são equivalentes em responsabilidades. O framework Django facilita na interface com o banco de dados. Cada classe da modelo se compara a uma tabela do banco de dados, e as instâncias destas classes, representam os registros destas tabelas. Para adicionar valores ao banco, basta definí-los nas respectivas variáveis. Esta camada contém qualquer coisa e tudo sobre os dados: como acessá-lo , como validá-lo , quais comportamentos que tem e as relações entre os dados. Para o mapeamento dos dados, não será necessário utilizar códigos em SQL para garantir a persistência dos dados no banco.

* View
---
A camada View é responsável pela implementação das regras de apresentação e negócio do nosso sistema. É nela onde iremos nos comunicar com a Model e a Template, cadastrando e tratando as informações recebidas. Retornando para o usuário uma resposta em JSON, ou erros encontrados. Esta é equivalente a Controller na arquitetura MVC

* Template
---
Templates é a camada que retorna a visão para o usuário do programa. Essa camada é composta por, HTML,CSS, javascript.

* Detalhes arquiteturais
---
As resoluções de urls, responsabilidade dada as controllers no MVC, é feita pela própria estrutura do framework

O Django oferece um sistema ORM com o banco de dados que permite ao desenvolvedor não se preocupar com querys explicitamente escritas. Com a intrudução do Banco de dados Não-Relacional MongoDB, o ORM é substituído pelo DRM, por conta das características exclusivas do banco.

### 2.2 Arquitetura de Microserviços

 arquitetura orientada a micro serviços foi adotada para este projeto devido a suas vantagens em relação a estrutura monolítica, dentre elas estão:
* Disponibilização de novos processos ou serviços sem impacto nos processos e serviços existentes.
* Alterações em processos e serviços sem a necessidade de parada de todo o sistema.
* Otimização da utilização da infraestrutura de nuvem.
* Redução da complexidade de manutenção.

## 3. Metas e Restrições da Arquitetura

### 3.1 Metas
A Arquitetura desse projeto tem como principal objetivo o desacoplamento do sistemas em diferentes microserviços, trazendo máxima independência possível, favorecendo o entendimento sobre o objetivo de cada microserviço, a manutenibilidade e evolução. O sistema deve proporcionar facilidade para os usuários poderem aferir os dados, além de facilitar a análise dos mesmos.

### 3.2 Restrições da Arquitetura
- O projeto possui as seguintes restrições:
- Framework Django 2.1 com Python 3.7
- Padrão MVT
- API's REST

## 4. Visão de Casos de Uso
### 4.1 Atores
### 4.2 Realizações de Casos de Uso

## 5. Visão de Procesos

## 6. Visão de Implementação
### 6.1 Visão Geral
### 6.2 Diagrama de Pacotes
### 6.3 Pacotes de Design Significativos do Ponto de Vista da Arquitetura

## 7. Arquitetura dos Serviços e visão de Implementação

### 7.1 Visão Geral

<p align="middle"><img src="https://i.imgur.com/XR9n6p2.jpg" ></p>

### 7.2 Microserviços e camadas

O esquema acima demonstra bem a arquitetura adotada. Consiste em várias em quatro REST API's feitas usando Django REST, uma framework para Python, linguagem esta ja conhecida pela sua facilidade e desempenho relacionados a Data Science e Machine Learning. Três delas serão responsáveis por buscar dados relacionados a jogos da Steam, Twich, e Youtube. A quarta API é responsável por fazer um cruzamento de dados entre os dados obtidos nas demais API's do microserviço. Esta possui o objetivo de realizar estatísticas relacionadas ao consolidado de todos os dados.

Todo este conteúdo será disponibilizado para a aplicação Front-End feita utilizando NodeJS, HTML, css até chegar ao usuário final. O usuário terá a possibilidade de ver as estatísticas e gráficos relacionados aos jogos de uma maneira interativa.

## 8 Visão de dados
