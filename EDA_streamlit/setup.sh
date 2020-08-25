mkdir -p ~/.streamlit/echo "\
[general]\n\
email = \"suellen-stefane@bol.com.br\"\n\
" > ~/.streamlit/credentials.tomlecho "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml