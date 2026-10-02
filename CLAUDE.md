# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A personal collection of Python study material and small projects, not a single application. Every folder holds standalone scripts: there is no package, `requirements.txt`, test suite, linter config or build step. [README.md](README.md) is the tutorial and index. Each topic there links to its folder by a full, percent-encoded GitHub URL (`https://github.com/marcospontoexe/Python/tree/main/...`), so a new example folder usually gets a matching README entry.

Everything is written in Brazilian Portuguese: comments, docs, output strings, and often identifiers with accents (`opção`, `cabeçalho`). New code should do the same.

## Layout

- `exercícios_curso em vídeo/`: numbered lessons from the "Curso em Vídeo" course (variables → functions → modules → error handling). `13-modularização/02-pacote(biblioteca)/` is the only multi-module example: `main.py` imports from the local `biblioteca/` package (`interface`, `arquivo`, `trat_erros`).
- `POO/`: OOP examples (`main.py` imports `Classe.Jedi`; `Heranca.py`, `Polimorfismo.py`, `Televisao.py`).
- `tkinter/`: one script per layout manager (place/pack/grid), widget, or event.
- `Pandas/`: numbered DataFrame lessons, each with its own data files next to it.
- `Pandas e e-mail/main.py`: groups `Vendas.xlsx` with pandas and **sends a real email through Outlook** (win32com) to a hardcoded address. Do not run it without asking.
- `MT5/`: MetaTrader5 API examples. They need the MetaTrader 5 terminal installed and logged in on Windows.
- `GNSS/Velocímetro/`: the only real application (see below).

## Running scripts

Run each script with its own folder as the working directory. Many scripts use cwd-relative paths or sibling imports: `Velocidade.py` loads `imagens/*.png` and writes `log.txt`, `POO/main.py` does `from Classe import Jedi`, and the modularization `main.py` imports `biblioteca`. A few scripts resolve paths with `os.path.dirname(os.path.realpath(__file__))` instead.

```powershell
Set-Location "exercícios_curso em vídeo\13-modularização\02-pacote(biblioteca)"; python main.py
```

Folder names contain spaces, accents and parentheses, so always quote paths.

Third-party dependencies, installed ad hoc with pip: `pandas`, `openpyxl` (for .xlsx), `pyserial`, `pytz`, `MetaTrader5`, `pywin32`, `cufflinks`, `matplotlib`, and `RPi.GPIO` (Raspberry Pi only).

## GNSS/Velocímetro architecture

This is a Tkinter speed-calibration tool that reads a u-blox GNSS receiver over a serial port. The folder holds two variants of the same app, each with its own `Com.py`, images and `log.txt`:

- `Versão para Raspbian/`: the build that ran on the Raspberry Pi 4 (systemd service). Spanish UI. It reads physical buttons with `RPi.GPIO`: BCM 27 triggers a capture through a falling-edge interrupt (`add_event_detect`, 500 ms bounce), and BCM 22 clears the history by polling inside the `read_serial` loop. Its window is `800x442+0-62`. `imagens/backup*` hold older background layouts.
- `Velocidade.py` (folder root): the desktop version (Portuguese UI, forward-slash image paths, debug prints off). There is no GPIO; the space bar stands in for the capture button.

Changes to the shared logic should go into both variants, or ask which one to change. The project's own [README.md](GNSS/Velocímetro/README.md) and [relatorio.md](GNSS/Velocímetro/relatorio.md) document it. relatorio.md is a Markdown transcription of the original Word report (since deleted), with its figures in `imagens/relatorio/`.

1. `import Com` has side effects: the module builds and runs its own blocking Tk window (`janela.mainloop()`) to pick the COM port and UTC offset. After that window closes, it opens `Com.ser` at 115200 baud and sets `Com.fusoLocal`. Nothing in `Velocidade.py` runs until this dialog is closed.
2. `Velocidade.py` then builds a fixed 800x480 window. Widgets are positioned with absolute `place()` coordinates over the background image `imagens/main.png`.
3. A `threading.Thread` runs `read_serial()`. It sends UBX `CFG-RATE` bytes (`SET_RATE_1/2`) to switch the receiver to 10 Hz, discards about 100 lines during cold start while it drives the progress bar, and then loops over NMEA sentences:
   - `$GNVTG` field 7 gives the speed in km/h. The label turns green when that speed is within ±1 km/h of the `Scale` setpoint, red otherwise.
   - `$GNRMC` with status `A` gives the UTC date and time, which is converted to local time via `pytz`.
4. State is shared through module globals (`hora`, `speed_str`, `data`). The worker thread updates Tk widgets directly.
5. Captures (button, space bar on desktop, GPIO button on the Pi) are appended to `log.txt`.

## Repository hygiene notes

