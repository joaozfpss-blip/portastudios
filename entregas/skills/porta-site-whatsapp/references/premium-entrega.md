# Entrega do Premium: Google Meu Negócio e domínio

Estes dois itens acontecem fora do código. Você prepara o material e o passo a passo; quem clica é o dono do negócio, ou a Porta Studio com o acesso dele.

## Google Meu Negócio (Perfil da Empresa no Google)

Entregue pronto para copiar:
- **Nome** exatamente como na fachada (sem palavras extras, o Google pune isso)
- **Categoria principal** e até 3 secundárias (ex.: "Hamburgueria"; secundárias "Restaurante fast-food", "Entrega de comida")
- **Descrição** de até 750 caracteres, na voz do negócio, com bairro e cidade
- **Horários**, telefone, site (o link novo) e endereço ou área de atendimento
- **Serviços ou produtos** com preço, iguais aos do site
- **10 fotos** sugeridas: fachada, interior, equipe, 5 produtos ou serviços, logo, capa
- **3 primeiras postagens** curtas (novidade, oferta, evento)

Passo a passo para o dono:
1. Entrar em https://business.google.com com a conta Google do negócio
2. "Adicionar empresa", preencher nome, categoria e endereço
3. Fazer a verificação que o Google pedir (vídeo, telefone ou carta)
4. Colar a descrição, os horários, os serviços e subir as fotos
5. Pedir avaliações aos clientes com o link "Pedir avaliações" do próprio perfil

Não escreva avaliações, nem sugira trocar avaliações por desconto: é contra as regras do Google.

## Domínio próprio (Registro.br para a Netlify)

1. O cliente registra `seunegocio.com.br` em https://registro.br, no CPF ou CNPJ dele (cerca de R$ 40 por ano)
2. Na Netlify, no site publicado: **Domain management → Add a domain** → digitar o domínio
3. A Netlify mostra os registros de DNS a criar. Use **exatamente os valores que ela mostrar**
4. No Registro.br: domínio → **DNS → Editar zona** (ou "Configurar endereçamento") e criar os registros que a Netlify pediu (normalmente um registro A para o domínio sem www e um CNAME para o www)
5. Esperar a propagação (de minutos a algumas horas). A Netlify ativa o HTTPS sozinha
6. Testar `seunegocio.com.br` e `www.seunegocio.com.br` no celular, fora do Wi-Fi

Depois que o domínio estiver no ar, atualize no site: `og:url`, o link do Google Meu Negócio e o `url` do JSON-LD.

## 30 dias de ajustes

Na mensagem de entrega, escreva a data de fim: "Ajustes inclusos até dd/mm". Ajustes são mudanças no que já existe (texto, foto, preço, cor). Página ou recurso novo é extra.
