# Pedido e agendamento pelo WhatsApp

Pacotes Completo e Premium. O cliente monta tudo no site e o botão final abre o WhatsApp do negócio com a mensagem já escrita. Não há servidor nem pagamento no site: o pedido é fechado na conversa.

## Dados num lugar só

Deixe no topo do script tudo que o dono vai querer trocar:

```js
const NEGOCIO = {
  nome: 'Pizzaria Forno Velho',
  whatsapp: '5562999999999',          // 55 + DDD + número, só dígitos
  taxaEntrega: 6,                     // 0 se não tiver
  pedidoMinimo: 30,
  horarios: { 2:['18:00','23:00'], 3:['18:00','23:00'] /* 0 = domingo */ },
};
const CARDAPIO = [
  { id:'marg', cat:'Pizzas', nome:'Margherita', desc:'Molho de tomate, muçarela, manjericão', preco:49.9 },
  { id:'calab', cat:'Pizzas', nome:'Calabresa', desc:'...', preco:52.9, opcoes:['Média','Grande'] },
];
```

## Montar a comanda

- Cada item tem botões de `−` e `+` (ou "Adicionar"), com área de toque de pelo menos 44px
- Um resumo fixo no rodapé do celular mostra a quantidade de itens e o total, e abre a sacola
- A sacola pede: nome, entrega ou retirada, endereço (se entrega), forma de pagamento (Pix, cartão na entrega, dinheiro com troco) e observação
- Guarde a sacola no `localStorage` dentro de `try/catch`, para não perder se a pessoa sair e voltar

## Mensagem gerada

Monte um texto curto e legível, com quebras de linha, e abra o WhatsApp:

```js
const brl = v => v.toLocaleString('pt-BR', { style:'currency', currency:'BRL' });
function mensagem(sacola, dados) {
  const linhas = sacola.map(i => `• ${i.qtd}x ${i.nome}${i.opcao ? ' (' + i.opcao + ')' : ''} — ${brl(i.qtd * i.preco)}`);
  const sub = sacola.reduce((a, i) => a + i.qtd * i.preco, 0);
  const taxa = dados.entrega ? NEGOCIO.taxaEntrega : 0;
  return [
    `Olá! Quero fazer um pedido pelo site:`, '',
    ...linhas, '',
    `Subtotal: ${brl(sub)}`,
    taxa ? `Entrega: ${brl(taxa)}` : 'Retirada no local',
    `*Total: ${brl(sub + taxa)}*`, '',
    `Nome: ${dados.nome}`,
    dados.entrega ? `Endereço: ${dados.endereco}` : null,
    `Pagamento: ${dados.pagamento}`,
    dados.obs ? `Obs.: ${dados.obs}` : null,
  ].filter(l => l !== null).join('\n');
}
const abrir = txt => `https://wa.me/${NEGOCIO.whatsapp}?text=${encodeURIComponent(txt)}`;
```

Use um `<a href>` com o link pronto (atualizado a cada mudança da sacola) em vez de `window.open`, que alguns celulares bloqueiam.

## Agendamento (salão, clínica, estúdio, pet shop)

Mesma ideia, trocando itens por serviço:
1. Escolher o serviço (com preço e duração)
2. Escolher o dia (próximos 14 dias, sem os dias fechados) e um horário dentro do expediente, em intervalos de 30 min
3. Nome e observação (no pet shop: nome e porte do pet)
4. Mensagem: "Olá! Quero agendar: [serviço] · [dia da semana, dd/mm] às [hh:mm] · Nome: ..." e a frase "Pode confirmar se esse horário está livre?"

O site não sabe quais horários estão ocupados. Deixe isso claro no texto ("o horário é confirmado pelo WhatsApp").

## Aberto ou fechado agora

Calcule no fuso de Brasília, mesmo que a pessoa esteja em outro fuso:

```js
const agora = new Date(new Date().toLocaleString('en-US', { timeZone: 'America/Sao_Paulo' }));
```

Mostre "Aberto agora, até 23h" ou "Fechado · abre terça às 18h". Fora do horário, o pedido ainda pode ser enviado, com o aviso de que será respondido quando abrir.
