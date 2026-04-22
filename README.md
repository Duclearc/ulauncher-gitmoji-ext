# Gitmoji para Ulauncher

Extensão para [Ulauncher](https://ulauncher.io/) inspirada no workflow [alfred-gitmoji](https://github.com/techouse/alfred-gitmoji): busca **gitmojis** offline (lista empacotada) e copia o **código** (`:bug:`) ou o **emoji** (`🐛`) para a área de transferência.

Os dados vêm do repositório oficial [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) (arquivo `data/gitmojis.json`).

## Requisitos

- Ulauncher com **Extension API v2** (veja em *Preferências → Sobre*).

## Instalação

### Pelo repositório Git (recomendado para desenvolvimento)

1. Clone este repositório (ou copie a pasta do projeto).
2. Crie um link simbólico na pasta de extensões do Ulauncher:

   ```bash
   mkdir -p ~/.local/share/ulauncher/extensions
   ln -sf /caminho/absoluto/para/ulauncher_gitmoji_extension \
     ~/.local/share/ulauncher/extensions/ulauncher-gitmoji
   ```

3. Reinicie o Ulauncher (ou recarregue as extensões nas preferências).

### Pela URL do GitHub (quando o repositório estiver público)

1. Abra *Ulauncher → Preferências → Extensões → Adicionar extensão*.
2. Cole a URL do repositório Git (HTTPS), por exemplo:  
   `https://github.com/SEU_USUARIO/ulauncher_gitmoji_extension.git`

O Ulauncher usa o arquivo [`versions.json`](versions.json) para escolher o branch compatível com a API (aqui: `master` + API `2`). Se o branch padrão do seu repositório for `main`, altere o campo `commit` em `versions.json` para `main`.

## Uso

1. Abra o Ulauncher (atalho padrão).
2. Digite a palavra-chave configurada (padrão: **`gm`**).

| Comando | Comportamento |
|---------|----------------|
| **`gm `** (só a keyword, sem termo) | Mostra **5** gitmojis iniciais (sugestões rápidas). |
| **`gm <termo>`** | Busca por código, nome ou descrição; até **25** resultados. Ex.: `gm bug`, `gm performance`. |
| **`gm all`** | Lista **todos** os gitmojis (~73), sem limite. |
| **`gm all <termo>`** | Filtra como na busca normal, mas **sem limite** de resultados. |

3. Cada gitmoji aparece como **um único item** (emoji + código no título; descrição abaixo).
4. **Enter** no item: copia o valor configurado em *Formato copiado* (código `:nome:` ou emoji unicode) e fecha o Ulauncher.

## Preferências

Em *Preferências → Extensões → Gitmoji*:

| Preferência | Descrição |
|-------------|-----------|
| **Gitmoji** (keyword) | Palavra que dispara a extensão (padrão `gm`). |
| **Formato copiado** | Define se o **Enter** copia o **código** (`:bug:`) ou o **emoji unicode** (`🐛`). |

## Desenvolvimento e teste manual

1. Instale a extensão via symlink (seção *Instalação*).
2. Rode o Ulauncher em modo verboso para ver logs da extensão:

   ```bash
   ulauncher -v
   ```

3. Teste no launcher: `gm`, `gm bug`, `gm all`, `gm all fix`.
4. Após selecionar um item, cole em um editor e confira se o texto copiado está correto (código vs emoji).

## Créditos

- Inspiração: [techouse/alfred-gitmoji](https://github.com/techouse/alfred-gitmoji)
- Dados e convenção gitmoji: [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji)
- Ícone: assets do site gitmoji ([`packages/website/public/static`](https://github.com/carloscuesta/gitmoji/tree/master/packages/website/public/static))

## Licença

MIT — veja [LICENSE](LICENSE).
