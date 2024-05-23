
<p align="center">
  <a href="https://github.com/cesarneves-security/blooker"><img src="/img/capa_bloker.gif" alt="bloker"></a>
</p>


---
# Blooker
Blooker é uma ferramenta de linha de comando em Python para encriptar e desencriptar dados e arquivos de forma segura, utilizando uma chave de criptografia fornecida pelo usuário. Proteja suas informações confidenciais e arquivos importantes contra acesso não autorizado com o Blooker.

### Como Funciona
Blooker utiliza um algoritmo de encriptação seguro para proteger seus dados e arquivos. Quando você encripta dados ou arquivos, o Blooker solicita uma chave de encriptação, que é usada para encriptar os dados ou o conteúdo do arquivo. O resultado encriptado é então salvo em um novo arquivo.

Para desencriptar, o Blooker solicita os dados ou arquivo encriptado e a chave de encriptação correspondente. Se a chave correta for fornecida, o Blooker desencripta os dados. No caso de arquivos, ele salva o arquivo desencriptado em um novo arquivo.

## Instalação
1. Clone o repositório:
```bash
git clone https://github.com/cesarneves-security/blooker.git
```
2. Navegue até o diretório do projeto:
```bash
cd bloker
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso:
- Dentro do diretório blooker, rode o comando:
```python3 main.py```

### Encriptar/Desencriptar Dados:

==Importante: Mantenha a chave de encriptação em segredo e não a perca.==
==Sem a chave correta, não será possível desencriptar os dados ou arquivos.==

##### 🔒 ENCRIPTAÇÃO

1. Escolha a opção `1`.

```bash
[E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?

[1] ENCRIPTAÇÃO.
[2] DECRIPTAÇÃO.

[?] : 1
 ```

2. Digite os dados que deseja encriptar.
3. Digite a chave que será usada para desencriptar esses dados.

 ```bash
[E N C R I P T A Ç Ã O]

[!] DEGITE A INFORMAÇÃO: eu amo python
[!] DEGITE A KEY PARA ENCRIPTAÇÃO: 12345

[-] ENCRIPTADO: vKJVTKGUhvePPb+yfw==*ZO+NhOxDl+pwuOU7gCEQ5g==*HLbHztUP5cl7X1QlYerGRg==*7lh1wHNsvB7WOhHZAjY6tg==
[-] KEY: 12345
 ```


 ##### 🔑 DECRIPTAÇÃO
1. Escolha a opção `2`.

```bash
[E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?

[1] ENCRIPTAÇÃO.
[2] DECRIPTAÇÃO.

[?] : 2
```
2. Digite os dados encriptados.
3. Digite a chave usada para encriptar os dados.

```bash
[D E C R I P T A Ç Ã O]

[!] DEGITE O TEXTO ENCRYPTADO: vKJVTKGUhvePPb+yfw==*ZO+NhOxDl+pwuOU7gCEQ5g==*HLbHztUP5cl7X1QlYerGRg==*7lh1wHNsvB7WOhHZAjY6tg==
[!] DEGITE A KEY DA ENCRIPTAÇÃO: 12345
```
```bash
[D E C R I P T A N D O. . .]

[!] DECODIFICADO: eu amo python
[!] KEY: 12345
```


### Encriptar/Desencriptar Arquivos:
##### 🔒 ENCRIPTAÇÃO

1. Escolha a opção `1`.

```bash
 [E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?

 [1] ENCRIPTAÇÃO.
 [2] DECRIPTAÇÃO.

 [?] : 1
 ```
1. Digite o nome do arquivo que deseja encriptar _(o arquivo deve estar na raiz do programa)_.

2. Digite a chave que será usada para desencriptar os dados do arquivo.

3. Digite um nome para o arquivo encriptado que será gerado.

```bash
 [file] FILE-NAME?: teste.py
 [key] KEY-CHAVE?: 12345
 [file-salve] FILE-SALVE?: encript-teste.py

 [F I L E -- E N C R I P T A D O]
```
> O arquivo será salvo dentro da pasta `CRYPTOGRAFADOS`.

 ##### 🔑 DECRIPTAÇÃO
1. Escolha a opção `2`.

```bash
 [E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?

 [1] ENCRIPTAÇÃO.
 [2] DECRIPTAÇÃO.

 [?] : 2

```
1. Digite o nome do arquivo que deseja decriptar _(o arquivo deve estar na raiz do programa)_.

2. Digite a chave usada para encriptar os dados do arquivo.

3. Digite um nome para o arquivo decriptado que será gerado.
```bash
[file] FILE-NAME-DECRYPT?: encript-teste.py
[key] KEY-CHAVE?: 12345
[file-salve] FILE-SALVE?: teste.py

[F I L E -- D E C R I P T A D O]
```
> O arquivo será salvo dentro da pasta `DESCRYPTOGRAFADOS`.

### Contribuição
Se você encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.
