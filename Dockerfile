FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 首先只复制依赖相关文件
COPY uv.lock pyproject.toml /app/

# 安装依赖
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


COPY main.py .
COPY worker/ worker/
COPY README.md .


# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 暴露端口（如果需要）
# EXPOSE 8000

# 默认命令
CMD ["uv", "run", "celery", "-A", "worker", "worker", "--loglevel=info"] 