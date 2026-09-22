---
name: out-of-the-box
description: "Use quando o usuário pedir pensar fora da caixa, soluções criativas, design diferenciado ou explorar e combinar bibliotecas para criar ou evoluir aplicações B2B e SaaS. Conecta descoberta de produto, GitHub Trending, pesquisa técnica e experimentos a uma arquitetura enxuta. Também se aplica a pedidos equivalentes como out-of-the-box e creative B2B product design. Não ativar para correções pontuais, mudanças mecânicas ou consultas de documentação sem decisão criativa de produto ou arquitetura."
---

# Out of the Box

Transforme uma dor de negócio em uma solução útil e diferenciada, pesquisando possibilidades além da stack habitual e escolhendo a menor arquitetura capaz de entregar o resultado.

**Princípio:** amplitude na exploração, rigor na seleção, simplicidade na execução.

## Contrato de atuação

- Comece pelo trabalho que a pessoa precisa realizar, e não por uma biblioteca favorita ou uma tela genérica de dashboard.
- Criatividade deve mudar a qualidade de uma decisão, reduzir trabalho ou habilitar uma capacidade importante. Novidade visual isolada não basta.
- Respeite instruções do projeto, stack existente, escopo, orçamento e ferramentas disponíveis. Esta skill não concede permissões nem exige agentes adicionais.
- Se o pedido for implementar, avance da exploração até a entrega e verificação. Se for idear ou comparar, entregue a decisão no nível solicitado.
- Pergunte apenas quando faltar uma informação que altere materialmente a solução. Para lacunas reversíveis, explicite uma hipótese e avance.
- Apresente conclusões, evidências, alternativas e trade-offs de forma concisa; não exponha raciocínio interno passo a passo.

## Profundidade proporcional

| Contexto | Aplicação |
| --- | --- |
| Ideia localizada ou prazo curto | Brief breve, 2 direções distintas, pesquisa focada na incerteza e um teste simples. |
| Novo fluxo, produto ou escolha técnica relevante | Fluxo completo abaixo; normalmente 3 direções e 3–5 candidatos técnicos relevantes. |
| Alto custo de migração ou incerteza técnica central | Aprofunde documentação e faça um spike da integração antes de comprometer a arquitetura. |

Os números são limites orientativos, não metas de volume. Não alongue uma tarefa pequena para preencher um ritual. Mudanças mecânicas dispensam este fluxo.

## 1. Entenda o trabalho e as restrições

Inspecione os arquivos e convenções relevantes: instruções locais, manifesto, lockfile, organização do código, componentes, integrações e testes existentes. Em projeto novo, estabeleça as restrições mínimas antes de escolher a stack.

Resuma:

1. **Pessoa e trabalho:** quem opera, quem compra e quem administra; o que precisa acontecer e com que frequência.
2. **Atrito atual:** onde há espera, erro, retrabalho, troca de ferramenta ou perda de contexto.
3. **Resultado observável:** tempo até concluir uma tarefa, taxa de erro, adoção do fluxo ou outro indicador ligado à dor.
4. **Restrições:** ambiente, prazo, custo, dados, integrações, experiência da equipe e volume esperado.
5. **Incerteza decisiva:** o que precisa ser aprendido para escolher bem.

Não invente entrevistas, métricas de baseline, requisitos enterprise ou validações com clientes. Identifique hipótese, evidência e meta proposta separadamente.

## 2. Expanda o espaço de soluções

Antes de escolher bibliotecas, formule direções que mudem o mecanismo da experiência. Use [os métodos criativos](references/creative-methods.md) quando precisar ampliar as opções.

Para o fluxo completo, considere:

- **Essencial:** resolver o trabalho com recursos existentes e o mínimo de mudança.
- **Transferência:** adaptar um padrão útil de outro domínio ao contexto B2B.
- **Recombinação:** unir capacidades complementares para entregar um resultado novo ou eliminar uma etapa.

Varie fluxo, interação ou distribuição do trabalho, não apenas cor e layout. Inclua uma opção de subtração: o que pode deixar de existir? Não imponha IA, chat, canvas ou colaboração em tempo real quando não melhorarem o trabalho.

Para cada direção, produza uma ficha curta: dor → mecanismo → benefício esperado → maior risco → menor experimento. Escolha uma **interação distintiva** para explorar primeiro.

## 3. Pesquise além do repertório habitual

Leia [o protocolo de pesquisa](references/research-and-selection.md) ao fazer descoberta externa ou selecionar dependências.

Em explorações completas, consulte GitHub Trending atual e busca orientada ao problema, além de alternativas maduras. Em tarefas rápidas, consulte Trending quando a descoberta de novas soluções puder influenciar a decisão. Se o usuário pedir explicitamente, tente a consulta mesmo no modo rápido.