- [.gitignore](.gitignore) excludes virtualenvs, `__pycache__`, Jupyter checkpoints and Office lock files (`~$*`). It also excludes the local working notes `CONTEXTO.md` and `DOCS/`, which are never committed. Some data files are large (`Pandas/03-explorando o arquivo/prices.csv` is about 15 MB, `Pandas e e-mail/Vendas.xlsx` about 4 MB).
- Before adding images or Office files, check their metadata for personal information: PNG text chunks, and the author and saved paths in `.xlsx`/`.docx` files.
- On this Windows machine `git` is not on PATH. Use the `git.exe` bundled with GitHub Desktop under `%LOCALAPPDATA%\GitHubDesktop\app-*\resources\app\git\cmd\`.

---

## Regra: Persistência de Contexto (Handoff entre sessões)

### Objetivo

Garantir que nenhum trabalho se perca quando a sessão atual se tornar demasiado longa. O agente deve gravar todo o estado da sessão num ficheiro de handoff, de forma que **qualquer outro chat consiga retomar exatamente de onde parou**, com o mesmo contexto.

### Gatilho

Execute o procedimento de salvamento abaixo **antes de continuar qualquer tarefa** sempre que uma das seguintes condições for atingida:
1. A conversa prolongar-se por muitas interações (aproximando-se do limite prático da janela de contexto).
2. Uma funcionalidade ou milestone importante for concluída.
3. O utilizador disser explicitamente: `salvar contexto`, `handoff` ou `checkpoint`.

### Procedimento de salvamento

1. **Termine** a tarefa atual.
2. Crie ou atualize o arquivo **`CONTEXTO.md`** na raiz do projeto.
   - Se já existir, **atualize** as seções em vez de duplicar (mantenha o histórico relevante, remova o que já foi superado).
   - Sempre atualize o campo de data/hora e o número da sessão.
3. Preencha **todas** as seções do template abaixo. Não deixe seções vazias — escreva "nenhum" quando não houver conteúdo.
4. Confirme ao usuário que o contexto foi salvo e informe o caminho do arquivo.
5. **Gestão do CONTEXTO.md:**  Mantenha o CONTEXTO.md enxuto. Ele segue o template abaixo, mas cada seção deve ter só o resumo. Quando um tópico precisar de mais detalhe (uma decisão longa, um passo a passo, etc.), escreva-o num ficheiro em DOCS/ na raiz do projeto e coloque no CONTEXTO.md apenas o link para ele. O objetivo é não sobrecarregar a janela de contexto ao ler o CONTEXTO.md. Se precisar de mais informações sobre um tópico, abra o ficheiro específico em DOCS/.

### Template do `CONTEXTO.md`

```markdown
# CONTEXTO DA SESSÃO

- **Última atualização:** AAAA-MM-DD HH:MM
- **Sessão nº:** N
- **Status geral:** (em andamento | bloqueado | pronto para revisão)

## 1. Objetivo da tarefa
Descrição em 1–3 frases do que estamos tentando alcançar (o "porquê").

## 2. Já feito ✅
- Itens concluídos, com o(s) arquivo(s) afetado(s).
- Ex.: "Implementado endpoint POST /login em `src/auth.py`"

## 3. Em andamento 🔧
- O que estava sendo feito no momento do checkpoint.
- Em qual arquivo/linha parei e qual era o próximo passo imediato.

## 4. Próximos passos (planejado) 📋
- Lista ordenada do que falta fazer.
- Quanto mais específico, melhor (arquivo, função, comportamento esperado).

## 5. Decisões e raciocínio 🧠
- Escolhas técnicas feitas e o porquê.
- Alternativas descartadas (para evitar refazer a análise).
- Suposições assumidas.

## 6. Estado do projeto / ambiente
- Arquivos-chave e o papel de cada um.
- Branch git atual, alterações não commitadas, migrations pendentes, etc.
- Variáveis de ambiente ou dependências relevantes.

## 7. Bloqueios e pendências ⚠️
- Erros não resolvidos, dúvidas para o usuário, decisões aguardando aprovação.

## 8. Comandos úteis
- Comandos para rodar/testar/buildar o projeto.
- Ex.: `npm run dev`, `pytest tests/`, etc.

## 9. Como retomar
Instrução direta para o próximo chat: "Leia este arquivo e continue a partir
da seção 3 / passo X."
```

### Como retomar em um novo chat

No início de qualquer nova sessão, o agente deve:

1. Verificar se existe o ficheiro `CONTEXTO.md` na raiz do projeto .
2. Se existir, **lê-lo por completo antes de qualquer outra ação**.
3. Resumir ao utilizador em 2–3 linhas onde o trabalho parou e qual é o próximo passo, e então continuar.

> Comando sugerido para o utilizador iniciar um novo chat:
> **"Leia o `CONTEXTO.md` e continue de onde a sessão anterior parou."**

### Boas práticas

- **Escreva para um estranho:** o próximo chat não tem memória nenhuma; seja explícito.
- **Caminhos absolutos ou relativos à raiz**, nunca referências vagas ("aquele arquivo").
- **Não salve segredos** (tokens, senhas, chaves) no `CLAUDE.md` e `CONTEXTO.md`.
- **Um arquivo por projeto:** mantenha `CONTEXTO.md` enxuto; arquive versões antigas em `CONTEXTO.arquivo.md` se necessário.
- **Commit opcional:** se o usuário usar git, ofereça commitar o `CONTEXTO.md` para que ele persista entre máquinas.
- **Feedback de alterações:** Caso algum ficheiro seja alterado durante a sessão, informe sempre qual o ficheiro e o que foi alterado no final de cada mensagem.
- **referenciar diretórios e arquivos atraves de links:** Sempre que se referir a um diretório ou arquivo local, use link e não backticks.
