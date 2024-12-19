docker run -p 8080:80 -v $((Get-Location).Path -replace '\\', '/'):/usr/share/nginx/html -d nginx
docker run -p 8080:80 -v $(pwd):/usr/share/nginx/html:ro -d nginx
http://localhost:8080/2017/
http://localhost:8080/2018/
http://localhost:8080/2019/
http://localhost:8080/2020/
http://localhost:8080/2021/
http://localhost:8080/2022/
http://localhost:8080/2023/