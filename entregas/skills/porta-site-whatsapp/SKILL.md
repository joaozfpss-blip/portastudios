---
name: porta-site-whatsapp
description: "Monta os sites com pedido no WhatsApp da Porta Studio nos pacotes Essencial, Completo e Premium, cada um com a lista exata do que o pacote inclui. Use sempre que o pedido for um site Essencial, Completo ou Premium, um site com cardápio, agendamento ou pedido pelo WhatsApp, ou um site para um estabelecimento (restaurante, hamburgueria, salão, clínica, pet shop, confeitaria, estúdio, barbearia etc.), mesmo que o pacote não seja dito. Funciona junto com a skill porta-studio-sites, que cuida do conceito visual."
---

# Sites com pedido no WhatsApp (Essencial, Completo, Premium)

Esta skill decide **o que entra** no site de acordo com o pacote vendido. O conceito visual, a estética e as animações seguem a skill `porta-studio-sites` (leia-a também, se estiver disponível). As duas juntas: o pacote define o escopo, a outra define a cara.

O escopo importa porque é o que o cliente comprou. Entregar menos quebra a promessa; entregar muito mais de graça (páginas extras, calculadora num Essencial) desvaloriza os pacotes de cima. Quando o cliente precisar de algo de outro pacote, sugira o pacote acima ou um extra, sem construir por conta própria.

## 1. Descobrir o pacote

Procure no pedido: "essencial", "completo", "premium". Se não vier dito, deduza e diga em uma linha qual vai usar:
- Só apresentar o negócio e levar para o WhatsApp → **Essencial**
- Cardápio, lista de serviços com preço, montar pedido ou agendar → **Completo**
- Várias páginas, calculadora, simulador, "monte sua caixa", Google Meu Negócio, domínio → **Premium**

## 2. Juntar as informações

Use o que veio no pedido. Se faltar algo essencial, pergunte **numa mensagem só**, com a lista do que falta:
- Nome do negócio, ramo, cidade e bairro
- WhatsApp do cliente (com DDD). Em demo, o WhatsApp é o da Porta Studio (veja `porta-studio-sites`)
- Serviços ou cardápio, com preços (Completo e Premium)
- Endereço, horários, Instagram
- Fotos e logo (se não houver, use imagens neutras e diga isso na entrega)

Se a pessoa mandar só "faz um site Completo para a Pizzaria X", sem dados, e não for demo, pergunte antes de construir: um site de cliente com preço inventado não serve. Texto de apresentação e descrições você pode escrever, e na entrega marque como "confirmar com o cliente".

## 3. O que cada pacote inclui (lista de entrega)

Cada item abaixo precisa estar no site entregue. Prazo de referência entre parênteses.

### Essencial (até 7 dias)
- **1 página com até 6 seções.** Sugestão: abertura, sobre, serviços ou destaques (sem carrinho), galeria ou diferenciais, localização e horário, chamada final. Conte as seções: são no máximo 6, sem contar o rodapé
- **Celular e computador.** Feito primeiro para ~390px, depois ajustado para telas largas
- **Botão de WhatsApp sempre à vista** (fixo no canto) e chamadas com mensagem pronta: `https://wa.me/55DDDNUMERO?text=...` com `encodeURIComponent`
- **Publicado com link** (veja a seção 5)
- Animações de entrada leves, no estilo do conceito. A animação de rolagem exclusiva é do Completo
- Básico de SEO: `<title>` com nome, ramo e cidade, meta description, Open Graph com `og.jpg` 1200×630

### Completo (até 12 dias): tudo do Essencial, mais
- **Cardápio ou serviços com valores**, montados a partir de uma lista de dados no script (fácil de atualizar preço depois)
- **Pedido ou agendamento montado no site e enviado no WhatsApp.** O cliente escolhe itens e quantidades (ou serviço, dia e horário), vê o total e o botão abre o WhatsApp com a comanda pronta. Padrão em `references/pedido-whatsapp.md`
- **Animação de rolagem exclusiva**: o momento assinatura do conceito (GSAP + ScrollTrigger), com versão calma para `prefers-reduced-motion`
- **Galeria, mapa e horários.** Mapa com link para o Google Maps (iframe de incorporação do Google Maps ou link "Como chegar"); horário com aviso de aberto/fechado no fuso de Brasília
- **Aparece no Google da região**: dados estruturados `LocalBusiness` (ou o tipo certo: `Restaurant`, `BeautySalon`, `Dentist`...) em JSON-LD com nome, endereço, telefone, horário e geo; título e descrição com bairro e cidade
- O número de seções pode passar de 6, mas continua sendo **uma página**

