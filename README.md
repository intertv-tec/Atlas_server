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

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/intertv-tec/monitor_server.git
   cd monitor_server
