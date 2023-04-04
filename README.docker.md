docker build -t feishu .
docker run --rm --env-file .env -v code_dir:/home/app -p 3003:3000 -it feishu
