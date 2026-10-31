#!/usr/bin/env python3
"""Gera o HTML do catálogo de preços da Porta Studio (6 slides 1080x1350)."""
import html, sys

FONT = open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'geist.css')).read()
ZAP = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="' + open('/tmp/cat/zap.txt').read() + '"/></svg>'
DOOR = '<svg class="logo__ic" viewBox="0 0 20 25" aria-hidden="true"><path d="M1 25V10a9 9 0 0 1 18 0v15z" fill="#1F3F8C"/><circle cx="13.6" cy="15.6" r="1.6" fill="#D89A2A"/></svg>'
WHATS = '(62) 99151-7901'
TOTAL = 6

e = html.escape


def top(n):
    return (f'<div class="top"><span class="logo">{DOOR}Porta Studio</span>'
            f'<span class="pg">{n:02d} / {TOTAL:02d}</span></div>')


def foot(note='', zap=True):
    n = f'<p class="note">{note}</p>' if note else '<span></span>'
    z = f'<span class="zap">{ZAP}{WHATS}</span>' if zap else '<span class="zap zap--muted">Goiânia, GO</span>'
    return f'<div class="foot">{n}{z}</div>'


def plan_card(p):
    cls = 'card card--hi' if p.get('hi') else 'card'
    tag = '<span class="tag">Mais escolhido</span>' if p.get('hi') else ''
    pre = f'<small>{e(p["pre"])}</small>' if p.get('pre') else ''
    items = ''.join(f'<li>{e(i)}</li>' for i in p['items'])
    return f'''
    <article class="{cls}">
      <div class="card__head">
        <div>
          <h3>{e(p["name"])}{tag}</h3>
          <p class="card__desc">{e(p["desc"])}</p>
        </div>
        <div class="price">{pre}<b>{e(p["price"])}</b><span class="card__prazo">Prazo: {e(p["sub"])}</span></div>
      </div>
      <ul class="feats">{items}</ul>
    </article>'''


def category(n, meta, title, lead, plans, note):
    cards = ''.join(plan_card(p) for p in plans)
    return f'''
<section class="slide">
  {top(n)}
  <header class="head">
    <p class="meta">{e(meta)}</p>
    <h2>{title}</h2>
    <p class="lead">{e(lead)}</p>
  </header>
  <div class="cards">{cards}</div>
  {foot(e(note))}
</section>'''


