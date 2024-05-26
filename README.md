
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
cd blooker
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Instalação da ferramenta:
```bash
python3 install.py
```
5. Remover a ferramenta:
```bash
python3 uninstall.py
```

### Encriptar/Desencriptar Dados:

==Importante: Mantenha a chave de encriptação em segredo e não a perca.==
==Sem a chave correta, não será possível desencriptar os dados ou arquivos.==


##### ENCRIPTAÇÃO E DECRIPTAÇÃO DE INFOR #############################################

##### 🔒 ENCRIPTAÇÃO /INFO

1. Escolha a opção `ENCRIPTAÇÃO`.

```bash
[E N C R I P T A Ç Ã O - INFO]
  blooker -encript-info --key admin123 --input "A minha senha é cesaradmin164" --output-info senha.txt
 ```

##### 🔒 DECRIPTAÇÃO /INFO

2. Escolha a opção `ENCRIPTAÇÃO`.

```bash
[D E C R I P T A Ç Ã O - INFO]
  blooker -decript-info --key admin123 --input "texto_encriptado" --output-info senha.txt
 ```

##### ENCRIPTAÇÃO E DECRIPTAÇÃO DE ARQUIVOS #############################################


##### 🔑 ENCRIPTAÇÃO /FILE
1. Escolha a opção `2`.

```bash
[E N C R I P T A Ç Ã O - FILE]
  blooker -encript-file --key admin123 --file files.txt --output-file saida_file.txt
```

##### 🔑 DECRIPTAÇÃO /FILE
2. Escolha a opção `2`.

```bash
[D E C R I P T A Ç Ã O - FILE]
  blooker -decript-file --key admin123 --file encript_files.txt --output-file saida_file.txt
```
==Importante: Mantenha a chave de encriptação em segredo e não a perca.==
==Sem a chave correta, não será possível desencriptar os dados ou arquivos.==

### Contribuição
Se você encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.
