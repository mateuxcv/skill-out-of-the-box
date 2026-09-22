# Design B2B e arquitetura enxuta

Use os critérios ligados ao caso concreto. Não transforme esta referência em uma lista de funcionalidades obrigatórias.

## Produto: organize em torno da decisão

- Diferencie comprador, operador e administrador quando tiverem necessidades distintas.
- Identifique a unidade de trabalho: pedido, conta, documento, incidente ou outro objeto do domínio.
- Faça a tela principal responder: o que exige atenção, por quê e o que posso fazer agora?
- Priorize tabelas quando comparar e ordenar for o trabalho. Use cards, grafos e timelines quando sua estrutura ajudar a decidir.
- Ofereça profundidade progressiva: resumo para triagem, detalhe para investigação e ação no contexto apropriado.
- Considere filtros salvos, ações em lote, teclado, importação/exportação e retomada de trabalho quando houver uso repetitivo.
- Observe adoção e custo de mudança: uma solução tecnicamente melhor pode falhar se romper integrações e hábitos indispensáveis.

## Identidade visual com intenção

Defina uma direção visual antes de produzir componentes:

1. **Caráter:** por exemplo, editorial e analítico, operacional e compacto, ou técnico e preciso; vincule a escolha ao público.
2. **Hierarquia:** destaque a informação decisiva e a ação principal, não todas as métricas igualmente.
3. **Tokens:** tipografia, espaçamento, cores semânticas, densidade, bordas e elevação coerentes com o sistema existente.
4. **Composição:** determine a proporção entre navegação, área de trabalho, evidência e detalhe.
5. **Feedback:** movimento e transições devem explicar mudança de estado ou preservar orientação.

Evite adotar como padrão universal hero com gradiente, excesso de cards, ícones sem função e uma paleta arbitrária. Também não os proíba quando fizerem sentido para a marca e a tarefa. Preserve a identidade existente ao evoluir um produto.

## Estados fazem parte da solução

Projete os estados relevantes: inicial vazio, carregando, parcial, sem resultados, erro recuperável, sucesso, conflito e acesso insuficiente.

- Erros devem mostrar o que aconteceu e como prosseguir sem perder trabalho.
- Confirme operações irreversíveis no ponto necessário; ofereça desfazer quando tecnicamente viável.
- Use HTML semântico, labels, ordem de foco, contraste e informação que não dependa só de cor.
- Em drag-and-drop, considere alternativa por teclado; em virtualização, confira foco e acessibilidade.
- Adapte ao dispositivo e contexto real: operação de campo móvel e estação de trabalho densa têm prioridades diferentes.

## IA como capacidade opcional

Use IA quando a tarefa envolver ambiguidade, linguagem ou síntese que regras simples não resolvam bem.

- Defina a ação concreta assistida, qualidade aceitável, latência e custo.
- Apresente origem e evidências para sugestões factuais quando disponíveis.
- Mantenha correção e continuidade do fluxo diante de erro ou indisponibilidade.
- Separe sugestão de execução de ações consequentes conforme o fluxo e as autorizações existentes.
- Não acrescente banco vetorial, framework de agentes ou interface de chat sem necessidade demonstrada.

## Fronteiras de arquitetura

Em projeto existente, melhore dentro das convenções atuais; não imponha uma nova organização apenas por preferência. Em projeto novo, comece com uma aplicação coesa e módulos por capacidade quando adequado.

Exemplo conceitual, a adaptar ao framework:

```text
features/
  reconciliation/
    ui/
    use-cases/
    domain/
    integrations/
```

Uma funcionalidade pequena pode caber em poucos arquivos. Separe domínio de detalhes voláteis quando isso facilitar evolução e testes; não crie interfaces e fábricas sem benefício.

- Mantenha regras de negócio fora de handlers visuais quando tiverem significado próprio.
- Estabeleça uma fonte de verdade para cada dado e uma responsabilidade por módulo.
- Isole integrações externas nos pontos em que troca, falha ou contrato justificarem o limite.
- Evite estado global, bibliotecas de UI concorrentes e motores duplicados de validação sem motivo concreto.
- Acrescente processamento assíncrono quando duração, confiabilidade ou volume exigirem; não por estética arquitetural.
- Prefira deploy e operação simples enquanto os requisitos não justificarem distribuição.

## Requisitos B2B orientados ao contexto

Se o sistema atender múltiplas empresas, verifique isolamento de tenant e autorização no servidor. Se lidar com aprovações ou alterações rastreáveis, modele autoria e histórico apropriados. Se houver integrações repetíveis, trate contratos e duplicação quando relevante.

SSO, RBAC sofisticado, auditoria extensa, residência de dados e múltiplas regiões são decisões motivadas pelo caso, não acessórios automáticos de todo MVP B2B.

## Prova mínima

Escolha a verificação que pode contrariar a proposta:

| Hipótese | Experimento útil |
| --- | --- |
| Fila de exceções reduz troca de contexto | Completar casos representativos e comparar passos com o fluxo atual. |
| Composição de bibliotecas suporta a experiência | Executar seleção, edição, filtro e recuperação de erro no runtime real. |
| Virtualização é necessária | Medir o cenário representativo sem e com ela; observar também foco e memória. |
| Automação é confiável | Usar casos normais, ambíguos e incorretos; verificar fallback e correção. |
| Identidade visual melhora legibilidade | Inspecionar conteúdo realista em densidades e tamanhos relevantes. |

Metas de negócio são hipóteses até haver dados. Uma demonstração técnica valida viabilidade; não comprova adoção ou ganho de receita.
