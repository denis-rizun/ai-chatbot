# AI Chatbot

Асинхронное FastAPI-приложение с WebSocket, PyTorch, PostgreSQL (pgvector) и Redis, построенное по принципу **DDD + Pipeline Architecture**.  
Система обрабатывает пользовательские сообщения через последовательные этапы (pipeline): кеш → контекст → AI → ответ.  
RAG (Retrieval-Augmented Generation) уже интегрирована для расширения контекста ответов.

---

## Цель

Создать инженерно корректную архитектуру для AI-взаимодействий в реальном времени с возможностью масштабирования в Kubernetes.

---

## Технологии

- **FastAPI + WebSocket** — асинхронный транспорт и двусторонняя связь с клиентом.  
- **PostgreSQL + pgvector** — хранение сообщений и embedding-контекста.  
- **Redis** — кеширование ответов и промежуточных вычислений.  
- **PyTorch** — модели эмбеддингов и генерации.  
- **DDD (Domain-Driven Design)** — разделение бизнес-логики и инфраструктуры.  
- **Pipeline Architecture** — обработка через независимые стадии.  
- **RAG (Retrieval-Augmented Generation)** — расширение контекста для ответов AI.  
- **Kubernetes + Helm** — деплой и масштабирование.

---

## MVP функциональность

1. WebSocket-соединение.  
2. Приём сообщений и создание embedding.  
3. Проверка кеша (Redis).  
4. Поиск контекста через pgvector.  
5. Генерация ответа AI.  
6. Отправка ответа клиенту через WebSocket.
7. Система аутентификации.
8. Рейт-лимит на пользователя.

---

## Текущий статус

- Приём сообщений и создание embedding.
- Проверка кеша.
- Поиск контекста через pgvector.  
- Генерация ответа AI.
- Отправка ответа клиенту через API (пока что без WebSocket'ов).

---

## Запуск

### Как запустить проект

Ниже два способа запуска: через Docker или через Kubernetes (Minikube\Helm).

1) Подготовка (обязательно для обоих способов)
- Спулить репозиторий с GitHub и перейти в каталог проекта:
  ```bash
  git clone https://github.com/denis-rizun/ai-chatbot
  cd ai-chatbot
  ```
- Создать собственный файл окружения `.env` по примеру `.env.example`:

2) Запуск через Docker
- Требования: установлен Docker и Docker Compose.
- Вариант A — через Makefile:
  ```bash
  make run
  ```
- Вариант B — напрямую через docker compose:
  ```bash
  docker compose --env-file=.env -f deploy/docker/compose.yml up --build
  ```

3) Запуск через Kubernetes (Minikube)
- Требования: установлен `minikube` и `kubectl`.
- Перед применением манифестов необходимо поместить ваши креды из `.env` в `deploy/k8s/secrets.yaml` и `deploy/k8s/configmap.yaml`.
  (Да, для pet-проекта это упрощение; в проде так делать не следует.)
- Затем выполните команды (из каталога `deploy/k8s` или указывая полный путь к файлам):
  ```bash
  minikube start
  kubectl apply -f deploy/k8s/namespace.yaml
  kubectl apply -f deploy/k8s/secrets.yaml
  kubectl apply -f deploy/k8s/configmap.yaml
  kubectl apply -f deploy/k8s/postgres-statefulset.yaml
  kubectl apply -f deploy/k8s/postgres-service.yaml
  kubectl apply -f deploy/k8s/redis-deployment.yaml
  kubectl apply -f deploy/k8s/redis-service.yaml
  kubectl apply -f deploy/k8s/ai-chatbot-deployment.yaml
  kubectl apply -f deploy/k8s/ai-chatbot-service.yaml
  ```
- Подождите 1–3 минуты, пока поднимутся поды и сервисы.

Подсказка: те же команды для Kubernetes собраны в вспомогательном файле `deploy/k8s/help-command.txt`.


4) Запуск через Helm (Minikube)
- Требования: установлен `helm`, `minikube`, `kubectl`.
- В этом репо добавлен чарт Helm: `deploy/helm/ai-chatbot`.
- Быстрый старт:
  ```bash
  cd deploy/helm/ai-chatbot
  helm template ai-chatbot . -f values-minikube.yaml
  helm lint .
  # установка (создаст namespace ai-chatbot)
  helm install ai-chatbot . -f values-minikube.yaml -n ai-chatbot --create-namespace

  # получить URL сервиса (в Minikube)
  minikube service ai-chatbot-service -n ai-chatbot --url
  ```
- Обновление после изменения values:
  ```bash
  helm upgrade ai-chatbot . -f values-minikube.yaml -n ai-chatbot
  ```
- Удаление релиза:
  ```bash
  helm uninstall ai-chatbot -n ai-chatbot
  ```
- Настройка переменных окружения выполняется через файл `values.yaml`/`values-minikube.yaml`:
  - Несекретные переменные — раздел `env.config` (ConfigMap)
  - Секретные переменные — раздел `env.secrets` (Secret)
- Встроенные Postgres/Redis можно отключить:
  ```yaml
  postgres:
    enabled: false
  redis:
    enabled: false
  ```
