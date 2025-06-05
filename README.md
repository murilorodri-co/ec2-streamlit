## 🚀Projeto Streamlit em EC2 com Análise de Dados Financeiros
### Descrição
Este projeto demonstra como configurar uma instância EC2 da AWS para executar uma aplicação Streamlit que realiza análise e visualização de dados financeiros utilizando um dataset CSV hospedado em um repositório GitHub.

### 🛠️Ferramentas e Bibliotecas Utilizadas
- AWS EC2: Instância de servidor na nuvem para hospedar e executar a aplicação.

- Git: Controle de versão para clonar o repositório com os arquivos da aplicação.

- Python 3: Linguagem utilizada para desenvolvimento da aplicação.

- Streamlit: Framework para construção rápida de interfaces web para visualização de dados.

- Pandas: Biblioteca para manipulação e análise de dados.

- Altair: Biblioteca para geração de gráficos interativos no Streamlit.

- Matplotlib / Seaborn (opcional): Bibliotecas de visualização usadas em versões locais ou testes.

### 🔄️Passo a passo para rodar a aplicação
1. Criar a instância EC2 na AWS
- Escolha a AMI (Ubuntu, Amazon Linux, Debian, etc).
- Configure o grupo de segurança liberando as portas
  - 22 (SSH) para acesso remoto
  - 8501 para acesso ao Streamlit.

- Faça o download da chave .pem para acesso via SSH.

2. Conectar à instância via SSH
    - ssh -i "minhachave.pem" usuario@<IP-da-instância>

3. Instalar Git
    - sudo apt update
    - sudo apt install git -y

4. Clonar o repositório do projeto
    - git clone https://github.com/usuario/repositorio.git

5. Instalar Python e bibliotecas necessárias
    - sudo apt install python3 python3-pip -y
    - pip3 install streamlit pandas altair

6. Rodar o app Streamlit
    - streamlit run app.py --server.port 8501 --server.address 0.0.0.0
- Acesse a aplicação via browser:
    - http://<IP-da-instância>:8501

### 🗃️Arquivos principais
- app.py: Script principal do Streamlit que carrega o dataset, faz o pré-processamento e plota gráficos usando Altair.

- MS_Financial Sample.csv: Dataset financeiro utilizado para análise (baixado do repositório GitHub).
