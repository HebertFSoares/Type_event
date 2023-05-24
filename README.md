# Type_event
Este é um projeto de desenvolvimento web com Django, é uma plataforma para gerenciamento de eventos. A plataforma contém as seguintes funcionalidades:

- Tela de cadastro e login de usuários
- Cadastro de novos eventos
- Inscrição de usuários em eventos cadastrados
- Geração de certificados para os participantes do evento
- Geração de link de convite para o evento

## Utilização
- Tela de Cadastro e Login
 Na tela inicial da plataforma é possível realizar o cadastro de um novo usuário ou fazer login com um usuário já existente. Para se cadastrar, clique em "Cadastrar" e preencha os dados solicitados. Para fazer login, preencha o formulário de login na parte superior da tela.

- Cadastro de Novo Evento
 Ao fazer login na plataforma, é possível cadastrar um novo evento clicando no botão "Novo Evento" na barra de navegação superior. Preencha as informações solicitadas, como nome do evento, data, local, etc.

- Inscrição em Evento
 Usuários cadastrados na plataforma podem se inscrever em eventos já cadastrados. Para isso, acesse a página do evento desejado e clique no botão "Inscrever-se". O usuário receberá uma confirmação de inscrição por e-mail.

- Geração de Certificado
 Após a realização do evento, os participantes poderão gerar um certificado de participação. Para isso, basta acessar a página do evento e clicar no botão "Gerar Certificado". O certificado será gerado em PDF e poderá ser salvo ou impresso.

- Geração de Link de Convite
 Ao cadastrar um novo evento, o usuário poderá gerar um link de convite para o evento. Esse link poderá ser compartilhado com outras pessoas, que poderão se inscrever no evento diretamente a partir desse link. Para gerar o link de convite, basta acessar a página do evento e clicar no botão "Gerar Link de Convite". O link será gerado e poderá ser copiado e compartilhado.

## Tecnologias
### Este projeto foi desenvolvido utilizando as seguintes tecnologias:

- Python
- Django 
- SQLite

## Requisitos
### Para executar o projeto em sua máquina local, você precisará ter o Python 3 instalado. Além disso, recomendamos utilizar um ambiente virtual para instalar as dependências necessárias.

## Instalação

### Clone este repositório em sua máquina local.

- Crie um ambiente virtual:
```
python3 -m venv myenv
```
- Ative o ambiente virtual:
```
source myenv/bin/activate
```
- Instale as dependências:
```
pip install -r requirements.txt
```
- Execute as migrações do banco de dados:
```
python manage.py migrate
```
- Crie um superusuário:
```
python manage.py createsuperuser
```
- Execute o servidor:
```
python manage.py runserver
```
## Utilização
Após a instalação, o sistema estará disponível em seu navegador através do endereço http://localhost:8000. Para acessar a área administrativa, utilize as credenciais do superusuário criado na instalação.

## Contribuição
Contribuições são bem-vindas! Se você quiser contribuir para este projeto, por favor siga estas instruções:

- Faça um fork deste repositório.
- Crie um branch com suas alterações:
```git checkout -b minha-alteracao```
- Faça o commit das suas alterações:
```git commit -m 'Minha alteração'```
- Faça o push para o branch:
```git push origin minha-alteracao```
- Abra um pull request para o branch principal.
## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
