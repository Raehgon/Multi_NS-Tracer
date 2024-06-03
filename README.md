# Teste Tracert e Nslookup Múltiplo

Este projeto fornece uma interface gráfica de usuário (GUI) para realizar testes de `tracert` e `nslookup` em múltiplos endereços IP e domínios, respectivamente. A GUI é construída usando a biblioteca `ttkbootstrap` com o tema "cyborg" e permite que os usuários vejam o progresso dos testes em tempo real.

## Funcionalidades

- **Executar Tracert**: Teste a rota até múltiplos endereços IP.
- **Executar Nslookup**: Realize consultas DNS para múltiplos domínios.
- **Barra de Progresso**: Visualize o progresso dos testes em tempo real.
- **Relatório TXT**: Gere um relatório em formato TXT com os resultados dos testes.
- **Multithreading**: Executa os testes em paralelo para melhorar a eficiência e reduzir o tempo de execução.

## Requisitos

- Python 3.x
- Bibliotecas Python: `ttkbootstrap`, `concurrent.futures`, `tkinter`

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/teste-tracert-nslookup-multiplo.git
    ```
2. Instale as bibliotecas necessárias:
    ```bash
    pip install ttkbootstrap
    ```

## Uso

1. Navegue até o diretório do projeto:
    ```bash
    cd teste-tracert-nslookup-multiplo
    ```
2. Execute o script:
    ```bash
    python script.py
    ```

## Interface do Usuário

- **Endereços IP**: Insira os endereços IP que deseja testar, separados por vírgula.
- **Domínios**: Insira os domínios que deseja consultar, separados por vírgula.
- **Servidor DNS**: Insira o servidor DNS que deseja utilizar para as consultas.
- **Executar Testes**: Clique neste botão para iniciar os testes. A barra de progresso exibirá o andamento dos testes.
- **Gerar Relatório**: Após a conclusão dos testes, clique neste botão para gerar um relatório TXT com os resultados.

## Exemplo

1. Insira `8.8.8.8, 1.1.1.1` no campo de endereços IP.
2. Insira `google.com, cloudflare.com` no campo de domínios.
3. Insira `8.8.8.8, 1.1.1.1` no campo de servidor DNS.
4. Clique em "Executar Testes".
5. Aguarde a conclusão dos testes enquanto a barra de progresso exibe o andamento.
6. Clique em "Gerar Relatório" para salvar os resultados em um arquivo TXT.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto. Suas contribuições são muito bem-vindas!

![image](https://github.com/Raehgon/Multi_NS-Tracer/assets/170561546/6ef787d5-dab5-4f57-a673-4ea9da6294a5)
![image](https://github.com/Raehgon/Multi_NS-Tracer/assets/170561546/01bed443-2349-478d-a26f-2b7b32d37886)
![image](https://github.com/Raehgon/Multi_NS-Tracer/assets/170561546/4b731745-728d-43fd-a7e8-10093e9495ca)