### Premium (até 20 dias): tudo do Completo, mais
- **Até 4 páginas** (ex.: início, cardápio ou serviços, sobre, contato). Cada página é um HTML com o mesmo menu, rodapé e conceito
- **Um recurso interativo** que faça sentido para o ramo: calculadora (docinhos por convidado, área do serviço), simulador (planos, orçamento) ou "monte sua caixa/kit". O resultado também vai para o WhatsApp
- **Google Meu Negócio configurado**: entregue o texto do perfil e o passo a passo em `references/premium-entrega.md`. A criação no Google é feita pelo dono ou pela Porta Studio com acesso dele
- **Domínio próprio configurado** (seunegocio.com.br): passo a passo do Registro.br para a Netlify no mesmo arquivo. O domínio é pago pelo cliente (cerca de R$ 40 por ano)
- **30 dias de ajustes após a entrega**: escreva isso na mensagem de entrega, com a data final

## 4. Como construir

1. **Conceito primeiro.** Siga `porta-studio-sites`: metáfora central, momento assinatura, estética própria, sem repetir os outros sites da Porta Studio
2. **Estrutura de arquivos** (igual aos modelos do repositório `portastudios`):
   ```
   clientes/<nome-do-negocio>/
     index.html        (e as outras páginas, no Premium)
     img/              (fotos otimizadas, .jpg ou .webp)
     favicon.svg
     og.jpg            (1200×630, prévia do link no WhatsApp)
   ```
   Em demo, use a pasta do ramo na raiz, como `hamburgueria/`. Fora do repositório (no chat do Claude), entregue um HTML autocontido
3. **Um HTML por página**, com CSS e JS no próprio arquivo. Bibliotecas só do cdnjs (GSAP 3.12.5 e ScrollTrigger, como nos modelos). Fontes do Google Fonts
4. **Dados num lugar só**: WhatsApp, horários, endereço e cardápio ficam num objeto no topo do script, para trocar rápido quando o cliente pedir ajuste
5. Enquanto for prévia, use `<meta name="robots" content="noindex">`. Tire na entrega final

## 5. Publicar com link

- **No Claude Code, com o repositório `portastudios`**: crie os arquivos em `clientes/<nome>/`, faça commit num branch `cliente/<nome>` e envie (push). Não junte no `main` sem a pessoa pedir: o `main` vai direto para o site público da Porta Studio
- **Link do cliente**: o jeito mais simples é a Netlify Drop. A pessoa entra em https://app.netlify.com/drop, arrasta a pasta do site e recebe um link `.netlify.app` na hora. Depois dá para renomear o site e ligar o domínio. Explique esse passo na entrega; você não tem acesso à conta Netlify dela
- **No chat do Claude** (sem repositório): entregue o HTML pronto e o mesmo passo da Netlify Drop

## 6. Conferir antes de entregar

Se houver navegador (Playwright), abra o site em 390px e em 1280px, tire um print de cada e olhe: textos cortados, sobreposição, animação travada, erros no console. Teste o botão de WhatsApp e, no Completo e no Premium, monte um pedido de teste e confira a mensagem gerada.

Lista final:
- [ ] Todos os itens do pacote estão no site, e nada de pacote acima foi dado de graça
- [ ] Número de WhatsApp certo (cliente x demo) e mensagem pronta funcionando
- [ ] Preços e dados são os do cliente; o que foi escrito por você está marcado para confirmar
- [ ] Celular e computador sem nada quebrado
- [ ] SEO e `og.jpg` prontos; `noindex` só na prévia

## 7. Mensagem de entrega

Responda curto, neste formato:

**Site [Pacote] · [Nome do negócio]**
- Conceito: uma frase
- O que foi entregue: a lista do pacote, marcada
- Link ou próximo passo para publicar
- Para confirmar com o cliente: textos, preços ou fotos que você supôs
- Sugestão de extra, se fizer sentido (ex.: página extra, Google Meu Negócio, plano de ajustes). Os preços atuais estão no painel pessoal da Porta Studio: https://claude.ai/artifact/Fk5wzknThSy6KMaQHmdnHg
