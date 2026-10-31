---
name: porta-saas
description: "Monta os sistemas e SaaS da Porta Studio nos pacotes Sistema MVP, SaaS Completo e Plataforma + IA, com a lista exata do que cada pacote inclui: login, painel, banco de dados, assinatura com cobrança recorrente, níveis de acesso, relatórios, IA e app instalável. Use sempre que o pedido for um Sistema MVP, SaaS Completo ou Plataforma + IA, ou um sistema web, SaaS, painel administrativo, sistema de agendamento, controle de pedidos ou estoque, app com login ou software por assinatura para um cliente, mesmo que o pacote não seja dito."
---

# SaaS e sistemas (Sistema MVP, SaaS Completo, Plataforma + IA)

Sistema é o pacote mais caro e o que mais dá problema quando o escopo fica solto. Por isso esta skill tem uma regra que as outras não têm: **escopo escrito e aprovado antes do código.** O pacote define o teto; o escopo diz exatamente quais telas e fluxos entram.

Entregue tudo do pacote e nada de pacote acima de graça. Se o cliente pedir mais no meio do caminho, anote como mudança de escopo, com prazo e valor à parte.

## 1. Descobrir o pacote

- "MVP", "primeira versão", "validar a ideia", um fluxo só → **Sistema MVP**
- Vender para várias empresas, mensalidade, planos, equipe com permissões → **SaaS Completo**
- Assistente com IA, atendimento automático, integração com outros sistemas, app no celular → **Plataforma + IA**

Diga em uma linha qual pacote vai usar e por quê.

## 2. Escopo antes do código

Escreva `escopo.md` e mostre para a pessoa aprovar:
- **Problema** em uma frase e **quem usa** (perfis de usuário)
- **Fluxo principal**, passo a passo, do jeito que o usuário faz
- **Telas**, numeradas, com o que cada uma mostra e faz (MVP: até 6)
- **Dados**: as tabelas e os campos principais
- **Fora do escopo**: o que fica para depois. Esta lista evita briga no fim
- **Etapas e pagamentos**: 30% no início, 40% na primeira versão navegável, 30% na entrega
- **Custos mensais do cliente**: hospedagem, banco, e-mail, IA, cobrança (estimativa)

Só comece a construir depois do "pode seguir". Se a pessoa já mandou um escopo, confira contra o pacote e aponte o que passa do limite.

## 3. O que cada pacote inclui (lista de entrega)

### Sistema MVP (3 a 5 semanas)
- **Login e cadastro de usuários**: e-mail e senha, recuperação de senha, sair
- **Painel administrativo**: o dono vê e gerencia os dados (lista, busca, editar, excluir)
- **Um fluxo principal** completo: agenda, pedidos, estoque, matrículas ou o que o cliente precisa
- **Até 6 telas**, contando login e painel
- **Funciona no celular e no computador**
- Banco com regras de acesso por usuário (cada um só vê o que é dele)
- Publicado com link e um README com como rodar, variáveis de ambiente e como publicar

### SaaS Completo (6 a 10 semanas): tudo do MVP, mais
- **Várias empresas na mesma plataforma** (multiempresa): cada empresa só vê os próprios dados, garantido no banco e não só na tela
- **Assinatura com cobrança recorrente**: planos, período de teste se fizer sentido, bloqueio quando a assinatura vence, reativação ao pagar. O status vem do aviso (webhook) do meio de pagamento, nunca só do navegador
- **Níveis de acesso por usuário**: dono, administrador e membro, no mínimo. Convite de equipe por e-mail
- **Relatórios e painel de métricas**: números principais do negócio do cliente, com filtro de período e exportar CSV
- **E-mails e avisos automáticos**: boas-vindas, convite, recuperação de senha, cobrança vencendo, e os avisos do fluxo principal
- Página de planos e termos de uso e privacidade

### Plataforma + IA (prazo na proposta): tudo do SaaS Completo, mais
- **Atendimento ou assistente com IA** sobre os dados do cliente: antes de escrever qualquer código de IA, leia a skill `claude-api` (modelos atuais, preços, streaming, ferramentas). A chave da API fica só no servidor; limite de uso por empresa para a conta não explodir
- **Integração com APIs e outros sistemas** (WhatsApp Business, ERP, agenda, pagamentos), com webhooks validados por assinatura
- **App instalável no celular** (PWA): manifesto, ícones, funciona com internet fraca nas telas principais
- **Escopo fechado em proposta**: este pacote sempre começa pela proposta, com estimativa de custo mensal de IA

## 4. Como construir

Stack padrão e padrões de código em `references/stack.md`. Em resumo: Next.js + Supabase (login, banco Postgres com regras por linha) + Tailwind, publicado na Vercel ou na Netlify. Use outra stack só se o cliente já tiver uma.

Ordem de trabalho:
1. Banco primeiro: tabelas, regras de acesso (RLS) e dados de exemplo
2. Login e o esqueleto das telas
3. O fluxo principal de ponta a ponta, feio mas funcionando: essa é a "primeira versão navegável" da etapa de 40%
4. Acabamento visual, celular, estados vazios, mensagens de erro
5. Pacotes acima: cobrança, equipe, relatórios, e-mails, IA

Visual: limpo e consistente, com a cara da marca do cliente. Sistema é ferramenta, não vitrine: clareza vem antes de animação. Se a skill `frontend-design` estiver disponível, use-a como apoio.

No Claude Code, trabalhe num repositório próprio do cliente (não dentro do site da Porta Studio). Se não houver, crie a pasta do projeto e diga à pessoa para criar o repositório no GitHub.

## 5. Segurança (sempre, em qualquer pacote)

- Regras de acesso no banco (RLS) ligadas em **todas** as tabelas, testadas com dois usuários diferentes
- Chaves secretas (service role, chave de IA, chave do meio de pagamento) só no servidor, nunca no navegador nem no repositório. Entregue `.env.example` sem valores
- Validar tudo que chega do formulário no servidor
- Webhooks de pagamento conferidos pela assinatura do provedor
- Dados pessoais: só o necessário, e a política de privacidade dizendo o que é guardado (LGPD)

## 6. Conferir antes de entregar

- [ ] Tudo do pacote e do escopo aprovado está feito, e nada de pacote acima foi dado de graça
- [ ] Testado com dois usuários (e duas empresas, no SaaS Completo): ninguém vê dado do outro
- [ ] Celular e computador sem nada quebrado
- [ ] Cobrança testada no modo de teste do provedor (SaaS Completo em diante)
- [ ] README, `.env.example` e passo a passo para publicar
- [ ] Custos mensais do cliente listados

## 7. Mensagem de entrega

**[Pacote] · [Nome do sistema]**
- O que foi entregue: a lista do pacote e do escopo, marcada
- Link da versão publicada e acesso de teste
- O que o cliente precisa fazer (criar contas em hospedagem, banco, cobrança, no nome dele)
- Custos mensais do cliente
- Fora do escopo e próximos passos possíveis
- Suporte mensal (hospedagem, correções, pequenas melhorias): preço no painel pessoal da Porta Studio: https://claude.ai/artifact/Fk5wzknThSy6KMaQHmdnHg
