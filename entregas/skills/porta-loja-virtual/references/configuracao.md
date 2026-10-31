# Passo a passo de configuração

Escreva o `configuracao.md` do cliente a partir deste roteiro, na ordem. Os nomes dos menus mudam com o tempo: escreva o caminho mais provável e avise que o botão pode ter outro nome.

## Shopify

### Antes do cliente pagar: loja de desenvolvimento
A Porta Studio pode ter uma conta de **Parceiro Shopify** (gratuita, em shopify.com/partners) e montar a loja numa loja de desenvolvimento, sem mensalidade. No fim, transfere a propriedade para o cliente, que escolhe o plano e paga direto à Shopify. Confira as condições atuais do programa antes de prometer ao cliente.

### Ordem de configuração
1. **Dados da loja**: Configurações → Detalhes da loja: nome, e-mail, endereço, moeda BRL, fuso de Brasília
2. **Tema**: Loja virtual → Temas → tema gratuito (Dawn ou o padrão atual) → Personalizar: cores, fontes, logo, banner, textos (valores do `identidade.md`)
3. **Produtos**: Produtos → Importar → enviar o `produtos.csv`. Conferir 3 produtos ao acaso depois da importação
4. **Pagamentos**: Configurações → Pagamentos. O Shopify Payments não funciona no Brasil; ligar um provedor que funcione aqui (ex.: Mercado Pago ou Pagar.me) com Pix, cartão e boleto. O cliente cria a conta no provedor no nome dele
5. **Frete**: Configurações → Frete e entrega: CEP de origem, pesos, e um app de frete com Correios e transportadoras (busque na Shopify App Store por apps brasileiros, como Melhor Envio ou Frenet). Retirada no local, se houver. Pro: regra de frete grátis acima de um valor
6. **Páginas e políticas**: Loja virtual → Páginas (sobre, contato) e Configurações → Políticas (trocas, privacidade, termos). Colar os textos de `paginas/`
7. **Menus**: Loja virtual → Navegação: menu principal e rodapé
8. **Domínio**: Configurações → Domínios → conectar domínio existente. No Registro.br, criar os registros de DNS que a Shopify mostrar
9. **Pro: cupons** em Descontos; **carrinho abandonado** em Marketing → Automações (ou Configurações → Notificações), com o texto da marca; **Instagram/Facebook e Google** pelos apps oficiais de canal de vendas
10. **Pro e Sob Medida: seções do tema**: Loja virtual → Temas → ⋯ → Editar código → `sections/` → adicionar as seções `.liquid` da pasta `tema/` e depois colocá-las na página pelo Personalizar
11. **Pedido de teste**: fazer uma compra real de valor baixo com Pix, conferir o e-mail de confirmação e o pedido no painel, e reembolsar
12. **Transferir a loja** para o cliente (se foi feita como loja de desenvolvimento) e ele escolhe o plano

## Nuvemshop

Mesma ordem, com estas diferenças:
- O plano é cobrado em reais e há opção para começar com custo baixo; confira os planos atuais no site da Nuvemshop
- Pagamento e frete têm soluções da própria Nuvemshop (Pix, cartão, boleto; envio com Correios e transportadoras), além de apps
- Produtos: Produtos → Importar e exportar → planilha no modelo da Nuvemshop (baixe o modelo no próprio painel; as colunas são diferentes das da Shopify)
- Personalização do layout: pelo editor de layout; a edição de código (HTML/CSS) depende do plano. No Pro e no Sob Medida, confira isso antes de prometer animações próprias

## Roteiro do vídeo (Start em diante)

Um vídeo de tela de 5 a 8 minutos, gravado pela pessoa, nesta ordem:
1. Onde ver os pedidos novos e como saber se o pagamento caiu
2. Como marcar o pedido como enviado e colocar o código de rastreio
3. Como cadastrar um produto novo e mudar preço e estoque
4. Como criar um cupom
5. Onde ficam as vendas do mês
