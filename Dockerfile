# 使用 Go 官方镜像
FROM golang:1.20

# 设置工作目录
WORKDIR /app

# 将代码拷贝到容器中
COPY . .

# 下载依赖并构建
RUN go mod tidy
RUN go build -o app .

# 启动应用
CMD ["./app"]