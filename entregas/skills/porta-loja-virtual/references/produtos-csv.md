# Planilha de produtos (importação)

A forma mais segura: peça à pessoa para baixar o **modelo oficial** no painel (Shopify: Produtos → Importar → "modelo de CSV"; Nuvemshop: Produtos → Importar e exportar) e use exatamente o cabeçalho desse modelo. Os formatos mudam de tempos em tempos.

## Shopify: colunas que mais importam

| Coluna | O que vai |
|---|---|
| `Handle` | identificador do produto, minúsculo e com hífen (`camiseta-basica-preta`). Igual em todas as linhas do mesmo produto |
| `Title` | nome do produto, só na primeira linha do produto |
| `Body (HTML)` | descrição, com `<p>` e `<ul>` simples |
| `Vendor`, `Type`, `Tags` | marca, tipo e etiquetas para filtros e coleções |
| `Published` / `Status` | `TRUE` / `active` para aparecer na loja |
| `Option1 Name`, `Option1 Value` | ex.: `Tamanho` / `M`. Até 3 opções (`Option2`, `Option3`) |
| `Variant SKU` | código único da variação |
| `Variant Price`, `Variant Compare At Price` | preço e preço "de" (só se o desconto for real) |
| `Variant Inventory Qty` | estoque |
| `Variant Grams` ou peso + `Variant Weight Unit` | peso para o frete |
| `Variant Requires Shipping` | `TRUE` para produto físico |
| `Image Src`, `Image Position`, `Image Alt Text` | foto (URL pública), ordem e texto alternativo |
| `SEO Title`, `SEO Description` | título e descrição para o Google |

Regras:
- **Uma linha por variação.** A primeira linha do produto tem título, descrição e a primeira variação; as seguintes repetem só o `Handle` e preenchem as colunas da variação
- **Fotos extras**: linhas com o mesmo `Handle`, só `Image Src` e `Image Position`
- **Imagens precisam de URL pública.** Se as fotos estão no computador do cliente, importe sem foto e suba as imagens pelo painel, ou hospede antes e use as URLs
- Preço com ponto decimal (`49.90`), sem `R$`
- Salve em UTF-8, para os acentos não quebrarem

## Conferência

Antes de entregar, rode uma checagem (Python ou planilha):
- número de produtos dentro do limite do pacote (Start 30, Pro 150)
- nenhum `Handle` repetido para produtos diferentes
- todos os preços maiores que zero e todos os pesos preenchidos
- toda variação com SKU único