# ---------------------------------------------------------------- conteúdo
SITES = [
    dict(name='Essencial', desc='Uma página para apresentar o negócio',
         price='R$ 700', sub='até 7 dias',
         items=['Página única com até 6 seções', 'Versão para celular e computador',
                'Botão de WhatsApp sempre à vista', 'Publicado, com link para divulgar']),
    dict(name='Completo', desc='Cardápio ou serviços com pedido pronto', hi=True,
         price='R$ 1.200', sub='até 12 dias',
         items=['Tudo do Essencial', 'Cardápio ou serviços com valores',
                'Pedido ou agenda montados no site', 'Animação de rolagem exclusiva',
                'Galeria, mapa e horários', 'Aparece no Google da sua região']),
    dict(name='Premium', desc='Interativo, com mais páginas',
         price='R$ 1.900', sub='até 20 dias',
         items=['Tudo do Completo', 'Até 4 páginas',
                'Calculadora ou simulador interativo', 'Google Meu Negócio configurado',
                'Domínio próprio configurado', '30 dias de ajustes após a entrega']),
]
LOJAS = [
    dict(name='Loja Start', desc='Para começar a vender online',
         price='R$ 2.500', sub='até 15 dias',
         items=['Até 30 produtos cadastrados', 'Tema ajustado à sua marca',
                'Pix, cartão e boleto', 'Frete calculado no carrinho',
                'Domínio configurado', 'Vídeo ensinando a usar a loja']),
    dict(name='Loja Pro', desc='Para quem já vende e quer crescer', hi=True,
         price='R$ 4.500', sub='até 25 dias',
         items=['Até 150 produtos com variações', 'Layout personalizado com animações',
                'Cupons e frete grátis por valor', 'Vitrine no Instagram e no Google',
                'Recuperação de carrinho abandonado', 'WhatsApp dentro da loja']),
    dict(name='Loja Sob Medida', desc='Design exclusivo e integrações',
         pre='a partir de', price='R$ 7.500', sub='definido na proposta',
         items=['Design 100% exclusivo', 'Produtos ilimitados',
                'Migração de outra plataforma', 'Integração com ERP e marketplaces']),
]
SAAS = [
    dict(name='Sistema MVP', desc='Primeira versão, com até 6 telas',
         pre='a partir de', price='R$ 6.000', sub='3 a 5 semanas',
         items=['Login e cadastro de usuários', 'Painel administrativo',
                'Um fluxo principal: agenda, pedidos…',
                'Funciona no celular e no computador']),
    dict(name='SaaS Completo', desc='Pronto para vender por assinatura', hi=True,
         pre='a partir de', price='R$ 15.000', sub='6 a 10 semanas',
         items=['Várias empresas na mesma plataforma', 'Assinatura com cobrança recorrente',
                'Níveis de acesso por usuário', 'Relatórios e painel de métricas',
                'E-mails e avisos automáticos', 'Tudo do Sistema MVP']),
    dict(name='Plataforma + IA', desc='Inteligência artificial e integrações',
         pre='a partir de', price='R$ 25.000', sub='definido na proposta',
         items=['Atendimento ou assistente com IA', 'Integração com APIs e outros sistemas',
                'App instalável no celular', 'Escopo fechado em proposta']),
]
EXTRAS = [
    ('Domínio próprio', 'seunegocio.com.br, registrado no Registro.br', 'R$ 40', '/ano'),
    ('Página extra', 'Em qualquer site', 'R$ 250', ''),
    ('Animação exclusiva extra', 'Uma nova cena que reage à rolagem', 'R$ 350', ''),
    ('Cadastro de produtos', 'Cada lote de 50 produtos na loja', 'R$ 150', ''),
    ('Google Meu Negócio', 'Criação e ajuste do perfil no Google', 'R$ 150', ''),
    ('Imagens e vídeos com IA', 'Pacote de cenas para o site', 'R$ 250', ''),
    ('Ajuste avulso', 'Troca de preço, foto ou horário', 'R$ 50', ''),
    ('Plano de ajustes do site', 'Até 4 alterações por mês', 'R$ 90', '/mês'),
    ('Manutenção da loja', 'Banners, cadastros e suporte', 'R$ 300', '/mês'),
    ('Hospedagem e suporte de sistemas', 'Servidor, backups e correções, a partir de', 'R$ 400', '/mês'),
]
PAGTO = [
    ('Sites com WhatsApp', 'Metade para começar, metade na entrega'),
    ('Lojas virtuais', 'Metade para começar, metade na entrega'),
    ('SaaS e sistemas', '30% para começar, 40% na primeira versão e 30% na entrega'),
    ('Cartão de crédito', 'Em até 10x, com a taxa da maquininha'),
]
PASSOS = [
    ('Conversa', 'Você conta sobre o negócio e manda fotos e serviços.'),
    ('Prévia', 'Você recebe um link com a primeira versão para ver no celular.'),
    ('Ajustes', 'Você aponta o que quer mudar antes da entrega.'),
    ('No ar', 'Com a segunda parte paga, o site é publicado.'),
]


def cover():
    rows = [('01', 'Sites com pedido no WhatsApp', 'R$ 700'),
            ('02', 'Lojas virtuais', 'R$ 2.500'),
            ('03', 'SaaS e sistemas', 'R$ 6.000')]
    lis = ''.join(f'<li><span class="idx">{i}</span><span class="nm">{e(n)}</span>'
                  f'<span class="fr"><small>a partir de</small>{e(p)}</span></li>' for i, n, p in rows)
    return f'''
<section class="slide cover">
  {top(1)}
  <div class="cover__hero">
    <div class="cover__txt">
      <p class="meta">Tabela de serviços · novembro de 2026</p>
      <h1>Quanto custa o seu site.</h1>
      <p class="lead">Do site com pedido no WhatsApp à loja virtual e ao sistema próprio. O valor fica fechado antes de começar.</p>
    </div>
    <div class="door" aria-hidden="true"><i></i></div>
  </div>
  <ol class="cover__list">{lis}</ol>
  {foot('Feito primeiro para o celular. Goiânia, GO.')}
</section>'''


def extras():
    rows = ''.join(f'<li><div><b>{e(a)}</b><span>{e(b)}</span></div>'
                   f'<p class="v">{e(c)}' + (f'<small>{e(d)}</small>' if d else '') + '</p></li>' for a, b, c, d in EXTRAS)
    return f'''
<section class="slide">
  {top(5)}
  <header class="head">
    <p class="meta">04 · Avulsos</p>
    <h2>Extras e manutenção</h2>
    <p class="lead">Para somar a qualquer pacote ou contratar depois da entrega.</p>
  </header>
  <ul class="table">{rows}</ul>
  {foot('O domínio é repassado pelo valor do Registro.br, sem taxa.')}
</section>'''


