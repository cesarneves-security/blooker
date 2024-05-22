
<p align="center">
  <a href="https://github.com/cesarneves-security/blooker"><img src="/img/capa_bloker.gif" alt="bloker"></a>
</p>


---
# Bloker
Bloker é uma ferramenta de linha de comando em Python que permite encriptar e desencriptar dados e arquivos de forma segura, utilizando uma chave de criptografia fornecida pelo usuário. Com o Bloker, você pode proteger suas informações confidenciais e arquivos importantes contra acesso não autorizado.

## Instalação
1. Clone o repositório: `git clone https://github.com/cesarneves-security/blooker.git`
2. Navegue até o diretório do projeto: `cd bloker`
3. Instale as dependências: `pip install -r requirements.txt`

## Uso:

### Encriptar/Desencriptar Dados:

```bash
INCRIPTAÇÃO:

    user = INPUT degite a informação para incriptação.
    user = INPUT degite a chave de bloqueio /OSB: sem a chave de bloquei, ninguém pode decriptar os seus dados.
    PROGRAMA = incriptação dos dados.
    PROGRAMA = salvar os dados e a chave em um arquivo. /OBS: o nome do arquivo séra o nome incriptado da informação
```
```bash
DECRIPTAÇÃO: 

    user = INPUT degite a informação incriptada.
    user = INPUT degite a chave da decriptação /OSB: sem a chave de bloquei, ninguém pode decriptar os seus dados.
    PROGRAMA = decriptar os dados, usando a chave como meio da descriptaçao. /SEM CHAVE SEM DECRIPTAÇÃO
    PROGRAMA = criar novo arquivo com dados decriptado.
```


### Encriptar/Desencriptar Arquivos:

```bash
INCRIPTAÇÃO:

        user = INPUT degite o arquivo para incriptação.
        user = INPUT degite a chave do arquivo /OSB: sem a chave do arquivo, ninguém pode decriptar os seus dados.
        PROGRAMA = incriptação dos dados.
        PROGRAMA = salvar os dados e a chave em um arquivo. /OBS: o nome do arquivo séra o nome incriptado da informação
```

```bash
DECRIPTAÇÃO: 

    user = INPUT degite o arquivo incriptado.
    user = INPUT degite a chave do arquivo para decriptação /OSB: sem a chave de bloquei, ninguém pode decriptar os seus dados.
    PROGRAMA = decriptar os dados, usando a chave como meio da descriptaçao. /SEM CHAVE SEM DECRIPTAÇÃO
    PROGRAMA = criar novo arquivo com dados decriptado.
```
$\text{\color{red}{ Importante: Mantenha a chave de encriptação em segredo e não a perca.}}$
$\text{\color{red}{ Sem a chave correta, não será possível desencriptar os dados ou arquivos.}}$

### Como Funciona
A ferramenta Bloker usa um algoritmo de encriptação seguro para proteger seus dados e arquivos. Quando você encripta dados ou arquivos, o Bloker solicita uma chave de encriptação. Esta chave é usada para encriptar os dados ou o conteúdo do arquivo. O resultado encriptado é então salvo em um novo arquivo.
Para desencriptar, o Bloker solicita o arquivo encriptado e a chave de encriptação correspondente. Se a chave correta for fornecida, o Bloker desencripta o conteúdo e salva os dados ou o arquivo desencriptado em um novo arquivo.
### Contribuição
Se você encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.
### Licença
Este projeto está licenciado sob a MIT License.
