---
name: porta-loja-virtual
description: "Monta as lojas virtuais da Porta Studio nos pacotes Loja Start, Loja Pro e Loja Sob Medida, na Shopify ou na Nuvemshop, com a lista exata do que cada pacote inclui: produtos, tema com a marca, pagamento (Pix, cartão, boleto), frete, domínio e o passo a passo de configuração. Use sempre que o pedido for uma Loja Start, Loja Pro ou Loja Sob Medida, uma loja virtual, e-commerce, loja Shopify ou Nuvemshop, ou um site para vender e receber pagamento direto, mesmo que o pacote não seja dito."
---

# Lojas virtuais (Loja Start, Loja Pro, Loja Sob Medida)

Uma loja virtual não é um HTML solto: ela vive numa plataforma (Shopify ou Nuvemshop), que cuida de carrinho, pagamento, frete e estoque. Por isso o trabalho tem duas partes:
1. **O que você produz**: o material da loja (produtos em planilha de importação, textos, identidade visual, seções de tema no Pro e no Sob Medida, políticas) e o passo a passo de configuração
2. **O que a pessoa clica**: criar a loja, ligar pagamento e frete, apontar o domínio. Você não tem acesso à conta Shopify ou Nuvemshop dela, então guie cada clique com clareza

O escopo importa porque é o que o cliente comprou. Entregue tudo do pacote e nada de pacote acima de graça; se o cliente precisar de mais, sugira o pacote acima ou um extra.

## 1. Descobrir o pacote e a plataforma

- "start" → **Loja Start** · "pro" → **Loja Pro** · "sob medida", migração, integração com ERP ou marketplace → **Loja Sob Medida**
- Sem pacote dito: até 30 produtos e sem variações complexas → Start; até 150 produtos ou com variações (tamanho, cor) → Pro; acima disso ou com migração e integrações → Sob Medida. Diga em uma linha qual vai usar
- **Plataforma**: Shopify por padrão. Sugira a Nuvemshop quando o cliente quiser pagar a plataforma em reais, suporte em português e começar com custo menor. A mensalidade e as taxas de venda são sempre do cliente, no nome e no cartão dele

## 2. Juntar as informações

Pergunte numa mensagem só o que faltar:
- Nome da loja, o que vende, público, Instagram
- Lista de produtos: nome, preço, variações, estoque, peso e medidas (para o frete), fotos. Se o cliente tiver planilha, peça ela
- De onde envia (CEP de origem), se tem retirada no local, se quer frete grátis acima de um valor
- Formas de pagamento desejadas e se já tem conta em algum meio de pagamento (Mercado Pago, Pagar.me etc.)
- Domínio (se já tem) e e-mail do dono

## 3. O que cada pacote inclui (lista de entrega)

### Loja Start (até 15 dias)
- **Até 30 produtos cadastrados**: planilha de importação pronta (veja `references/produtos-csv.md`), com título, descrição vendedora, preço, peso, SKU e fotos
- **Tema ajustado à marca**: tema gratuito da plataforma com as cores, fontes, logo, banner da página inicial e textos da marca. Entregue os valores exatos (cores em hex, fontes, textos de cada bloco) e onde colar cada um
- **Pix, cartão e boleto** ligados por um meio de pagamento que funcione no Brasil
- **Frete calculado no carrinho** (app de frete ou tabela da plataforma) e retirada no local se houver
- **Domínio configurado** (ou o passo a passo, se o cliente ainda não tiver)
- **Páginas obrigatórias**: trocas e devoluções, privacidade, termos, contato e "sobre". Textos escritos por você, com os dados do cliente e a observação de que não é parecer jurídico
- **Vídeo ensinando a usar a loja**: entregue o roteiro do vídeo (cadastrar produto, ver pedido, marcar como enviado, criar cupom). A pessoa grava a tela seguindo o roteiro

### Loja Pro (até 25 dias): tudo da Start, mais
- **Até 150 produtos com variações** (tamanho, cor, sabor), com estoque e foto por variação
- **Layout personalizado com animações**: seções próprias do tema (na Shopify, seções Liquid adicionadas no editor de código: banner animado, vitrine em carrossel, faixa de benefícios, depoimentos reais). Siga a skill `porta-studio-sites` para o conceito visual
- **Cupons e frete grátis por valor**: crie a lista de cupons de lançamento e a regra de frete grátis
- **Vitrine no Instagram e no Google**: ligar os canais da plataforma para Instagram/Facebook e Google, com o catálogo sincronizado
- **Recuperação de carrinho abandonado**: ligar a automação da plataforma e escrever o e-mail na voz da marca
- **WhatsApp dentro da loja**: botão flutuante com mensagem pronta, incluindo o nome do produto quando estiver na página dele

### Loja Sob Medida (prazo na proposta): tudo da Pro, mais
Comece por um **documento de escopo** e só construa depois que a pessoa aprovar, porque cada loja sob medida é diferente:
- **Design 100% exclusivo**: tema próprio ou personalização profunda, com o conceito de `porta-studio-sites`
- **Produtos ilimitados**, importação em lotes
- **Migração de outra plataforma**: exportar produtos, clientes e pedidos da plataforma antiga, converter para o formato novo, redirecionar as URLs antigas
- **Integrações**: ERP (Bling, Tiny ou outro que o cliente use), marketplaces (Mercado Livre, Shopee), sempre por apps oficiais da plataforma. Liste o app, o custo mensal e quem paga

## 4. Como produzir

Organize os arquivos assim (no repositório `portastudios`, numa pasta fora do site público ou num branch próprio):
```
clientes/<nome-da-loja>/
  escopo.md              (pacote, plataforma, o que entra e o que não entra)
  produtos.csv           (planilha de importação)
  identidade.md          (cores, fontes, logo, textos de cada bloco da página inicial)
  paginas/               (trocas.md, privacidade.md, termos.md, sobre.md)
  tema/                  (Pro e Sob Medida: seções .liquid, CSS e instruções)
  configuracao.md        (passo a passo do que o dono precisa clicar)
  roteiro-video.md
```

O passo a passo de configuração fica em `references/configuracao.md`: siga-o e adapte ao cliente. Os nomes dos menus das plataformas mudam com o tempo; escreva o caminho mais provável e avise que o nome do botão pode variar.

Se houver navegador, faça uma página de prévia em HTML com a vitrine (página inicial, um produto, o carrinho) com a identidade da marca, para o cliente aprovar o visual antes de ir para a plataforma.

## 5. Conferir antes de entregar

- [ ] Tudo do pacote está entregue, e nada de pacote acima foi dado de graça
- [ ] A planilha tem o número certo de produtos, preços conferidos e uma linha por variação
- [ ] O passo a passo cobre pagamento, frete, domínio, páginas e um pedido de teste
- [ ] Mensalidade da plataforma e taxas de venda explicadas, no nome do cliente
- [ ] Nada inventado como real: avaliações, números de vendas, selos

## 6. Mensagem de entrega

**[Pacote] · [Nome da loja] · [Plataforma]**
- O que foi entregue: a lista do pacote, marcada
- O que o cliente precisa fazer, em ordem (criar conta, ligar pagamento, importar a planilha...)
- Custos do cliente: plano da plataforma, taxas do meio de pagamento, apps pagos
- Para confirmar com o cliente: preços, pesos, textos que você supôs
- Sugestão de extra, se fizer sentido (cadastro de mais produtos, manutenção mensal). Preços atuais no painel pessoal da Porta Studio: https://claude.ai/artifact/Fk5wzknThSy6KMaQHmdnHg