def pagamento():
    rows = ''.join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in PAGTO)
    steps = ''.join(f'<li><span class="n">{i+1}</span><b>{e(a)}</b><p>{e(b)}</p></li>'
                    for i, (a, b) in enumerate(PASSOS))
    return f'''
<section class="slide">
  {top(6)}
  <header class="head">
    <p class="meta">05 · Pagamento e etapas</p>
    <h2>Como você paga</h2>
  </header>
  <dl class="cond">{rows}</dl>
  <ol class="steps">{steps}</ol>
  <div class="cta">
    <div>
      <p class="cta__k">Orçamento pelo WhatsApp, sem reunião</p>
      <p class="cta__n">{WHATS}</p>
    </div>
    <span class="cta__ic">{ZAP}</span>
  </div>
  {foot('Valores de novembro de 2026. O preço final depende do escopo e fica combinado antes de começar.', zap=False)}
</section>'''


CSS = r'''
:root{--bg:#F4F4F1;--surface:#FFFFFF;--surface-2:#ECECE7;--line:#DDDCD5;--text:#17181C;--text-2:#5B5E66;
--primary:#1F3F8C;--primary-2:#183372;--accent:#D89A2A;--r:28px}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#cfcfca}
body{font-family:Geist,system-ui,sans-serif;color:var(--text);-webkit-font-smoothing:antialiased;
  font-feature-settings:"ss01","tnum" 0}
ul,ol{list-style:none}
.slide{width:1080px;height:1350px;background:var(--bg);position:relative;overflow:hidden;
  padding:64px 72px 56px;display:flex;flex-direction:column;margin:0 auto 40px}
.top{display:flex;justify-content:space-between;align-items:center}
.logo{display:inline-flex;align-items:center;gap:12px;font-weight:600;font-size:26px;letter-spacing:-.015em}
.logo__ic{width:22px;height:28px}
.pg{font-size:20px;color:var(--text-2);font-weight:500;letter-spacing:.02em}
.meta{display:inline-flex;align-items:center;gap:12px;font-size:21px;font-weight:500;color:var(--text-2);letter-spacing:.005em}
.meta::before{content:"";width:9px;height:9px;border-radius:3px;background:var(--accent);flex:none}
.head{margin-top:44px}
h2{font-size:64px;line-height:1.02;font-weight:500;letter-spacing:-.035em;margin-top:18px}
.lead{font-size:24px;line-height:1.4;color:var(--text-2);margin-top:14px;max-width:38em}
.foot{margin-top:auto;padding-top:22px;display:flex;justify-content:space-between;align-items:center;gap:24px;
  border-top:1px solid var(--line)}
.note{font-size:18px;line-height:1.4;color:var(--text-2)}
.zap{display:inline-flex;align-items:center;gap:10px;font-size:21px;font-weight:600;white-space:nowrap;color:var(--primary)}
.zap svg{width:24px;height:24px}
.zap--muted{color:var(--text-2);font-weight:500;font-size:18px}

/* cards de plano */
.cards{display:flex;flex-direction:column;gap:18px;margin-top:34px}
.card{background:var(--surface);border-radius:var(--r);padding:26px 32px 28px;
  box-shadow:0 1px 2px rgba(23,24,28,.06),0 12px 32px rgba(23,24,28,.06)}
.card__head{display:flex;justify-content:space-between;align-items:flex-start;gap:24px}
.card h3{font-size:32px;font-weight:600;letter-spacing:-.02em;display:flex;align-items:center;gap:14px}
.card__desc{font-size:21px;color:var(--text-2);margin-top:4px}
.card__prazo{display:table;margin-left:auto;font-size:16px;font-weight:600;letter-spacing:.01em;margin-top:10px;padding:5px 11px;border-radius:999px;background:var(--surface-2);color:var(--text-2)}
.card--hi .card__prazo{background:rgba(255,255,255,.12);color:rgba(255,255,255,.85)}
.tag{font-size:15px;font-weight:600;letter-spacing:.02em;background:var(--accent);color:#17181C;
  padding:6px 12px;border-radius:999px}
.price{text-align:right;flex:none}
.price small{font-size:17px;color:var(--text-2);font-weight:500;margin-right:10px}
.price b{display:inline-block;font-size:56px;line-height:1;font-weight:500;letter-spacing:-.045em}
.feats{display:grid;grid-template-columns:1fr 1fr;column-gap:28px;row-gap:8px;margin-top:18px;
  padding-top:16px;border-top:1px solid var(--line)}
.feats li{font-size:21px;line-height:1.3;padding-left:22px;position:relative}
.feats li::before{content:"";position:absolute;left:0;top:.48em;width:8px;height:8px;border-radius:2px;background:var(--accent)}
.card--hi{background:var(--primary);color:#fff;box-shadow:0 40px 80px -30px rgba(31,63,140,.55)}
.card--hi .card__desc,.card--hi .price small{color:rgba(255,255,255,.72)}
.card--hi .feats{border-top-color:rgba(255,255,255,.18)}

/* capa */
.cover__hero{display:grid;grid-template-columns:1fr 300px;gap:40px;margin-top:96px;align-items:end}
.cover h1{font-size:112px;line-height:.94;font-weight:500;letter-spacing:-.055em;margin-top:26px}
.cover .lead{font-size:27px;margin-top:30px}
.door{height:500px;background:var(--primary);border-radius:150px 150px 0 0;position:relative;
  box-shadow:0 40px 80px -30px rgba(31,63,140,.55)}
.door::before{content:"";position:absolute;inset:22px 22px 0;border-radius:128px 128px 0 0;
  border:2px solid rgba(255,255,255,.16);border-bottom:0}
.door i{position:absolute;right:52px;top:56%;width:22px;height:22px;border-radius:50%;background:var(--accent)}
.cover__list{margin-top:80px;border-top:1px solid var(--line)}
.cover__list li{display:grid;grid-template-columns:64px 1fr auto;align-items:baseline;gap:8px;
  padding:30px 0;border-bottom:1px solid var(--line)}
.idx{font-size:21px;color:var(--text-2);font-weight:500}
.nm{font-size:34px;font-weight:500;letter-spacing:-.02em}
.fr{font-size:40px;font-weight:500;letter-spacing:-.035em;text-align:right;color:var(--primary)}
.fr small{font-size:18px;color:var(--text-2);letter-spacing:0;margin-right:12px;font-weight:500}

/* extras */
.table{margin-top:28px;border-top:1px solid var(--line)}
.table li{display:flex;justify-content:space-between;align-items:center;gap:24px;padding:15px 0;border-bottom:1px solid var(--line)}
.table b{display:block;font-size:25px;font-weight:600;letter-spacing:-.015em}
.table span{display:block;font-size:18px;color:var(--text-2);margin-top:2px}
.table .v{font-size:34px;font-weight:500;letter-spacing:-.035em;white-space:nowrap}
.table .v small{font-size:19px;color:var(--text-2);letter-spacing:0;margin-left:4px}

/* pagamento */
.cond{margin-top:34px;display:grid;grid-template-columns:1fr 1fr;column-gap:36px;border-top:1px solid var(--line)}
.cond div{padding:20px 0;border-bottom:1px solid var(--line)}
.cond dt{font-size:19px;font-weight:500;color:var(--text-2)}
.cond dd{font-size:24px;line-height:1.3;font-weight:500;letter-spacing:-.01em;margin-top:6px}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:52px}
.steps li{background:var(--surface);border-radius:22px;padding:24px 22px 26px;
  box-shadow:0 1px 2px rgba(23,24,28,.06),0 12px 32px rgba(23,24,28,.06)}
.steps .n{display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:var(--surface-2);
  font-size:19px;font-weight:600;color:var(--primary)}
.steps b{display:block;font-size:24px;font-weight:600;margin-top:18px;letter-spacing:-.015em}
.steps p{font-size:18px;line-height:1.4;color:var(--text-2);margin-top:6px}
.cta{margin-top:52px;background:var(--primary);color:#fff;border-radius:var(--r);padding:36px 40px;
  display:flex;justify-content:space-between;align-items:center;box-shadow:0 40px 80px -30px rgba(31,63,140,.55)}
.cta__k{font-size:22px;color:rgba(255,255,255,.75);font-weight:500}
.cta__n{font-size:60px;font-weight:500;letter-spacing:-.04em;margin-top:6px}
.cta__ic{width:92px;height:92px;border-radius:50%;background:var(--accent);display:grid;place-items:center;color:#17181C}
.cta__ic svg{width:48px;height:48px}
'''

body = (cover()
        + category(2, '01 · Pagamento único, sem mensalidade', 'Sites com pedido no WhatsApp',
                   'O cliente escolhe no site e o pedido chega pronto no seu WhatsApp.', SITES,
                   'Para restaurantes, salões, clínicas, pet shops, confeitarias e estúdios.')
        + category(3, '02 · Venda direto no site', 'Lojas virtuais',
                   'Na Shopify ou na Nuvemshop, com pagamento e frete automáticos.', LOJAS,
                   'A mensalidade da plataforma e as taxas de venda ficam com o cliente.')
        + category(4, '03 · Sistemas na web', 'SaaS e sistemas',
                   'Para vender software por assinatura ou organizar o seu negócio.', SAAS,
                   'Hospedagem e suporte a partir de R$ 400/mês, conforme o uso.')
        + extras() + pagamento())

out = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Porta Studio · Tabela de serviços</title>
<style>{FONT}{CSS}</style></head><body>{body}</body></html>'''
open(sys.argv[1] if len(sys.argv) > 1 else 'catalogo.html', 'w').write(out)
print('ok')
