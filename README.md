
<h1 align="center">
  <br>
  <a href="http://www.ricardodarocha.com.br"><img src="https://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png" alt="Markdownify" width="200"></a>
  <br>
  designed by Ricardo da Rocha
  <br>
</h1>

<h4 align="center">
*Int cpf* é um experimento em Rust para calcular o dígito verificador de um CPF armazenado no formato inteiro, em vez de string. Inspirado na comunidade <a href="https://github.com/fabriziomello/pg_toolkit_brazil/blob/main/cpf.c">Postgres Brasil</a>

<p align="center">
</p>

<p align="center">
  <a href="#introdução">Introdução</a> •
  <a href="#como-usar">Como usar</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

<p align="center">
<img src="https://github.com/ricardodarocha/sidebar/blob/master/img/screenshot.gif">
</p>

## Introdução

É muito comum as aplicações gravarem o CPF no banco de dados no formato String, muitas vezes com a formatação. Em outros casos também é usado String, porém sem as pontuações. Neste experimento o tipo u_64 é usado. Em vez de string, o CPF é gravado como um número inteiro. A intenção é otimizar o cálculo de verificação do CPF.

## Disclaimer

Este é um recurso experimental

## Como usar

Clone este repositório [Git](https://github.com/ricardodarocha/int_cpf.git) 
Rode o comando `cargo test`

```bash
# Clone this repository
$ git clone https://github.com/ricardodarocha/int_cpf.git

# Go into the repository
$ cd int_cpf

# Abra com VSCode
$ code .

# Rode o aplicativo passando os parâmetros
$ cargo test
```

## Download

Por enquanto ainda não há assets disponíveis

## Emailware

Caso necessite de suporte ou queira personalizar este projeto você pode entrar em contato comigo <ricardodarocha@outlook.com> 

## Credits

This software uses the following open source packages:

- [Flet](flet.dev)

This was based in video from Line Indent
- [Line Indent Youtube Chanel](https://www.youtube.com/watch?v=lu1obAGKxmE)

## Related

https://github.com/fabriziomello/pg_toolkit_brazil/blob/main/cpf.c

## Contato

> Linkedin [ricardo-da-rocha-vitor](https://www.linkedin.com/in/ricardo-da-rocha-vitor-a0983932/)
> Site [ricardodarocha.com.br](https://www.ricardodarocha.com.br) &nbsp;&middot;&nbsp;
> GitHub [@ricardodarocha](https://github.com/ricardodarocha) &nbsp;&middot;&nbsp;
> Twitter [@ricardorochadev](https://twitter.com/ricardorochadev)


## You may also like...

- Ainda não há outros links

## License

GNU - Livre, de uso geral


---


