# Stack e padrões de código

Padrão da Porta Studio, escolhido para dar para manter sozinho e com custo baixo no começo. Confira as versões atuais das bibliotecas ao criar o projeto e fixe as versões no `package.json`.

## Base

- **Next.js** (App Router, TypeScript) + **Tailwind**
- **Supabase**: login (e-mail e senha, link mágico), banco Postgres, regras de acesso por linha (RLS), armazenamento de arquivos
- **Hospedagem**: Vercel ou Netlify, ligada ao repositório do GitHub (cada push no `main` publica)
- **E-mails**: Resend (ou o SMTP configurado no Supabase)
- O plano gratuito de cada serviço costuma bastar no MVP; avise o cliente quando o uso pedir plano pago

Estrutura:
```
app/
  (publico)/login, cadastro, planos
  (app)/painel, [telas do fluxo]
  api/webhooks/[provedor]/route.ts
lib/supabase/ (cliente do navegador e do servidor)
supabase/migrations/*.sql
.env.example
README.md
```

## Banco e regras de acesso

MVP (cada usuário vê o que é dele):
```sql
create table pedidos (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) default auth.uid(),
  cliente text not null,
  total numeric(10,2) not null check (total >= 0),
  status text not null default 'novo',
  criado_em timestamptz not null default now()
);
alter table pedidos enable row level security;
create policy "dono lê"     on pedidos for select using (user_id = auth.uid());
create policy "dono cria"   on pedidos for insert with check (user_id = auth.uid());
create policy "dono altera" on pedidos for update using (user_id = auth.uid());
create policy "dono apaga"  on pedidos for delete using (user_id = auth.uid());
```

SaaS Completo (várias empresas):
```sql
create table empresas (id uuid primary key default gen_random_uuid(), nome text not null,
  plano text not null default 'teste', assinatura_status text not null default 'trial',
  assinatura_ate timestamptz);
create table membros (empresa_id uuid references empresas(id) on delete cascade,
  user_id uuid references auth.users(id) on delete cascade,
  papel text not null check (papel in ('dono','admin','membro')),
  primary key (empresa_id, user_id));

create function public.sou_membro(e uuid) returns boolean language sql stable security definer
  set search_path = public as $$ select exists(select 1 from membros where empresa_id = e and user_id = auth.uid()) $$;

alter table empresas enable row level security;
alter table membros enable row level security;
create policy "vejo minhas empresas" on empresas for select using (public.sou_membro(id));
create policy "vejo meus vínculos" on membros for select using (user_id = auth.uid());

-- toda tabela de dados tem empresa_id e esta política:
create policy "membros da empresa" on pedidos for all
  using (public.sou_membro(empresa_id)) with check (public.sou_membro(empresa_id));
```
Ações de dono e admin (convidar, mudar plano) conferem o `papel` numa função ou rota do servidor. Teste sempre com dois usuários de empresas diferentes.

## Cobrança recorrente (SaaS Completo em diante)

- **No Brasil, com Pix e boleto**: Asaas ou Mercado Pago (assinaturas). **Só cartão**: Stripe também serve. Confira taxas e se o provedor tem assinatura com Pix antes de escolher
- A conta do provedor é do cliente, no CNPJ dele
- Fluxo: a pessoa escolhe o plano → o servidor cria o cliente e a assinatura no provedor → o provedor avisa por webhook cada pagamento, atraso e cancelamento → o servidor atualiza `assinatura_status` e `assinatura_ate`
- O acesso às telas pagas é decidido no servidor a partir desses campos
- Teste tudo no modo de teste (sandbox) do provedor antes de ligar o modo real

## IA (Plataforma + IA)

- Leia a skill `claude-api` antes de escrever o código: ela tem os modelos atuais, preços, streaming e uso de ferramentas
- A chamada à API fica numa rota do servidor; a chave nunca vai para o navegador
- Contexto: mande só os dados da empresa de quem está perguntando, já filtrados pelas regras de acesso
- Limite de uso por empresa e por dia, guardado no banco, para controlar o custo
- Registre tokens gastos por empresa, para o relatório de custo e para cobrar se o plano tiver limite

## App instalável (PWA)

- `app/manifest.ts` com nome, cores e ícones (192 e 512 px)
- Service worker simples para guardar a estrutura das telas principais (ex.: Serwist ou o recurso nativo do Next que estiver em uso)
- Testar "Adicionar à tela inicial" no Android e no iPhone

## Publicar

1. Criar o projeto no Supabase (no e-mail do cliente, ou transferir depois), rodar as migrations
2. Criar o projeto na Vercel ou Netlify ligado ao repositório e colar as variáveis do `.env.example`
3. Configurar no Supabase a URL do site (para os e-mails de login) e o domínio
4. Fazer o teste completo com uma conta nova: cadastro, fluxo principal, cobrança (se houver)