- Comece por https://github.com/trending?since=weekly e restrinja por linguagem se isso ajudar.
- Cruze descobertas com documentação oficial, repositório, releases e registro de pacotes.
- Busque capacidades e gargalos, não somente nomes de bibliotecas conhecidas.
- Registre URL, data de consulta, achado relevante e o que ainda não foi verificado.
- Não confunda Trending, estrelas, atividade recente ou uma demo bonita com maturidade e adequação.
- Se a rede ou a ferramenta falhar, informe a limitação, use o material local e trate candidatos lembrados como não verificados. Nunca afirme pesquisa atual que não realizou.

Faça uma primeira rodada curta. Encerre a exploração quando houver uma opção adequada, uma alternativa comparável e um caminho para testar a incerteza decisiva. Aprofunde somente se uma lacuna puder mudar a escolha. Não instale candidatos apenas para aumentar a lista.

## 4. Combine capacidades com responsabilidade

Para cada composição proposta, escreva:

> Capacidade A resolve __. Capacidade B resolve __. Juntas permitem __. Integram-se por __. O custo adicional é __. Sem B, perderíamos __.

Verifique compatibilidade real de runtime, versões, contratos de dados, renderização e responsabilidade sobre estado. A existência de dois pacotes não comprova que funcionem juntos.

Compare sempre com reutilizar a stack, usar uma API nativa ou uma implementação pequena. Escolha **nenhuma dependência nova** quando essa opção entregar melhor o resultado total.

Uma dependência precisa demonstrar contribuição concreta. Duas soluções para a mesma responsabilidade exigem uma justificativa específica. Licença incompatível ou incompatibilidade técnica comprovada impedem adoção; incerteza relevante pede verificação, não uma nota otimista.

## 5. Convirja em produto e arquitetura

Use [os critérios de design B2B e arquitetura](references/b2b-design-and-architecture.md) conforme o trabalho envolver interface, domínio ou integração.

Compare as direções por valor ao usuário, diferenciação útil, viabilidade, custo total e confiança nas evidências. As notas, se usadas, são heurísticas de decisão, não medições objetivas.

Escolha uma direção e explique por que supera a melhor alternativa. Defina:

- jornada principal e interação distintiva;
- linguagem visual vinculada à marca, ao domínio e à densidade de trabalho;
- módulos e responsabilidades, fonte de verdade e limites das integrações;
- dependências essenciais e o papel exclusivo de cada uma;
- principal trade-off, risco não resolvido e experimento que pode invalidar a escolha.

Prefira organização coesa por funcionalidade e fronteiras explícitas. Introduza camadas, serviços, filas e abstrações somente quando resolvam uma necessidade demonstrável. Arquitetura limpa não se mede por quantidade de pastas.

## 6. Prove a hipótese e entregue

Implemente a menor fatia vertical que una interação, regra de negócio e dados necessários para testar o valor. Em trabalho exclusivamente visual, prototipe o fluxo e seus estados em vez de construir infraestrutura desnecessária.

Antes do experimento, declare o critério de sucesso ou fracasso. Exemplos: tarefa concluível por teclado; importação com erro recuperável; integração viável no runtime alvo; redução de passos sem ocultar informação decisiva.

- Verifique a integração arriscada primeiro, com versões reais e dados sintéticos representativos.
- Aproveite comandos e testes do projeto. Teste comportamento relevante, especialmente contratos, transições e falhas.
- Se houver ferramentas de navegador, confira o fluxo, responsividade, foco e estados visuais. Sem elas, registre que a inspeção visual não ocorreu.
- Não apresente mock como integração real, hipótese como ganho medido ou teste não executado como aprovado.
- Se a composição falhar, reduza ou substitua a parte problemática e reavalie o critério. Evite empilhar bibliotecas para encobrir uma incompatibilidade.
- Conclua o escopo solicitado após o spike; o experimento não substitui a implementação pedida.

## Entrega proporcional

Comunique, no tamanho adequado à tarefa:

1. **Solução escolhida** e resultado que pretende melhorar.
2. **Diferencial concreto** e por que faz sentido para esse trabalho B2B.
3. **Evidências e alternativas:** fontes verificadas, alternativa mais forte e incertezas.
4. **Composição técnica:** responsabilidades, dependências e trade-off principal.
5. **Execução:** o que foi feito, o que foi testado e limitações reais.

Use [o template de decisão](assets/decision-brief.md) para decisões extensas ou documentação solicitada; em tarefas pequenas, responda diretamente. Não crie arquivos de processo por obrigação.

## Revisão final

- A proposta ainda seria valiosa se removêssemos os nomes das tecnologias?
- As alternativas mudam o trabalho, ou são a mesma tela com outra aparência?
- Cada dependência remove complexidade relevante ou habilita algo necessário?
- A combinação foi verificada no nível exigido pela decisão?
- O usuário consegue compreender, executar e recuperar o fluxo principal?
- A arquitetura respeita o projeto e pode evoluir sem uma reescrita previsível?
- As fontes e o relato de verificação correspondem ao que realmente foi consultado e executado?

Para avaliar a própria skill, use [os cenários comportamentais](references/evaluation.md). Eles não precisam ser carregados durante tarefas normais de produto.
