---
layout: page 	
title: Pipeline de DevOps
icon: fa-pencil-alt
order: 4
---

## Histórico de Revisões

|Data|Versão|Descrição|Autor|
| --- | --- | --- | --- |
|28/08/2018|0.1|Criação da estrutura do documento|Felipe Osório|
|29/08/2018|0.2|Adição das políticas de branches|Felipe Osório|

### Sumário
---

* 1  [Introdução](#1-introdução)
* 2  [Integração contínua](#2-integração-contínua)
    * 2.1 [Políticas de commit](#21-políticas-de-commit)
	* 2.2 [Políticas de branches](#22-políticas-de-branches)
	* 2.3 [Folha de estilo e Testes](#23-folha-de-estilo-e-testes)
	* 2.4 [Pull requests](#24-pull-requests)
	* 2.5 [Builds](#25-builds)
* 3  [Deploy Contínuo](#3-deploy-contínuo)
	* 3.1  [Pipeline](#31-pipeline)


---
## 1. Introdução

Este documento visa apresentar todas as políticas adotadas pela equipe para atingir a integração contínua e o deploy contínuo da aplicação. Tendo isso em vista, este documento irá ser dividido em duas partes, visando a melhor apresentação dos dados. A primeira parte do documento irá ser apresentado como foi realizado a integração contínua, e na segunda parte, o deploy contínuo.

## 2. Integração contínua

A integração contínua visa promover um desenvolvimento fluído, no qual cada desenvolvedor consiga integrar o código desenvolvido na mesma frequência com que as funcionalidades são desenvolvidas. Para isso, utilizamos várias ferramentas e políticas que irão ser explicadas mais detalhadamente adiante.

### 2.1 Políticas de commit
A estrutura do commit é dado pelas seguintes regras:
```bash
[<1>] #<2> <3>
```
* Onde <1> é a operação feita:
  * [ADD] - Quando novo código/feature é adicionada ao repositório
  * [DEL] - QUando código/feature é deletada
  * [UPDATE] - Quando código/feature existente é atualizada ou refatorada
  * [FIX] - Correção de bugs, código quebrado, etc
* <2> o número da issue relacionada
* <3> Texto explicativo sobre o que foi realizado:
  * Todos os textos em INGLÊS

### 2.2 Políticas de branches
Para a política de branches, utilizamos seguir o padrão utilizado pelo gitflow, que utiliza as seguintes branches:

* **master**, é utlizada para guardar a história oficial de releases do software, no qual está contido a versão mais recente e estável da aplicação.
* **develop**, é utilizada para a integração de todas as features desenvolvidas neste novo insumo de código.
* **feature**, é utilizada para a codificação da feature em questão. A nomeação dessa feature é dada da seguinte forma: feature_#0, no qual #0 é o número da issue(ex: feature_#23, caso a issue em questão seja a issue de número 23). Assim que a feature for completa, ela é integrada à branch develop.
* **release**, é utilizada após o insumo de código estiver apropriado para ser lançado como uma novo release. É possível realizar ajustes rápidos para poder ser lançado como uma nova release. Assim que estiver pronta, esta branch è integrada à master e à develop.
* **hotfix**, caso haja algum problema urgente, é criado essa branch para realizar ajustes e logo após integrar à master.

### 2.3 Folha de estilo e Testes
Uma folha de estilo é necessária para garantir a qualidade do código desenvolvido. Visto que todas as API's que iremos desenvolver irão ser feitas em python, a folha de estilo que decidimos utilizar é o PEP8, que é considerada padrão para projetos em python. Utilizando a ferramenta Code Climate, é possível verificar, a cada insumo de código, se o mesmo segue o padrão definido pelo PEP8.

Em relação aos testes, possuímos uma métrica bastante importante, que é a cobertura de teste. Essa métrica é capaz de garantir a por centagem de código testado na aplicação. Para gerarmos e controlarmos essa métrica, utilizamos o Coveralls, bastante parecido com o Code Climate, no sentido de que a cada insumo de código, também é gerado um relatório identificando o aumento ou a diminuição da cobertura de testes.

### 2.4 Pull requests
Após a codificação de uma história de usuário, o desenvolvedor deverá abrir um pull request a partir de sua branch em relação à branch master do repositório oficial. Todos os pull requests deverão seguir um template já definido dentro do repositório, descrevendo as alterações que foram realizadas assim como as issues relacionadas à esse pull request. 

Depois da criação do pull request, todos os CI's que estamos utilizando deverão dar um visto, afirmando que essas alterações seguem a folha de estilo definida, não houve uma diminuição da cobertura de teste e se a build está sendo criada corretamente. Em seguida, ao passar em todos os vistos, o pull request necessitará de um reviewer para aprovar as alterações feitas. Com isso feito, o pull request estará pronto a ser aceito na master.

### 2.5 Builds
Como dito anteriormente, as builds são geradas ao final de cada pull request, à fim de testar a criação desses insumos de código. Caso esse passo ou qualquer um dos outros CI's dê algum tipo de problema, essas ferramentas irão informar aos mantenedores do repositório via email e pelo próprio pull request também.

## 3. Deploy Contínuo

### 3.1 Pipeline
