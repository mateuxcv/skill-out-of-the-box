# Contribuindo com Out of the Box

Obrigado por ajudar a melhorar a skill. O objetivo é aumentar a utilidade das decisões de produto e arquitetura, mantendo as instruções claras e proporcionais à tarefa.

## Onde contribuir

- Métodos criativos com exemplos concretos de trabalho B2B.
- Critérios melhores para pesquisar, comparar e combinar soluções.
- Orientações de design, acessibilidade e arquitetura aplicáveis ao contexto.
- Cenários que revelem ativação indevida, decisões ruins ou pesquisa sem evidência.
- Correções de documentação, instalação e validação.

## Reportar um problema

Abra uma [issue](https://github.com/mateuxcv/skill-out-of-the-box/issues) contendo:

1. O objetivo da tarefa e o prompt utilizado.
2. Modelo, versão do OpenCode e ferramentas disponíveis, quando conhecidos.
3. Comportamento esperado e comportamento observado.
4. Um exemplo mínimo reproduzível, removendo credenciais e dados privados.
5. A seção da skill relacionada, se conseguir identificá-la.

Diferencie o que foi observado do que é uma hipótese sobre a causa.

## Propor uma mudança

1. Crie um fork e uma branch descritiva.
2. Faça uma mudança focada e explique qual problema ela resolve.
3. Preserve o frontmatter e mantenha o `SKILL.md` abaixo de 500 linhas.
4. Leve detalhes extensos para `references/`, com um link direto no arquivo principal.
5. Atualize exemplos e cenários afetados pela alteração.
6. Execute o validador estrutural:

   ```bash
   python scripts/validate_skill.py
   ```

7. Se alterar o comportamento, experimente os cenários relevantes em sessões novas e registre o resultado. Reinicie o OpenCode após editar a skill.
8. Abra um pull request com objetivo, resumo da mudança e verificações realizadas.

## Princípios editoriais

- Escreva em português claro, com instruções acionáveis.
- Prefira critérios observáveis a adjetivos genéricos.
- Evite regras que obriguem a adotar uma stack, biblioteca ou arquitetura específica.
- Distinga exemplos ilustrativos de compatibilidades e resultados verificados.
- Registre fontes para afirmações técnicas que dependam de informação externa.
- Mantenha a profundidade proporcional ao problema.

## Como relatar a avaliação

Use os [cenários comportamentais](.opencode/skills/out-of-the-box/references/evaluation.md) como referência. Inclua:

| Campo | O que informar |
| --- | --- |
| Ambiente | Modelo, data, ferramentas e contexto fornecido. |
| Cenário | Prompt e restrições usadas. |
| Evidência | Entrega e chamadas de ferramentas pertinentes. |
| Resultado | O que funcionou, o que falhou e o que não foi verificado. |

A aprovação do CI confirma a validação estrutural. A eficácia de uma mudança de instruções precisa de avaliação comportamental separada.
