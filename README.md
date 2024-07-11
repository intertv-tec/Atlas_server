# Sistema de Monitoramento de Automações

## Descrição

Este sistema foi desenvolvido para monitorar automações, verificando se estão ativas ou inativas com base em pings enviados periodicamente. O sistema utiliza Django para o backend e Celery para tarefas assíncronas.

## Funcionalidades

- **Registro de Automações:** Permite registrar novas automações no sistema.
- **Monitoramento de Pings:** Recebe pings das automações para atualizar seu status.
- **Verificação de Status:** Verifica periodicamente se as automações estão ativas ou inativas com base no último ping recebido.
- **Painel Administrativo:** Acesso ao Django Admin para gerenciar as automações.

## Requisitos

- Python 3.x
- Django
- Celery
- Redis (ou outro backend para Celery)

## Uso

Ping 
- curl -X GET http://ip_do_servidor:8100/ping/id_da_automacao/senha_da_automacao/

## Entrando no servidor
![Login](https://github.com/intertv-tec/monitor_server/blob/main/print/login.png)

## Criando Usuário
![Usuario](https://github.com/intertv-tec/monitor_server/blob/main/print/novo_usuario.png)
![Usuario](https://github.com/intertv-tec/monitor_server/blob/main/print/novo_usuario2.png)

## Criando Automação
![Automacao](https://github.com/intertv-tec/monitor_server/blob/main/print/automacao.png)
![Automacao](https://github.com/intertv-tec/monitor_server/blob/main/print/nova_automacao.png)
